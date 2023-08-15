from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "register_class", "placeholder": "Firstname"}),
							   max_length=30)
	lastname = forms.CharField(widget=forms.TextInput(attrs={"class": "register_class", "placeholder": "Lastname"}),
							   max_length=30)
	age = forms.CharField(widget=forms.NumberInput(attrs={"class": "register_class", "placeholder": "Age"}),
						  max_length=3)
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "register_class", "placeholder": "Email"}),
							 max_length=30)
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={"class": "register_class", "placeholder": "Password"}), min_length=8,
		max_length=25)
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class": "register_class", "placeholder": "Confirm Password"}), min_length=8,
		max_length=25)


class UserLoginForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "register_class", "placeholder": "Email"}),
								max_length=30)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={"class": "register_class", "placeholder": "Password"}), min_length=8,
		max_length=25)
