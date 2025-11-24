# ServersLinkResource

The servers linked to the VM Auto Scaling Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | [readonly] 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.servers_link_resource import ServersLinkResource

# TODO update the JSON string below
json = "{}"
# create an instance of ServersLinkResource from a JSON string
servers_link_resource_instance = ServersLinkResource.from_json(json)
# print the JSON string representation of the object
print(ServersLinkResource.to_json())

# convert the object into a dict
servers_link_resource_dict = servers_link_resource_instance.to_dict()
# create an instance of ServersLinkResource from a dict
servers_link_resource_from_dict = ServersLinkResource.from_dict(servers_link_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


