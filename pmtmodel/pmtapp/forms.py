from django import forms
from django.forms import ModelForm
from .models import DemographicInformation


class DemographicInformationForm(ModelForm):
    class Meta:
        model = DemographicInformation
        fields = "__all__"
