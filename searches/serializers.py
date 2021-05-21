from drf_haystack.serializers import HaystackSerializer

from .search_indexes import (
    HotelIndex,
    HotelSpecIndex,
    HotelImageIndex,
    HotelAddressIndex,
)


class AggregateSerializer(HaystackSerializer):
    class Meta:
        index_classes = [HotelIndex, HotelSpecIndex, HotelImageIndex, HotelAddressIndex]
        fields = [
            "name",
            "hotel",
            "config_choice",
            "value",
            "image_urls",
            "caption",
            "address",
            "autocomplete",
        ]
