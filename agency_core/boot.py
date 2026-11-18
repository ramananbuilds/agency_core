# Desk launcher branding + routing.
#
# Frappe v16 renders the /desk app grid from `frappe.boot.app_data`
# (frappe/desk/page/desktop/desktop.js -> render_app_icons). Each entry's
# `app_title` comes from that app's own `add_to_apps_screen` hook, and there is
# no server-side way to override another app's hook entry: frappe.get_hooks()
# filters by app_name and loads only that app's hooks.py. Translation via _()
# does not fire for English either.
#
# The opening: sessions.py builds bootinfo.app_data and only afterwards runs
# `extend_bootinfo` hooks, passing bootinfo by reference -- so this hook runs
# last and wins.
#
# Kept in agency_core rather than patching erpnext/hrms/frappe, so app upgrades
# can never reintroduce the old names. Per-client values are DATA: override
# these dicts per instance if a client wants different labels or landings.

# app_name -> desk tile title
APP_TILE_TITLES = {
	"erpnext": "ERP",
	"hrms": "HR",
	"crm": "CRM",
	"helpdesk": "Helpdesk",
	"frappe": "Bizsmith",
}

# app_name -> where its tile lands. Unset means Frappe picks the app's first
# navigable module; set it to send the tile somewhere specific.
APP_ROUTES = {
	"erpnext": "/desk",
}


def extend_bootinfo(bootinfo):
	apps = bootinfo.get("app_data") or []
	for app in apps:
		name = app.get("app_name")

		title = APP_TILE_TITLES.get(name)
		if title and app.get("app_title") != title:
			app["app_title"] = title

		route = APP_ROUTES.get(name)
		if route:
			# app_landing_route() (sidebar.js) prefers the first dock entry over
			# app_route, so a forced route only holds if the dock cannot answer.
			# ERPNext's first dock row is Setup -> ERP Settings, which is not a
			# landing anyone wants, so the dock rows go with the override.
			app["dock"] = []
			app["app_route"] = route
