frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo page',
		single_column: true
	});

	page.set_title('My page')

	page.set_indicator('success','green')

	let $btn=page.set_primary_action('new',()=>frappe.msgprint("clicked new"),'octicon')
	let $btnone=page.set_secondary_action('Refresh',()=>frappe.msgprint("clicked the refresh button"),'octicon')

	page.add_menu_item(__('Send Email'), ()=>frappe.msgprint("clicked send email"), 'octicon');
	page.add_menu_item(__("send contact"),()=>frappe.msgprint("clicked send contact"),'octicon')

	page.add_action_item("Delete",()=>frappe.msgprint("clicked form delete"))

	let field=page.add_field({
		label:'status',
		fieldtype:'Select',
		fieldname:'status',
		options:[
			'open',
			'closed',
			'cancelled'
		],
		change(){
		
			frappe.msgprint(this.value)
		}
	})

	// $(frappe.render_template("programming_page",{})).appendTo(page.body)

	$(frappe.render_template("programming_page",{
		data:"hi frappe"
	})).appendTo(page.body)
}