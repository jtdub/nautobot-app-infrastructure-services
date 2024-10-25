"""API views for infrastructure_services."""

from nautobot.apps.api import NautobotModelViewSet

from infrastructure_services import filters, models
from infrastructure_services.api import serializers


class InfrastructureServiceModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """InfrastructureServiceModel viewset."""

    queryset = models.InfrastructureServiceModel.objects.all()
    serializer_class = serializers.InfrastructureServiceModelSerializer
    filterset_class = filters.InfrastructureServiceModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
