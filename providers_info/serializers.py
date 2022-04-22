from .models import Provider, Polygon
from rest_framework import serializers


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class PolygonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Polygon
        fields = "__all__"


class CustomPolygonSerializer(serializers.ModelSerializer):
    provider_name = serializers.SerializerMethodField()

    class Meta:
        model = Polygon
        fields = ['name', 'price', 'provider_name']

    def get_provider_name(self, obj):
        return obj.provider.name
