"""Test infrastructureservicemodel forms."""

from django.test import TestCase

from infrastructure_services import forms


class InfrastructureServiceModelTest(TestCase):
    """Test InfrastructureServiceModel forms."""

    def test_specifying_all_fields_success(self):
        form = forms.InfrastructureServiceModelForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.InfrastructureServiceModelForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_infrastructureservicemodel_is_required(self):
        form = forms.InfrastructureServiceModelForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
