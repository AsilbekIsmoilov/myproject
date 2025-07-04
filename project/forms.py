from django import forms
from .models import *

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule1000
        fields = ['title', 'pdf_file']

class ManagementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['title', 'pdf_file']



class Schedule1009Form(forms.ModelForm):
    class Meta:
        model = Schedule1009
        fields = ['title', 'pdf_file']

class ManagementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['title', 'pdf_file']

class Management112Form(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['title', 'pdf_file']


class Schedule112Form(forms.ModelForm):
    class Meta:
        model = Schedule112
        fields = ['title', 'pdf_file']

class ManagementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['title', 'pdf_file']
