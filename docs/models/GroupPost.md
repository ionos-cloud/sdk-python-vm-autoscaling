# GroupPost

A group of virtual servers where the number of replicas can be scaled automatically.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**properties** | [**GroupProperties**](GroupProperties.md) |  | 
**entities** | [**GroupPostEntities**](GroupPostEntities.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_post import GroupPost

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPost from a JSON string
group_post_instance = GroupPost.from_json(json)
# print the JSON string representation of the object
print(GroupPost.to_json())

# convert the object into a dict
group_post_dict = group_post_instance.to_dict()
# create an instance of GroupPost from a dict
group_post_from_dict = GroupPost.from_dict(group_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


