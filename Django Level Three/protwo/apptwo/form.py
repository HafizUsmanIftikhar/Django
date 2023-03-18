from django import forms
from apptwo.models import users

class NewUserForm(forms.ModelForm):
    class Meta():
        model=users
        fields='__all__'
