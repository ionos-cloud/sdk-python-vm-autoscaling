# GroupPolicyScaleInAction

Defines the action to be taken when the 'scaleInThreshold' is exceeded. Here, scaling is always about removing VMs associated with this VM Auto Scaling Group. By default, the termination policy is 'OLDEST_SERVER_FIRST' is effective.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | &#39;amountType&#x3D;ABSOLUTE&#39; specifies the absolute number of VMs that are added or removed. The value must be between 1 to 10.   &#39;amountType&#x3D;PERCENTAGE&#39; specifies the percentage value that is applied to the current number of replicas of the VM Auto Scaling Group. The value must be between 1 to 200.   At least one VM is always added or removed.   Note that for &#39;SCALE_IN&#39; operations, volumes are not deleted after the server is deleted. | 
**amount_type** | [**ActionAmount**](ActionAmount.md) |  | 
**cooldown_period** | **str** | The minimum time that elapses after the start of this scaling action until the next scaling action is started. With a scaling action in progress, no second scaling action is started for the same VM Auto Scaling Group. Instead, the metric is re-evaluated after the current scaling action completes (either successfully or with errors). This is currently validated with a minimum value of 2 minutes and a maximum value of 24 hours. The default value is 5 minutes if not specified. | [optional] [default to '5m']
**termination_policy** | [**TerminationPolicyType**](TerminationPolicyType.md) |  | [optional] 
**delete_volumes** | **bool** | If set to &#x60;true&#x60;, when deleting an replica during scale in, any attached volume will also be deleted. When set to &#x60;false&#x60;, all volumes remain in the datacenter and must be deleted manually.  **Note**, that every scale-out creates new volumes. When they are not deleted, they will eventually use all of your contracts resource limits. At this point, scaling out would not be possible anymore. | 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_policy_scale_in_action import GroupPolicyScaleInAction

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPolicyScaleInAction from a JSON string
group_policy_scale_in_action_instance = GroupPolicyScaleInAction.from_json(json)
# print the JSON string representation of the object
print(GroupPolicyScaleInAction.to_json())

# convert the object into a dict
group_policy_scale_in_action_dict = group_policy_scale_in_action_instance.to_dict()
# create an instance of GroupPolicyScaleInAction from a dict
group_policy_scale_in_action_from_dict = GroupPolicyScaleInAction.from_dict(group_policy_scale_in_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


