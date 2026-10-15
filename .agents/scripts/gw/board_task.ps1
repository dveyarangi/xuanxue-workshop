param(
    [Parameter(Mandatory)][ValidateSet('Install', 'Check', 'Disable', 'Run')][string]$Mode,
    [Parameter(Mandatory)][string]$Root,
    [Parameter(Mandatory)][string]$Repo,
    [Parameter(Mandatory)][string]$Labels,
    [string]$Report = '',
    [string]$TaskName = 'WorkshopBoardReview',
    [string]$Uv = '',
    [switch]$DiscoverOnly
)

$ErrorActionPreference = 'Stop'
trap {
    $reviewErrorDirectory = Join-Path $Root '.local/board-review'
    New-Item -ItemType Directory -Path $reviewErrorDirectory -Force | Out-Null
    $_ | Out-String | Set-Content -LiteralPath (Join-Path $reviewErrorDirectory 'task-error.log')
    exit 1
}
$reviewRoot = (Resolve-Path -LiteralPath $Root).Path
$reviewScript = Join-Path $reviewRoot '.agents/scripts/gw/board_run.py'
if (!(Test-Path -LiteralPath $reviewScript) -or $Repo -notmatch '^[\w.-]+/[\w.-]+$') {
    throw 'A review controller root and explicit owner/repository are required'
}
$reviewLabels = $Labels.Split(',')
if (!$reviewLabels.Count -or ($reviewLabels | Where-Object { $_ -notmatch '^[\w:.-]+$' })) {
    throw 'Recipient labels must be comma-separated identifiers'
}

if ($Mode -eq 'Run') {
    if (!$Report) { throw 'An explicit shared report path is required' }
    Set-Location -LiteralPath $reviewRoot
    $reviewArguments = @('run', '--offline', '--no-project', 'python', $reviewScript,
                         '--root', $reviewRoot, '--repo', $Repo, '--report', $Report)
    foreach ($reviewLabel in $reviewLabels) { $reviewArguments += @('--label', $reviewLabel) }
    if ($DiscoverOnly) { $reviewArguments += '--discover-only' }
    $reviewLocal = Join-Path $reviewRoot '.local/board-review'
    New-Item -ItemType Directory -Path $reviewLocal -Force | Out-Null
    if (!$Uv) { $Uv = (Get-Command uv.exe -ErrorAction Stop).Source }
    $ErrorActionPreference = 'Continue'
    & $Uv @reviewArguments *> (Join-Path $reviewLocal 'task.log')
    exit $LASTEXITCODE
}

$reviewTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($reviewTask -and ($reviewTask.Actions.WorkingDirectory -ne $reviewRoot -or
                     ($reviewTask.Actions.Arguments -notlike '*board_task.ps1*' -and
                      $reviewTask.Actions.Arguments -notlike '*board_run.py*'))) {
    throw 'The named task belongs to another action; choose a different name'
}
if ($Mode -eq 'Disable') {
    if ($reviewTask) { Disable-ScheduledTask -InputObject $reviewTask | Out-Null }
} elseif ($Mode -eq 'Install') {
    if (!$Report) { throw 'An explicit shared report path is required' }
    if (!$Uv) { $Uv = (Get-Command uv.exe -ErrorAction Stop).Source }
    $Uv = (Resolve-Path -LiteralPath $Uv).Path
    $reviewPython = (& $Uv run --offline --no-project python -c 'import sys; print(sys.executable)' 2>$null | Select-Object -Last 1).Trim()
    $reviewPython = Join-Path (Split-Path -Parent $reviewPython) 'pythonw.exe'
    if (!(Test-Path -LiteralPath $reviewPython)) { throw 'A windowless Python runtime is required' }
    $reviewCommand = '"{0}" --root "{1}" --repo "{2}" --report "{3}"' -f $reviewScript, $reviewRoot, $Repo, $Report
    foreach ($reviewLabel in $reviewLabels) { $reviewCommand += ' --label "{0}"' -f $reviewLabel }
    if ($DiscoverOnly) { $reviewCommand += ' --discover-only' }
    $reviewAction = New-ScheduledTaskAction -Execute $reviewPython -Argument $reviewCommand -WorkingDirectory $reviewRoot
    $reviewTrigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddHours(1) -RepetitionInterval (New-TimeSpan -Hours 1)
    $reviewPrincipal = New-ScheduledTaskPrincipal -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
    $reviewSettings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Minutes 55)
    Register-ScheduledTask -TaskName $TaskName -Action $reviewAction -Trigger $reviewTrigger -Principal $reviewPrincipal -Settings $reviewSettings -Description 'Mechanical assignment discovery before model activation' -Force | Out-Null
}
$reviewTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction Stop
$reviewInfo = Get-ScheduledTaskInfo -TaskName $TaskName
[pscustomobject]@{ Name = $TaskName; State = [string]$reviewTask.State;
    Action = $reviewTask.Actions.Arguments; Interval = $reviewTask.Triggers.Repetition.Interval;
    NextRun = $reviewInfo.NextRunTime; LastResult = $reviewInfo.LastTaskResult } | ConvertTo-Json -Depth 4
