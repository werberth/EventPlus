from django.conf.urls import url

from .views import CreateEventView, UpdateEventView, DeleteEventView

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
    )
]
