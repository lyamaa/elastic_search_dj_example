from .serializers import AggregateSerializer
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView


class AggregateSearchViewSet(ListModelMixin, HaystackGenericAPIView):

    serializer_class = AggregateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
