"""Create fixtures for tests."""

from infrastructure_services.models import InfrastructureServiceModel


def create_infrastructureservicemodel():
    """Fixture to create necessary number of InfrastructureServiceModel for tests."""
    InfrastructureServiceModel.objects.create(name="Test One")
    InfrastructureServiceModel.objects.create(name="Test Two")
    InfrastructureServiceModel.objects.create(name="Test Three")
