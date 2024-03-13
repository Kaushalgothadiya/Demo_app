frappe.ready(function() {
	// frappe.throw('error')
	frappe.web_form.validate = () =>{
        age_val=frappe.web_form.get_value('age');
        if (age_val < 18){
            frappe.msgprint('age should be greater than 18');
            return false;
        }
        return true;
    }

    frappe.web_form.on('firstname',(field,value)=>{
        frappe.msgprint('firstname inserted : '+value)
    })
	
});
