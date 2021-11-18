from django import forms
from .models import AnnouncedPuResults, Party

class UserLoginForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g haroun@gmail.com'}))
    phone = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': '*******'}))


class PollingForm(forms.ModelForm):
    party = forms.ModelChoiceField(
        required=True, queryset=Party.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = AnnouncedPuResults
        include = ('party_score')
