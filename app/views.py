from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from .pagination import MyPagination
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class SocialViewset(ModelViewSet):
    queryset = SocialLink.objects.all().order_by('-id')[:1]
    serializer_class = SocialLinkSerializers


class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all().order_by('-id')[:1]
    serializer_class = ProfileSerializers


class PortfolioViewset(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializers
    pagination_class = MyPagination


class InfoViewset(ModelViewSet):
    queryset = Info.objects.all().order_by('-id')[:1]
    serializer_class = InfoSerializers


class MyVisitors(APIView):
    def get(self, request):
        data = Visitors.objects.get(id=1)
        data.count=data.count+1
        data.save()
        mydata = Visitors.objects.get(id=1)
        return Response({'count':mydata.count})
