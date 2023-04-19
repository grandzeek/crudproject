from django import forms
from crudapp.models import Student


class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email']
