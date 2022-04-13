# GroupProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **max_replica_count** | **int** | Maximum replica count value for &#x60;targetReplicaCount&#x60;. Will be enforced for both automatic and manual changes. | [optional]  |
| **min_replica_count** | **int** | Minimum replica count value for &#x60;targetReplicaCount&#x60;. Will be enforced for both automatic and manual changes. | [optional]  |
| **target_replica_count** | **int** | The target number of VMs in this Group. Depending on the scaling policy, this number will be adjusted automatically. VMs will be created or destroyed automatically in order to adjust the actual number of VMs to this number. If targetReplicaCount is given in the request body then it must be &gt;&#x3D; minReplicaCount and &lt;&#x3D; maxReplicaCount. | [optional]  |
| **name** | **str** | User-defined name for the autoscaling group. | [optional]  |
| **policy** | [**GroupPolicy**](GroupPolicy.md) |  | [optional]  |
| **replica_configuration** | [**ReplicaPropertiesPost**](ReplicaPropertiesPost.md) |  | [optional]  |
| **datacenter** | [**Resource**](Resource.md) |  | [optional]  |
| **location** | **str** | Location of the data center. | [readonly]  |


