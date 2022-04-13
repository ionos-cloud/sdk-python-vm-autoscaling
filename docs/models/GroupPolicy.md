# GroupPolicy

Specifies the behavior of this autoscaling group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and the Trigger defines the circumstances, under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through the thresholds, defined for a given Metric.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **metric** | [**Metric**](Metric.md) |  |  |
| **range** | **str** | Defines the time range, for which the samples will be aggregated. | [optional] [default to '120s'] |
| **scale_in_action** | [**GroupPolicyScaleInAction**](GroupPolicyScaleInAction.md) |  |  |
| **scale_in_threshold** | **float** | The lower threshold for the value of the &#x60;metric&#x60;. Will be used with &#x60;less than&#x60; (&lt;) operator. Exceeding this will start a Scale-In action as specified by the &#x60;scaleInAction&#x60; property. The value must have a higher minimum delta to the &#x60;scaleOutThreshold&#x60; depending on the &#x60;metric&#x60; to avoid competitive actions at the same time. |  |
| **scale_out_action** | [**GroupPolicyScaleOutAction**](GroupPolicyScaleOutAction.md) |  |  |
| **scale_out_threshold** | **float** | The upper threshold for the value of the &#x60;metric&#x60;.  Will be used with &#x60;greater than&#x60; (&gt;) operator. Exceeding this will start a Scale-Out action as specified by the &#x60;scaleOutAction&#x60; property. The value must have a lower minimum delta to the &#x60;scaleInThreshold&#x60; depending on the &#x60;metric&#x60; to avoid competitive actions at the same time. |  |
| **unit** | [**QueryUnit**](QueryUnit.md) |  |  |


