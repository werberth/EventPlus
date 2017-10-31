from django.conf.urls import url

from .views import CreateUserView

urlpatterns = [
    url(r'^create/$', CreateUserView.as_view(), name='create')
]
