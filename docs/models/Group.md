# Group

A group of virtual servers where the number of replicas can be scaled automatically.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**properties** | [**GroupProperties**](GroupProperties.md) |  | 
**entities** | [**GroupEntities**](GroupEntities.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


