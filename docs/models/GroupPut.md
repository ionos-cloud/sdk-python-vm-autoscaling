# GroupPut

The update request for a VM Auto Scaling Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**GroupPutProperties**](GroupPutProperties.md) |  | 

## Example

```python
from ionoscloud_vm_autoscaling.models.group_put import GroupPut

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPut from a JSON string
group_put_instance = GroupPut.from_json(json)
# print the JSON string representation of the object
print(GroupPut.to_json())

# convert the object into a dict
group_put_dict = group_put_instance.to_dict()
# create an instance of GroupPut from a dict
group_put_from_dict = GroupPut.from_dict(group_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


