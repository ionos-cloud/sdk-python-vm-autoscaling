# DatacenterServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.datacenter_server import DatacenterServer

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterServer from a JSON string
datacenter_server_instance = DatacenterServer.from_json(json)
# print the JSON string representation of the object
print(DatacenterServer.to_json())

# convert the object into a dict
datacenter_server_dict = datacenter_server_instance.to_dict()
# create an instance of DatacenterServer from a dict
datacenter_server_from_dict = DatacenterServer.from_dict(datacenter_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


