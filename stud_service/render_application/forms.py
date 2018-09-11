from render_application import models as ra_models
from django import forms


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ra_models.Application
        fields = '__all__'

