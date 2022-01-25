from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Chat
        exclude = ("user", )