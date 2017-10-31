from django.conf.urls import url

from .views import (
    CreateRoomView,
    UpdateRoomView,
    DeleteRoomView,
    CreateTalkView
)

urlpatterns = [
    url(r'^room/create/$', CreateRoomView.as_view(), name="room_create"),
    url(
        r'^room/update/(?P<pk>\d+)/$',
        UpdateRoomView.as_view(),
        name="room_update"
    ),
    url(
        r'^room/delete/(?P<pk>\d+)/$',
        DeleteRoomView.as_view(),
        name="room_delete"
    ),
    url(r'^create/$', CreateTalkView.as_view(), name="create"),
]
