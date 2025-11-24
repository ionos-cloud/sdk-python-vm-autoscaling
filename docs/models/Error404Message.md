# Error404Message


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.error404_message import Error404Message

# TODO update the JSON string below
json = "{}"
# create an instance of Error404Message from a JSON string
error404_message_instance = Error404Message.from_json(json)
# print the JSON string representation of the object
print(Error404Message.to_json())

# convert the object into a dict
error404_message_dict = error404_message_instance.to_dict()
# create an instance of Error404Message from a dict
error404_message_from_dict = Error404Message.from_dict(error404_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


