from django import forms
from .models import *

class Nameform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        






    """employee=forms.CharField(label='Naming', max_length=100)
    employee_id=forms.CharField(label='Suggest', max_length=100)
    employee_num= forms.IntegerField(label='Number', max_value=10)
    competency=forms.CharField(label='Competency', max_length=100)
"""
