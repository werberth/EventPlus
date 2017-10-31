from django.conf.urls import url

from .views import (
    CreateRoomView,
    UpdateRoomView,
    DeleteRoomView,
    CreateTalkView,
    UpdateTalkView,
    DeleteTalkView,
    ListTalkView
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
    url(
        r'^update/(?P<pk>\d+)/$',
        UpdateTalkView.as_view(),
        name="update"
    ),
    url(
        r'^delete/(?P<pk>\d+)/$',
        DeleteTalkView.as_view(),
        name="delete"
    ),
    url(r'^$', ListTalkView.as_view(), name="list"),
]
