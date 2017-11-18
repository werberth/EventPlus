from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy as r

from .models import Room, Talk
from .forms import RoomForm, TalkForm, IntervalForm

from eventplus.events.views import KwargsEventView
from eventplus.events.models import Event


class CreateRoomView(LoginRequiredMixin, KwargsEventView, generic.CreateView):
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


class UpdateRoomView(LoginRequiredMixin, KwargsEventView, generic.UpdateView):
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


class DeleteRoomView(LoginRequiredMixin, generic.DeleteView):
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


class ListRoomView(LoginRequiredMixin, KwargsEventView, generic.ListView):
    model = Room
    template_name = 'talks/list_rooms.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs['event'])
        queryset = self.event.rooms.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListRoomView, self).get_context_data(**kwargs)
        context['event'] = self.event
        return context


class CreateTalkView(LoginRequiredMixin, KwargsEventView, generic.CreateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/crud_talk.html'

    def get_success_url(self):
        event = get_object_or_404(Event, pk=self.kwargs['event'])
        url = r(
            'events:edit',
            kwargs={
                'slug': event.slug
            }
        )
        return url


class CreateIntervalView(
        LoginRequiredMixin,
        KwargsEventView,
        generic.CreateView):

    model = Talk
    form_class = IntervalForm
    template_name = 'talks/crud_interval.html'

    def get_success_url(self):
        event = get_object_or_404(Event, pk=self.kwargs['event'])
        url = r(
            'events:edit',
            kwargs={
                'slug': event.slug
            }
        )
        return url


class UpdateIntervalView(
        LoginRequiredMixin,
        KwargsEventView,
        generic.UpdateView):

    model = Talk
    form_class = IntervalForm
    template_name = 'talks/crud_interval.html'

    def get_success_url(self):
        event = get_object_or_404(Event, pk=self.kwargs['event'])
        url = r(
            'events:edit',
            kwargs={
                'slug': event.slug
            }
        )
        return url


class UpdateTalkView(LoginRequiredMixin, KwargsEventView, generic.UpdateView):
    model = Talk
    form_class = TalkForm
    template_name = 'talks/crud_talk.html'

    def get_success_url(self):
        event = get_object_or_404(Event, pk=self.kwargs['event'])
        url = r(
            'events:edit',
            kwargs={
                'slug': event.slug
            }
        )
        return url


class DeleteIntervalView(LoginRequiredMixin, generic.DeleteView):
    model = Talk

    def get_success_url(self):
        url = r(
            'events:edit',
            kwargs={
                'slug': self.kwargs['event_slug']
            }
        )
        return url

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DeleteTalkView(LoginRequiredMixin, generic.DeleteView):
    model = Talk

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        url = r(
            'events:edit',
            kwargs={
                'slug': self.kwargs['event_slug']
            }
        )
        return url
