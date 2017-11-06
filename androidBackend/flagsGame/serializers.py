from rest_framework.serializers import ModelSerializer
from .models import DublinFlags


class DublinFlagsSerializer(ModelSerializer):

    class Meta:
        model = DublinFlags  # Model wish to serialize
        fields = "__all__"  # This is the fields wish to serialize

