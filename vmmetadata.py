from azure.identity import InteractiveBrowserCredential
from azure.mgmt.compute import ComputeManagementClient

cred = InteractiveBrowserCredential()

compute_client = ComputeManagementClient(credential, "<your_subscription_id>")

vm_list = compute_client.virtual_machines.list_all()

for vm in vm_list:
    print(f"VM Name: {vm.name}")
    print(f"Resource Group: {vm.location}")
    print(f"Location: {vm.location}")
    print(f"VM Size: {vm.hardware_profile.vm_size}")
    print(f"OS Disk ID: {vm.storage_profile.os_disk.managed_disk.id}")
    print(f"Data Disks: {[disk.managed_disk.id for disk in vm.storage_profile.data_disks]}")
