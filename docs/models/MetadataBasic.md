# MetadataBasic

The resource metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | The date the resource was created. | 
**etag** | **str** | The resource etag. | 
**last_modified_date** | **datetime** | The date the resource was last modified. | 
**state** | **str** | The resource state. | 

## Example

```python
from ionoscloud_vm_autoscaling.models.metadata_basic import MetadataBasic

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataBasic from a JSON string
metadata_basic_instance = MetadataBasic.from_json(json)
# print the JSON string representation of the object
print(MetadataBasic.to_json())

# convert the object into a dict
metadata_basic_dict = metadata_basic_instance.to_dict()
# create an instance of MetadataBasic from a dict
metadata_basic_from_dict = MetadataBasic.from_dict(metadata_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


