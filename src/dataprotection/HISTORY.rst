.. :changelog:

Release History
===============

1.5.6
+++++
* Updated the packaged AKS-preview SDK.

1.5.5
+++++
* `az dataprotection backup-vault initialize-restoreconfig:` Fixed a bug when initializing a restore object for Vaulted AKS Backups.
* Added CRR support for southeastus, westus3 region.

1.5.4
+++++
* Removed dependency on `msrestazure.tools`

1.5.3
+++++
* `az dataprotection backup-instance initialize-for-data-recovery`: Fixed a bug when trying to initialize AKS restore.

1.5.2
+++++
* Added support for multi-user authentication for dataprotection policy updates
* `az dataprotection backup-instance update-policy`: New parameters - `--operation-requests` and `--tenant-id` for allowing operations on MUA-protected resources.

1.5.1
+++++
* Added support for multi-user authentication for CMK encryption changes

1.5.0
+++++
* Support for vaulted backup for AKS
* `az dataprotection backup-policy get-default-policy-template`: For AzureKubernetesService, default policy now adds vaulted backup rules.
* `az dataprotection backup-vault initialize-restoreconfig:` Three new parameters - `--staging-resource-group-id`, `--staging-storage-account-id`, `--resource-modifier-reference`.


1.4.0
+++++
* Added support for cmk encryption on backup vault
* `az dataprotection backup-vault create ` Added parameters `--user-assigned-identities` to provide list of user assigned managed identities to backup-vault
* `az dataprotection backup-vault create ` Added parameters `--cmk-encryption-state`, `cmk-infrastructure-encryption`, `--cmk-encryption-key-uri`, `--cmk-identity-type`, `--cmk-user-assigned-identity-id` to enable cmk encryption on backup-vault
* `az dataprotection backup-vault update ` Added parameters `--user-assigned-identities` to update list of user assigned managed identities to backup-vault
* `az dataprotection backup-vault update ` Added parameters `--cmk-encryption-state`, `--cmk-encryption-key-uri`, `--cmk-identity-type`, `--cmk-user-assigned-identity-id` to update cmk encryption settings on backup-vault


1.3.0
+++++
* Added support for vaulted blob backup and restore
* `az dataprotection backup-instance initialize-backupconfig`: Added parameters `--vaulted-backup-containers` to provide list of containers to backup
* `az dataprotection backup-instance initialize-backupconfig`: Added parameters `--include-all-containers`, `--storage-account-name`, `storage-account-resource-group` to backup all containers in a storage storage-account-resource-group
* `az dataprotection backup-instance update`: New command, which takes `--vaulted-blob-container-list` to which we pass the output of `initialize-backupconfig`
* `az dataprotection backup-instance update-policy`: Had a bug where policy update for a vaulted blob container would remove the backed up containers entirely. This was rewritten to fix that
* `az dataprotection backup-instance restore initialize-for-item-recovery`: now takes `--vaulted-blob-prefix-pattern`, a new prefix pattern for vaulted blobs restore

1.2.0
+++++
* The following commands and scenarios now have resourceguard-based MUA protection
* `az dataprotection backup-vault update` - Modify Soft Delete and Immutability State
* `az dataprotection backup-instance stop-protection` - Stop Protection
* `az dataprotection backup-instance suspend-backups` - Suspend Backups
* `az dataprotection backup-instance restore trigger` - Trigger Restore
* `az dataprotection resource-guard` - Also now supporting shorthands for new RecoveryServices critical operations.

1.1.0
+++++
* Added dataprotection support for PostgreSQLFlexibleServer and MySQL workloads: new manifests, code cleanup.
* `az dataprotection backup-instance update-msi-permissions`: New parameter `--target-storage-account-id` for Restore, support Restore for new workloads, code cleanup.

1.0.0
++++++
* Added support for Cross Region Restore for Backup Vaults.
* `az dataprotection backup-vault create`: New parameter `--cross-region-restore-state/--crr-state` that can be set to Enabled/Disabled.
* `az dataprotection backup-vault update`: New parameter `--cross-region-restore-state/--crr-state` that can be set to Enabled/Disabled.
* `az dataprotection backup-vault list-from-resourcegraph`: New command to fetch Backup Vault details from Azure Resource Graph.
* `az dataprotection recovery-point list`: New parameter `--use-secondary-region` to be used when listing from the secondary region.
* `az dataprotection backup-instance validate-for-restore`: New parameter `--use-secondary-region` to be used when restoring to the secondary region.
* `az dataprotection backup-instance restore trigger`: New parameter `--use-secondary-region` to be used when restoring to the secondary region.
* `az dataprotection backup-job list`: New parameter `--use-secondary-region` which can be used in disaster scenario when primary region is down.
* `az dataprotection backup-job show`: New parameter `--use-secondary-region` which can be used in disaster scenario when primary region is down.

0.11.2
++++++
* `az dataprotection backup-instance update-msi-permissions`: Added UAMI support for AKS backup/restore.

0.11.1
++++++
* Added '-v' option for all --vault-name parameters

0.11.0
++++++
* Add support for Multi-User Authentication for Backup vaults
* `az dataprotection backup-vault resource-guard-mapping`: Support the creation and management of ResourceGuard Mappings onto a Backup Vault.
* `az dataprotection resource-guard unlock`: Unlock ResourceGuard in order to perform protected/Critical operations

0.10.0
++++++
* Add complete support for Soft Delete
* `az dataprotection backup-instance deleted-backup-instance`: Add support to list, show, and undelete soft deleted backed up instances

0.9.2
++++++
* Updated API version to 2023-05-01 across the board
* `az dataprotection backup-instance initialize-backupconfig`: Added support for AKS Hooks
* `az dataprotection backup-instance initialize-restoreconfig`: Added support for AKS Hooks

0.9.1
+++++
* `az dataprotection update-msi-permissions`: Fixed bug in fetching AKS workload resource group
* `az dataprotection backup-policy create-generic-criteria`: Bug-fix in day-of-month argument validation
* `az dataprotection recovery-point`: Added user warning when start-time is after end-time
* `az dataprotection backup-instance`: Migrated to AAZ-dev-tools
* `az dataprotection backup-policy`: Migrated to AAZ-dev-tools
* `az dataprotection resource-guard`: Migrated to AAZ-dev-tools
* `az dataprotection restorable-time-range`: Migrated to AAZ-dev-tools

0.9.0
+++++
* Add support for cross-subscription-restore for Dataprotection.
* `az dataprotection backup-vault create`: Add parameter (`--cross-subscription-restore-state`/ `--csr-state`), allowing backup vault creation with the cross-subscription-restore state flag set.
* `az dataprotection backup-vault update`: Add parameter (`--cross-subscription-restore-state`/ `--csr-state`), allowing updating the cross-subscription-restore state flag in backup vaults.
* `az dataprotection backup-instance restore initialize-for-data-recovery-as-files`: Add parameter `--target-resource-id`, required for cross-subscription-restore of OSS Scenario as files.

0.8.2
+++++
* No user-facing updates - quickfix making the `aaz_operations` folder a module.

0.8.1
+++++
* `az dataprotection recovery-point`: Migrated to AAZ-dev-tools
* `az dataprotection job`: Migrated to AAZ-dev-tools

0.8.0
+++++
* Add support for new datasource type: AzureKubernetesService (for all relevant operations in `backup-instance`` and `backup-policy`)
* `az dataprotection backup-instance initialize-backupconfig`: New command to create a backup configuration required for AzureKubernetesService backup.
* `az dataprotection backup-instance initialize-restoreconfig`: New command to create a restore configuration required for AzureKubernetesService restore.
* `az dataprotection backup-instance update-msi-permissions`: Added support for "Restore" operation.
* `az dataprotection backup-instance initialize`: Add parameters `--friendly-name` and `--backup-configuration` for AzureKubernetesService support.
* `az dataprotection backup-instance initialize-for-data-recovery`: Add parameter `--backup-instance-id`, adding support for Original Location Restore.
* `az dataprotection backup-instance initialize-for-item-recovery`: Add parameter `--target-resource-id`, adding support for Alternate Location Restore.

0.7.0
++++++
* `az dataprotection backup-vault create`: Add support for optional `--immutability-state`, `--soft-delete-state`, `--soft-delete-retention` parameters, corresponding to new Immutable Vault and Enhanced Soft Delete features
* `az dataprotection backup-vault update`: Add support for optional `--soft-delete-state`, `--soft-delete-retention` parameters.

0.6.0
++++++
* `az dataprotection backup-instance initialize`: Add optional `--tags` parameter

0.5.0
++++++
* `az dataprotection backup-instance update-msi-permissions`: New command to grant missing permissions to backup vault MSI
* `az dataprotection backup-instance initialize`: Added optional `--snapshot-resource-group-name` parameter

0.4.0
++++++
* `az dataprotection resource-guard`: Onboard ResourceGuard to dataprotection extension
* `az dataprotection backup-vault create/update`: Add support for Azure Monitor based alerts

0.3.0
++++++
* API version upgrade with bug fixes
* az dataprotection backup-instance: Support stop-protection/suspend-backup/resume-protection

0.2.0
++++++
* onboard OSS workload to dataprotection extension.
* [BREAKING CHANGE] `az dataprotection restorable-time-range find`: `--backup-instances` renamed to `--backup-instance-name`.

0.1.0
++++++
* Initial release.
