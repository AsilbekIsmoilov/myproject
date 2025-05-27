import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from project.models import *
import datetime
import sys
from io import StringIO
from project.sheets import get_archive,update_call_data
from datetime import datetime
from statistics import mean
from django.views.decorators.csrf import csrf_exempt
import requests





def index(request):
    selected_name = request.GET.get("operator-name")
    selected_month_param = request.GET.get("month")
    operators = CallData.objects.all().order_by('name')

    selected_operator = None
    monthly_scores = None
    month_names_in_db = []
    selected_month = ""
    selected_month_pair = ""
    selected_month_int = None
    source_label = ""

    month_pairs = {
        1: "Январь-Февраль",
        2: "Февраль-Март",
        3: "Март-Апрель",
        4: "Апрель-Май",
        5: "Май-Июнь",
        6: "Июнь-Июль",
        7: "Июль-Август",
        8: "Август-Сентябрь",
        9: "Сентябрь-Октябрь",
        10: "Октябрь-Ноябрь",
        11: "Ноябрь-Декабрь",
        12: "Декабрь-Январь"
    }

    if selected_name:
        try:
            selected_operator = CallData.objects.get(name=selected_name)

            months_set = set()

            if selected_operator.month is not None:
                months_set.add(selected_operator.month)

            archived_months = ScoresForMonth.objects.filter(operator=selected_operator) \
                .values_list('month', flat=True).distinct()
            months_set.update(m for m in archived_months if m is not None)

            months_in_db = sorted(int(m) for m in months_set)
            month_names_in_db = [(f"{m:02}", month_pairs.get(m)) for m in months_in_db]

            if selected_month_param:
                try:
                    selected_month_int = int(selected_month_param)

                    monthly_scores = ScoresForMonth.objects.filter(
                        operator=selected_operator,
                        month=selected_month_int
                    ).first()

                    if monthly_scores:
                        source_label = "Источник: архив"

                    elif selected_operator.month == selected_month_int:
                        monthly_scores = selected_operator

                except (ValueError, TypeError):
                    selected_month_int = selected_operator.month or 1
                    monthly_scores = selected_operator
            else:
                selected_month_int = selected_operator.month or 1
                monthly_scores = selected_operator

            if selected_month_int:
                selected_month = f"{selected_month_int:02}"
                selected_month_pair = month_pairs.get(selected_month_int)
            else:
                selected_month = ""
                selected_month_pair = ""

        except CallData.DoesNotExist:
            selected_operator = None
            monthly_scores = None
            month_names_in_db = []
            selected_month = ""
            selected_month_pair = ""

    return render(request, 'project/index.html', {
        "title": "UZTELECOM Layout",
        "operators": operators,
        "selected_operator": selected_operator,
        "monthly_scores": monthly_scores,
        "selected_month": selected_month,
        "selected_month_pair": selected_month_pair,
        "month_names_in_db": month_names_in_db,
        "selected_month_param": selected_month_param,
    })

def get_quarter_score(operator: CallData, quarter: str) -> float | None:
    QUARTERS = {
        "Q1": [1, 2, 3],
        "Q2": [4, 5, 6],
        "Q3": [7, 8, 9],
        "Q4": [10, 11, 12],
    }

    months = QUARTERS.get(quarter)
    if not months:
        return None

    scores = []

    for month in months:
        if operator.month == month and operator.mark is not None:
            scores.append(float(operator.mark))
        else:
            archived = ScoresForMonth.objects.filter(
                operator=operator,
                month=str(month),
                mark__isnull=False
            ).first()

            if archived:
                scores.append(float(archived.mark))

    return round(mean(scores), 1) if scores else None

def get_current_quarter():
    month = datetime.now().month
    if month in [1, 2, 3]:
        return "Q1"
    elif month in [4, 5, 6]:
        return "Q2"
    elif month in [7, 8, 9]:
        return "Q3"
    else:
        return "Q4"

def get_month_names_for_quarter(quarter: str):
    mapping = {
        "Q1": ["Янв", "Фев", "Мар"],
        "Q2": ["Апр", "Май", "Июнь"],
        "Q3": ["Июль", "Авг", "Сен"],
        "Q4": ["Окт", "Ноя", "Дек"],
    }
    return mapping.get(quarter, ["—", "—", "—"])

def get_criteria_penalties(operator, quarter):
    QUARTERS = {
        "Q1": [1, 2, 3],
        "Q2": [4, 5, 6],
        "Q3": [7, 8, 9],
        "Q4": [10, 11, 12],
    }

    group = str(operator.group) if operator.group else ""

    criteria_titles = {
        "greeting": "<div style='margin-top:5px; margin-bottom:10px;'>Приветствие</div>" if group == "1009" else "Приветствие / Прощание",
        "hearing": "Внимательное слушание",
        "question": "Исп. уточняющих вопросов",
        "interest": "Заинтересованность в проблеме",
        "cons": "Понятное пред.. информации" if group == "1009" else "Консультация / Понятное пред..",
        "polite": "Доброжелательн.. Вежливость",
        "speech": "Грамотная<br>речь",
        "note": 'Установка на "Удержание"' if group == "1009" else "Оформление и обработка заявок",
        "warning": "Предупреждение об ожидании",
        "emotion": "Скорость обслуживания" if group == "1009" else "Эмоц. окраска голоса / Темп д..",
        "solution": "<div style='margin-top:5px; margin-bottom:10px;'>Прощание</div>" if group == "1009" else "Быстрое решение вопроса",
    }

    months = QUARTERS.get(quarter, [])
    result = []

    for criterion, title in criteria_titles.items():
        criterion_penalties = []

        for month in months:
            # берём данные либо из CallData, либо из архива
            if operator.month == month:
                source = operator
            else:
                source = ScoresForMonth.objects.filter(operator=operator, month=str(month)).first()
                if not source:
                    criterion_penalties.append(0)
                    continue

            penalties = 0
            for i in range(1, 11):
                val = getattr(source, f"{criterion}{i}", None)
                if val == 2:
                    penalties += 1
                elif val == 1:
                    penalties += 2

            criterion_penalties.append(penalties)

        result.append({"title": title, "data": criterion_penalties})

    return result

def get_total_penalty_sum(operator, quarter):
    """
    Возвращает общее количество ошибок по всем критериям за указанный квартал.
    """
    criteria_data = get_criteria_penalties(operator, quarter)
    total = 0

    for item in criteria_data:
        total += sum(item["data"])  # item["data"] = список из 3 месяцев

    return total

def get_penalties_per_quarter(operator):
    return [
        get_total_penalty_sum(operator, "Q1"),
        get_total_penalty_sum(operator, "Q2"),
        get_total_penalty_sum(operator, "Q3"),
        get_total_penalty_sum(operator, "Q4"),
    ]


def get_comments_for_quarter(operator, quarter):
    if not operator:
        return []

    QUARTERS = {
        "Q1": [1, 2, 3],
        "Q2": [4, 5, 6],
        "Q3": [7, 8, 9],
        "Q4": [10, 11, 12],
    }

    MONTH_NAMES = {
        1: "Январь-Февраль", 2: "Февраль-Март", 3: "Март-Апрель",
        4: "Апрель-Май", 5: "Май-Июнь", 6: "Июнь-Июль",
        7: "Июль-Август", 8: "Август-Сентябрь", 9: "Сентябрь-Октябрь",
        10: "Октябрь-Ноябрь", 11: "Ноябрь-Декабрь", 12: "Декабрь-Январь"
    }

    months = QUARTERS.get(quarter, [])
    comments = []

    # CallData
    call_entries = CallData.objects.filter(name=operator, month__in=months)
    for entry in call_entries:
        for i in range(1, 11):
            comment = getattr(entry, f'comment{i}', '')
            if comment:
                comments.append({
                    "text": comment,
                    "month": int(entry.month),
                    "month_name": MONTH_NAMES.get(int(entry.month), "Неизвестно")
                })

    # ScoresForMonth
    score_entries = ScoresForMonth.objects.filter(operator__name=operator.name, month__in=months)
    for entry in score_entries:
        for i in range(1, 11):
            comment = getattr(entry, f'comment{i}', '')
            if comment:
                comments.append({
                    "text": comment,
                    "month": int(entry.month),
                    "month_name": MONTH_NAMES.get(int(entry.month), "Неизвестно")
                })

    return comments

def get_mistakes_for_quarter(operator, quarter):
    if not operator:
        return []

    QUARTERS = {
        "Q1": [1, 2, 3],
        "Q2": [4, 5, 6],
        "Q3": [7, 8, 9],
        "Q4": [10, 11, 12],
    }

    months = QUARTERS.get(quarter, [])
    mises = []

    TYPE_MAP = {
        1: "severe",
        2: "major",
        3: "minor"
    }

    # CallData
    call_entries = CallData.objects.filter(name=operator, month__in=months)
    for entry in call_entries:
        for i in range(1, 4):
            count = getattr(entry, f'mis{i}', 0) or 0
            for _ in range(count):  # 🔁 добавим N раз, если misN = N
                mises.append({
                    "type": TYPE_MAP.get(i, "unknown"),
                    "month": int(entry.month),
                })

    # ScoresForMonth
    score_entries = ScoresForMonth.objects.filter(operator__name=operator.name, month__in=months)
    for entry in score_entries:
        for i in range(1, 4):
            count = getattr(entry, f'mis{i}', 0) or 0
            for _ in range(count):
                mises.append({
                    "type": TYPE_MAP.get(i, "unknown"),
                    "month": int(entry.month),
                })

    return mises


def list2(request):
    selected_name = request.GET.get("operator-name")
    selected_quarter = request.GET.get("quarter", get_current_quarter())
    operator = None
    chart_score = None
    quarter_penalties = 0
    criteria_data = []
    operators = CallData.objects.all().order_by('name')
    monthly_marks = []
    quarter_comments = []
    quarter_mises = []

    MONTH_NAME_TO_NUMBER = {
        "Янв": 1, "Фев": 2, "Мар": 3, "Апр": 4,
        "Май": 5, "Июнь": 6, "Июль": 7, "Авг": 8,
        "Сен": 9, "Окт": 10, "Ноя": 11, "Дек": 12
    }

    if selected_name:
        operator = get_object_or_404(CallData, name=selected_name)
        raw_score = get_quarter_score(operator, selected_quarter)
        chart_score = str(raw_score).replace('.', ',') if raw_score is not None else None
        criteria_data = get_criteria_penalties(operator, selected_quarter)
        quarter_comments = get_comments_for_quarter(operator, selected_quarter)
        quarter_mises = get_mistakes_for_quarter(operator,selected_quarter)
        quarter_penalties = get_penalties_per_quarter(operator) if operator else [0, 0, 0, 0]

        months = get_month_names_for_quarter(selected_quarter)
        for month in months:
            month_num = MONTH_NAME_TO_NUMBER.get(month)
            score_entry = ScoresForMonth.objects.filter(operator__name=selected_name, month=month_num).first()
            if score_entry and score_entry.mark is not None:
                monthly_marks.append(round(score_entry.mark, 1))
            else:
                call_entry = CallData.objects.filter(name=selected_name, month=month_num).first()
                if call_entry and call_entry.mark is not None:
                    monthly_marks.append(round(call_entry.mark, 1))
                else:
                    monthly_marks.append(0)


    context = {
        "operator": operator,
        "selected_quarter": selected_quarter,
        "chart_score": chart_score,
        "month_names": get_month_names_for_quarter(selected_quarter),
        "criteria_data": json.dumps(criteria_data, ensure_ascii=False),
        "operators": operators,
        "monthly_marks": [round(float(mark), 1) for mark in monthly_marks],
        "quarter_comments": json.dumps(quarter_comments),
        "quarter_mises":json.dumps(quarter_mises),
        "quarter_penalties": quarter_penalties,
    }

    return render(request, 'project/list2.html', context)


def update_page(request):
    context = {
        "title":"Update Page"
    }
    return render(request, 'components/update_page.html',context)

def update_process(request, action):
    old_stdout = sys.stdout
    mystdout = StringIO()
    sys.stdout = mystdout

    try:
        print(f"🔄 Начало обновления: {action}")

        if action == "current":
            print("▶ Обновляем текущий месяц...\n")
            update_call_data()
        elif action == "archive":
            print("▶ Обновляем архив...\n")
            get_archive()
        else:
            print("❌ Неизвестная команда.\n")

        print("\n✅ Обновление завершено.\n")

    except Exception as e:
        print(f"\n❗ Ошибка: {e}\n")
    finally:
        sys.stdout = old_stdout

    return HttpResponse(f"<pre>{mystdout.getvalue()}</pre>", )


# Для теста добавлен
