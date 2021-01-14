from django import forms

from .models import Doner, Resource

class DonerForm(forms.ModelForm):

    class Meta:
        model = Doner
        fields = ('name', 'cpf', 'blood_type', 'birth_date', 'phone_number',)

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = ('supply',)