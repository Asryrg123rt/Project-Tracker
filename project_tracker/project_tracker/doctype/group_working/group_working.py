import frappe
from frappe.model.document import Document
 
class GroupWorking(Document):
 
    def on_update(self):
        self.update_group_progress()
 
    def update_group_progress(self):
        project = self.name
 
        total_tasks = frappe.db.count("New Task", {"project": project})
        completed_tasks = frappe.db.count(
            "New Task",
            {"project": project, "status": "Completed"}
        )
 
        progress = 0
        if total_tasks > 0:
            progress = (completed_tasks / total_tasks) * 100
 
        self.progress = round(progress, 2)
 
        if completed_tasks == total_tasks and total_tasks > 0:
            self.status = "Completed"
        else:
            self.status = "In Progress"