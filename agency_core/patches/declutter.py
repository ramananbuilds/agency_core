"""Hide the ERPNext modules a client instance does not use.

Three separate Frappe mechanisms are involved, which is why a single switch
never did the job:

  Workspace.is_hidden       -> workspace cards (soft flag; Workspace Manager
                              roles are exempt, see desk/desktop.py)
  User.block_modules        -> the left module rail (applies to everyone,
                              including Administrator)
  Sidebar Item.hidden       -> the nested link trees (Setup -> Settings etc.)

Everything here is idempotent: safe to re-run on every migrate, and safe when
the rows do not exist yet (fresh install before erpnext fixtures load).
"""

import frappe

# Workspaces to hide. Selling is deliberately NOT here: it carries Customer,
# Quotation, Sales Order and Item, which every client needs.
HIDDEN_WORKSPACES = [
	"Assets",
	"Buying",
	"Stock",
	"Manufacturing",
	"Quality",
	"Quality Management",
]

# Modules removed from the left rail. Same set, minus Quality (its workspace is
# "Quality" but the module is "Quality Management").
BLOCKED_MODULES = [
	"Assets",
	"Buying",
	"Stock",
	"Manufacturing",
	"Quality Management",
]

# Entries hidden inside the Setup sidebar's Settings group.
HIDDEN_SETUP_LINKS = [
	"Buying Settings",
	"Stock Settings",
	"Manufacturing Settings",
	"POS Settings",
	"Subscription Settings",
	"Item Variant Settings",
	"Delivery Settings",
	"Currency Exchange Settings",
	"Appointment Booking Settings",
	"Stock Reposting Settings",
]

# The per-user rail block has to be applied to somebody. New users get it from
# the role profile at provisioning time; until then the primary admin carries it.
BLOCKED_MODULES_USERS = ["Administrator"]


def execute():
	hide_workspaces()
	block_modules()
	hide_setup_links()
	frappe.db.commit()


def hide_workspaces():
	for name in HIDDEN_WORKSPACES:
		if frappe.db.exists("Workspace", name) and not frappe.db.get_value(
			"Workspace", name, "is_hidden"
		):
			frappe.db.set_value("Workspace", name, "is_hidden", 1)


def block_modules():
	for user in BLOCKED_MODULES_USERS:
		if not frappe.db.exists("User", user):
			continue
		current = [d.module for d in frappe.get_doc("User", user).get("block_modules")]
		for module in BLOCKED_MODULES:
			if module not in current:
				frappe.get_doc("User", user).append("block_modules", {"module": module})
				current.append(module)
		frappe.get_doc("User", user).save(ignore_permissions=True)


def hide_setup_links():
	rows = frappe.get_all(
		"Sidebar Item",
		filters={"parent": "Setup", "label": ["in", HIDDEN_SETUP_LINKS]},
		fields=["name", "hidden"],
	)
	for row in rows:
		if not row.hidden:
			frappe.db.set_value("Sidebar Item", row.name, "hidden", 1)
