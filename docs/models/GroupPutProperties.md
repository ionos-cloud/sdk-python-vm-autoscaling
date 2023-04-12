# GroupPutProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **datacenter** | [**GroupPutPropertiesDatacenter**](GroupPutPropertiesDatacenter.md) |  | [optional]  |
| **location** | **str** | The data center location. | [readonly]  |
| **max_replica_count** | **int** | The maximum value for the number of replicas for &#39;targetReplicaCount&#39;. Must be &gt;&#x3D; 0 and &lt;&#x3D; 200. Will be enforced for both automatic and manual changes. |  |
| **min_replica_count** | **int** | The minimum value for the number of replicas for &#39;targetReplicaCount&#39;. Must be &gt;&#x3D; 0 and &lt;&#x3D; 200. Will be enforced for both automatic and manual changes |  |
| **target_replica_count** | **int** | The target number of VMs in this group. Depending on the scaling policy, this number is automatically adjusted. VMs are automatically created or destroyed to adjust the actual number of VMs to this target number. If &#39;targetReplicaCount&#39; is specified in the request body, it must be &#39;&gt;&#x3D; minReplicaCount&#39; and &#39;&lt;&#x3D; maxReplicaCount&#39;. | [optional]  |
| **name** | **str** | The name of the Auto Scaling group. This field must not be null or blank. |  |
| **policy** | [**GroupPolicy**](GroupPolicy.md) |  |  |
| **replica_configuration** | [**ReplicaPropertiesPost**](ReplicaPropertiesPost.md) |  |  |


