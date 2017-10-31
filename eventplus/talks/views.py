from django.views import generic

from .models import Room
from .forms import RoomForm


class CreateRoomView(generic.CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'talks/crud_room.html'
