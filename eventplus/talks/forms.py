from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Room, Talk


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['event'].required = False

    def save(self, commit=True):
        room = super().save(commit=False)
        room.event = self.event
        room.save()
        return room


class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        exclude = ['event']

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        super(TalkForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(TalkForm, self).clean()
        initial = cleaned_data.get('start_at')
        end = cleaned_data.get('end')
        day = cleaned_data.get('date')
        room = cleaned_data.get('room')

        if(initial < end):
            if(
                Talk.objects.filter(
                    start_at__gte=initial,
                    end__lte=end,
                    date=day,
                    room=room
                )
            ).exists():
                raise forms.ValidationError(
                    _("Já existe uma palestra nesse horario, verfique a lista\
                    de palestras para saber quais horarios já extão reservados\
                    e tente novamente")
                )

            return super(TalkForm, self).clean()
        else:
            raise forms.ValidationError(
                _("Periodo de Inicio ou Fim da Palestra inválido(s).\
                Verfique se o horário de inicio da Palestra é anterior\
                ao horário de termino e vice-versa.")
            )

    def clean_date(self):
        data = self.cleaned_data['date']
        if not (self.event.start_date <= data <= self.event.end_date):
            raise forms.ValidationError(
                _("Invalid date! Make sure the reported date is in the\
                interval between the start and end date of the event.")
            )
        return data

    def save(self, commit=True):
        talk = super().save(commit=False)
        talk.event = self.event
        talk.save()
        return talk
