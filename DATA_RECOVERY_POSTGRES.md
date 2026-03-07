# Data Recovery (PostgreSQL)

This project uses PostgreSQL configured in [settings.py](file:///c:/Users/Oppen/OneDrive/Desktop/Backend/Backend_TGRWA_DiracAI/myproject/settings.py).

## What happened

If records disappeared from employee / gis-services / projects tables, they must be restored from a database backup (pg_dump or snapshot). Source code cannot reconstruct old database rows unless you already exported them earlier.

## Create a backup now (recommended)

Use [scripts/pg_dump.ps1](file:///c:/Users/Oppen/OneDrive/Desktop/Backend/Backend_TGRWA_DiracAI/scripts/pg_dump.ps1).

## Restore from a pg_dump file

Use [scripts/pg_restore.ps1](file:///c:/Users/Oppen/OneDrive/Desktop/Backend/Backend_TGRWA_DiracAI/scripts/pg_restore.ps1).

## Targeted backup/restore (Django fixtures)

Create a JSON backup for employee-critical models:

```bash
python manage.py dumpdata account.GisService account.Service account.Project account.EmployeeProfile account.EmployeeDocument account.LeaveRequest account.OvertimeRequest --indent 2 > employee_critical_backup.json
```

Restore it:

```bash
python manage.py loaddata employee_critical_backup.json
```

