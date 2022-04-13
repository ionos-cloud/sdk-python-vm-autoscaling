# ReplicaProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  |  |
| **cores** | **int** | The total number of cores for the VMs. |  |
| **cpu_family** | [**CpuFamily**](CpuFamily.md) |  | [optional]  |
| **nics** | [**list[ReplicaNic]**](ReplicaNic.md) | List of NICs associated with this Replica. | [optional]  |
| **ram** | **int** | The amount of memory for the VMs in MB, e.g. 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB. |  |


