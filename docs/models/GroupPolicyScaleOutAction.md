# GroupPolicyScaleOutAction

Defines the action to be performed when the 'scaleOutThreshold' is exceeded. Here, scaling is always about adding new VMs to this Auto Scaling group.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **amount** | **float** | &#39;amountType&#x3D;ABSOLUTE&#39; specifies the absolute number of VMs that are added or removed. The value must be between 1 to 10.   &#39;amountType&#x3D;PERCENTAGE&#39; specifies the percentage value that is applied to the current &#39;targetReplicaCount&#39; of the autoscaling group. The value must be between 1 to 200.   At least one VM is always added or removed.   Note that for &#39;SCALE_IN&#39; operations, volumes are not deleted after the server is deleted. |  |
| **amount_type** | [**ActionAmount**](ActionAmount.md) |  |  |
| **cooldown_period** | **str** | The minimum time that elapses after the start of this scaling action until the following scaling action is started. While a scaling action is in progress, no second action is initiated for the same Auto Scaling group. Instead, the metric is re-evaluated after the current scaling action completes (either successfully or with errors). This is currently validated with a minimum value of 2 minutes and a maximum of 24 hours. The default value is 5 minutes if not specified. | [optional] [default to '5m'] |


