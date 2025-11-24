# Server

Links a data center server to an autoAuto Scaling scaling group. Note that this entities UUID is different from that of the data center server, whose UUID is stored in the `datacenterServer` property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 
**metadata** | [**MetadataBasic**](MetadataBasic.md) |  | [optional] 
**properties** | [**ServerProperties**](ServerProperties.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print(Server.to_json())

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_from_dict = Server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


