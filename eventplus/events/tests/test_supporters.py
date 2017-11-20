from ..models import Supporters
from .test_event_model import EventSetup


class SupporterModelTest(EventSetup):

    def setUp(self):
        super(SupporterModelTest, self).setUp()
        self.supporter = Supporters.objects.create(
            event=self.event,
            name="Google",
            website="http://www.google.com",
            types="sponsors",
        )

    def test_create(self):
        self.assertTrue(Supporters.objects.exists())

    def test_str(self):
        self.assertEqual('Google', str(self.supporter))
