"""Test InfrastructureServiceModel."""

from django.test import TestCase

from infrastructure_services import models


class TestInfrastructureServiceModel(TestCase):
    """Test InfrastructureServiceModel."""

    def test_create_infrastructureservicemodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        infrastructureservicemodel = models.InfrastructureServiceModel.objects.create(name="Development")
        self.assertEqual(infrastructureservicemodel.name, "Development")
        self.assertEqual(infrastructureservicemodel.description, "")
        self.assertEqual(str(infrastructureservicemodel), "Development")

    def test_create_infrastructureservicemodel_all_fields_success(self):
        """Create InfrastructureServiceModel with all fields."""
        infrastructureservicemodel = models.InfrastructureServiceModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(infrastructureservicemodel.name, "Development")
        self.assertEqual(infrastructureservicemodel.description, "Development Test")
