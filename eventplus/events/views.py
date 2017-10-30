from django.views import generic

from .models import Event
from .forms import CreateEventForm


class CreateEventView(generic.CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/create_event.html'
