from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy as r
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import SetPasswordForm
from .forms import CreateUserForm, UpdateUserForm


class IndexView(generic.RedirectView):

    """
    View de homepage que redirecionárá para pagina de
    Listagem dos eventos, quando a url '/' for acessada.
    """

    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect(r('events:list'))


class CreateUserView(generic.CreateView):

    """
    View de criação do usuário
    """

    model = User
    form_class = CreateUserForm
    template_name = 'accounts/crud_accounts.html'
    success_url = r('events:myevents')

    def form_valid(self, form):
        user = form.save()
        auth_login(
            self.request,
            user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return HttpResponseRedirect(self.success_url)


class UpdateUserView(LoginRequiredMixin, generic.UpdateView):

    """
        View de edição dos dados do usuário (email e username)
    """

    model = User
    form_class = UpdateUserForm
    template_name = 'accounts/crud_accounts.html'
    success_url = r('events:myevents')

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):

    """
        View de alteração de senha
    """

    model = User
    form_class = SetPasswordForm
    template_name = 'accounts/crud_accounts.html'
    success_url = r('events:myevents')
