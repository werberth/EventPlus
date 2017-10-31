from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import widgets

from .models import Event, Supporters


class CreateEventForm(forms.ModelForm):
    start_date = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_date = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        fields = '__all__'

    def clean_address(self):
        data = self.cleaned_data['address']
        components_of_adress = data.split(',')
        if (len(components_of_adress) != 3):
            raise forms.ValidationError(
                _('Invalid Address. Make sure your address contains street, \
                    neighborhood and house number, separated by commas.')
            )
        return data


class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporters
        fields = '__all__'
