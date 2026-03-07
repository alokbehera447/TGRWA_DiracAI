# Employee Dashboard: Current Project (Employee + Project Manager)

## Backend behavior

### Employee self endpoint

`GET /api/employees/me/` returns:
- `current_project` (project id)
- `current_project_title` (project title)

These values are resolved in this order:
1) `EmployeeProfile.current_project` (if set)
2) any project where `Project.employee_team_members` contains the employee
3) any project where `Project.project_manager` is the logged-in user

This makes the “Current Project” field work even when the employee is only assigned via the project’s team member list.

### Project details endpoint

Use `GET /api/employees/projects/<id>/` to load the full project details for the tab.

## Frontend implementation (tab)

### 1) Load the current project id

```js
const me = await fetch("http://127.0.0.1:8000/api/employees/me/", {
  headers: { Authorization: `JWT ${token}` },
}).then(r => r.json());

const currentProjectId = me.current_project;
const currentProjectTitle = me.current_project_title;
```

### 2) If there is a current project, load its details

```js
let project = null;

if (currentProjectId) {
  project = await fetch(`http://127.0.0.1:8000/api/employees/projects/${currentProjectId}/`, {
    headers: { Authorization: `JWT ${token}` },
  }).then(r => r.json());
}
```

### 3) Render the tab

Show:
- `project.title`
- `project.shortDescription`
- `project.status`
- `project.employee_team_members_data` (employee list)
- `project.project_manager_name`

If `currentProjectId` is null:
- show “No current project assigned”.

## Notes

- If you want employees to always have a single “current project”, set `EmployeeProfile.current_project` during onboarding. The API still works if you don’t.
- If you assign employees only via `employee_team_members`, the dashboard still shows the current project because of the fallback logic.

