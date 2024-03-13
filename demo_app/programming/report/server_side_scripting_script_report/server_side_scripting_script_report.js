// Copyright (c) 2024, kaushal and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["server side scripting script report"] = {
	"filters": [
		
		{
			"fieldname":"age",
			"label":__("Age"),
            "fieldtype":"Int",
            "width":100
		},
		{
			"fieldname":"email",
			"label":__("Email"),
            "fieldtype":"Data",
            "width":100
		},
		{
			"fieldname":"name",
			"label":__("Server side scripting name"),
            "fieldtype":"Link",
			"options":"Server side scripting",
            "width":100
		},
		{
			"fieldname":"dob",
			"label":__("Date of Birth"),
            "fieldtype":"Date",
            "width":100
		},
		
		
	]
};
