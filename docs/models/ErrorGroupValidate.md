# ErrorGroupValidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** |  | [optional] 
**messages** | [**list[ErrorGroupValidateMessage]**](ErrorGroupValidateMessage.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.error_group_validate import ErrorGroupValidate

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorGroupValidate from a JSON string
error_group_validate_instance = ErrorGroupValidate.from_json(json)
# print the JSON string representation of the object
print(ErrorGroupValidate.to_json())

# convert the object into a dict
error_group_validate_dict = error_group_validate_instance.to_dict()
# create an instance of ErrorGroupValidate from a dict
error_group_validate_from_dict = ErrorGroupValidate.from_dict(error_group_validate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


