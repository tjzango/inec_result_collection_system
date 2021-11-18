from django.urls import path
from .views import BasePageView, LgaResultsView, StoreResultsView


urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('lga/', LgaResultsView.as_view(), name='lga-result'),
    path('store/', StoreResultsView.as_view(), name='store-result'),
    
]
