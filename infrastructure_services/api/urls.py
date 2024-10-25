"""Django API urlpatterns declaration for infrastructure_services app."""

from nautobot.apps.api import OrderedDefaultRouter

from infrastructure_services.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("infrastructureservicemodel", views.InfrastructureServiceModelViewSet)

urlpatterns = router.urls
