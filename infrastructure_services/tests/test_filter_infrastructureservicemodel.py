"""Test InfrastructureServiceModel Filter."""

from django.test import TestCase

from infrastructure_services import filters, models
from infrastructure_services.tests import fixtures


class InfrastructureServiceModelFilterTestCase(TestCase):
    """InfrastructureServiceModel Filter Test Case."""

    queryset = models.InfrastructureServiceModel.objects.all()
    filterset = filters.InfrastructureServiceModelFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for InfrastructureServiceModel Model."""
        fixtures.create_infrastructureservicemodel()

    def test_q_search_name(self):
        """Test using Q search with name of InfrastructureServiceModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for InfrastructureServiceModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
