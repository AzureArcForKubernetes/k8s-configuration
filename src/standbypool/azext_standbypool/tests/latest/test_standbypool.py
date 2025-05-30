# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import *
from azure.cli.testsdk.scenario_tests import AllowLargeResponse
import os
import array

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class StandbypoolScenario(ScenarioTest):

    @ResourceGroupPreparer(location="eastus")
    @AllowLargeResponse()
    def test_standby_virtual_machine_pool_scenarios(self):
        self.kwargs.update({
            "location": "eastus",
            "vmss_name": "myVMSS",
            "standby_pool_name": "testPool",
            "maxReadyCapacity": 3,
            "minReadyCapacity": 3,
            "virtual_machine_state": "Running",
            'template': os.path.join(TEST_DIR, 'CreateVMOTemplate.json')
        })
        
        self.cmd(
            'az deployment group create --resource-group {rg} --name {vmss_name} '
            '--template-file "{template}" '
        )

        # Create
        self.cmd(
            'az standby-vm-pool create --resource-group {rg} --name {standby_pool_name} '
            '--max-ready-capacity {maxReadyCapacity} '
            '--min-ready-capacity {minReadyCapacity} '
            '--vm-state {virtual_machine_state} '
            '--vmss-id /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{rg}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmss_name}',
            checks=[
                JMESPathCheck('name', self.kwargs.get('standby_pool_name', '')),
                JMESPathCheck('provisioningState', 'Succeeded'),
                JMESPathCheck('elasticityProfile.maxReadyCapacity', self.kwargs.get('maxReadyCapacity', 0)),

            ]
        )

        # show
        standbyVMPool = self.cmd(
            'az standby-vm-pool show --resource-group {rg} --name {standby_pool_name}',
            checks=[
                JMESPathCheck('name', self.kwargs.get('standby_pool_name', '')),
                JMESPathCheck('virtualMachineState', self.kwargs.get('virtual_machine_state', '')),
                JMESPathCheck('elasticityProfile.maxReadyCapacity', self.kwargs.get('maxReadyCapacity', 0)),
                JMESPathCheck('provisioningState', 'Succeeded'),
            ]
        )

        # Get runtimeView
        standbyVMPool = self.cmd(
            'az standby-vm-pool status --resource-group {rg} --name {standby_pool_name} --version latest',
            checks=[
                JMESPathCheck('name', 'latest'),
            ]
        ).get_output_in_json()

        assert len(standbyVMPool["instanceCountSummary"][0][ "instanceCountsByState"]) > 0
        assert len(standbyVMPool["status"][ "code"]) > 0    

        # list by resource group
        list_by_rg = self.cmd(
            'az standby-vm-pool list --resource-group {rg}'
        ).get_output_in_json()
        assert(len(list_by_rg) > 0)

        # list by subscription
        list_by_sub = self.cmd(
            'az standby-vm-pool list'
        ).get_output_in_json()
        assert(len(list_by_sub) > 0)


        # delete
        self.cmd(
            'az standby-vm-pool delete --resource-group {rg} --name {standby_pool_name} -y'
        )

    @ResourceGroupPreparer(location="centralindia")
    @AllowLargeResponse()
    def test_standby_container_group_pool_scenarios(self):
        self.kwargs.update({
            "vnet_name": 'myTestVnet',
            "subnet_name": "myTestSubnet",
            "location": "centralindia",
            "standby_pool_name": "cgname",
            "container_profile_name":  "testCGP",
            'template': os.path.join(TEST_DIR, 'CreateContainerGroupProfileTemplate.json')
        })
        self.cmd(
            'az network vnet create --name {vnet_name} --resource-group {rg} '
            '--location {location} --address-prefix "10.0.0.0/16" --subnet-name {subnet_name} --subnet-prefix "10.0.2.0/24"'
        )
        subnet = self.cmd(
            'az network vnet subnet show --resource-group {rg} --name {subnet_name} --vnet-name {vnet_name}'
        ).get_output_in_json()
        subnetId = subnet["id"]
        self.cmd(
            'az deployment group create --resource-group {rg} --name {container_profile_name} '
            '--template-file "{template}" '
        )

        # create
        self.cmd(
            'az standby-container-group-pool create '
            '--resource-group {rg} --name {standby_pool_name} '
            '--container-profile-id /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/{rg}/providers/Microsoft.ContainerInstance/containerGroupProfiles/{container_profile_name} '
            '--profile-revision 1 '
            '--subnet-ids [0].id=' + subnetId + ' '
            '--max-ready-capacity 1 --location {location} '
            '--zones [1]',
            checks=[
                JMESPathCheck('name', self.kwargs.get('standby_pool_name', '')),
                JMESPathCheck('provisioningState', 'Succeeded'),
            ]
        )

        # show
        standbyPool = self.cmd(
            'az standby-container-group-pool show --resource-group {rg} --name {standby_pool_name}',
            checks=[
                JMESPathCheck('name', self.kwargs.get('standby_pool_name', '')),
                JMESPathCheck('provisioningState', 'Succeeded'),
            ]
        )

        # get runtimeView
        standbyVMPool = self.cmd(
            'az standby-container-group-pool status --resource-group {rg} --name {standby_pool_name} --version latest',
            checks=[
                JMESPathCheck('name', 'latest'),
            ]
        ).get_output_in_json()

        assert len(standbyVMPool["instanceCountSummary"][0][ "instanceCountsByState"]) > 0
        assert len(standbyVMPool["status"][ "code"]) > 0

        # list by resource group
        list_by_rg = self.cmd(
            'az standby-container-group-pool list --resource-group {rg}'
        ).get_output_in_json()
        assert(len(list_by_rg) > 0)

        # list by subscription
        list_by_sub = self.cmd(
            'az standby-container-group-pool list'
        ).get_output_in_json()
        assert(len(list_by_rg) > 0)

        # delete
        self.cmd(
            'az standby-container-group-pool delete --resource-group {rg} --name {standby_pool_name} -y'
        )
