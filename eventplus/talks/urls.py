from django.conf.urls import url

from .views import (
    CreateRoomView,
    UpdateRoomView,
    DeleteRoomView,
    CreateTalkView,
    CreateIntervalView,
    UpdateTalkView,
    UpdateIntervalView,
    DeleteTalkView,
    DeleteIntervalView,
    ListTalkView
)

urlpatterns = [
    url(
        r'^room/create/(?P<event>\d+)/$',
        CreateRoomView.as_view(),
        name="room_create"
    ),
    url(
        r'^room/update/(?P<event>\d+)/(?P<pk>\d+)/$',
        UpdateRoomView.as_view(),
        name="room_update"
    ),
    url(
        r'^room/delete/(?P<pk>\d+)/$',
        DeleteRoomView.as_view(),
        name="room_delete"
    ),
    url(r'^create/(?P<event>\d+)/$', CreateTalkView.as_view(), name="create"),
    url(
        r'^interval/create/(?P<event>\d+)/$',
        CreateIntervalView.as_view(),
        name="create_interval"
    ),
    url(
        r'^interval/create/(?P<event>\d+)/(?P<pk>\d+)/$',
        UpdateIntervalView.as_view(),
        name="update_interval"
    ),
    url(
        r'^interval/delete/(?P<event_slug>[\w-]+)/(?P<pk>\d+)/$',
        DeleteIntervalView.as_view(),
        name="delete_interval"
    ),
    url(
        r'^update/(?P<event>\d+)/(?P<pk>\d+)/$',
        UpdateTalkView.as_view(),
        name="update"
    ),
    url(
        r'^delete/(?P<event_slug>[\w-]+)/(?P<pk>\d+)/$',
        DeleteTalkView.as_view(),
        name="delete"
    ),
    url(r'^$', ListTalkView.as_view(), name="list"),
]
