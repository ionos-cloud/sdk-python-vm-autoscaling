# ErrorAuthorize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** |  | [optional] 
**messages** | [**list[ErrorAuthorizeMessage]**](ErrorAuthorizeMessage.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.error_authorize import ErrorAuthorize

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorAuthorize from a JSON string
error_authorize_instance = ErrorAuthorize.from_json(json)
# print the JSON string representation of the object
print(ErrorAuthorize.to_json())

# convert the object into a dict
error_authorize_dict = error_authorize_instance.to_dict()
# create an instance of ErrorAuthorize from a dict
error_authorize_from_dict = ErrorAuthorize.from_dict(error_authorize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


