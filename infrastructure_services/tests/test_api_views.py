"""Unit tests for infrastructure_services."""

from nautobot.apps.testing import APIViewTestCases

from infrastructure_services import models
from infrastructure_services.tests import fixtures


class InfrastructureServiceModelAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for InfrastructureServiceModel."""

    model = models.InfrastructureServiceModel
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_infrastructureservicemodel()
