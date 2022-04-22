from .models import Provider, Polygon
from rest_framework import viewsets, status, permissions
from .serializers import ProviderSerializer, PolygonSerializer, CustomPolygonSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Provider to be viewed or edited.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]


class PolygonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Polygon to be viewed or edited.
    """
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(cache_page(7200))
    @action(detail=False, methods=['get'], url_name='given-coordinates-return-polygons',
            serializer_class=CustomPolygonSerializer)
    def given_coordinates_return_polygons(self, request):
        """
            API endpoint that allows Polygons to be retrieved given some coordinates.
            url ex. /polygons/given_coordinates_return_polygons/?lat=125.6&lng=10.1
            where lat means latitude and lng longitude
        """
        error_message = None
        try:
            lat = float(request.query_params.get('lat'))
            lng = float(request.query_params.get('lng'))
        except ValueError:
            error_message = {'detail': 'lat or lng malformed'}
        except TypeError:
            error_message = {'detail': 'missing lat or lng'}

        if error_message is not None:
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        polygons_queryset = Polygon.objects.filter(geo_data__geometry__coordinates=[lat, lng]).select_related(
            'provider').order_by('id')

        page = self.paginate_queryset(polygons_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(polygons_queryset, many=True)
        return Response(serializer.data)
