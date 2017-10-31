from django.conf.urls import url

from .views import (
    CreateRoomView,
    UpdateRoomView,
    DeleteRoomView
)

urlpatterns = [
    url(r'^room/create/$', CreateRoomView.as_view(), name="create"),
    url(
        r'^room/update/(?P<pk>\d+)/$',
        UpdateRoomView.as_view(),
        name="supporter_update"
    ),
    url(
        r'^room/delete/(?P<pk>\d+)/$',
        DeleteRoomView.as_view(),
        name="supporter_delete"
    ),
]
