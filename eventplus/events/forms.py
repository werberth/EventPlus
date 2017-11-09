from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import widgets

from .models import Event, Supporters


class FormKwargsEvent(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        super(FormKwargsEvent, self).__init__(*args, **kwargs)
        self.fields['event'].required = False


class FormKwargsUser(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(FormKwargsUser, self).__init__(*args, **kwargs)
        self.fields['user'].required = False


class CreateEventForm(FormKwargsUser):

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

    def save(self, commit=True):
        event = super(CreateEventForm, self).save(commit=False)
        event.user = self.user
        if commit:
            event.save()
        return event


class SupporterForm(FormKwargsEvent):
    class Meta:
        model = Supporters
        fields = '__all__'

    def save(self):
        supporter = super().save(commit=False)
        supporter.event = self.event
        supporter.save()
        return supporter
