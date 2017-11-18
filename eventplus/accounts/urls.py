from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import CreateUserView, UpdateUserView, ChangePasswordView

urlpatterns = [
    url(r'^create/$', CreateUserView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', UpdateUserView.as_view(), name='update'),
    url(
        r'^change-password/$',
        ChangePasswordView.as_view(),
        name='change_password'
    ),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
