from datetime import datetime
from django.shortcuts import get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from .models import Event, Supporters
from .forms import CreateEventForm, SupporterForm


class KwargsEventView(object):
    def get_form_kwargs(self):
        kwargs = super(KwargsEventView, self).get_form_kwargs()
        kwargs['event'] = get_object_or_404(Event, pk=self.kwargs['event'])
        return kwargs


class CreateEventView(generic.CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/crud_event.html'


class UpdateEventView(generic.UpdateView):
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
