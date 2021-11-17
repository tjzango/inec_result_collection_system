from django.shortcuts import render
from django.views import View
from .models import (
    Lga,
    States,
    Party,
    Ward,
    AnnouncedWardResults,
    PollingUnit,
    Agentname,
    AnnouncedPuResults,
    AnnouncedLgaResults,
    AnnouncedStateResults,
)

# Create your views here.
class BasePage(View):
    
    def get(self, request, **kwarg):
        context = {
            'polling_units': AnnouncedPuResults.objects.all()
        }
        return render(request,"home.html")