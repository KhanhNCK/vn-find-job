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
from .utils import get_data_ho_so
import json
from apps.seeker.models import HoSoUngTuyen

@app.task
def gui_hoso_mana(id):
    hoso = HoSoUngTuyen.objects.get(id=id)
    data = get_data_ho_so(id)
    hashdata = get_request_hash_data(data,settings.SECURITY_KEY_MANA_JOB)
    url = settings.MANAGER_URL + "quanlycongtacvien/user-register-ctv/"
    r = requests.post(url, json=hashdata)
    if r.status_code==200:
        hoso.is_send_mana = True
        hoso.save()


@shared_task
def filter_hoso_chua_gui_mana():
    hoso = HoSoUngTuyen.objects.filter(is_send_mana=False)
    for obj in hoso:
        gui_hoso_mana.delay(obj.id)