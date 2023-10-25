# GroupProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **datacenter** | [**GroupPropertiesDatacenter**](GroupPropertiesDatacenter.md) |  | [optional]  |
| **location** | **str** | The data center location. | [readonly]  |
| **max_replica_count** | **int** | The maximum value for the number of replicas. Must be &gt;&#x3D; 0 and &lt;&#x3D; 100. Will be enforced for both automatic and manual changes. | [optional]  |
| **min_replica_count** | **int** | The minimum value for the number of replicas. Must be &gt;&#x3D; 0 and &lt;&#x3D; 100. Will be enforced for both automatic and manual changes | [optional]  |
| **name** | **str** | The name of the VM Auto Scaling Group. This field must not be null or blank. | [optional]  |
| **policy** | [**GroupPolicy**](GroupPolicy.md) |  | [optional]  |
| **replica_configuration** | [**ReplicaPropertiesPost**](ReplicaPropertiesPost.md) |  | [optional]  |


