from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    name = models.CharField(_("Name"), max_length=155)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    start_date = models.DateTimeField(_('Start Date'))
    end_date = models.DateTimeField(_('End Date'))

    def __str__(self):
        return '{0} - {1}, {2}'.format(self.name, self.country, self.city)


class Supporters(models.Model):
    TYPE_CHOICES = (
        ('sponsors', _('Sponsors')),
        ('promoters', _('Promoters')),
        ('organizers', _('Organizers'))
    )

    event = models.ForeignKey(
        Event,
        related_name='supporters',
        verbose_name=_('Event')
    )

    name = models.CharField(max_length=155)
    image_logo = models.URLField(_('Logo'))
    types = models.CharField(
        max_length=155,
        choices=TYPE_CHOICES
    )

    def __str__(self):
        return self.name
