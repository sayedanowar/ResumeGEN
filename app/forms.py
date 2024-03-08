from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms

# Create your forms here.

class SignupForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control', 'onkeyup':'validateEmail()', 'placeholder':'Email', 'required':True}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username':'', 'email':''}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'required':True})
    }
        
class LoginForm(AuthenticationForm):
    username = UsernameField(label='', widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))