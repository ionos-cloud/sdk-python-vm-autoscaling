# ErrorMessageParse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.error_message_parse import ErrorMessageParse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessageParse from a JSON string
error_message_parse_instance = ErrorMessageParse.from_json(json)
# print the JSON string representation of the object
print(ErrorMessageParse.to_json())

# convert the object into a dict
error_message_parse_dict = error_message_parse_instance.to_dict()
# create an instance of ErrorMessageParse from a dict
error_message_parse_from_dict = ErrorMessageParse.from_dict(error_message_parse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


