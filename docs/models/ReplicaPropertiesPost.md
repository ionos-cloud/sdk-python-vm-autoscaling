# ReplicaPropertiesPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | [optional] 
**cores** | **int** | The total number of cores for the VMs. | 
**cpu_family** | [**CpuFamily**](CpuFamily.md) |  | [optional] 
**nics** | [**list[ReplicaNic]**](ReplicaNic.md) | The list of NICs associated with this replica. | [optional] 
**ram** | **int** | The size of the memory for the VMs in MB. The size must be in multiples of 256 MB, with a minimum of 256 MB; if you set &#39;ramHotPlug&#x3D;TRUE&#39;, you must use at least 1024 MB. If you set the RAM size to more than 240 GB, &#39;ramHotPlug&#x3D;FALSE&#39; is fixed. | 
**volumes** | [**list[ReplicaVolumePost]**](ReplicaVolumePost.md) | List of volumes associated with this Replica. | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.replica_properties_post import ReplicaPropertiesPost

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaPropertiesPost from a JSON string
replica_properties_post_instance = ReplicaPropertiesPost.from_json(json)
# print the JSON string representation of the object
print(ReplicaPropertiesPost.to_json())

# convert the object into a dict
replica_properties_post_dict = replica_properties_post_instance.to_dict()
# create an instance of ReplicaPropertiesPost from a dict
replica_properties_post_from_dict = ReplicaPropertiesPost.from_dict(replica_properties_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


