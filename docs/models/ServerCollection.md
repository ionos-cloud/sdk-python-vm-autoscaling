# ServerCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 
**items** | [**list[Server]**](Server.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.server_collection import ServerCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ServerCollection from a JSON string
server_collection_instance = ServerCollection.from_json(json)
# print the JSON string representation of the object
print(ServerCollection.to_json())

# convert the object into a dict
server_collection_dict = server_collection_instance.to_dict()
# create an instance of ServerCollection from a dict
server_collection_from_dict = ServerCollection.from_dict(server_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


