from django.conf.urls import url

from .views import CreateRoomView


urlpatterns = [
    url(r'^room/create/$', CreateRoomView.as_view(), name="create"),
]
