from django.conf.urls import url

from .views import CreateEventView

urlpatterns = [
    url(r'^create/$', CreateEventView.as_view(), name="create"),
]
