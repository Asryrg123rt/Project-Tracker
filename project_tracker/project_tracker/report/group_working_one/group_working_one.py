# Copyright (c) 2025, sruthi and contributors
# For license information, please see license.txt

# import frappe
# from frappe import _
 
# def execute(filters: dict | None = None):
#     """
#     Main report execution function.
#     Returns columns and data for Project Progress report.
#     """
#     if not filters:
#         filters = {}

#     columns = get_columns()
#     data = get_project_progress_data(filters)

#     return columns, data
 
# def get_columns():
#     return [
#         {"label": "Project Name", "fieldname": "project_name", "fieldtype": "Data", "width": 200},
#         {"label": "Start Date", "fieldname": "start_date", "fieldtype": "Date", "width": 150},
#         {"label": "End Date", "fieldname": "end_date", "fieldtype": "Date", "width": 120},
#         {"label": "Status", "fieldname": "status", "fieldtype": "Select", "width": 150},
#         {"label": "%completed", "fieldname": "progress", "fieldtype": "Select", "width": 100}
#     ]
 
 
# def get_project_progress_data(filters):
#     """
#     Returns a list of projects with total tasks, completed tasks and progress %
#     """
#     conditions = ""
#     values = {}

#     # Filter by project name
#     if filters.get("project_name"):
#         conditions += " AND p.name = %(project_name)s"
#         values["project_name"] = filters["project_name"]

#     # Filter by status
#     if filters.get("status"):
#         conditions += " AND p.status = %(status)s"
#         values["status"] = filters["status"]

#     query = f"""
#         SELECT
#             p.name AS project,
#             p.status AS status,
#             COUNT(t.name) AS total_tasks,
#             SUM(CASE WHEN t.status = 'Completed' THEN 1 ELSE 0 END) AS completed_tasks,
#             IF(COUNT(t.name)=0, 0, (SUM(CASE WHEN t.status = 'Completed' THEN 1 ELSE 0 END) / COUNT(t.name)) * 100) AS progress
#         FROM `tabProject` p
#         LEFT JOIN `tabTask` t
#             ON t.project = p.name
#         WHERE 1 = 1 {conditions}
#         GROUP BY p.name, p.status
#         ORDER BY p.name
#     """

#     return frappe.db.sql(query, values, as_dict=True)
