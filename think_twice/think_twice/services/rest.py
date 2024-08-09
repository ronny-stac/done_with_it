import frappe


@frappe.whitelist(allow_guest=True)
def get_user():
     return frappe.db.get_all("User")

         

