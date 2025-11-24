# GroupEntities

The entities associated with this resource. The content depends on the resource type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**ActionCollection**](ActionCollection.md) |  | [optional] 
**servers** | [**ServerCollection**](ServerCollection.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_entities import GroupEntities

# TODO update the JSON string below
json = "{}"
# create an instance of GroupEntities from a JSON string
group_entities_instance = GroupEntities.from_json(json)
# print the JSON string representation of the object
print(GroupEntities.to_json())

# convert the object into a dict
group_entities_dict = group_entities_instance.to_dict()
# create an instance of GroupEntities from a dict
group_entities_from_dict = GroupEntities.from_dict(group_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


