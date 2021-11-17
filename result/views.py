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
        key = request.GET.get('lg')
        context = {

        }
        context['lgas'] = Lga.objects.all()
        if key != "":
            data = PollingUnit.objects.filter(uniqueid=key)
            context["lga_results"] = data        
            return render(request,"lga.html", context)
        
        context['polling_units_relults'] = AnnouncedPuResults.objects.all(),
        return render(request,"lga.html", context)

    