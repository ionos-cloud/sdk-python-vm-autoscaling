# GroupPropertiesDatacenter

The VMs for this VM Auto Scaling Description are created in this virtual data center.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier. | 
**type** | **str** | The resource type. | [optional] [readonly] 
**href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_properties_datacenter import GroupPropertiesDatacenter

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPropertiesDatacenter from a JSON string
group_properties_datacenter_instance = GroupPropertiesDatacenter.from_json(json)
# print the JSON string representation of the object
print(GroupPropertiesDatacenter.to_json())

# convert the object into a dict
group_properties_datacenter_dict = group_properties_datacenter_instance.to_dict()
# create an instance of GroupPropertiesDatacenter from a dict
group_properties_datacenter_from_dict = GroupPropertiesDatacenter.from_dict(group_properties_datacenter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


