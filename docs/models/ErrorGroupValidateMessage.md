# ErrorGroupValidateMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.error_group_validate_message import ErrorGroupValidateMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorGroupValidateMessage from a JSON string
error_group_validate_message_instance = ErrorGroupValidateMessage.from_json(json)
# print the JSON string representation of the object
print(ErrorGroupValidateMessage.to_json())

# convert the object into a dict
error_group_validate_message_dict = error_group_validate_message_instance.to_dict()
# create an instance of ErrorGroupValidateMessage from a dict
error_group_validate_message_from_dict = ErrorGroupValidateMessage.from_dict(error_group_validate_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


