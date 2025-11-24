# Metadata

The resource metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The user who created the resource. | 
**created_by_user_id** | **str** | The ID of the user who created the resource. | 
**created_date** | **datetime** | The date the resource was created. | 
**etag** | **str** | The resource etag. | 
**last_modified_by** | **str** | The last user who modified the resource. | 
**last_modified_by_user_id** | **str** | The ID of the last user who modified the resource. | 
**last_modified_date** | **datetime** | The date the resource was last modified. | 
**state** | [**MetadataState**](MetadataState.md) |  | 

## Example

```python
from ionoscloud_vm_autoscaling.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


