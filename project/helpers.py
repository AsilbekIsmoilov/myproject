import os
import re
import requests
import subprocess
import zipfile
from django.conf import settings
from django.core.files.base import File
from .models import CallData, Records
from io import BytesIO
from django.utils.timezone import now, timedelta
from dotenv import load_dotenv
load_dotenv()

def get_operator_from_request(request):
    name_from_url = request.GET.get("operator-name")
    if name_from_url:
        request.session["selected_operator"] = name_from_url
        return name_from_url
    return request.session.get("selected_operator")




API_BASE_URL = os.getenv("API_BASE_URL")
FFMPEG_PATH = r"C:\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"

def extract_zip(call_code):
    temp_dir = os.path.join(settings.BASE_DIR, "temp_audio")
    os.makedirs(temp_dir, exist_ok=True)

    zip_code_raw = call_code.split('_')[0]
    zip_code = re.sub(r"^0+", "", zip_code_raw)

    zip_url = f"{API_BASE_URL}{zip_code}"
    response = requests.get(zip_url)
    if response.status_code != 200:
        print(f"Not found zip: {zip_code}")
        return None

    try:
        with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
            for name in zip_file.namelist():
                if call_code in name and name.endswith(".spx"):
                    spx_path = os.path.join(temp_dir, f"{call_code}.spx")
                    with zip_file.open(name) as zf, open(spx_path, "wb") as f:
                        f.write(zf.read())
                    print(f".spx taked : {name}")
                    return spx_path

            print(f"not found .spx in zip file: {call_code}")
            return None

    except zipfile.BadZipFile:
        print(f"Invalid zip file: {zip_code}")
        return None

def extract_and_download_records():
    temp_dir = os.path.join(settings.BASE_DIR, "temp_audio")
    mp3_dir = os.path.join(settings.MEDIA_ROOT, "records")
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(mp3_dir, exist_ok=True)

    for cd in CallData.objects.all():
        for i in range(1, 11):
            comment = getattr(cd, f"comment{i}", "")
            match = re.search(r"Код звонка:\s*([\w\-]+)", comment or "")
            if not match:
                continue

            call_code = match.group(1)
            record = Records.objects.filter(call_code=call_code).first()
            if not record:
                record = Records.objects.create(operator=cd, call_code=call_code)
                print(f"New record created: {call_code} ({cd.name})")
            else:
                print(f"Already exist record: {call_code}")

            if record.record:
                continue  

            spx_path = os.path.join(temp_dir, f"{call_code}.spx")
            url = f"{API_BASE_URL}{call_code}"
            response = requests.get(url)
            if response.status_code == 200:
                with open(spx_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {call_code}")
            else:
                spx_path = extract_zip(call_code)
                if not spx_path:
                    print(f"File not found: {call_code}")
                    continue

            mp3_filename = f"{call_code}.mp3"
            mp3_path = os.path.join(mp3_dir, mp3_filename)
            command = f'"{FFMPEG_PATH}" -y -i "{spx_path}" -codec:a libmp3lame -q:a 2 "{mp3_path}"'
            result = subprocess.run(command, capture_output=True, text=True, shell=True)

            os.remove(spx_path)

            if result.returncode != 0 or not os.path.exists(mp3_path):
                print(f"Convert error: {call_code}")
                continue

            record.record.name = f"records/{mp3_filename}"
            record.save()
            print(f"Saved: {call_code}")



MONTH_FILE_PATH = ".current_month"

def get_actual_month_from_db():
    return CallData.objects.order_by('-id').first().month

def read_stored_month():
    if os.path.exists(MONTH_FILE_PATH):
        with open(MONTH_FILE_PATH, 'r') as f:
            return int(f.read().strip())
    return None

def write_current_month(month):
    with open(MONTH_FILE_PATH, 'w') as f:
        f.write(str(month))

def delete_all_records():
    records = Records.objects.all()
    count = 0
    for record in records:
        if record.record and os.path.isfile(record.record.path):
            try:
                os.remove(record.record.path)
            except Exception as e:
                print(f"Ошибка при удалении файла {record.record.path}: {e}")
        record.delete()
        count += 1
    print(f"Удалено {count} записей (месяц сменился).")
    return count

def delete_records_if_month_changed():
    actual_month = get_actual_month_from_db()
    stored_month = read_stored_month()

    if stored_month != actual_month:
        print(f"Месяц изменился: {stored_month} → {actual_month}")
        delete_all_records()
        write_current_month(actual_month)
    else:
        print(f"Месяц не изменился ({actual_month}) — удаление не требуется.")

