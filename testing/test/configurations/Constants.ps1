$ENVCONFIG = Get-Content -Path $PSScriptRoot\..\..\settings.json | ConvertFrom-Json
$SUCCESS_MESSAGE = "Successfully installed the operator"
$FAILED_MESSAGE = "Failed the install of the operator"
$TMP_DIRECTORY = "$PSScriptRoot\..\..\tmp"

$POD_RUNNING = "Running"
$SUCCEEDED = "Succeeded"
$COMPLIANT= "Compliant"

$MAX_RETRY_ATTEMPTS = 24