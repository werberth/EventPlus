from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from django.test import TestCase


class TestLoginViewBackend(TestCase):
    """
        Testando custom backend, e verificando se é possivel
        autenticar o usuário atráves do email ou username.
    """

    def setUp(self):
        """ Definindo variáveis recorrentes no teste """

        self.user = User.objects.create_user(
            username="werberth",
            password="@12345abc",
            email="werberthvinicius@gmail.com"
        )

        self.url = r('accounts:login')
        self.resp = self.client.get(self.url)

    def test_get(self):
        """ testando get method """
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        """ testando template usado"""
        self.assertTemplateUsed(self.resp, 'accounts/login.html')

    def test_login_with_username(self):
        """ verficando se é possivel logar na view de login usando username"""
        data = dict(
            username="werberth",
            password="@12345abc"
        )
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, r('events:myevents'))

    def test_login_with_email(self):
        """ verficando se é possivel logar na view de login usando email"""
        data = dict(
            username="werberthvinicius@gmail.com",
            password="@12345abc"
        )
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, r('events:myevents'))

    def test_login_with_invalid_username(self):
        """
            verificando se é há errors no formulários
            ao inserir um username inválido
        """
        data = dict(
            username="userabcd",
            password="@12345abc"
        )
        resp = self.client.post(self.url, data)
        form = resp.context['form']
        self.assertTrue(form.errors)

    def test_assert_login(self):
        """
            Verficando se o client consegue logar um
            usuário pelo email.
        """
        login_bool = self.client.login(
            username="werberthvinicius@gmail.com",
            password="@12345abc"
        )
        self.assertTrue(login_bool)

    def test_logout_redirect(self):
        """
            testando url de redirecionamento após o logout
        """
        logout = self.client.get(r('accounts:logout'))
        self.assertRedirects(logout, r('events:list'))
