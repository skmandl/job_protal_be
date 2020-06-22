from django.shortcuts import render

# Create your views here.
from .serializers import *
from.models import *

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

class CompanyList(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerialize


class JobCategory(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=Categoryserializer


class JobDetailView(ModelViewSet):
    queryset=JobList.objects.all()
    serializer_class=JobSerializer

    def get_queryset(self):
        catg=self.request.query_params.get('category')
        if catg is not None:
            job=JobList.objects.filter(job_category=Category.objects.get(pk=catg))
        else:
            job=JobList.objects.all()
        
        return job


class DescriptionView(ModelViewSet):
    queryset=JobDetail.objects.all()
    serializer_class=JobDetailSerializer

    def get_queryset(self):
        jobg=self.request.query_params.get('job')
        if jobg is not None:
            queryset=JobDetail.objects.filter(job=JobList.objects.get(pk=jobg))
        else:
            queryset=JobDetail.objects.all()
        return queryset