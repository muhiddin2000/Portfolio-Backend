from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from .pagination import MyPagination


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
