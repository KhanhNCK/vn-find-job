from rest_framework import serializers


class AddDataThanhPhoAPISer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.IntegerField()
    group = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()


class AddDataNgheNghiepAPISer(serializers.Serializer):
    ten_nganh_nghe = serializers.CharField()
    code_nganh_nghe = serializers.IntegerField()
    thong_tin_ve_nghe = serializers.CharField()
