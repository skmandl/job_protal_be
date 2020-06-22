from rest_framework import serializers
from .models import *

class CompanySerialize(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

class RecuirementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recuirement
        fields=('id','job_detail','name')

class ResponsibilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Responsibilities
        fields=('id','job_detail','name')

class JobDetailSerializer(serializers.ModelSerializer):
    recuirements=serializers.SerializerMethodField()
    responsibilities=serializers.SerializerMethodField()

    def get_responsibilities(self,obj):
        resp=Responsibilities.objects.filter(job_detail=obj)
        resp_data=ResponsibilitiesSerializer(resp,many=True).data
        return resp_data
    def get_recuirements(self,obj):
        rec=Recuirement.objects.filter(job_detail=obj)
        rec_data=RecuirementSerializer(rec,many=True).data
        return rec_data

    class Meta:
        model=JobDetail
        fields=('id','overview','job','salary_from','salary_to','recuirements','responsibilities')

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','types')

class JobSerializer(serializers.ModelSerializer):
    degree=serializers.StringRelatedField()
    company_detail=serializers.SerializerMethodField()
    # description=serializers.SerializerMethodField()

    # def get_description(self,obj):
    #     des=JobDetail.objects.filter(job=obj)
    #     des_data=JobDetailSerializer(des,many=True).data
    #     return des_data


    def get_company_detail(self,obj):
        print('obj=',obj)
        cmp=Company.objects.filter(id=obj.company.id)
        print('company=',cmp)
        cmp_data=CompanySerialize(cmp,many=True).data
        return cmp_data
    class Meta:
        model=JobList
        fields=('id','job_category','job_type','post_name','company_detail','degree','is_active','last_date')
