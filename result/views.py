from django.shortcuts import render
from django.views import View


# Create your views here.
class BasePage(View):
    
    def get(self, request, **kwarg):
        return render(request,"home.html")