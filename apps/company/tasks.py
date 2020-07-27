from __future__ import absolute_import, unicode_literals

from datetime import timedelta
import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
import time
from vnjobfind.celery import app
from celery.schedules import crontab
from celery import shared_task
_logger = get_task_logger(__name__)
from apps.users.models import User
from apps.core.utils import get_request_hash_data
# from .models import BankAccount, LenhRutTien
from datetime import datetime
from .utils import get_data_tin_tuyendung
import json
from apps.company.models import TinTuyenDung

@app.task
def gui_tin_tuyen_dung_mana(id):
    tin_td = TinTuyenDung.objects.get(id=id)
    data = get_data_tin_tuyendung(id)
    hashdata = get_request_hash_data(data,settings.SECURITY_KEY_MANA_JOB)
    url = settings.MANAGER_URL + "company/api-nhan-tin-tuyendung/"
    r = requests.post(url, json=hashdata)
    if r.status_code==200:
        tin_td.is_send_mana = True
        tin_td.save()
    print(r.status_code)
    print(hashdata)


@shared_task
def filter_hoso_chua_gui_mana():
    tin_td = TinTuyenDung.objects.filter(is_send_mana=False)
    for obj in tin_td:
        gui_tin_tuyen_dung_mana.delay(obj.id)