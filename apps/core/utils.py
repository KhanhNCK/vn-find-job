from rest_framework.serializers import Serializer
import locale
import json
import hashlib
from django.utils import timezone
from datetime import timedelta
import random
import string
from apps.company.models import TinTuyenDung
from apps.seeker.models import HoSoUngTuyen

def convert_price_to_string(price):
    return f"{price:,}"

def validate_data(schema_cls: Serializer, data: dict) -> dict:
    """Validate data using Marshmallow schema
    Return validated data if success, raise ValidationError if failed
    """
    schema = schema_cls(data=data)
    schema.is_valid(raise_exception=True)
    return schema.validated_data

def h__md5(input):
    byteInput = input.encode('utf-8')
    return hashlib.sha256(byteInput).hexdigest()

def get_request_hash_data(data_dict, secret_key):
    hash_value = data_dict
    data = json.dumps(data_dict)
    hashValue = h__md5(secret_key + data)
    hash_value['secret'] = hashValue
    return hash_value

def validate_response(data_dict, secret_key):
    secure_hash = data_dict.pop('secret')
    data = json.dumps(data_dict)
    hashValue = h__md5(secret_key + data)
    return secure_hash == hashValue


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance,trans):
    code_trans= random_string_generator()

    Klass= instance.__class__
    if trans == 1:
        qs_exists= HoSoUngTuyen.objects.filter(code_hoso=code_trans).exists()
        if qs_exists:
            return unique_order_id_generator(instance,trans)
        return code_trans
    elif trans == 2:
        qs_exists= TinTuyenDung.objects.filter(code_tin=code_trans).exists()
        if qs_exists:
            return unique_order_id_generator(instance,trans)
        return code_trans


def convert_sex(sex_gt):
    if sex_gt == 1:
        sex_gt="Nữ"
    elif sex_gt == 2:
        sex_gt = "Nam"
    else:
        sex_gt=""
    return sex_gt

def convert_tthn(hn):
    if hn == 1:
        sex_gt="Độc thân"
    elif hn == 2:
        sex_gt = "Có gia đình"
    else:
        sex_gt=""
    return sex_gt

def convert_tthn(hn):
    if hn == 1:
        hn="Độc thân"
    elif hn == 2:
        hn = "Có gia đình"
    else:
        hn=""
    return hn

def convert_hocvan(hv):
    if hv == 1:
        hv="Trên đại học"
    elif hv == 2:
        hv = "Đại học"
    elif hv == 3:
        hv = "Cao đẳng"
    elif hv == 4:
        hv = "Trung cấp"
    elif hv == 5:
        hv = "Chứng chỉ nghề "
    else:
        hv=""
    return hv

def convert_trinhdo(td):
    if td == 1:
        td="Xuất sắc"
    elif td == 2:
        td = "Giỏi"
    elif td == 3:
        td = "Khá"
    elif td == 4:
        td = "Trung bình"
    else:
        td=""
    return td

def convert_hinhthuc(td):
    if td == 1:
        td="Toàn thời gian cố định"
    elif td == 2:
        td = "Toàn thời gian tạm thời"
    elif td == 3:
        td = "Bán thời gian cố định"
    elif td == 4:
        td = "Bán thời gian tạm thời"
    elif td == 5:
        td = "Thực tập"
    elif td == 6:
        td = "Khác"
    else:
        td=""
    return td

def convert_ngoaingu(td):
    if td == "EN":
        td="Tiếng Anh"
    elif td == "JP":
        td = "Tiếng Nhật"
    elif td == "FR":
        td = "Tiếng Pháp"
    elif td == "CN":
        td = "Tiếng Trung"
    elif td == "RU":
        td = "Tiếng Nga"
    elif td == "KR":
        td = "Tiếng Hàn"
    elif td == "IT":
        td = "Tiếng Ý"
    elif td == "OTHER":
        td = "Ngoại ngữ khác"
    else:
        td=""
    return td