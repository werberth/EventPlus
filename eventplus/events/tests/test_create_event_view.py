import datetime
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from django.test import TestCase


class TestCreateEventView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="werberth",
            password="@12345abc",
            email="werberthvinicius@gmail.com"
        )

        self.client.login(
            username="werberth",
            password="@12345abc",
        )

        self.url = r('events:create')
        self.resp = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'events/crud_event.html')

    def test_create(self):
        data = dict(
            name="Evento Inicial",
            address="Rua Qualquer, Bairro Aleatorio, 123",
            city="Aleatoria",
            state="Desconhecido",
            start_date=datetime.date(2017, 11, 20),
            end_date=datetime.date(2017, 11, 22),
            start_at=datetime.time(8),
            end_at=datetime.time(17),
        )
        resp_post = self.client.post(self.url, data)
        redirect_url = 'events:edit'
        self.assertRedirects(resp_post, r(redirect_url, 'evento-inicial'))

    def test_validate_date(self):
        data = dict(
            name="Evento Inicial",
            address="Rua Qualquer, Bairro Aleatorio, 123",
            city="Aleatoria",
            state="Desconhecido",
            start_date=datetime.date(2017, 11, 20),
            end_date=datetime.date(2017, 11, 19),
            start_at=datetime.time(8),
            end_at=datetime.time(17),
        )
        resp_post = self.client.post(self.url, data)
        form = resp_post.context['form']
        self.assertTrue(form.errors)

    def test_validate_time(self):
        data = dict(
            name="Evento Inicial",
            address="Rua Qualquer, Bairro Aleatorio, 123",
            city="Aleatoria",
            state="Desconhecido",
            start_date=datetime.date(2017, 11, 20),
            end_date=datetime.date(2017, 11, 22),
            start_at=datetime.time(18),
            end_at=datetime.time(8),
        )
        resp_post = self.client.post(self.url, data)
        form = resp_post.context['form']
        self.assertTrue(form.errors)
