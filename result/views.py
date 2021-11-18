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
class BasePageView(View):
    
    def get(self, request, **kwarg):
        context = {

        }
        
        context['polling_units_relults'] = AnnouncedPuResults.objects.all(),
        return render(request,"home.html", context)


class LgaResultsView(View):
    
    def get(self, request, **kwarg):
        key = request.GET.get('lg')
        context = {

        }
        if key != "":
            data = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=key)
            context["lga_results"] = data        
            return render(request,"lga.html", context)
        
        
        return render(request,"lga.html", context)
