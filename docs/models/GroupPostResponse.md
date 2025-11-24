# GroupPostResponse

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
**started_actions** | [**list[ActionResource]**](ActionResource.md) | Any background activity caused by this request. You can use this to track the progress of such activities. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_post_response import GroupPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPostResponse from a JSON string
group_post_response_instance = GroupPostResponse.from_json(json)
# print the JSON string representation of the object
print(GroupPostResponse.to_json())

# convert the object into a dict
group_post_response_dict = group_post_response_instance.to_dict()
# create an instance of GroupPostResponse from a dict
group_post_response_from_dict = GroupPostResponse.from_dict(group_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


