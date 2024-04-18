from django.forms import ModelForm
from .models import *

#create a new model
class AddBabeForm(ModelForm):
    class Meta:
        model = Babe
        fields = '__all__'
