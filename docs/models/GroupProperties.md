# GroupProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**GroupPropertiesDatacenter**](GroupPropertiesDatacenter.md) |  | 
**location** | **str** | The data center location. | [readonly] 
**max_replica_count** | **int** | The maximum value for the number of replicas. Must be &gt;&#x3D; 0 and &lt;&#x3D; 100. Will be enforced for both automatic and manual changes. | [optional] 
**min_replica_count** | **int** | The minimum value for the number of replicas. Must be &gt;&#x3D; 0 and &lt;&#x3D; 100. Will be enforced for both automatic and manual changes | [optional] 
**name** | **str** | The name of the VM Auto Scaling Group. This field must not be null or blank. | [optional] 
**policy** | [**GroupPolicy**](GroupPolicy.md) |  | [optional] 
**replica_configuration** | [**ReplicaPropertiesPost**](ReplicaPropertiesPost.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_properties import GroupProperties

# TODO update the JSON string below
json = "{}"
# create an instance of GroupProperties from a JSON string
group_properties_instance = GroupProperties.from_json(json)
# print the JSON string representation of the object
print(GroupProperties.to_json())

# convert the object into a dict
group_properties_dict = group_properties_instance.to_dict()
# create an instance of GroupProperties from a dict
group_properties_from_dict = GroupProperties.from_dict(group_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


