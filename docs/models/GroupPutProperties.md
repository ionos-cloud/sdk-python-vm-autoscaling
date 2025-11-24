# GroupPutProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**GroupPutPropertiesDatacenter**](GroupPutPropertiesDatacenter.md) |  | 
**location** | **str** | The data center location. | [readonly] 
**max_replica_count** | **int** | The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;&#x3D; 0 and &lt;&#x3D; 200. Will be enforced for both automatic and manual changes. | 
**min_replica_count** | **int** | The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;&#x3D; 0 and &lt;&#x3D; 200. Will be enforced for both automatic and manual changes | 
**name** | **str** | The name of the VM Auto Scaling Group. This field must not be null or blank. | 
**policy** | [**GroupPolicy**](GroupPolicy.md) |  | 
**replica_configuration** | [**ReplicaPropertiesPost**](ReplicaPropertiesPost.md) |  | 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_put_properties import GroupPutProperties

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPutProperties from a JSON string
group_put_properties_instance = GroupPutProperties.from_json(json)
# print the JSON string representation of the object
print(GroupPutProperties.to_json())

# convert the object into a dict
group_put_properties_dict = group_put_properties_instance.to_dict()
# create an instance of GroupPutProperties from a dict
group_put_properties_from_dict = GroupPutProperties.from_dict(group_put_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


