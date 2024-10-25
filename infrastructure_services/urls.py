"""Django urlpatterns declaration for infrastructure_services app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter

from infrastructure_services import views

router = NautobotUIViewSetRouter()
router.register("infrastructureservicemodel", views.InfrastructureServiceModelUIViewSet)

urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("infrastructure_services/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
