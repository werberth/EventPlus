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

    def clean(self):
        cleaned_data = super(CreateEventForm, self).clean()
        start_at = cleaned_data.get('start_at')
        end_at = cleaned_data.get('end_at')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date > end_date:
            raise forms.ValidationError(
                _("Invalid Start Date or End Date Period of the Event.\
                Check if the Start Date of the event is before the\
                End Date.")
            )
        if start_at > end_at:
            raise forms.ValidationError(
                _("Invalid Start At or End At Period of the Event.\
                Check if the Start At of the event is before the\
                End At.")
            )
        return cleaned_data

    def clean_name(self):
        data = self.cleaned_data['name']
        if Event.objects.filter(name=data).exists():
            if hasattr(self, 'instance'):
                error_message = _("An event with this name already exists on\
                the platform, enter another name, and try again.")
                event_search = Event.objects.get(name=data)
                if (event_search.pk != self.instance.pk):
                    raise forms.ValidationError(error_message)
                return data
            raise forms.ValidationError(error_message)
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
