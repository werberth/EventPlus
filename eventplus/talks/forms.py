from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Room, Talk
from eventplus.events.forms import FormKwargsEvent


class CleanDate(forms.ModelForm):

    def clean(self):
        cleaned_data = super(CleanDate, self).clean()
        initial = cleaned_data.get('start_at')
        end = cleaned_data.get('end')
        day = cleaned_data.get('date')
        room = cleaned_data.get('room')

        if(initial < end):
            if initial < self.event.start_at or end > self.event.end_at:
                raise forms.ValidationError(
                    _(
                        "The start or end time of the talk\
                        exceeds the limits of the time of the event."
                    )
                )
            if(
                Talk.objects.filter(
                    start_at__gte=initial,
                    end__lte=end,
                    date=day,
                    room=room
                )
            ).exists():
                error_message = _(
                    "Já existe uma palestra nesse horario, verfique a lista\
                    de palestras para saber quais horarios já extão reservados\
                    e tente novamente"
                )
                if hasattr(self, 'instance'):
                    talk_search = Talk.objects.get(
                        start_at__gte=initial,
                        end__lte=end,
                        date=day,
                        room=room
                    )
                    if (talk_search.pk != self.instance.pk):
                        raise forms.ValidationError(error_message)
                else:
                    raise forms.ValidationError(error_message)

            return super(CleanDate, self).clean()
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


class RoomForm(FormKwargsEvent):
    class Meta:
        model = Room
        fields = '__all__'

    def save(self, commit=True):
        room = super().save(commit=False)
        room.event = self.event
        room.save()
        return room


class TalkForm(CleanDate, FormKwargsEvent):
    class Meta:
        model = Talk
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TalkForm, self).__init__(*args, **kwargs)
        self.fields['speaker_name'].required = True
        self.fields['speaker_photo'].required = True
        self.fields['talk_description'].required = True
        self.fields['speaker_description'].required = True
        self.fields['description_file'].required = True
        self.fields['is_interval'].required = False
        self.fields['room'].required = True

    def clean_talk_title(self):
        data = self.cleaned_data['talk_title']
        if Talk.objects.filter(
            talk_title=data,
            event=self.event
        ):
            error_message = _(
                "Sorry, there is already a Talk on this Event\
                with this title, please insert another title and\
                try again."
            )
            if hasattr(self, 'instance'):
                talk_search = Talk.objects.get(
                    talk_title=data,
                    event=self.event
                )
                if (talk_search.pk != self.instance.pk):
                    raise forms.ValidationError(error_message)
            else:
                raise forms.ValidationError(error_message)
        return data


class IntervalForm(CleanDate, FormKwargsEvent):
    class Meta:
        model = Talk
        fields = ('talk_title', 'event', 'date', 'start_at', 'end', 'talk_description')

    def __init__(self, *args, **kwargs):
        super(IntervalForm, self).__init__(*args, **kwargs)
        self.fields['talk_title'].required = False

    def save(self, commit=True):
        interval = super(IntervalForm, self).save(commit=False)
        interval.event = self.event
        interval.is_interval = True
        interval.talk_title = "Intervalo"
        interval.save()
        return interval
