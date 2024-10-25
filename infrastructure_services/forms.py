"""Forms for infrastructure_services."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from infrastructure_services import models


class InfrastructureServiceModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """InfrastructureServiceModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.InfrastructureServiceModel
        fields = [
            "name",
            "description",
        ]


class InfrastructureServiceModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """InfrastructureServiceModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.InfrastructureServiceModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class InfrastructureServiceModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.InfrastructureServiceModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
