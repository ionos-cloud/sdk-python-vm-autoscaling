# GroupPostEntities

The entities associated with this resource. The content depends on the resource type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**ActionsLinkResource**](ActionsLinkResource.md) |  | [optional] 
**servers** | [**ServersLinkResource**](ServersLinkResource.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_post_entities import GroupPostEntities

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPostEntities from a JSON string
group_post_entities_instance = GroupPostEntities.from_json(json)
# print the JSON string representation of the object
print(GroupPostEntities.to_json())

# convert the object into a dict
group_post_entities_dict = group_post_entities_instance.to_dict()
# create an instance of GroupPostEntities from a dict
group_post_entities_from_dict = GroupPostEntities.from_dict(group_post_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


