"""App declaration for infrastructure_services."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class InfrastructureServicesConfig(NautobotAppConfig):
    """App configuration for the infrastructure_services app."""

    name = "infrastructure_services"
    verbose_name = "Infrastructure Services"
    version = __version__
    author = "Network to Code, LLC"
    description = "Infrastructure Services."
    base_url = "infrastructure-services"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:infrastructure_services:docs"


config = InfrastructureServicesConfig  # pylint:disable=invalid-name
