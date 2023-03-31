from django import forms
from .models import *

class uform(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__"
class cform(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"