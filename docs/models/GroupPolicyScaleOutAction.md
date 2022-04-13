# GroupPolicyScaleOutAction

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **amount** | **float** | When &#x60;amountType &#x3D;&#x3D; ABSOLUTE&#x60;, this is the number of VMs added or removed in one step. When &#x60;amountType &#x3D;&#x3D; PERCENTAGE&#x60;, this is a percentage value, which will be applied to the autoscaling group&#39;s current &#x60;targetReplicaCount&#x60; in order to derive the number of VMs that will be added or removed in one step. There will always be at least one VM added or removed.   For SCALE_IN operation now volumes are NOT deleted after the server deletion. |  |
| **amount_type** | [**ActionAmount**](ActionAmount.md) |  |  |
| **cooldown_period** | **str** | Minimum time to pass after this Scaling action has started, until the next Scaling action will be started. Additionally, if a Scaling action is currently in progress, no second Scaling action will be started for the same autoscaling group. Instead, the Metric will be re-evaluated after the current Scaling action is completed (either successfully or with failures). This is validated with a minimum value of 2 minutes and a maximum of 24 hours currently. Default value is 5 minutes if not given. | [optional] [default to '5m'] |


