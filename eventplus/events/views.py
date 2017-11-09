from datetime import datetime
from django.shortcuts import get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from eventplus.talks.models import Talk

from .models import Event, Supporters
from .forms import CreateEventForm, SupporterForm



class KwargsEventView(object):
    def get_form_kwargs(self):
        kwargs = super(KwargsEventView, self).get_form_kwargs()
        kwargs['event'] = get_object_or_404(Event, pk=self.kwargs['event'])
        return kwargs


class KwargsUserView(object):
    def get_form_kwargs(self):
        kwargs = super(KwargsUserView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateEventView(KwargsUserView, generic.CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/crud_event.html'


class UpdateEventView(KwargsUserView, generic.UpdateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/create_event.html'


class DeleteEventView(generic.DeleteView):
    model = Event
    success_url = r('events:create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ListEventView(generic.ListView):
    model = Event

    queryset = Event.objects.filter(
        end_date__gte=datetime.today()
    ).order_by('-start_date')

    template_name = 'events/list_events.html'
    context_object_name = 'events'


class MyEventsView(generic.ListView):
    model = Event
    template_name = 'events/my_events.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Event.objects.filter(
            user=self.request.user
        ).order_by('-start_date')
        return queryset


class EventView(generic.TemplateView):
    template_name = 'events/event.html'

    def get_context_data(self, **kwargs):
        kwargs = super(EventView, self).get_context_data(**kwargs)
        kwargs['event'] = get_object_or_404(Event, slug=kwargs['slug'])
        talks = Talk.objects.filter(event=kwargs['event'])
        kwargs['talks'] = sorted(talks, key=lambda x: x.start_at and x.date)
        return kwargs


class CreateSupporterView(KwargsEventView, generic.CreateView):
    model = Supporters
    form_class = SupporterForm
    template_name = 'events/crud_supporter.html'


class UpdateSupporterView(KwargsEventView, generic.UpdateView):
    model = Supporters
    form_class = SupporterForm
    template_name = 'events/crud_supporter.html'


class DeleteSupporterView(generic.DeleteView):
    model = Supporters
    success_url = r('events:supporter_create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
