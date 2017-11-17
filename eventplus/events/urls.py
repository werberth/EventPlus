from django.conf.urls import url

from .views import (
    CreateEventView,
    UpdateEventView,
    DeleteEventView,
    ListEventView,
    CreateSupporterView,
    UpdateSupporterView,
    DeleteSupporterView,
    MyEventsView,
    EventView
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
    url(r'^my-events/$', MyEventsView.as_view(), name="myevents"),
    url(r'^(?P<slug>[\w-]+)$', EventView.as_view(), name="event"),
    url(
        r'^supporter/create/(?P<event>\d+)/$',
        CreateSupporterView.as_view(),
        name="supporter_create"
    ),
    url(
        r'^supporter/update/(?P<event>\d+)/(?P<pk>\d+)/$',
        UpdateSupporterView.as_view(),
        name="supporter_update"
    ),
    url(
        r'^supporter/delete/(?P<event>[\w-]+)/(?P<pk>\d+)/$',
        DeleteSupporterView.as_view(),
        name="supporter_delete"
    ),
]
