from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ntpcusers, ntpcvisitors

class Visitors(forms.ModelForm):
    class Meta:
        model = ntpcusers
        fields = ('empid', 'fname','mname','lname','designation','department','location','remarks' )        

class Meetings(forms.ModelForm):
    class Meta:
        model = ntpcvisitors
        fields = '__all__'
        labels = {
            'empid' : _('Employee ID'),
            'timein' : _('In time'), 
            'timeout' : _('Out time'), 
        }
        field_classes = {
            'timein': forms.SplitDateTimeField,
            'timeout': forms.SplitDateTimeField,
        }

