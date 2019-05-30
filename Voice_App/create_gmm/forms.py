from django import forms
from .models import AcousticModel

class AcousticForm(forms.ModelForm):
    class Meta:
        model = AcousticModel
