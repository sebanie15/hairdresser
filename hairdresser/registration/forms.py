
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Salon
from django.utils.translation import gettext as _


class SalonForm(forms.Form):
    required_css_class = "required"
    salons = Salon.objects.all().order_by('-name')
    choices = []

    for salon in salons:
        choices.append((str(salon.pk), salon.name))

    CHOICES = set(choices)

    selected_salon = forms.ChoiceField(choices=CHOICES, label=_("Select salon"))

    def get_salon_pk(self):
        # print(self.selected_salon[1])
        return self.cleaned_data['selected_salon']


