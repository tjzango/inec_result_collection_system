from .models import Agentname
from .forms import UserLoginForm

def user(request):
    try:
        # email = request.session['user_email']
        # agentdata = Agentname.objects.get(email=email)
        # if agentdata:'''
        return {
        #        'agentdata': agentdata,
                'form': UserLoginForm(),
            }
    except Agentname.DoesNotExist:
        return {'agentdata': False}
