"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from infrastructure_services import models
from infrastructure_services.tests import fixtures


class InfrastructureServiceModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the InfrastructureServiceModel views."""

    model = models.InfrastructureServiceModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_infrastructureservicemodel()
