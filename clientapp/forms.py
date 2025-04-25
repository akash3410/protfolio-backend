from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ClientInfo
from phonenumber_field.formfields import PhoneNumberField

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': "Enter your username", 'class': "form-control"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': "Enter a valid email", 'class': "form-control"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': "Enter your password", 'class': "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': "Confirm your password", 'class': "form-control"})
    )
    is_staff = forms.BooleanField(
        required=False,
        label="You are Client ?",
        widget=forms.CheckboxInput(attrs={'class': "form-check-input"})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': "Enter your username", 'class': "form-control"})
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': "Enter your password", 'class': "form-control"})
    )

class ClientInfoForm(forms.ModelForm):
    full_name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={'placeholder': "Full Name", 'class': "form-control"})
    )
    bio = forms.CharField(
        label="Bio",
        widget=forms.TextInput(attrs={'placeholder': "Write your bio", 'class': "form-control"})
    )
    company = forms.CharField(
        label="Company",
        widget=forms.TextInput(attrs={'placeholder': "Your Company", 'class': "form-control"})
    )
    designation = forms.CharField(
        label="Designation",
        widget=forms.TextInput(attrs={'placeholder': "Your Designation", 'class': "form-control"})
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'placeholder': "Address EX: Mirpur, Dhaka-1216", 'class': "form-control"})
    )
    phone = PhoneNumberField(
        label="Phone Number",
        widget=forms.TextInput(attrs={'placeholder': "Phone Ex: +8801xxxxxxxxx", 'class': "form-control"})
    )
    dob = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={'placeholder': "YYYY-MM-DD", 'class': "form-control", 'type': 'date'})
    )
    profile_photo = forms.ImageField(
        label="Profile Picture",
        widget=forms.ClearableFileInput(attrs={'class': "form-control"})
    )
    cover_photo = forms.ImageField(
        label="Cover Photo",
        widget=forms.ClearableFileInput(attrs={'class': "form-control"})
    )
    class Meta:
        model = ClientInfo
        fields = ['full_name', 'bio', 'company', 'designation', 'address', 'phone', 'dob', 'profile_photo', 'cover_photo']