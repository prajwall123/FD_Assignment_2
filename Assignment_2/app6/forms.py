from django import forms
from app6.models import Accounts
class inputform(forms.ModelForm):
    class Meta:
        model=Accounts
        fields=['firstname','lastname','aadhaar','phone']