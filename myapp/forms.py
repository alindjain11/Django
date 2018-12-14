from django import forms
from .models import *

class Nameform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter username'}
    ),required=True, max_length=30)

    email=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter email'}
    ),required=True, max_length=30)

    first_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter first name'}
    ),required=True, max_length=30)

    last_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter last name'}
    ),required=True, max_length=30)

    password=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Enter password'}
    ),required=True, max_length=30)

    confirm_password=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Enter password again'}
    ),required=True, max_length=30)

    class Meta:
        model= User
        fields=['username','email','first_name', 'last_name', 'password', 'confirm_password']
    # def clean_email(self):
    #     email=self.cleaned_data['email']
    #     try:
    #         ema=validate_email(email)
    #     except:
    #         raise forms.ValidationError("email is not valid")
    #     return email

    def clean_confirm_password(self):
        p=self.cleaned_data['password']
        cp=self.cleaned_data['confirm_password']
        if(p!=cp):
            raise forms.ValidationError('Passwords are not same')
        else:
            if(len(p)<8):
                raise forms.ValidationError('password at least 8 characteers')
            if(p.isdigit()):
                raise forms.ValidationError('passowrd must contain characteers')

class ChangePassword(forms.ModelForm):
    old_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class':'form-control'}),
    label="old Password",
    required=True)
    new_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class':'form-control'}),
    label="New Password",
    required=True)
    confirm_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class':'form-control'}),
    label="Confirm Password",
    required=True)

    class Meta:
        model=User
        fields=['old_password', 'new_password', 'confirm_password']




    """employee=forms.CharField(label='Naming', max_length=100)
    employee_id=forms.CharField(label='Suggest', max_length=100)
    employee_num= forms.IntegerField(label='Number', max_value=10)
    competency=forms.CharField(label='Competency', max_length=100)
"""
