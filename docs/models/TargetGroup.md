# TargetGroup

In order to link VM to ALB, target group must be provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_group_id** | **str** | id | 
**port** | **int** | port | 
**weight** | **int** | weight | 

## Example

```python
from ionoscloud_vm_autoscaling.models.target_group import TargetGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGroup from a JSON string
target_group_instance = TargetGroup.from_json(json)
# print the JSON string representation of the object
print(TargetGroup.to_json())

# convert the object into a dict
target_group_dict = target_group_instance.to_dict()
# create an instance of TargetGroup from a dict
target_group_from_dict = TargetGroup.from_dict(target_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


