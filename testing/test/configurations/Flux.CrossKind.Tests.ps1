Describe 'Bucket Flux Configuration Testing' {
    BeforeAll {
        $configurationName = "cross-kind-config"
        . $PSScriptRoot/Constants.ps1
        . $PSScriptRoot/Helper.ps1
    }

    It 'Creates a configuration and checks that it onboards correctly' {
        az k8s-configuration flux create -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" --kind bucket -u "http://52.190.35.89" --bucket-name flux -n $configurationName --scope cluster --namespace $configurationName --bucket-access-key test --bucket-secret-key test --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            Write-Host "Provisioning State: $provisioningState"
            if ($provisioningState -eq $SUCCEEDED) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Performs a show on the configuration" {
        $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName
        $? | Should -BeTrue
        $output | Should -Not -BeNullOrEmpty
    }

    It "Performs an update on the configuration changing the kind from Bucket to Git" {
        $output = az k8s-configuration flux update -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName --kind git -u "https://github.com/Azure/arc-k8s-demo" --branch main --no-wait
        $? | Should -BeTrue

        # Loop and retry until the configuration installs
        $n = 0
        do {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            Write-Host "Provisioning State: $provisioningState"
            if ($provisioningState -eq $SUCCEEDED) {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
        $output | Should -Not -BeNullOrEmpty
    }

    It "Lists the configurations on the cluster" {
        $output = az k8s-configuration flux list -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters
        $? | Should -BeTrue

        $configExists = $output | ConvertFrom-Json | Where-Object { $_.id -Match $configurationName }
        $configExists | Should -Not -BeNullOrEmpty
    }

    It "Deletes the configuration from the cluster" {
        az k8s-configuration flux delete -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName --force
        $? | Should -BeTrue

        # Configuration should be removed from the resource model
        az k8s-configuration show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters -n $configurationName
        $? | Should -BeFalse
    }

    It "Performs another list after the delete" {
        $output = az k8s-configuration flux list -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type connectedClusters
        $configExists = $output | ConvertFrom-Json | Where-Object { $_.id -Match $configurationName }
        $configExists | Should -BeNullOrEmpty
    }
}