# GroupPutProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **datacenter** | [**GroupPutPropertiesDatacenter**](GroupPutPropertiesDatacenter.md) |  | [optional]  |
| **location** | **str** | The data center location. | [readonly]  |
| **max_replica_count** | **int** | The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;&#x3D; 0 and &lt;&#x3D; 200. Will be enforced for both automatic and manual changes. |  |
| **min_replica_count** | **int** | The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;&#x3D; 0 and &lt;&#x3D; 200. Will be enforced for both automatic and manual changes |  |
| **name** | **str** | The name of the VM Auto Scaling Group. This field must not be null or blank. |  |
| **policy** | [**GroupPolicy**](GroupPolicy.md) |  |  |
| **replica_configuration** | [**ReplicaPropertiesPost**](ReplicaPropertiesPost.md) |  |  |


