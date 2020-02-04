from django import forms
from .models import People
from django.forms import ModelForm
class PeopleForm (ModelForm):
    class Meta:
        model = People
        fields =  ['name', 'tel' ]
