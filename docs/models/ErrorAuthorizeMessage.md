# ErrorAuthorizeMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.error_authorize_message import ErrorAuthorizeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorAuthorizeMessage from a JSON string
error_authorize_message_instance = ErrorAuthorizeMessage.from_json(json)
# print the JSON string representation of the object
print(ErrorAuthorizeMessage.to_json())

# convert the object into a dict
error_authorize_message_dict = error_authorize_message_instance.to_dict()
# create an instance of ErrorAuthorizeMessage from a dict
error_authorize_message_from_dict = ErrorAuthorizeMessage.from_dict(error_authorize_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


