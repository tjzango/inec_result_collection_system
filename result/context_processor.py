from .models import Agentname


def user(request):
    try:
        email = request.session['user_email']
        agentdata = Agentname.objects.get(email=email)
        if agentdata:
            return {
                'agentdata': agentdata,
            }
    except Agentname.DoesNotExist:
        return {'agentdata': False}
