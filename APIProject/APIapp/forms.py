from django import forms
from .models import student,Movie


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        field = '__all__'