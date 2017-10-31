from django.views import generic
from django.contrib.auth.models import User
from .forms import CreateUserForm


class CreateUserView(generic.CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'accounts/crud_accounts.html'
