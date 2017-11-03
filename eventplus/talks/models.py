from django.db import models

from django.utils.translation import gettext_lazy as _

from eventplus.events.models import Event


class Room(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    event = models.ForeignKey(
        Event,
        related_name='rooms',
        verbose_name=_('Event')
    )

    def __str__(self):
        return "{}".format(self.name)


class Talk(models.Model):
    talk_title = models.CharField(_('Talk Title'), max_length=255)
    talk_description = models.TextField(_('Talk Description'), blank=True)
    speaker_name = models.CharField(_('Speaker Name'), max_length=255)
    speaker_photo = models.URLField(_('Speaker Photograph'))
    speaker_description = models.TextField(
        _('Speaker Description'),
        blank=True
    )
    room = models.ForeignKey(
        Room,
        related_name='talks',
        verbose_name=_('Room'),
        null=False,
    )
    start_at = models.TimeField(_('Start at'))
    end = models.TimeField(_('End'))
    date = models.DateField(_('Date'))
    description_file = models.URLField(_('Explanatory File'))

    def __str__(self):
        return "{0} - {1}".format(self.talk_title, self.speaker_name)
