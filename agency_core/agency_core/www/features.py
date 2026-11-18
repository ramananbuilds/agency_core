import frappe
from urllib.parse import quote

# Workspace Link -> desk route
ROUTES = {
    "DocType": lambda v: "/app/" + frappe.scrub(v).replace("_", "-"),
    "Page": lambda v: "/app/" + frappe.scrub(v).replace("_", "-"),
    "Report": lambda v: "/app/query-report/" + quote(v),
    "Dashboard": lambda v: "/app/dashboard-view/" + quote(v),
    "URL": lambda v: v,
}

# Setup / developer areas are not product capabilities
SKIP_WORKSPACES = {
    "Build",
    "Users",
    "Website",
    "Integrations",
    "Tools",
    "Settings",
    "Home",
}


def get_context(context):
    context.no_cache = 1
    context.title = "Everything in Bizsmith"

    groups, seen, total = [], set(), 0

    for ws in frappe.get_all(
        "Workspace",
        filters={"public": 1, "is_hidden": 0},
        fields=["name", "label", "title", "sequence_id"],
        order_by="sequence_id asc",
    ):
        if ws.name in SKIP_WORKSPACES:
            continue

        cards, reports = [], []
        for link in frappe.get_all(
            "Workspace Link",
            filters={
                "parent": ws.name,
                "parenttype": "Workspace",
                "hidden": 0,
                "type": "Link",
            },
            fields=["label", "link_type", "link_to"],
            order_by="idx asc",
        ):
            make_url = ROUTES.get(link.link_type)
            if not make_url or not link.link_to or link.label in seen:
                continue
            # single-doctype settings screens are configuration, not capabilities
            if link.link_type == "DocType" and frappe.get_meta(link.link_to).issingle:
                continue
            seen.add(link.label)
            item = {"label": link.label, "url": make_url(link.link_to)}
            (reports if link.link_type == "Report" else cards).append(item)

        if cards:
            groups.append(
                {
                    "name": ws.get("label") or ws.get("title") or ws.name,
                    "cards": cards,
                    "reports": reports,
                }
            )
            total += len(cards)

    context.groups = groups
    context.total = total
