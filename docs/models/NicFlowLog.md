# NicFlowLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The flow log name. | 
**action** | **str** | Specifies the traffic action pattern. | 
**direction** | **str** | Specifies the traffic direction pattern. | 
**bucket** | **str** | The S3 bucket name of an existing IONOS Cloud S3 bucket. | 

## Example

```python
from ionoscloud_vm_autoscaling.models.nic_flow_log import NicFlowLog

# TODO update the JSON string below
json = "{}"
# create an instance of NicFlowLog from a JSON string
nic_flow_log_instance = NicFlowLog.from_json(json)
# print the JSON string representation of the object
print(NicFlowLog.to_json())

# convert the object into a dict
nic_flow_log_dict = nic_flow_log_instance.to_dict()
# create an instance of NicFlowLog from a dict
nic_flow_log_from_dict = NicFlowLog.from_dict(nic_flow_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


