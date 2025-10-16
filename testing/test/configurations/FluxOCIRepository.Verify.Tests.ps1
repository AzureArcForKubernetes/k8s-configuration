Describe 'Flux Configuration (OCI Repository - Verification) Testing' {
    BeforeAll {
        . $PSScriptRoot/Constants.ps1
        . $PSScriptRoot/Helper.ps1

        $url = "oci://ghcr.io/stefanprodan/manifests/podinfo"
        $configurationName = "oci-verification-config"
        $tag = "latest"
        $provider = "cosign"
        $issuer = "^https://token.actions.githubusercontent.com$"
        $subject = "^https://github.com/stefanprodan/podinfo.*$"
        $verificationConfigKey = "verifyKeys"
        $verificationConfigValue = "Y2xpZW50Q2VydGlmaWNhdGU="
    }

    It 'Creates a configuration with OCI verification enabled on the cluster' {
        $oidcIdentityJsonSafe = '{"issuer":"' + $issuer + '","subject":"' + $subject + '"}'
        Write-Host "Safe OIDC Identity JSON: $oidcIdentityJsonSafe"

        # Create configuration with verification settings
        $output = az k8s-configuration flux create -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName --namespace $configurationName --scope cluster --kind oci -u $url --tag $tag --verification-provider $provider --match-oidc-identity $oidcIdentityJsonSafe --verification-config "$verificationConfigKey=$verificationConfigValue" --kustomization name=verificationtest path=./ prune=true --no-wait
        $? | Should -BeTrue

        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName
            $jsonOutput = [System.Text.Json.JsonDocument]::Parse($output)
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            $urlReturned = $jsonOutput.RootElement.GetProperty("ociRepository").GetProperty("url").GetString()
            $tagReturned = $jsonOutput.RootElement.GetProperty("ociRepository").GetProperty("repositoryRef").GetProperty("tag").GetString()
            
            # Check verification properties
            $verifyElement = $jsonOutput.RootElement.GetProperty("ociRepository").GetProperty("verify")
            $providerReturned = $verifyElement.GetProperty("provider").GetString()
            $matchOidcIdentity = $verifyElement.GetProperty("matchOidcIdentity")[0]
            $issuerReturned = $matchOidcIdentity.GetProperty("issuer").GetString()
            $subjectReturned = $matchOidcIdentity.GetProperty("subject").GetString()
            $verificationConfigReturned = $verifyElement.GetProperty("verificationConfig").GetProperty($verificationConfigKey).GetString()
            
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "OCI Repository URL: $urlReturned"
            Write-Host "OCI Repository Tag: $tagReturned"
            Write-Host "Verification Provider: $providerReturned"
            Write-Host "OIDC Issuer: $issuerReturned"
            Write-Host "OIDC Subject: $subjectReturned"
            Write-Host "Verification Config Key: $verificationConfigReturned"
            
            if ($provisioningState -eq $SUCCEEDED -and 
                $urlReturned -eq $url -and 
                $tagReturned -eq $tag -and
                $providerReturned -eq $provider -and
                $issuerReturned -eq $issuer -and
                # $subjectReturned -eq $subject -and
                $verificationConfigReturned -eq "<redacted>") {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Updates verification settings for the flux configuration on the cluster" {
        # Update with new verification settings
        $newTag = "1.2.0"
        $newUrl = "oci://ghcr.io/stefanprodan/manifests/podinfo2"
        $newProvider = "cosign"
        $newIssuer = "https://accounts.google.com"
        $newSubject = "https://github.com/example/repo/.github/workflows/build.yml@refs/heads/main"
        $newVerificationConfigKey = "verifycert"
        $newVerificationConfigValue = "Y2FDZXJ0aWZpY2F0ZU5ldw=="
        
        $output = az k8s-configuration flux update -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName --kind oci -u $newUrl --tag $newTag --verification-provider $newProvider --match-oidc-identity "{`"issuer`":`"$newIssuer`",`"subject`":`"$newSubject`"}" --verification-config "$newVerificationConfigKey=$newVerificationConfigValue" --no-wait
        $? | Should -BeTrue

        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName
            $jsonOutput = [System.Text.Json.JsonDocument]::Parse($output)
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            $urlReturned = $jsonOutput.RootElement.GetProperty("ociRepository").GetProperty("url").GetString()
            $tagReturned = $jsonOutput.RootElement.GetProperty("ociRepository").GetProperty("repositoryRef").GetProperty("tag").GetString()
            
            # Check updated verification properties
            $verifyElement = $jsonOutput.RootElement.GetProperty("ociRepository").GetProperty("verify")
            $providerReturned = $verifyElement.GetProperty("provider").GetString()
            $matchOidcIdentity = $verifyElement.GetProperty("matchOidcIdentity")[0]
            $issuerReturned = $matchOidcIdentity.GetProperty("issuer").GetString()
            $subjectReturned = $matchOidcIdentity.GetProperty("subject").GetString()
            $verificationConfigReturned = $verifyElement.GetProperty("verificationConfig").GetProperty($newVerificationConfigKey).GetString()
            
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "OCI Repository URL: $urlReturned"
            Write-Host "OCI Repository Tag: $tagReturned"
            Write-Host "Verification Provider: $providerReturned"
            Write-Host "OIDC Issuer: $issuerReturned"
            Write-Host "OIDC Subject: $subjectReturned"
            Write-Host "Verification Config Key: $verificationConfigReturned"
            
            if ($provisioningState -eq $SUCCEEDED -and 
                $urlReturned -eq $newUrl -and 
                $tagReturned -eq $newTag -and
                $providerReturned -eq $newProvider -and
                $issuerReturned -eq $newIssuer -and
                # $subjectReturned -eq $newSubject -and
                $verificationConfigReturned -eq "<redacted>") {
                break
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Updates configuration with multiple OIDC identities and multiple verification config entries" {
        # Test with multiple OIDC identities and multiple verification config entries
        $multipleIdentities = @(
            "{`"issuer`":`"https://token.actions.githubusercontent.com`",`"subject`":`"https://github.com/repo1/.github/workflows/release.yml@refs/heads/main`"}",
            "{`"issuer`":`"https://accounts.google.com`",`"subject`":`"https://github.com/repo2/.github/workflows/build.yml@refs/heads/main`"}"
        )
        
        # Multiple verification config entries in key=value format
        $multipleVerificationConfigs = @(
            "publicKey1=Y29zaWduUHVibGljS2V5MQ==",
            "publicKey2=Y29zaWduUHVibGljS2V5Mg=="
        )
        
        $output = az k8s-configuration flux update -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName --kind oci --verification-provider "cosign" --match-oidc-identity $multipleIdentities --verification-config $multipleVerificationConfigs --no-wait
        $? | Should -BeTrue

        $n = 0
        do 
        {
            $output = az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName
            $jsonOutput = [System.Text.Json.JsonDocument]::Parse($output)
            $provisioningState = ($output | ConvertFrom-Json).provisioningState
            
            # Check multiple OIDC identities and verification config entries
            $verifyElement = $jsonOutput.RootElement.GetProperty("ociRepository").GetProperty("verify")
            $matchOidcIdentities = $verifyElement.GetProperty("matchOidcIdentity")
            $identityCount = $matchOidcIdentities.GetArrayLength()
            
            $verificationConfig = $verifyElement.GetProperty("verificationConfig")
            $hasPublicKey1 = $verificationConfig.TryGetProperty("publicKey1", [ref]$null)
            $hasPublicKey2 = $verificationConfig.TryGetProperty("publicKey2", [ref]$null)
            
            Write-Host "Provisioning State: $provisioningState"
            Write-Host "Number of OIDC Identities: $identityCount"
            Write-Host "Has publicKey1: $hasPublicKey1"
            Write-Host "Has publicKey2: $hasPublicKey2"
            
            if ($provisioningState -eq $SUCCEEDED -and $identityCount -eq 2 -and $hasPublicKey1 -and $hasPublicKey2) {
                # Verify both identities are present
                $firstIdentity = $matchOidcIdentities[0]
                $secondIdentity = $matchOidcIdentities[1]
                
                $firstIssuer = $firstIdentity.GetProperty("issuer").GetString()
                $secondIssuer = $secondIdentity.GetProperty("issuer").GetString()
                
                Write-Host "First Identity Issuer: $firstIssuer"
                Write-Host "Second Identity Issuer: $secondIssuer"
                
                if (($firstIssuer -eq "https://token.actions.githubusercontent.com" -or $firstIssuer -eq "https://accounts.google.com") -and
                    ($secondIssuer -eq "https://token.actions.githubusercontent.com" -or $secondIssuer -eq "https://accounts.google.com") -and
                    $firstIssuer -ne $secondIssuer) {
                    break
                }
            }
            Start-Sleep -Seconds 10
            $n += 1
        } while ($n -le $MAX_RETRY_ATTEMPTS)
        $n | Should -BeLessOrEqual $MAX_RETRY_ATTEMPTS
    }

    It "Deletes the configuration from the cluster" {
        az k8s-configuration flux delete -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName --force
        $? | Should -BeTrue

        # Configuration should be removed from the resource model
        az k8s-configuration flux show -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters" -n $configurationName
        $? | Should -BeFalse
    }

    It "Performs another list after the delete" {
        $output = az k8s-configuration flux list -c $ENVCONFIG.arcClusterName -g $ENVCONFIG.resourceGroup --cluster-type "connectedClusters"
        $configExists = $output | ConvertFrom-Json | Where-Object { $_.id -Match $configurationName }
        $configExists | Should -BeNullOrEmpty
    }
}