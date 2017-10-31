from django.views import generic
from django.contrib.auth.models import User
from .forms import CreateUserForm, UpdateUserForm, NewSetPasswordForm


class CreateUserView(generic.CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'accounts/crud_accounts.html'


class UpdateUserView(generic.UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'accounts/crud_accounts.html'


class ChangePasswordView(generic.FormView):
    model = User
    form_class = NewSetPasswordForm
    template_name = 'accounts/crud_accounts.html'

    def get_form_kwargs(self):
        '''
            O formulário NewSetPasswordForm exige a passagem de vários
            parâmetros, dentre eles o usuário o qual deseja-se modificar
            sua senha. Por meio desse método, o usuário é definido junto
            ao kwargs e passado ao formulário.
        '''
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs['user'] = User.objects.get(pk=self.kwargs['pk'])
        return kwargs
