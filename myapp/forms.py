from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'placeholder': "Your Name", 'class': "form-control"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': "Your Email", 'class': "form-control"})
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={'placeholder': "Subject", 'class': "form-control"})
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'placeholder': "Message", 'class': "form-control", 'rows': 4})
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', ]