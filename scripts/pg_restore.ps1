$ErrorActionPreference = "Stop"

param(
  [Parameter(Mandatory = $true)][string]$InFile,
  [string]$HostName = "127.0.0.1",
  [string]$Port = "5432",
  [string]$DbName = "myproject",
  [string]$DbUser = "diracai"
)

if (-not (Test-Path -LiteralPath $InFile)) {
  throw ("File not found: " + $InFile)
}

if (-not $env:PGPASSWORD) {
  throw "PGPASSWORD environment variable is required."
}

pg_restore -h $HostName -p $Port -U $DbUser -d $DbName --clean --if-exists $InFile
Write-Output ("OK: restored " + $InFile)

