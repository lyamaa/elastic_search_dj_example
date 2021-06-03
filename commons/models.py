# commons/models.py

from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django.contrib.gis.geos import Point


def slugify(value):
    return value.replace(" ", "-").lower()


class ConfigChoiceCategory(models.Model):

    name = models.CharField(
        _("Config Choice Category Name"),
        help_text=_("Required and Unique"),
        max_length=255,
        unique=True,
    )
    slug = AutoSlugField(
        verbose_name=_("Config Choice Category Slug"),
        populate_from="name",
        slugify=slugify,
    )
    entered_by = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Config Choice Category")
        verbose_name_plural = _(" Config Choice Categories")

    def __str__(self):
        return self.name


class ConfigChoice(models.Model):
    name = models.CharField(
        _("Config Choice Name"),
        help_text=_("Required and Unique"),
        max_length=255,
        unique=True,
    )
    description = models.TextField()
    slug = AutoSlugField(
        verbose_name=_("Config Choice Slug"),
        populate_from="name",
        slugify=slugify,
    )
    config_choice_category = models.ForeignKey(
        ConfigChoiceCategory, on_delete=models.CASCADE
    )
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Config Choice")
        verbose_name_plural = _("Config Choices")

    def __str__(self) -> str:
        return self.name


class Address(models.Model):
    street_1 = models.CharField(max_length=200)
    street_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.street_1}, {self.city}, {self.state}, {self.country}"

    @property
    def coordinates(self):
        return Point(self.longitude, self.latitude)
