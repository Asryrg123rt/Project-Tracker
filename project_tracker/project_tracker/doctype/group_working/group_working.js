// Copyright (c) 2025, sruthi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Group Working", {
	refresh(frm) {

	},
});

frappe.ui.form.on("New Task", {

    due_date: function(frm, cdt, cdn) {

        let row = locals[cdt][cdn];

        if(!row.due_date) return;
 
        let due = moment(row.due_date);

        let today = moment();

        let diff = due.diff(today, "days");
 
        if (diff <= 10) {

            row.priority = "High";

        } else if (diff === 20) {

            row.priority = "Medium";

        } else {

            row.priority = "Low";

        }
 
        frm.refresh_field("new_task");

    }

});

 

