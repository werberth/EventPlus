from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
        label=_("Email address"),
        required=True,
        help_text=_("Required."),
        validators=[EmailValidator]
    )

    class Meta:
        model = User
        fields = ("username", "email")
