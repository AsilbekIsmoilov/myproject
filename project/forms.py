from django import forms
from .models import *

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['code','title', 'pdf_file']

class ManagementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['title', 'pdf_file']

