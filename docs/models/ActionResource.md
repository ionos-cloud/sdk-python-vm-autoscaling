# ActionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.action_resource import ActionResource

# TODO update the JSON string below
json = "{}"
# create an instance of ActionResource from a JSON string
action_resource_instance = ActionResource.from_json(json)
# print the JSON string representation of the object
print(ActionResource.to_json())

# convert the object into a dict
action_resource_dict = action_resource_instance.to_dict()
# create an instance of ActionResource from a dict
action_resource_from_dict = ActionResource.from_dict(action_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


