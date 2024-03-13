# Copyright (c) 2024, kaushal and contributors
# For license information, please see license.txt

import frappe



def execute(filters=None):
	if  not filters:filters={}
	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)
	
	if not cs_data:
		# msgprint(("no data found"))
		frappe.msgprint("cs_data is emty")
		return columns, cs_data	
	
	data=[]

	for d in cs_data:
		row=frappe._dict({
			'firstname':d.firstname,
			'age':d.age,
			'dob':d.dob
		})
		data.append(row)

	chart=get_chart_data(data)
	summary=get_report_summary(data)
	return columns, data, None,chart,summary
		
def get_columns():
	return[
		{
			"label": ("First Name"),
			"fieldname": "firstname",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": ("Age"),
			"fieldname": "age",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": ("DOB"),
			"fieldname": "dob",
			"fieldtype": "Date",
			"width": 100
		}
	]

def get_cs_data(filters):
	condtions=get_conditions(filters)
	data=frappe.get_all(
		doctype='Server side scripting',
		fields=['firstname','age','dob'],
        filters=condtions,
		# filters=filters,
		order_by='firstname desc'
	)
	return data
	frappe.msgprint("get_cs_data worked")

def get_conditions(filters):
	conditions={}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key]=value

	return conditions



def get_chart_data(data):
	if not data:
		return None
	
	labels=['Age <=45','Age>45']

	age_data={
		'Age >45':0,
		'Age <=45':0
	}

	dataset=[]

	for entry in data:
		if entry.age <=45:
			age_data['Age <=45']=age_data['Age <=45']+1
		else:
			age_data['Age >45']=age_data['Age >45']+1

	dataset.append({
		'name':'Age status',
		'values':[age_data.get('Age <=45'),age_data.get('Age >45')]
	})

			
	# dataset=[{
	# 	'name':'Age status',
	# 	'values':[age_data.get('Age <=45'),age_data.get('Age >45')]
	# }]

	chart={
		'data':{
			'labels':labels,
			'datasets':dataset
		},
		'type':'pie',
		'hight':300
	}

	return chart

def get_report_summary(data):
	if not data:
		return None
	
	age_below_45,age_above_45=0,0

	for entry in data:
		if entry.age <=45:
			age_below_45=age_below_45+1
		else:
			age_above_45=age_above_45+1

	return[
		{
			'value':age_below_45,
			'indicator':'Green',
			'label':'Age Below 45',
			'datatype':'Int'
		},
		{
			'value':age_above_45,
            'indicator':'Red',
            'label':'Age Above 45',
            'datatype':'Int'
		}
	]