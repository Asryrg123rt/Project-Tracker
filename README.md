### Project Tracker

### Overview
I created a Finance project with a parent DocType named Group Working.
Under this parent,I added two child table DocTypes:

1.New Task

2.New Milestones

These child DocTypes are included inside the Group Working parent DocType as table fields.
This structure allows you to store multiple tasks and milestones under one Group Working record, making it easy to manage related activities in a structured and organized way.

### Technologies Used
1.Framework: Frappe

2.Server-side: Python

3.Client-side: JavaScript

### Reports
A custom Query Report was created using the Task table to track and analyze the progress of tasks under the project.
The report uses the Status field from each task to categorize and calculate task distribution across different stages.

The report provides the following insights:

Total Tasks
Counts all tasks available in the Task table.

To-Do Tasks
Filters and counts tasks whose status is marked as "To Do".

In-Progress Tasks
Counts tasks that are currently "In Progress".

Completed Tasks
Counts tasks marked as "Completed".

Based on these values, the report also calculates the overall progress of the project.
Progress is measured by comparing the number of completed tasks against the total number of tasks.

### Dashboard
1.Active projects 

2.Overdue tasks 

3.Near deadlines


### Print formats
I created a custom print format that displays the total number of tasks and milestones available for a project.
This allows users to quickly see how many tasks and milestones are included without manually counting them.

After that,I created a Task Assignment setup, where tasks are assigned to specific users.
