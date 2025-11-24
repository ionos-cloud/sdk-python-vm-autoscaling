# ActionProperties

The properties of the resource; the content depends on the resource type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_status** | [**ActionStatus**](ActionStatus.md) |  | 
**action_type** | [**ActionType**](ActionType.md) |  | 

## Example

```python
from ionoscloud_vm_autoscaling.models.action_properties import ActionProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ActionProperties from a JSON string
action_properties_instance = ActionProperties.from_json(json)
# print the JSON string representation of the object
print(ActionProperties.to_json())

# convert the object into a dict
action_properties_dict = action_properties_instance.to_dict()
# create an instance of ActionProperties from a dict
action_properties_from_dict = ActionProperties.from_dict(action_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


