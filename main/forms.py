from django import forms
from .models import Comments

class comments_section(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'Comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'email', 'placeholder': 'Email'}),
            'Comment': forms.Textarea(attrs={'class': 'Commentbox', 'placeholder': 'Type Your Comment'})
        }