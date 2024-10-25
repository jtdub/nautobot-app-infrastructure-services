"""API serializers for infrastructure_services."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from infrastructure_services import models


class InfrastructureServiceModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """InfrastructureServiceModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.InfrastructureServiceModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
