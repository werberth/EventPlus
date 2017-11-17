from django.shortcuts import get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from .models import Room, Talk
from .forms import RoomForm, TalkForm, IntervalForm

from eventplus.events.views import KwargsEventView
from eventplus.events.models import Event

class CreateRoomView(KwargsEventView, generic.CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'talks/crud_room.html'

    def get_success_url(self):
        url = r(
            'talks:rooms',
            kwargs={
                'event': self.kwargs['event']
            }
        )
        return url


class UpdateRoomView(KwargsEventView, generic.UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'talks/crud_room.html'

    def get_success_url(self):
        url = r(
            'talks:rooms',
            kwargs={
                'event': self.kwargs['event']
            }
        )
        return url


class DeleteRoomView(generic.DeleteView):
    model = Room
    form_class = RoomForm
    success_url = r('talks:room_create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        url = r(
            'talks:rooms',
            kwargs={
                'event': self.kwargs['event']
            }
        )
        return url


class ListRoomView(KwargsEventView, generic.ListView):
    model = Room
    template_name = 'talks/list_rooms.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        event = get_object_or_404(Event, pk=self.kwargs['event'])
        queryset = event.rooms.all()
        return queryset


class ListTalkView(generic.ListView):
    model = Talk
    queryset = Talk.objects.all()
    template_name = 'events/list_talks.html'
    context_object_name = 'talks'


class CreateTalkView(KwargsEventView, generic.CreateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/crud_talk.html'


class CreateIntervalView(KwargsEventView, generic.CreateView):
    model = Talk
    form_class = IntervalForm
    template_name = 'talks/crud_interval.html'


class UpdateIntervalView(KwargsEventView, generic.UpdateView):
    model = Talk
    form_class = IntervalForm
    template_name = 'talks/crud_interval.html'


class UpdateTalkView(KwargsEventView, generic.UpdateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/crud_talk.html'


class DeleteIntervalView(generic.DeleteView):
    model = Talk

    def get_success_url(self):
        url = r(
            'events:event',
            kwargs={
                'slug': self.kwargs['event_slug']
            }
        )
        return url

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DeleteTalkView(generic.DeleteView):
    model = Talk

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        url = r(
            'events:event',
            kwargs={
                'slug': self.kwargs['event_slug']
            }
        )
        return url


class ListTalkView(generic.ListView):
    model = Talk
    queryset = Talk.objects.all()
    template_name = 'events/list_talks.html'
    context_object_name = 'talks'
