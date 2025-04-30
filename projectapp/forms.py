from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(
        label="Comments",
        widget=forms.Textarea(attrs={
            'placeholder': "Write a comment here...",
            'class': "form-control",
            'rows': 2,
        })
    )
    class Meta:
        model = Review
        fields = ['rating', 'comment']