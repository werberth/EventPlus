from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from .models import Event, Supporters
from .forms import CreateEventForm, SupporterForm


class CreateEventView(generic.CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/create_event.html'


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
    queryset = Event.objects.all()
    template_name = 'events/list_events.html'
    context_object_name = 'events'


class CreateSupporterView(generic.CreateView):
    model = Supporters
    form_class = SupporterForm
    template_name = 'events/crud_supporter.html'
