app_name = "agency_core"
app_title = "Agency Core"
app_publisher = "Bizsmith"
app_description = "Shared core app for Bizsmith client instances"
app_email = "hello@bizsmith.example"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "agency_core",
# 		"logo": "/assets/agency_core/logo.png",
# 		"title": "Agency Core",
# 		"route": "/agency_core",
# 		"has_permission": "agency_core.api.permission.has_app_permission",
# 	}
# ]

# The dock, the rail down the left of the desk, is a document rather than a hook. Author it in
# Manage Dock on a developer-mode site and press Export to App, and it is written to
# `agency_core/dock/agency_core/agency_core.json` for git to carry. An app that ships none has no
# rail: its sidebar gets a switcher in the header instead.
#
# A companion app, one that extends a host app rather than standing on its own, says so with
# `mount_on` on that same record, and its entries are appended to the host's rail. Mounting keeps
# the companion off the apps screen, so it takes precedence over any add_to_apps_screen above.

# Branding
# --------
# App tile titles, logos and landing routes are DATA, not code: white_label's own
# extend_bootinfo rewrites bootinfo.app_data from `App Branding Config` rows
# (custom_title, custom_logo, custom_home_route, hide_in_apps_screen). Configure
# them in the UI. No extend_bootinfo hook belongs here.

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/agency_core/css/agency_core.css"
# app_include_js = "/assets/agency_core/js/agency_core.js"

# include js, css files in header of web template
# web_include_css = "/assets/agency_core/css/agency_core.css"
# web_include_js = "/assets/agency_core/js/agency_core.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "agency_core/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_kanban_js = {"doctype" : "public/js/doctype_kanban.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "agency_core/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "agency_core.utils.jinja_methods",
# 	"filters": "agency_core.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "agency_core.install.before_install"
# after_install = "agency_core.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "agency_core.uninstall.before_uninstall"
# after_uninstall = "agency_core.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "agency_core.utils.before_app_install"
# after_app_install = "agency_core.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "agency_core.utils.before_app_uninstall"
# after_app_uninstall = "agency_core.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "agency_core.build.after_build"

# To hook into the build process of other apps
# The list of apps being built is passed as an argument

# after_app_build = "agency_core.build.after_app_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "agency_core.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["agency_core.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"agency_core.tasks.all"
# 	],
# 	"daily": [
# 		"agency_core.tasks.daily"
# 	],
# 	"hourly": [
# 		"agency_core.tasks.hourly"
# 	],
# 	"weekly": [
# 		"agency_core.tasks.weekly"
# 	],
# 	"monthly": [
# 		"agency_core.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "agency_core.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "agency_core.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "agency_core.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "agency_core.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# white_label swaps out a whitelisted print method at request time, which drops
# it from frappe's whitelist set. Re-register it before the method resolves.
before_request = ["agency_core.print_fix.fix_print_whitelist"]
# after_request = ["agency_core.utils.after_request"]

# SPA tab title. CRM ships its own index.html with the upstream <title>; white_label only
# rewrites document.title client-side, so the tab flashes the upstream name while loading.
after_request = ["agency_core.spa_title.fix_spa_title"]

# Job Events
# ----------
# before_job = ["agency_core.utils.before_job"]
# after_job = ["agency_core.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"agency_core.auth.validate"
# ]

# on_social_login = "agency_core.auth.on_social_login"

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


# Installation
# ------------
# A fresh site has no patch history, so apply the declutter on install too.
# Patches.txt keeps it correct on every subsequent migrate.
after_install = "agency_core.patches.declutter.execute"
