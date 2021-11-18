from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
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
from django.contrib import messages
from .forms import UserLoginForm, PollingForm
# Create your views here.


class BasePageView(View):
    
    def get(self, request, **kwarg):
        context = {
            'polling_units_relults': AnnouncedPuResults.objects.all(),
            'agents': Agentname.objects.all()
        }
        
        return render(request,"home.html", context)
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            phone = form.cleaned_data['phone']
            try:
                print (phone)
                user = Agentname.objects.get(email=email, phone=phone)
                if user.email == email and user.phone==phone:
                    request.session['is_active'] = True
                    return redirect('store-result')
            except Exception as e:
                messages.error(
                    request, 'Email phone/number does not match')
        return redirect('base')



class LgaResultsView(View):
    
    def get(self, request, **kwarg):
        key = request.GET.get('lg')
        context = {
            'agents': Agentname.objects.all()
        }
        context['lgas'] = Lga.objects.all()
        if key != "":
            data = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=key)
            context["lga_results"] = data        
            return render(request,"lga.html", context)
        
        
        return render(request,"lga.html", context)

   
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            phone = form.cleaned_data['phone']
            try:
                print (phone)
                user = Agentname.objects.get(email=email, phone=phone)
                if user.email == email and user.phone==phone:
                    request.session['is_active'] = True
                    return redirect('store-result')
            except Exception as e:
                messages.error(
                    request, 'Email phone/number does not match')
        return redirect('base')

class StoreResultsView(View):
    
    def get(self, request, **kwarg):
        if 'polling_unit' in request.session:
            polling_unit = request.session['polling_unit']
            polling = PollingUnit.objects.get(uniqueid=int(polling_unit))

            context = {
                'polling_unit': polling,
                'polling_form': PollingForm() 
            }
        
        return render(request,"store_result.html", context)




