from django import forms
from .models import CustomUser, Object


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'accessed_objects']


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['file_name', 'size', 'type', 'owner']
