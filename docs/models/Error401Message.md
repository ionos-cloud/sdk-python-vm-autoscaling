# Error401Message


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.error401_message import Error401Message

# TODO update the JSON string below
json = "{}"
# create an instance of Error401Message from a JSON string
error401_message_instance = Error401Message.from_json(json)
# print the JSON string representation of the object
print(Error401Message.to_json())

# convert the object into a dict
error401_message_dict = error401_message_instance.to_dict()
# create an instance of Error401Message from a dict
error401_message_from_dict = Error401Message.from_dict(error401_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


