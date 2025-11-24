# GroupResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_resource import GroupResource

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResource from a JSON string
group_resource_instance = GroupResource.from_json(json)
# print the JSON string representation of the object
print(GroupResource.to_json())

# convert the object into a dict
group_resource_dict = group_resource_instance.to_dict()
# create an instance of GroupResource from a dict
group_resource_from_dict = GroupResource.from_dict(group_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


