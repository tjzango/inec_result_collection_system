from django.urls import path
from .views import BasePage


urlpatterns = [
    path('', BasePage, name='base'),
]
