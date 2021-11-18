from django.urls import path
from .views import BasePageView, LgaResultsView


urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('lga/', LgaResultsView.as_view(), name='lga-result'),

]
