from django import forms
from linkmain.models import link

class linkForm(forms.ModelForm):
    class Meta:
        model=link
        fields=('title', 'url')

class RegisterForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()

