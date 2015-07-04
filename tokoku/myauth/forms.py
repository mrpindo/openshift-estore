"""
Forms for django-signup.
"""

from django.forms import ModelForm
from django import forms
#from django.contrib.auth.models import User
from myauth.models import MyUser, SignUpProfile

class SignUpForm(ModelForm):

    def clean_email(self):
        # Check email address is not already in use
        if MyUser.objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError('Email address already in use.')
        return self.cleaned_data['email']

    class Meta:
        model = SignUpProfile
        fields = ('email', )


attrs_dict = {'class': 'required'}

class ActivateForm(ModelForm):


    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=("Password (again)"))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    class Meta:
        model = MyUser
        fields = ('password1', )
