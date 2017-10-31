from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from .models import Event
from .forms import CreateEventForm


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
