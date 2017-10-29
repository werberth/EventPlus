from django.db import models

from django.utils.translation import gettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    slug = models.SlugField(_('Slug'))
    photo = models.URLField(_('Photograph'))
    description = models.TextField(_('Description'), blank=True)

    def __str__(self):
        return self.name


class Talk(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.ForeignKey(
        Speaker,
        related_name='talks',
        verbose_name=_('Speaker')
    )
    description = models.TextField(_('Description'), blank=True)
    start_at = models.TimeField(_('Start at'))
    end = models.TimeField(_('End'))
    date = models.DateTimeField(_('Date'))
    description_file = models.URLField(_('Explanatory File'))

    def __str__(self):
        return "{0} - {1}".format(self.title, self.speaker)
