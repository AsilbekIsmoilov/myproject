from django.contrib import admin
from .models import CallData, ScoresForMonth, QuarterScores


class CallDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'bl', 'group', 'mark','month')
    search_fields = ('name',)
    ordering = ('name',)


class ScoresForMonthAdmin(admin.ModelAdmin):
    # Указываем поля для отображения в админке
    list_display = ('name', 'operator', 'id','mark','month')  # Добавить другие поля, если необходимо
    search_fields = ('name',)  # Поиск по имени
    list_filter = ('operator',)  # Фильтрация по оператору
    ordering = ('name',)  # Сортировка по имени

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('name')

class QuarterScoresAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Поиск по имени
    list_filter = ('operator',)  # Фильтрация по оператору
    ordering = ('name',)  # Сортировка по имени
    list_display = ('name','operator','group','quarterscore1','quarterscore2','quarterscore3','quarterscore4')

admin.site.register(CallData, CallDataAdmin)
admin.site.register(ScoresForMonth,ScoresForMonthAdmin)
admin.site.register(QuarterScores,QuarterScoresAdmin)

