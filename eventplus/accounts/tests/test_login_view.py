from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from django.test import TestCase


class TestLoginViewBackend(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="werberth",
            password="@12345abc",
            email="werberthvinicius@gmail.com"
        )

        self.url = r('accounts:login')
        self.resp = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'accounts/login.html')

    def test_login_with_username(self):
        data = dict(
            username="werberth",
            password="@12345abc"
        )
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, r('events:myevents'))

    def test_login_with_email(self):
        data = dict(
            username="werberthvinicius@gmail.com",
            password="@12345abc"
        )
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, r('events:myevents'))

    def test_login_with_invalid_username(self):
        data = dict(
            username="userabcd",
            password="@12345abc"
        )
        resp = self.client.post(self.url, data)
        form = resp.context['form']
        self.assertTrue(form.errors)

    def test_assert_login(self):
        login_bool = self.client.login(
            username="werberthvinicius@gmail.com",
            password="@12345abc"
        )
        self.assertTrue(login_bool)

    def test_logout_redirect(self):
        logout = self.client.get(r('accounts:logout'))
        self.assertRedirects(logout, r('events:list'))
