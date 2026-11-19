"""Keep print preview working while white_label monkeypatches it.

white_label replaces `frappe.www.printview.get_html_and_style` -- a
@frappe.whitelist() method -- with a bare closure so it can inject brand text
before the browser sees it. Frappe's permission gate is a *set membership* test
(`is_whitelisted` -> `method not in whitelisted`), so the replacement closure
drops out and every print preview fails with:

    You are not permitted to access this resource. Login to access
    Function white_label.print_overrides.wrapped is not whitelisted.

before_request hooks run in init_request() before the method is resolved, so
re-adding the patched function to the set is enough. Drop this module once
white_label keeps the decorator (functools.wraps) in its own wrapper.
"""

import frappe
import frappe.utils.pdf as pdfmod
import frappe.www.printview as pv

_METHODS = ["GET", "POST", "PUT", "DELETE"]


def fix_print_whitelist():
	try:
		from white_label import print_overrides as po

		pv = frappe.www.printview

		# Apply the branding wrappers directly: install_once() ends by writing a
		# flag through frappe.local.__setattr__, which Frappe's Local rejects and
		# logs as an Error Log row on every request.
		if not getattr(frappe.utils.pdf, "_wl_wrapped", False):
			po._install_pdf_patch()
		if not getattr(pv, "_wl_wrapped", False):
			po._install_printview_patch()
		po._PATCHED = True

		fn = pv.get_html_and_style
		if fn not in frappe.whitelisted:
			frappe.whitelisted.add(fn)
			frappe.allowed_http_methods_for_whitelisted_func[fn] = (
				frappe.allowed_http_methods_for_whitelisted_func.get(
					getattr(fn, "__wrapped__", None), _METHODS
				)
			)
	except Exception:
		frappe.log_error(title="agency_core.print_fix.fix_print_whitelist failed")
