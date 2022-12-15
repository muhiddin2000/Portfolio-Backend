from rest_framework.serializers import ModelSerializer
from .models import *


class SocialLinkSerializers(ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PortfolioSerializers(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class VisitorsSerializers(ModelSerializer):
    class Meta:
        model = Visitors
        fields = '__all__'


class InfoSerializers(ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
