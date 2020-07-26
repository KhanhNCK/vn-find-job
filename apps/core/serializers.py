from rest_framework import serializers


class AddDataThanhPhoAPISer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.IntegerField()
    group = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()


class AddDataNgheNghiepAPISer(serializers.Serializer):
    name_job = serializers.CharField()
    job_info = serializers.CharField()
    code_job = serializers.IntegerField()


class SearchHomeAPISer(serializers.Serializer):
    key_job = serializers.CharField(allow_blank=True)
    nganh_nghe = serializers.IntegerField()
    thanh_pho = serializers.IntegerField()