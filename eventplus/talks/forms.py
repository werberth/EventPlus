from django import forms

from .models import Room, Talk


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = '__all__'
