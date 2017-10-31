from django.conf.urls import url

from .views import (
    CreateEventView,
    UpdateEventView,
    DeleteEventView,
    ListEventView,
    CreateSupporterView,
    UpdateSupporterView,
    DeleteSupporterView
)

urlpatterns = [
    url(r'^create/$', CreateEventView.as_view(), name="create"),
    url(
        r'^update/(?P<slug>[\w-]+)$',
        UpdateEventView.as_view(),
        name="update"
    ),
    url(
        r'^delete/(?P<slug>[\w-]+)$',
        DeleteEventView.as_view(),
        name="delete"
    ),
    url(r'^$', ListEventView.as_view(), name="list"),
    url(
        r'^supporter/create/$',
        CreateSupporterView.as_view(),
        name="supporter_create"
    ),
    url(
        r'^supporter/update/(?P<pk>\d+)/$',
        UpdateSupporterView.as_view(),
        name="supporter_update"
    ),
    url(
        r'^supporter/delete/(?P<pk>\d+)/$',
        DeleteSupporterView.as_view(),
        name="supporter_delete"
    ),
]
