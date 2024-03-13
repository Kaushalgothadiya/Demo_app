// Copyright (c) 2024, kaushal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	//  refresh: function(frm) {
	// 	// frappe.msgprint("hello frappe")
	// 	// frappe.throw("error: Enter the name")
	// }

	// onload:function(frm){
	// 	frappe.msgprint("Hello from the onload event")
	// }

	// validate:function(frm){
	// 	frappe.throw("hello from validate event")
	// }

	// before_save:function(frm){
	// 	frappe.throw("Hello from the before save function")
	// }

	// after_save:function(frm){
	// 	frappe.throw("Hello from the before save function")
	// }

	// age:function(frm){
	// 	frappe.throw("Hello from the age field function")
	// }

	// family_details_on_form_rendered:function(frm){
	// 	frappe.msgprint("error from family member added")
	// }

	// before_submit:function(frm){
	// 	frappe.throw("error throw before the submit")
	// }

	// on_submit:function(frm){
	// 	frappe.throw("error throw On submit")
	// }

	// before_cancel:function(frm){
	// 		frappe.throw("error throw before cancel")
	// 	}

	// after_cancel:function(frm){
	// 		frappe.throw("error throw before cancel")
	// 	}


	// ################# Fetch the value ###########################

	// after_save:function(frm){
	// 	// frappe.msgprint(__("The full name is '{0}'",
	// 	// [frm.doc.firstname+" "+frm.doc.lastname+" "+frm.doc.family_details]
	// 	// ))
	// 	console.log(frm.doc.family_details)
	// 	// for(let row of frm.doc.family_details){
	// 	// 	frappe.msgprint(__("{0} The family name is '{1}' and relation is '{2}'",
	// 	// 	[row.index,row.name,row.relation]
	// 	// 	))
	// 	// }
	// 	let obj=frm.doc.family_details
	// 	frappe.msgprint(obj[1])
	// 	for(let row of frm.doc.family_details){
	// 		frappe.msgprint(__("successfully entered child name index is {0} name is '{1}' and age is '{2}'",
	// 		[row.index,row.name1,row.age]
	// 		))
	// 	}

	// }


	// ############ fire when form is new ##########################

	// refresh:function(frm){
	// 	if(frm.is_new()){
	// 		frm.set_intro('now you can create a new client side scripting doctype')
	// 	}
	// }


	// ############## frm.set value ################################

	// validate:function(frm){
	// 	frm.set_value("full_name",frm.doc.firstname+" "+frm.doc.lastname)
	// }

	// // ################  frm.addchild ##############################

	// validate:function(frm){
	// 	frm.add_child('family_details',{
	// 		name1:'Default child1',
	// 		age:33,
	// 		realtion:'Father'
	// 	})
	// }

	// ##################  frm.df_property ###########################

	// enable:function(frm){
	// 	// frm.set_df_property('firstname','reqd',1)

	// 	// frm.set_df_property('lastname','read_only',1)

	// 	frm.toggle_reqd('age',true)
	// }

	// #################  Add a custom Button ########################
	refresh:function(frm){
		// frm.add_custom_button('Click this button',()=>{
		// 	frappe.msgprint(__("you clicked me"))
		// })

		frm.add_custom_button('click me 1',()=>{
			frappe.msgprint(__("you cliked the 1"))
		},'click me')

		frm.add_custom_button('click me 2',()=>{
			frappe.msgprint(__("you clicked the 2"))
		},'click me')

	}

});

// ################ child client scripting ##########################
frappe.ui.form.on('Family',{
	// age:function(frm){
	// 	frappe.throw("Error from child side")
	// },

	// relation:function(frm,cdt,cdn){
	// 	frappe.throw("Error for relation field")
	// }
});

