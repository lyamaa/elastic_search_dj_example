from drf_haystack.serializers import HaystackSerializer

from .search_indexes import (
    HotelIndex,
    HotelSpecIndex,
    HotelImageIndex,
    HotelAddressIndex,
)


class AggregateSerializer(HaystackSerializer):
    class Meta:
        index_classes = [HotelIndex]
        fields = [
            "name",
            "hotel",
            "hotel_type",
            "slug",
            "image_urls",
            "caption",
            "address",
            "autocomplete",
        ]
