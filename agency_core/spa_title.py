"""Server-render the SPA <title> so the browser tab shows the brand name at once.

CRM and Helpdesk ship their own index.html with the upstream title ("Frappe CRM").
white_label rewrites `document.title` from the text-replacement rules, but that
runs only after the bundle loads — so the tab flashes the upstream name on every
cold load. Rewriting the HTML here removes the flash, and the value still comes
from the App Branding Config rows (custom_title / original_title), so it stays
UI-configured.

ponytail: cosmetic-only, no timeout handling — a failure just logs and leaves the
original title in place.
"""

import html
import re

import frappe

_TITLE_RE = re.compile(r"<title>.*?</title>", re.IGNORECASE | re.DOTALL)


def _title_for_path(path: str) -> str | None:
	from white_label.boot import _get_bootinfo_payload

	payload = _get_bootinfo_payload() or {}
	for cfg in (payload.get("apps") or {}).values():
		spa = (cfg or {}).get("spa") or {}
		prefix = spa.get("route_prefix")
		if not (cfg.get("is_active") and spa.get("is_spa") and prefix):
			continue
		if path == prefix or path.startswith(prefix + "/"):
			return (cfg.get("custom_title") or cfg.get("original_title") or "").strip()
	return None


def fix_spa_title(response=None, request=None) -> None:
	try:
		if response is None or request is None:
			return
		if not (response.headers.get("Content-Type") or "").startswith("text/html"):
			return
		path = (request.path or "/").rstrip("/") or "/"
		title = _title_for_path(path)
		if not title:
			return
		body = response.get_data(as_text=True)
		new_body, subs = _TITLE_RE.subn(f"<title>{html.escape(title)}</title>", body, count=1)
		if not subs or new_body == body:
			return
		response.set_data(new_body)
		response.headers["Content-Length"] = str(len(response.get_data()))
	except Exception:
		frappe.log_error(title="agency_core.spa_title.fix_spa_title failed")