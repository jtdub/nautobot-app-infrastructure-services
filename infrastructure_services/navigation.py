"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:infrastructure_services:infrastructureservicemodel_list",
        name="Infrastructure Services",
        permissions=["infrastructure_services.view_infrastructureservicemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:infrastructure_services:infrastructureservicemodel_add",
                permissions=["infrastructure_services.add_infrastructureservicemodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Infrastructure Services", items=tuple(items)),),
    ),
)
