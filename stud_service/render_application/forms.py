from render_application import models as ra_models
from django import forms

EnterFirstLabel = 'Заявление от (имя)'
EnterSecondLabel = '(фамилия)'
GroupLabel = 'Группа'
PhoneLabel = 'Телефон'
ReasonLabel = 'По причине'
MoneyLabel = 'В размере'


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ra_models.Application
        fields = [
            'first_name',
            'second_name',
            'group',
            'phone',
            'reason',
            'money'
        ]

        labels = {
            'first_name': EnterFirstLabel,
            'second_name': EnterSecondLabel,
            'group': GroupLabel,
            'phone': PhoneLabel,
            'reason': ReasonLabel,
            'money': MoneyLabel
        }

