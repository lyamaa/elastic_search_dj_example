from django.utils import timezone
from haystack import indexes

from .models import Hotel, HotelAddress, HotelImage, HotelSpecificationValue


class HotelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")
    hotel_type = indexes.CharField(model_attr="hotel_type")
    config_choice = indexes.CharField(model_attr="config_choice")
    autocomplete = indexes.EdgeNgramField()

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((obj.name, obj.hotel_type.name, obj.config_choice.name))

    def get_model(self):
        return Hotel


class HotelSpecIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    value = indexes.CharField(model_attr="value")

    def get_model(self):
        return HotelSpecificationValue


class HotelImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    image_urls = indexes.CharField(model_attr="image_urls")
    caption = indexes.CharField(model_attr="caption")

    def get_model(self):
        return HotelImage


class HotelAddressIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    address = indexes.CharField(model_attr="address")

    def get_model(self):
        return HotelAddress
