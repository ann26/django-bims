from rest_framework import serializers
from bims.models.location_site import LocationSite
from bims.models.biological_collection_record import BiologicalCollectionRecord
from bims.serializers.location_site_serializer import LocationSiteSerializer
from bims.serializers.bio_collection_serializer import BioCollectionSerializer


class LocationSiteDetailSerializer(LocationSiteSerializer):
    """
    Serializer for location site detail.
    """
    biological_collection_record = serializers.SerializerMethodField()

    def get_biological_collection_record(self, obj):
        collections = BiologicalCollectionRecord.objects.filter(
            site=obj, validated=True,
        )
        return BioCollectionSerializer(collections, many=True).data

    class Meta:
        model = LocationSite
        fields = [
            'id',
            'name',
            'geometry',
            'location_type',
            'biological_collection_record',
        ]
