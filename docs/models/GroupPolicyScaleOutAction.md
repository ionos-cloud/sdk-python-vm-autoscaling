# GroupPolicyScaleOutAction

Defines the action to be performed when the 'scaleOutThreshold' is exceeded. Here, scaling is always about adding new VMs to this VM Auto Scaling Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | &#39;amountType&#x3D;ABSOLUTE&#39; specifies the absolute number of VMs that are added or removed. The value must be between 1 to 10.   &#39;amountType&#x3D;PERCENTAGE&#39; specifies the percentage value that is applied to the current number of replicas of the VM Auto Scaling Group. The value must be between 1 to 200.   At least one VM is always added or removed.   Note that for &#39;SCALE_IN&#39; operations, volumes are not deleted after the server is deleted. | 
**amount_type** | [**ActionAmount**](ActionAmount.md) |  | 
**cooldown_period** | **str** | The minimum time that elapses after the start of this scaling action until the following scaling action is started. While a scaling action is in progress, no second action is initiated for the same VM Auto Scaling Group. Instead, the metric is re-evaluated after the current scaling action completes (either successfully or with errors). This is currently validated with a minimum value of 2 minutes and a maximum of 24 hours. The default value is 5 minutes if not specified. | [optional] [default to '5m']

## Example

```python
from ionoscloud_vm_autoscaling.models.group_policy_scale_out_action import GroupPolicyScaleOutAction

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPolicyScaleOutAction from a JSON string
group_policy_scale_out_action_instance = GroupPolicyScaleOutAction.from_json(json)
# print the JSON string representation of the object
print(GroupPolicyScaleOutAction.to_json())

# convert the object into a dict
group_policy_scale_out_action_dict = group_policy_scale_out_action_instance.to_dict()
# create an instance of GroupPolicyScaleOutAction from a dict
group_policy_scale_out_action_from_dict = GroupPolicyScaleOutAction.from_dict(group_policy_scale_out_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


