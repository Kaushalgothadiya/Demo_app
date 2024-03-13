# Copyright (c) 2024, kaushal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ClientSideScripting(Document):
	pass

# @frappe.whitelist()
# def frappe_call(self,msg):
# 	# import time
#     # time.sleep(2)
#     # frappe.msgprint(msg+" "+place)
#     # self.email='kaushalgothadiya1@gmail.com'
#     return "request is successfully recieved in server"