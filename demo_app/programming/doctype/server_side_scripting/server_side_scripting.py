# Copyright (c) 2024, kaushal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Serversidescripting(Document):
	
	# def validate(self):
	# 	frappe.msgprint("successfully validate")

	# def before_save(self):
	# 	frappe.throw("message from before save ")

	# def before_insert(self):
	# 	frappe.msgprint("message from before insert")

	# def after_insert(self):
	# 	frappe.throw("message from after insert")

	# def on_update(self):
	#     frappe.throw("message from on update")

	# def before_submit(self):
	# 	frappe.throw("message from before submit")

	# def on_submit(self):
	# 	frappe.throw("message from on submit")

	# def on_cancel(self):
	# 	frappe.throw("message from on cancel")

	# def after_delete(self):
	# 	frappe.throw("message from after delete")
	# def on_trash(self):
	# 	frappe.throw("message from on trash")


########################  fetching the values #############################

	# def validate(self):
	# 	frappe.msgprint("your full name is '{0}' ".format(self.firstname+" "+self.lastname))

	# def validate(self):
	# 	for row in self.get('family_details'):
	# 		frappe.msgprint(_(
	# 			"{0}. your name is '{1}' and age is '{2}' ".format(row.index,row.name1,row.age)))

		# def validate(self):
		# 	for row in self.get('family_details'):
		# 		frappe.msgprint("your age is '{0}'  and name is '{1}' and index is {2}.".format(row.age,row.name1,row.idx))


######################### fetching the doctype ############################

		# def validate(self):
		# 	self.get_document()

		# def get_document(self):
		# 	doc=frappe.get_doc('Client Side Scripting',self.client_side_scripting)
		# 	frappe.msgprint("the fistname is '{0}' and last name is '{1}'".format(doc.firstname,doc.lastname))

		# 	# -----------------child data from doc---------------------------

		# 	for row in doc.get('family_details'):
		# 		frappe.msgprint("The name of child is '{0}' and age is '{1}' .".format(row.name1,row.age))
    
	    ########################### create a doc type ####################################
    
		# def validate(self):
		# 	self.delete_documents()

		# def create_doc_type(self):
		# 	doc=frappe.new_doc('Client Side Scripting')
		# 	doc.firstname='addedfirstname'
		# 	doc.lastname='addedlastname'
		# 	doc.age=22
		# 	doc.append("family_details",{
		# 		'name1':'added child1',
		# 		'age':22,
		# 		'relation':'child'
		# 	})
		# 	doc.insert()
			
		# def delete_documents(self):
		# 	frappe.delete_doc('Client Side Scripting','c956c36ed3')

		# some escape hatches that uses skips the certain checks
		# doc.insert(
		# 	ignore_permissions=True,
        #     ignore_mandatory=True,
		# 	ignore_if_duplicate=True,
		# 	ignore_mandatory=True
		# )

			# def validate(self):
			# 	self.set_documents()

			# def set_documents(self):
			# 	doc=frappe.get_doc('Client Side Scripting','5af80375a3')
			# 	doc.db_set('age',99)
			# 	doc.db_set('firstname','karan')

			# def delete_documents(self):
			# 	doc=frappe.get_doc('Client Side Scripting','55845ac6f6')
			# 	doc.delete()

			# def save_documents(self):
			# 	doc=frappe.new_doc('Client Side Scripting')
			# 	doc.firstname='vaishniv'
			# 	doc.lastname='kumar'
			# 	doc.age=50
			# 	# doc.save()

			# 	doc.save(
			# 		ignore_permissions=True,
            #         ignore_version=True
			# 	)

			

			#------------------ Database API---------------------------------

			# get a list:
			# def validate(self):
			# 	self.set_value()

			#---------------------- Get the values from doctype -----------------------------------------------------
			#pass the parameter: get_value(doctype,name,fieldname)
			# def get_value(self):
			# 	firstname,age=frappe.db.get_value('Client Side Scripting','5af80375a3',['firstname','age'])
			# 	frappe.msgprint("The firstname is '{0}' and age is '{1}'.".format(firstname,age))

			# def set_value(self):
			# 	frappe.db.set_value('Client Side Scripting','0b46c00bd0','age',100)
			# 	firstname,age=frappe.db.get_value('Client Side Scripting','0b46c00bd0',['firstname','age'])
			# 	frappe.msgprint("The firstname is '{0}' and age is '{1}'.".format(firstname,age))

			# def get_list(self):
			# 	doc=frappe.db.get_list(
			# 		"Client Side Scripting",
            #         fields=["firstname","age"],
            #         filters={
            #             "age": 22
            #         }
			# 	)

			# 	for idx,row in enumerate(doc):
			# 		frappe.msgprint(" '{0}' :The firstname is '{1}' and age is '{2}.'".format(idx,row.firstname,row.age))

			##################----------> exits or not <----------------######################

			# def validate(self):
			# 	self.count()

			# def exits_or_not(self):
			# 	doc=frappe.get_doc('Client Side Scripting','5af80375a3')
			# 	if doc.exists():
			# 		frappe.msgprint("the document exists")
			# 	else:
			# 		frappe.msgprint("the document does not exist")
				
			# def exits_or_not(self):
			# 	# doc=frappe.get_doc('Client Side Scripting','5af80375a3')
			# 	if frappe.db.exists('Client Side Scripting','5af80375a3'):
			# 		frappe.msgprint("the document exists")
			# 	else:
			# 		frappe.msgprint("the document does not exist")
				
			# def count(self):
				# count=frappe.db.count('Client Side Scripting',{'enable':1})
				# frappe.msgprint("The count is '{0}'.".format(count))
				
	
			

			# def validate(self):
			# 	self.sql_doc

			# def sql_doc(self):
			# 	# data=frappe.db.sql("""
			# 	# 						SELECT *
			# 	# 	   					FROM `tabServer side scripting`
					   					
			# 	# 				""",as_dict=1)
				
			# 	# for d in data:
			# 	# 	# frappe.msgprint("The firstname is '{0}' and age is '{1}'.".format(d.firstname,d.age))
			# 	# 	frappe.msgprint("data is found",d)

			# 	frappe.msgprint("success")
			# @frappe.whitelist()
			# def frm_call(self,msg,place):
			# 	import time
			# 	time.sleep(2)
			# 	# frappe.msgprint(msg+" "+place)
			# 	self.email='kaushalgothadiya1@gmail.com'
			# 	# return "request is successfully recieved in server"
    
			# @frappe.whitelist()
			# def frappe_call(msg):
			# 	import time
			# 	time.sleep(2)
			# 	# frappe.msgprint(msg)
			# 	# self.email='kaushalgothadiya1@gmail.com'
			# 	return "request is successfully recieved in server"
			pass