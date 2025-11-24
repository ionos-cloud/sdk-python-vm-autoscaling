# ActionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 
**items** | [**list[Action]**](Action.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.action_collection import ActionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ActionCollection from a JSON string
action_collection_instance = ActionCollection.from_json(json)
# print the JSON string representation of the object
print(ActionCollection.to_json())

# convert the object into a dict
action_collection_dict = action_collection_instance.to_dict()
# create an instance of ActionCollection from a dict
action_collection_from_dict = ActionCollection.from_dict(action_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


