# ActionsLinkResource

The scaling actions of the specified VM Auto Scaling Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.actions_link_resource import ActionsLinkResource

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsLinkResource from a JSON string
actions_link_resource_instance = ActionsLinkResource.from_json(json)
# print the JSON string representation of the object
print(ActionsLinkResource.to_json())

# convert the object into a dict
actions_link_resource_dict = actions_link_resource_instance.to_dict()
# create an instance of ActionsLinkResource from a dict
actions_link_resource_from_dict = ActionsLinkResource.from_dict(actions_link_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


