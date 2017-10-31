from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email address"),
        required=True,
        help_text=_("Required."),
        validators=[EmailValidator]
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UpdateUserForm(CreateUserForm):
    class Meta:
        model = User
        fields = ("username", "email")


class NewSetPasswordForm(SetPasswordForm):
    '''
        Esse formulário herda do SetPasswordForm, modificando
        apenas a forma como a instancia do usuário (o qual senha será
        modificada) é passada, utilizando o kwargs da CBV.
    '''

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NewSetPasswordForm, self).__init__(self.user, *args, **kwargs)
