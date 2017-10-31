from django.views import generic
from django.core.urlresolvers import reverse_lazy as r

from .models import Room
from .forms import RoomForm


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
    success_url = r('talks:create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

