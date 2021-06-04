from commons.models import Address, ConfigChoice
from django.db import models
from django.utils.translation import gettext_lazy as _
from haystack import signals
from django.dispatch import receiver
from django_q.tasks import async_task
from .tasks import handle_save, handle_delete
from autoslug import AutoSlugField


def slugify(value):
    return value.replace(" ", "-").lower()


class CoreModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HotelType(models.Model):
    name = models.CharField(_("Hotel Types Name"), max_length=255)

    class Meta:
        verbose_name = _("Hotel Type")
        verbose_name_plural = _("Hotel Types")

    def __str__(self) -> str:
        return self.name


class HotelSpecifications(models.Model):
    hotel_type = models.ForeignKey(HotelType, on_delete=models.RESTRICT)
    name = models.CharField(_("Hotel Spec Name"), max_length=255)

    class Meta:
        verbose_name = _("Hotel Specification")
        verbose_name_plural = _("Hotel Specifications")

    def __str__(self) -> str:
        return f"{self.name}"


class Hotel(CoreModel):
    name = models.CharField(_("Hotel Name"), max_length=50)
    description = models.TextField(_("Hotel Descriptions"), default="")
    hotel_type = models.ForeignKey(HotelType, on_delete=models.CASCADE)
    slug = AutoSlugField(
        verbose_name=_("Hotel Slug"),
        populate_from="name",
        slugify=slugify,
    )
    is_active = models.BooleanField(default=True)
    config_choice = models.ForeignKey(ConfigChoice, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = _("Hotel")
        verbose_name_plural = _("Hotels")

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def __str__(self) -> str:
        return self.name


class HotelSpecificationValue(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    specification = models.ForeignKey(HotelSpecifications, on_delete=models.RESTRICT)
    value = models.CharField(
        _("Value"),
        max_length=255,
        help_text=_("Hotel specification value (maximum of 255 words"),
    )

    class Meta:
        verbose_name = _("Hotel Specification Value")
        verbose_name_plural = _("Hotel Specification Values")

    def __str__(self):
        return self.value


class HotelImage(CoreModel):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="hotel_image"
    )
    image_urls = models.URLField(
        _("Hotel Image URLs"),
        help_text=_("Images Urls"),
    )
    caption = models.CharField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Hotel Image")
        verbose_name_plural = _("Hotel Images")


class HotelAddress(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="hotel_addres"
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hotel.name} {self.address.city}"


class HotelOnlySignalProcessor(signals.BaseSignalProcessor):
    def setup(self):
        # Listen only to the ``Hotel`` model.
        async_task(models.signals.post_save.connect(self.handle_save, sender=Hotel))
        async_task(models.signals.post_delete.connect(self.handle_delete, sender=Hotel))

    def teardown(self):
        # Disconnect only for the ``Hotel`` model.
        async_task(models.signals.post_save.disconnect(handle_save, sender=Hotel))
        async_task(
            models.signals.post_delete.disconnect(self.handle_delete, sender=Hotel)
        )
