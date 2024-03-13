// Copyright (c) 2024, kaushal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Practise', {
	after_save: function(frm) {
		// frm.set_value("fullname",frm.doc.firstname+" "+frm.doc.lastname)
		frm.set_value("name1",frm.doc.firstname)
	}
});
