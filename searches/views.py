from .serializers import AggregateSerializer
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView
from drf_haystack.mixins import FacetMixin


class AggregateSearchViewSet(ListModelMixin, FacetMixin, HaystackGenericAPIView):

    serializer_class = AggregateSerializer
    facet_serializer_class = AggregateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
