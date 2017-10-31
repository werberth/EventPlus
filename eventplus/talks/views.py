from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from .models import Room, Talk
from .forms import RoomForm, TalkForm


class CreateRoomView(generic.CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'talks/crud_room.html'


class UpdateRoomView(generic.UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'talks/crud_room.html'


class DeleteRoomView(generic.DeleteView):
    model = Room
    form_class = RoomForm
    success_url = r('talks:room_create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CreateTalkView(generic.CreateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/crud_talk.html'


class UpdateTalkView(generic.UpdateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/crud_talk.html'


class DeleteTalkView(generic.DeleteView):
    model = Talk
    form_class = RoomForm
    success_url = r('talks:create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
