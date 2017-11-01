import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Room, Talk


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = '__all__'

    def clean(self):
        initial = self.cleaned_data['start_at']
        end = self.cleaned_data['end']
        day = self.cleaned_data['date']
        room = self.cleaned_data['room']

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
