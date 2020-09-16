from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ntpcuser, externaluser, meeting

class NTPCVisitors(forms.ModelForm):
    class Meta:
        model = ntpcuser
        fields = ('empid', 'fname','mname','lname','designation','department','location','remarks' )        

class ExternalVisitors(forms.ModelForm):
    class Meta:
        model = externaluser
        fields = '__all__'

class Meeting(forms.ModelForm):
    class Meta:
        model = meeting
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