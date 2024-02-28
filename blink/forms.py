from django import forms
from blink.models import Links

class Linkform(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['link', 'newlink']
