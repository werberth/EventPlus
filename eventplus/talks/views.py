from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from .models import Room, Talk
from .forms import RoomForm, TalkForm, IntervalForm
from eventplus.events.views import KwargsEventView


class CreateRoomView(KwargsEventView, generic.CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'talks/crud_room.html'


class UpdateRoomView(KwargsEventView, generic.UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'talks/crud_room.html'


class DeleteRoomView(generic.DeleteView):
    model = Room
    form_class = RoomForm
    success_url = r('talks:room_create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CreateTalkView(KwargsEventView, generic.CreateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/crud_talk.html'


class CreateIntervalView(KwargsEventView, generic.CreateView):
    model = Talk
    form_class = IntervalForm
    template_name = 'talks/crud_interval.html'


class UpdateTalkView(KwargsEventView, generic.UpdateView):
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
