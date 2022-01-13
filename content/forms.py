from django.forms import ModelForm
from .models import *

class SlamForm(ModelForm):
    class Meta:
        model = Slamm
        fields =['name','blood','t','mail','address','contact', 'contact1']
