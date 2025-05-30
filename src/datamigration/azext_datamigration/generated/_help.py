# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['datamigration'] = '''
    type: group
    short-summary: Manage Data Migration
'''

helps['datamigration sql-db'] = """
    type: group
    short-summary: Manage database migrations to SQL DB.
"""

helps['datamigration sql-db show'] = """
    type: command
    short-summary: "Retrieve the specified database migration for a given SQL DB."
    examples:
      - name: Get Sql DB database Migration with the expand parameter.
        text: |-
               az datamigration sql-db show --expand "MigrationStatusDetails" --resource-group "testrg" \
--sqldb-instance-name "sqldbinstance" --target-db-name "db1"
      - name: Get Sql DB database Migration without the expand parameter.
        text: |-
               az datamigration sql-db show --resource-group "testrg" --sqldb-instance-name "sqldbinstance" \
--target-db-name "db1"
"""

helps['datamigration sql-db create'] = """
    type: command
    short-summary: "Create a new database migration to a given SQL Db. This command can migrate data from the selected source database tables to the target database tables. If the target database have no table existing, please use New-AzDataMigrationSqlServerSchema command to migrate schema objects from source database to target databse. The link of New-AzDataMigrationSqlServerSchema is https://learn.microsoft.com/cli/azure/datamigration?view=azure-cli-latest#az-datamigration-sql-server-schema"
    parameters:
      - name: --source-sql-connection
        short-summary: "Source SQL Server connection details."
        long-summary: |
            Usage: --source-sql-connection data-source=XX authentication=XX user-name=XX password=XX \
encrypt-connection=XX trust-server-certificate=XX

            data-source: Data source.
            authentication: Authentication type.
            user-name: User name to connect to source SQL.
            password: Password to connect to source SQL.
            encrypt-connection: Whether to encrypt connection or not.
            trust-server-certificate: Whether to trust server certificate or not.
      - name: --target-sql-connection
        short-summary: "Target SQL DB connection details."
        long-summary: |
            Usage: --target-sql-connection data-source=XX authentication=XX user-name=XX password=XX \
encrypt-connection=XX trust-server-certificate=XX

            data-source: Data source.
            authentication: Authentication type.
            user-name: User name to connect to source SQL.
            password: Password to connect to source SQL.
            encrypt-connection: Whether to encrypt connection or not.
            trust-server-certificate: Whether to trust server certificate or not.
    examples:
      - name: Create or Update Database Migration resource with Maximum parameters.
        text: |-
               az datamigration sql-db create --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/\
resourceGroups/testrg/providers/Microsoft.DataMigration/sqlMigrationServices/testagent" --scope \
"/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Sql/servers/sqldbinstanc\
e" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication" data-source="aaa" \
encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" --table-list \
"[Schema1].[TableName1]" "[Schema2].[TableName2]" --target-sql-connection authentication="SqlAuthentication" \
data-source="sqldbinstance" encrypt-connection=true password="placeholder" trust-server-certificate=true \
user-name="bbb" --resource-group "testrg" --sqldb-instance-name "sqldbinstance" --target-db-name "db1"
      - name: Create or Update Database Migration resource with Minimum parameters.
        text: |-
               az datamigration sql-db create --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/\
resourceGroups/testrg/providers/Microsoft.DataMigration/sqlMigrationServices/testagent" --scope \
"/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Sql/servers/sqldbinstanc\
e" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication" data-source="aaa" \
encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" --target-sql-connection \
authentication="SqlAuthentication" data-source="sqldbinstance" encrypt-connection=true password="placeholder" \
trust-server-certificate=true user-name="bbb" --resource-group "testrg" --sqldb-instance-name "sqldbinstance" \
--target-db-name "db1"
"""

helps['datamigration sql-db delete'] = """
    type: command
    short-summary: "Delete an in-progress or completed database migration to SQL DB."
    examples:
      - name: Delete Database Migration resource.
        text: |-
               az datamigration sql-db delete --resource-group "testrg" --sqldb-instance-name "sqldbinstance" \
--target-db-name "db1"
"""

helps['datamigration sql-db cancel'] = """
    type: command
    short-summary: "Stop in-progress database migration to SQL DB."
    examples:
      - name: Stop ongoing migration for the database.
        text: |-
               az datamigration sql-db cancel --migration-operation-id "9a90bb84-e70f-46f7-b0ae-1aef5b3b9f07" \
--resource-group "testrg" --sqldb-instance-name "sqldbinstance" --target-db-name "db1"
"""

helps['datamigration sql-db wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datamigration sql-db is met.
    examples:
      - name: Pause executing next line of CLI script until the datamigration sql-db is successfully created.
        text: |-
               az datamigration sql-db wait --resource-group "testrg" --sqldb-instance-name "sqldbinstance" \
--target-db-name "db1" --created
      - name: Pause executing next line of CLI script until the datamigration sql-db is successfully deleted.
        text: |-
               az datamigration sql-db wait --resource-group "testrg" --sqldb-instance-name "sqldbinstance" \
--target-db-name "db1" --deleted
"""

helps['datamigration sql-managed-instance'] = """
    type: group
    short-summary: Manage database migrations to SQL Managed Instance.
"""

helps['datamigration sql-managed-instance show'] = """
    type: command
    short-summary: "Retrieve the specified database migration for a given SQL Managed Instance."
    examples:
      - name: Get Sql MI database Migration with the expand parameter.
        text: |-
               az datamigration sql-managed-instance show --expand "MigrationStatusDetails" --managed-instance-name \
"managedInstance1" --resource-group "testrg" --target-db-name "db1"
      - name: Get Sql MI database Migration without the expand parameter.
        text: |-
               az datamigration sql-managed-instance show --managed-instance-name "managedInstance1" --resource-group \
"testrg" --target-db-name "db1"
"""

helps['datamigration sql-managed-instance create'] = """
    type: command
    short-summary: "Create a new database migration to a given SQL Managed Instance."
    parameters:
      - name: --source-sql-connection
        short-summary: "Source SQL Server connection details."
        long-summary: |
            Usage: --source-sql-connection data-source=XX authentication=XX user-name=XX password=XX \
encrypt-connection=XX trust-server-certificate=XX

            data-source: Data source.
            authentication: Authentication type.
            user-name: User name to connect to source SQL.
            password: Password to connect to source SQL.
            encrypt-connection: Whether to encrypt connection or not.
            trust-server-certificate: Whether to trust server certificate or not.
      - name: --offline-configuration
        short-summary: "Offline configuration."
        long-summary: |
            Usage: --offline-configuration offline=XX last-backup-name=XX

            offline: Offline migration
            last-backup-name: Last backup name for offline migration. This is optional for migrations from file share. \
If it is not provided, then the service will determine the last backup file name based on latest backup files present \
in file share.
      - name: --target-location
        short-summary: "Target location for copying backups."
        long-summary: |
            Usage: --target-location storage-account-resource-id=XX account-key=XX

            storage-account-resource-id: Resource Id of the storage account copying backups.
            account-key: Storage Account Key.
    examples:
      - name: Create or Update Database Migration resource with Maximum parameters.
        text: |-
               az datamigration sql-managed-instance create --managed-instance-name "managedInstance1" \
--source-location "{\\"fileShare\\":{\\"path\\":\\"C:\\\\\\\\aaa\\\\\\\\bbb\\\\\\\\ccc\\",\\"password\\":\\"placeholder\
\\",\\"username\\":\\"name\\"}}" --target-location account-key="abcd" storage-account-resource-id="account.database.win\
dows.net" --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Micr\
osoft.DataMigration/sqlMigrationServices/testagent" --offline-configuration last-backup-name="last_backup_file_name" \
offline=true --scope "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Sql\
/managedInstances/instance" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication"\
 data-source="aaa" encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" \
--resource-group "testrg" --target-db-name "db1"
      - name: Create or Update Database Migration resource with Minimum parameters.
        text: |-
               az datamigration sql-managed-instance create --managed-instance-name "managedInstance1" \
--source-location "{\\"fileShare\\":{\\"path\\":\\"C:\\\\\\\\aaa\\\\\\\\bbb\\\\\\\\ccc\\",\\"password\\":\\"placeholder\
\\",\\"username\\":\\"name\\"}}" --target-location account-key="abcd" storage-account-resource-id="account.database.win\
dows.net" --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Micr\
osoft.DataMigration/sqlMigrationServices/testagent" --scope "/subscriptions/00000000-1111-2222-3333-444444444444/resour\
ceGroups/testrg/providers/Microsoft.Sql/managedInstances/instance" --source-database-name "aaa" \
--source-sql-connection authentication="WindowsAuthentication" data-source="aaa" encrypt-connection=true \
password="placeholder" trust-server-certificate=true user-name="bbb" --resource-group "testrg" --target-db-name "db1"
      - name: Create or update a Database Migration resource using Azure Blob storage (via System-Assigned Managed Identity) as the backup source.
        text: |-
               az datamigration sql-managed-instance create --managed-instance-name "managedInstance1" \
--source-location '{\\"AzureBlob\\":{\\"storageAccountResourceId\\":\\"/subscriptions/1111-2222-3333-4444/resourceGroups/RG/prooviders\
/Microsoft.Storage/storageAccounts/MyStorage\\",\\"authType\\":\\"ManagedIdentity\\",\\"identity\\":{\\"type\\":\\"SystemAssigned\\"},\\"blobContainerName\\":\\"ContainerName\
-X\\"}}' --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Micr\
osoft.DataMigration/sqlMigrationServices/testagent" --offline-configuration last-backup-name="last_backup_file_name" \
offline=true --scope "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Sql\
/managedInstances/instance" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication"\
 data-source="aaa" encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" \
--resource-group "testrg" --target-db-name "db1"
      - name: Create or update a Database Migration resource using Azure Blob storage (via User-Assigned Managed Identity) as the backup source.
        text: |-
               az datamigration sql-managed-instance create --managed-instance-name "managedInstance1" \
--source-location '{\\"AzureBlob\\":{\\"storageAccountResourceId\\":\\"/subscriptions/1111-2222-3333-4444/resourceGroups/RG/prooviders\
/Microsoft.Storage/storageAccounts/MyStorage\\",\\"authType\\":\\"ManagedIdentity\\",\\"identity\\":{\\"type\\":\\"UserAssigned\\",\\"userAssignedIdentities\\":{\\"/subscriptions/00000000-1111-2222-3333-444444444444/resourcegroups/testrg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/test-uami\":{}}},\\"blobContainerName\\":\\"ContainerName\
-X\\"}}' --migration-service "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Micr\
osoft.DataMigration/sqlMigrationServices/testagent" --offline-configuration last-backup-name="last_backup_file_name" \
offline=true --scope "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Sql\
/managedInstances/instance" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication"\
 data-source="aaa" encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" \
--resource-group "testrg" --target-db-name "db1"
"""

helps['datamigration sql-managed-instance cancel'] = """
    type: command
    short-summary: "Stop in-progress database migration to SQL Managed Instance."
    examples:
      - name: Stop ongoing migration for the database.
        text: |-
               az datamigration sql-managed-instance cancel --managed-instance-name "managedInstance1" \
--migration-operation-id "4124fe90-d1b6-4b50-b4d9-46d02381f59a" --resource-group "testrg" --target-db-name "db1"
"""

helps['datamigration sql-managed-instance cutover'] = """
    type: command
    short-summary: "Initiate cutover for in-progress online database migration to SQL Managed Instance."
    examples:
      - name: Cutover online migration operation for the database.
        text: |-
               az datamigration sql-managed-instance cutover --managed-instance-name "managedInstance1" \
--migration-operation-id "4124fe90-d1b6-4b50-b4d9-46d02381f59a" --resource-group "testrg" --target-db-name "db1"
"""

helps['datamigration sql-managed-instance wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datamigration sql-managed-instance is \
met.
    examples:
      - name: Pause executing next line of CLI script until the datamigration sql-managed-instance is successfully \
created.
        text: |-
               az datamigration sql-managed-instance wait --managed-instance-name "managedInstance1" --resource-group \
"testrg" --target-db-name "db1" --created
"""

helps['datamigration sql-vm'] = """
    type: group
    short-summary: Manage database migrations to SQL VM.
"""

helps['datamigration sql-vm show'] = """
    type: command
    short-summary: "Retrieve the specified database migration for a given SQL VM."
    examples:
      - name: Get Sql VM database Migration with the expand parameter.
        text: |-
               az datamigration sql-vm show --expand "MigrationStatusDetails" --resource-group "testrg" --sql-vm-name \
"testvm" --target-db-name "db1"
      - name: Get Sql VM database Migration without the expand parameter.
        text: |-
               az datamigration sql-vm show --resource-group "testrg" --sql-vm-name "testvm" --target-db-name "db1"
"""

helps['datamigration sql-vm create'] = """
    type: command
    short-summary: "Create a new database migration to a given SQL VM."
    parameters:
      - name: --source-sql-connection
        short-summary: "Source SQL Server connection details."
        long-summary: |
            Usage: --source-sql-connection data-source=XX authentication=XX user-name=XX password=XX \
encrypt-connection=XX trust-server-certificate=XX

            data-source: Data source.
            authentication: Authentication type.
            user-name: User name to connect to source SQL.
            password: Password to connect to source SQL.
            encrypt-connection: Whether to encrypt connection or not.
            trust-server-certificate: Whether to trust server certificate or not.
      - name: --offline-configuration
        short-summary: "Offline configuration."
        long-summary: |
            Usage: --offline-configuration offline=XX last-backup-name=XX

            offline: Offline migration
            last-backup-name: Last backup name for offline migration. This is optional for migrations from file share. \
If it is not provided, then the service will determine the last backup file name based on latest backup files present \
in file share.
      - name: --target-location
        short-summary: "Target location for copying backups."
        long-summary: |
            Usage: --target-location storage-account-resource-id=XX account-key=XX

            storage-account-resource-id: Resource Id of the storage account copying backups.
            account-key: Storage Account Key.
    examples:
      - name: Create or Update Database Migration resource with Maximum parameters.
        text: |-
               az datamigration sql-vm create --source-location "{\\"fileShare\\":{\\"path\\":\\"C:\\\\\\\\aaa\\\\\\\\b\
bb\\\\\\\\ccc\\",\\"password\\":\\"placeholder\\",\\"username\\":\\"name\\"}}" --target-location account-key="abcd" \
storage-account-resource-id="account.database.windows.net" --migration-service "/subscriptions/00000000-1111-2222-3333-\
444444444444/resourceGroups/testrg/providers/Microsoft.DataMigration/sqlMigrationServices/testagent" \
--offline-configuration last-backup-name="last_backup_file_name" offline=true --scope "/subscriptions/00000000-1111-222\
2-3333-444444444444/resourceGroups/testrg/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachines/testvm" \
--source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication" data-source="aaa" \
encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" --resource-group "testrg" \
--sql-vm-name "testvm" --target-db-name "db1"
      - name: Create or Update Database Migration resource with Minimum parameters.
        text: |-
               az datamigration sql-vm create --source-location "{\\"fileShare\\":{\\"path\\":\\"C:\\\\\\\\aaa\\\\\\\\b\
bb\\\\\\\\ccc\\",\\"password\\":\\"placeholder\\",\\"username\\":\\"name\\"}}" --target-location account-key="abcd" \
storage-account-resource-id="account.database.windows.net" --migration-service "/subscriptions/00000000-1111-2222-3333-\
444444444444/resourceGroups/testrg/providers/Microsoft.DataMigration/sqlMigrationServices/testagent" --scope \
"/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.SqlVirtualMachine/sqlVir\
tualMachines/testvm" --source-database-name "aaa" --source-sql-connection authentication="WindowsAuthentication" \
data-source="aaa" encrypt-connection=true password="placeholder" trust-server-certificate=true user-name="bbb" \
--resource-group "testrg" --sql-vm-name "testvm" --target-db-name "db1"
"""

helps['datamigration sql-vm cancel'] = """
    type: command
    short-summary: "Stop in-progress database migration to SQL VM."
    examples:
      - name: Stop ongoing migration for the database.
        text: |-
               az datamigration sql-vm cancel --migration-operation-id "4124fe90-d1b6-4b50-b4d9-46d02381f59a" \
--resource-group "testrg" --sql-vm-name "testvm" --target-db-name "db1"
"""

helps['datamigration sql-vm cutover'] = """
    type: command
    short-summary: "Initiate cutover for in-progress online database migration to SQL VM."
    examples:
      - name: Cutover online migration operation for the database.
        text: |-
               az datamigration sql-vm cutover --migration-operation-id "4124fe90-d1b6-4b50-b4d9-46d02381f59a" \
--resource-group "testrg" --sql-vm-name "testvm" --target-db-name "db1"
"""

helps['datamigration sql-vm wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datamigration sql-vm is met.
    examples:
      - name: Pause executing next line of CLI script until the datamigration sql-vm is successfully created.
        text: |-
               az datamigration sql-vm wait --resource-group "testrg" --sql-vm-name "testvm" --target-db-name "db1" \
--created
"""

helps['datamigration sql-service'] = """
    type: group
    short-summary: Manage Database Migration Service.
"""

helps['datamigration sql-service list'] = """
    type: command
    short-summary: "Retrieve all Database Migration Services in the resource group. And Retrieve all Database \
Migration Services in the subscription."
    examples:
      - name: Get Migration Services in the Resource Group.
        text: |-
               az datamigration sql-service list --resource-group "testrg"
      - name: Get Services in the Subscriptions.
        text: |-
               az datamigration sql-service list
"""

helps['datamigration sql-service show'] = """
    type: command
    short-summary: "Retrieve the Database Migration Service."
    examples:
      - name: Get Migration Service.
        text: |-
               az datamigration sql-service show --resource-group "testrg" --name "service1"
"""

helps['datamigration sql-service create'] = """
    type: command
    short-summary: "Create Database Migration Service."
    examples:
      - name: Create or Update SQL Migration Service with maximum parameters.
        text: |-
               az datamigration sql-service create --location "northeurope" --resource-group "testrg" --name \
"testagent"
      - name: Create or Update SQL Migration Service with minimum parameters.
        text: |-
               az datamigration sql-service create --location "northeurope" --resource-group "testrg" --name \
"testagent"
"""

helps['datamigration sql-service update'] = """
    type: command
    short-summary: "Update Database Migration Service."
    examples:
      - name: Update SQL Migration Service.
        text: |-
               az datamigration sql-service update --tags mytag="myval" --resource-group "testrg" --name "testagent"
"""

helps['datamigration sql-service delete'] = """
    type: command
    short-summary: "Delete Database Migration Service."
    examples:
      - name: Delete SQL Migration Service.
        text: |-
               az datamigration sql-service delete --resource-group "testrg" --name "service1"
"""

helps['datamigration sql-service delete-node'] = """
    type: command
    short-summary: "Delete the integration runtime node."
    examples:
      - name: Delete the integration runtime node.
        text: |-
               az datamigration sql-service delete-node --ir-name "IRName" --node-name "nodeName" --resource-group \
"testrg" --name "service1"
"""

helps['datamigration sql-service list-auth-key'] = """
    type: command
    short-summary: "Retrieve the List of Authentication Keys for Self Hosted Integration Runtime."
    examples:
      - name: Retrieve the List of Authentication Keys.
        text: |-
               az datamigration sql-service list-auth-key --resource-group "testrg" --name "service1"
"""

helps['datamigration sql-service list-integration-runtime-metric'] = """
    type: command
    short-summary: "Retrieve the registered Integration Runtine nodes and their monitoring data for a given Database \
Migration Service."
    examples:
      - name: Retrieve the Monitoring Data.
        text: |-
               az datamigration sql-service list-integration-runtime-metric --resource-group "testrg" --name \
"service1"
"""

helps['datamigration sql-service list-migration'] = """
    type: command
    short-summary: "Retrieve the List of database migrations attached to the service."
    examples:
      - name: List database migrations attached to the service.
        text: |-
               az datamigration sql-service list-migration --resource-group "testrg" --name "service1"
"""

helps['datamigration sql-service regenerate-auth-key'] = """
    type: command
    short-summary: "Regenerate a new set of Authentication Keys for Self Hosted Integration Runtime."
    examples:
      - name: Regenerate the of Authentication Keys.
        text: |-
               az datamigration sql-service regenerate-auth-key --key-name "authKey1" --resource-group "testrg" --name \
"service1"
"""

helps['datamigration sql-service wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datamigration sql-service is met.
    examples:
      - name: Pause executing next line of CLI script until the datamigration sql-service is successfully created.
        text: |-
               az datamigration sql-service wait --resource-group "testrg" --name "service1" --created
      - name: Pause executing next line of CLI script until the datamigration sql-service is successfully updated.
        text: |-
               az datamigration sql-service wait --resource-group "testrg" --name "service1" --updated
      - name: Pause executing next line of CLI script until the datamigration sql-service is successfully deleted.
        text: |-
               az datamigration sql-service wait --resource-group "testrg" --name "service1" --deleted
"""
