"""Filtering for infrastructure_services."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from infrastructure_services import models


class InfrastructureServiceModelFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for InfrastructureServiceModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.InfrastructureServiceModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]
