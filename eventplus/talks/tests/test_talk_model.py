import datetime
from eventplus.events.tests.test_event_model import EventSetup
from ..models import Talk, Room


class TalkModelTest(EventSetup):
    def setUp(self):
        super(TalkModelTest, self).setUp()
        self.room = Room.objects.create(
            name="Sala 01",
            event=self.event
        )
        self.talk = Talk(
            event=self.event,
            talk_title="Titulo da Palestra",
            talk_description="Um breve palestra que deverá \
            sera apresentada durante o evento.",
            speaker_name="Palestrante Da Silva",
            speaker_photo="https://goo.gl/PhGVJw",
            speaker_description="Um breve descrição\
            sobre o palestrante que deverá ministrar\
            a palestra sobre algum tema que devera ser\
            predefinido anteriormente.",
            room=self.room,
            date=datetime.date(2017, 11, 21),
            start_at=datetime.time(8),
            end=datetime.time(9),
            description_file="https://goo.gl/pdSCTe",
        )

        self.talk.save(),

        self.interval = Talk(
            event=self.event,
            talk_title="Interval",
            talk_description="Um breve palestra que deverá \
            sera apresentada durante o evento.",
            is_interval=True,
            date=datetime.date(2017, 11, 22),
            start_at=datetime.time(8),
            end=datetime.time(8, 30),
        )

        self.interval.save()

    def test_create_talk(self):
        self.assertTrue(Talk.objects.exists())

    def test_create_room(self):
        self.assertTrue(Room.objects.exists())

    def test_str_talk(self):
        self.assertEqual(
            "Titulo da Palestra - Palestrante Da Silva",
            str(self.talk)
        )

    def test_str_room(self):
        self.assertEqual("Sala 01", str(self.room))

    def test_is_not_interval_talk(self):
        self.assertFalse(self.talk.is_interval)

    def test_is_interval(self):
        self.assertTrue(self.interval.is_interval)
