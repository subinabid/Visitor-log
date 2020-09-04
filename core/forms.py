from django import forms
from .models import ntpcusers

class Visitors(forms.ModelForm):
    class Meta:
        model = ntpcusers
        fields = ('empid', 'fname','mname','lname','designation','department','location','remarks' )        



