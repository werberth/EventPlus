from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from eventplus.events.models import Event
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

    def get_form_kwargs(self):
        kwargs = super(CreateTalkView, self).get_form_kwargs()
        kwargs['event'] = Event.objects.get(pk=self.kwargs['pk'])
        return kwargs


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


class ListTalkView(generic.ListView):
    model = Talk
    queryset = Talk.objects.all()
    template_name = 'events/list_talks.html'
    context_object_name = 'talks'