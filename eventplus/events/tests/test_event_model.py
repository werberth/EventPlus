import datetime
from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Event


class EventSetup(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="user",
            email="user@email.com",
            password="12345abcd",
        )
        self.event = Event.objects.create(
            user=self.user,
            name="Evento Test",
            slug="evento-test",
            address="Rua Anonima, Bairro Aleatorio, 123",
            city="Não Existe",
            state="Desconhecido",
            start_date=datetime.date(2017, 11, 20),
            end_date=datetime.date(2017, 11, 22),
            start_at=datetime.time(8),
            end_at=datetime.time(17),
        )


class EventModelTest(EventSetup):

    def test_create(self):
        self.assertTrue(Event.objects.exists())

    def test_str(self):
        self.assertEqual(
            'Evento Test - Desconhecido, Não Existe',
            str(self.event)
        )
