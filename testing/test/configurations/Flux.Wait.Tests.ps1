Describe 'Basic Flux Configuration Testing' {
    BeforeAll {
        $configurationName = "cluster-config"
        $secondConfig = "wait-config2"
        . $PSScriptRoot/Constants.ps1
        . $PSScriptRoot/Helper.ps1
    }

    It 'Creates a configuration for testing default wait value' {
        az k8s-configuration flux create -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -u "https://github.com/Azure/gitops-flux2-kustomize-helm-mt" -n $configurationName --scope cluster --namespace $configurationName --branch main --kustomization name=infra path=./infrastructure prune=true --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
            $jsonOutput = $output | ConvertFrom-Json
            $provisioningState = $jsonOutput.provisioningState
            $complianceState = $jsonOutput.complianceState
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "Compliance State: $complianceState"
            Write-Host "Json Output: $jsonOutput"
            Write-Host "Output: $output"

            if ($jsonOutput.kustomizations -and $jsonOutput.kustomizations["infra"]) {
                $waitState = $jsonOutput.kustomizations["infra"]["wait"]
            } else {
                $waitState = $null
            }
            Write-Host "Wait State: $waitState"
            if ($provisioningState -eq $SUCCEEDED -and $waitState -eq $true -and $complianceState -eq $COMPLIANT) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Performs a re-PUT of the configuration on the cluster, with health check disabled for kustomization" {
        az k8s-configuration flux update -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -u "https://github.com/Azure/gitops-flux2-kustomize-helm-mt" -n $configurationName --kustomization name=infra path=./infrastructure disable-health-check=true --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            $waitState = ($output | ConvertFrom-Json).kustomizations["infra"]["wait"]
            $pruneState = ($output | ConvertFrom-Json).kustomizations["infra"]["prune"]
            $complianceState = ($output | ConvertFrom-Json).complianceState
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "Compliance State: $complianceState"
            Write-Host "Wait State: $waitState"
            Write-Host "Prune State: $pruneState"
            if ($provisioningState -eq $SUCCEEDED -and $waitState -eq $false -and $pruneState -eq $true -and $complianceState -eq $COMPLIANT) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Create a new kustomization for the existing configuration on the cluster" {
        az k8s-configuration flux kustomization create -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName --kustomization-name apps --path ./apps/staging --prune --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            $complianceState = ($output | ConvertFrom-Json).complianceState
            $waitState = ($output | ConvertFrom-Json).kustomizations["apps"]["wait"]
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "Compliance State: $complianceState"
            Write-Host "Wait State: $waitState"
            if ($provisioningState -eq $SUCCEEDED -and $waitState -eq $true -and $complianceState -eq $COMPLIANT) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Updates the existing kustomization on the cluster, setting wait to false" {
        az k8s-configuration flux kustomization update -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName --kustomization-name apps --path ./apps/staging --prune --disable-health-check --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            $waitState = ($output | ConvertFrom-Json).kustomizations["apps"]["wait"]
            $pruneState = ($output | ConvertFrom-Json).kustomizations["apps"]["prune"]
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "Wait State: $waitState"
            Write-Host "Prune State: $pruneState"
            if ($provisioningState -eq $SUCCEEDED -and $waitState -eq $false -and $pruneState -eq $true) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Deletes the configuration from the cluster" {
        az k8s-configuration flux delete -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName --force
        $? | Should -BeTrue

        # Configuration should be removed from the resource model
        az k8s-configuration show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
        $? | Should -BeFalse
    }

    It 'Creates a configuration for testing with health check disabled for kustomization' {
        az k8s-configuration flux create -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -u "https://github.com/Azure/gitops-flux2-kustomize-helm-mt" -n $secondConfig --scope cluster --namespace $secondConfig --branch main --kustomization name=infra path=./infrastructure prune=true disable-health-check=true --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $secondConfig
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            $waitState = ($output | ConvertFrom-Json).kustomizations["infra"]["wait"]
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "Wait State: $waitState"
            if ($provisioningState -eq $SUCCEEDED -and $waitState -eq $false) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Create a new kustomization for the existing configuration on the cluster with health check disabled" {
        az k8s-configuration flux kustomization create -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $secondConfig --kustomization-name apps --path ./apps/staging --prune --disable-health-check --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $secondConfig
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            $waitState = ($output | ConvertFrom-Json).kustomizations["apps"]["wait"]
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "Wait State: $waitState"
            if ($provisioningState -eq $SUCCEEDED -and $waitState -eq $false) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Deletes the configuration from the cluster" {
        az k8s-configuration flux delete -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $secondConfig --force
        $? | Should -BeTrue

        # Configuration should be removed from the resource model
        az k8s-configuration show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $secondConfig
        $? | Should -BeFalse
    }
}