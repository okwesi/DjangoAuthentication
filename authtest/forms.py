from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#this field changes the usercreation form from its default and adds the name and email fields to the signup form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


#this functions enables us to change the the default username and password to deafult bootstrap form styling
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

