from django.shortcuts import render

# Create your views here.
from .serializers import *
from.models import *
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import Response

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

class ContactData(generics.ListAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

    def get_queryset(self):
        queryset=Contact.objects.filter(user=request.user)

@csrf_exempt
@api_view(['POST'])
def CreateContact(request):
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        fname=data['fname']
        lname=data['lname']
        data_email=data['email']
        ph_no=data['phone']
        passwrd=data['password']
        try:
            usr=User.objects.create(email=data_email,first_name=fname,last_name=lname,password=passwrd)
        except Exception as e:
            return Response({"msg":str(e)},status=500)
        try:
            cntact=Contact.objects.create(user=usr,phone=ph_no)
        except Exception as e:
            return Response({"msg":str(e)},status=500)
        return Response({
            "success":"New contact is created",
            "first_name":usr.first_name,
            "last_name":usr.last_name,
            "email":usr.email
        })
