from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('social', SocialViewset)
router.register('profile', ProfileViewset)
router.register('portfolio', PortfolioViewset)
router.register('info', InfoViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('visitors', MyVisitors.as_view())
]
