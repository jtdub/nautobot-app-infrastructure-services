"""Views for infrastructure_services."""

from nautobot.apps.views import NautobotUIViewSet

from infrastructure_services import filters, forms, models, tables
from infrastructure_services.api import serializers


class InfrastructureServiceModelUIViewSet(NautobotUIViewSet):
    """ViewSet for InfrastructureServiceModel views."""

    bulk_update_form_class = forms.InfrastructureServiceModelBulkEditForm
    filterset_class = filters.InfrastructureServiceModelFilterSet
    filterset_form_class = forms.InfrastructureServiceModelFilterForm
    form_class = forms.InfrastructureServiceModelForm
    lookup_field = "pk"
    queryset = models.InfrastructureServiceModel.objects.all()
    serializer_class = serializers.InfrastructureServiceModelSerializer
    table_class = tables.InfrastructureServiceModelTable
