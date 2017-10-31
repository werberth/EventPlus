from django.conf.urls import url

from .views import CreateUserView, UpdateUserView, ChangePasswordView

urlpatterns = [
    url(r'^create/$', CreateUserView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', UpdateUserView.as_view(), name='update'),
    url(
        r'^change-password/(?P<pk>\d+)/$',
        ChangePasswordView.as_view(),
        name='change_password'
    )
]
