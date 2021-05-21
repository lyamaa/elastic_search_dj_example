from django.urls import path

from .views import AggregateSearchViewSet


urlpatterns = [path("hotels/search/", AggregateSearchViewSet.as_view())]
