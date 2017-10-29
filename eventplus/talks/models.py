from django.db import models

from django.utils.translation import gettext_lazy as _


class Speaker(models.Model):

    name = models.CharField(_('Name'), max_length=255)
    slug = models.SlugField(_('Slug'))
    photo = models.URLField(_('Photograph'))
    description = models.TextField(_('Description'), blank=True)

    def __str__(self):
        return self.name
