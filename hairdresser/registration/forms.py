from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

from .models import Salon, Visit
from django.utils.translation import gettext as _


class SalonForm(forms.Form):
    required_css_class = "required"
    salons = Salon.objects.all().order_by('pk')
    choices = []

    for salon in salons:
        choices.append((str(salon.pk), salon.name))

    CHOICES = tuple(choices)

    print('-----<<<<<<<<<<<>>>>>>>>>>>>>>---------')
    print(CHOICES)

    selected_salon = forms.ChoiceField(choices=CHOICES, label=_("Select salon"))

    def get_salon_pk(self):
        # print(self.selected_salon[1])
        return self.cleaned_data['selected_salon']
      
      
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'is_active')


class NewSalonForm(ModelForm):
    class Meta:
        model = Salon
        fields = '__all__'

