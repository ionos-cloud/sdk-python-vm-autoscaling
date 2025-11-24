# GroupPutPropertiesDatacenter

The VMs for this VM Auto Scaling Group are created in this virtual data center.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_put_properties_datacenter import GroupPutPropertiesDatacenter

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPutPropertiesDatacenter from a JSON string
group_put_properties_datacenter_instance = GroupPutPropertiesDatacenter.from_json(json)
# print the JSON string representation of the object
print(GroupPutPropertiesDatacenter.to_json())

# convert the object into a dict
group_put_properties_datacenter_dict = group_put_properties_datacenter_instance.to_dict()
# create an instance of GroupPutPropertiesDatacenter from a dict
group_put_properties_datacenter_from_dict = GroupPutPropertiesDatacenter.from_dict(group_put_properties_datacenter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


