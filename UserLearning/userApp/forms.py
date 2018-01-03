from django import forms
from django.contrib.auth.models import User
from userApp.models import UserProfileInfo

#class starting from here
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolioSite', 'profilePics')