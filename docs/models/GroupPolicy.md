# GroupPolicy

Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**Metric**](Metric.md) |  | 
**range** | **str** | Specifies the time range for which the samples are to be aggregated. Must be &gt;&#x3D; 2 minutes. | [optional] [default to '120s']
**scale_in_action** | [**GroupPolicyScaleInAction**](GroupPolicyScaleInAction.md) |  | 
**scale_in_threshold** | **float** | The lower threshold for the value of the &#39;metric&#39;. Used with the &#x60;less than&#x60; (&lt;) operator. When this value is exceeded, a scale-in action is triggered, specified by the &#39;scaleInAction&#39; property. The value must have a higher minimum delta to the &#39;scaleOutThreshold&#39;, depending on the &#39;metric&#39;, to avoid competing for actions at the same time. | 
**scale_out_action** | [**GroupPolicyScaleOutAction**](GroupPolicyScaleOutAction.md) |  | 
**scale_out_threshold** | **float** | The upper threshold for the value of the &#39;metric&#39;. Used with the &#39;greater than&#39; (&gt;) operator. A scale-out action is triggered when this value is exceeded, specified by the &#39;scaleOutAction&#39; property. The value must have a lower minimum delta to the &#39;scaleInThreshold&#39;, depending on the metric, to avoid competing for actions simultaneously. If &#39;properties.policy.unit&#x3D;TOTAL&#39;, a value &gt;&#x3D; 40 must be chosen. | 
**unit** | [**QueryUnit**](QueryUnit.md) |  | [default to QueryUnit.TOTAL]

## Example

```python
from ionoscloud_vm_autoscaling.models.group_policy import GroupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPolicy from a JSON string
group_policy_instance = GroupPolicy.from_json(json)
# print the JSON string representation of the object
print(GroupPolicy.to_json())

# convert the object into a dict
group_policy_dict = group_policy_instance.to_dict()
# create an instance of GroupPolicy from a dict
group_policy_from_dict = GroupPolicy.from_dict(group_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


