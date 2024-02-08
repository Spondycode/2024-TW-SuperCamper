from django.forms import ModelForm
from .models import InboxMessage
from django import forms

class InboxNewMessageForm(ModelForm):
    class Meta:
        model = InboxMessage
        fields = ['body']
        labels = {
            'body': (''),
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your message here...'}),
        }