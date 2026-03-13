$ErrorActionPreference = "Stop"

param(
  [string]$OutFile = ("backup_" + (Get-Date -Format "yyyyMMdd_HHmmss") + ".dump"),
  [string]$HostName = "127.0.0.1",
  [string]$Port = "5432",
  [string]$DbName = "myproject",
  [string]$DbUser = "diracai"
)

if (-not $env:PGPASSWORD) {
  throw "PGPASSWORD environment variable is required."
}

pg_dump -Fc -h $HostName -p $Port -U $DbUser -f $OutFile $DbName
Write-Output ("OK: " + $OutFile)

