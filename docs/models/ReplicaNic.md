# ReplicaNic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lan** | **int** | The LAN ID of this replica NIC. | 
**name** | **str** | The replica NIC name. | 
**dhcp** | **bool** | DHCP for this replica NIC. This is an optional attribute with the default value &#39;TRUE&#39; if not specified in the request payload or as null. | [optional] 
**firewall_active** | **bool** | Activate or deactivate the firewall. By default, an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, IP addresses and ports. | [optional] 
**firewall_type** | **str** | The type of firewall rules that will be allowed on the NIC. If not specified, the default INGRESS value is used. | [optional] 
**flow_logs** | [**list[NicFlowLog]**](NicFlowLog.md) | List of all flow logs for the specified NIC. | [optional] 
**firewall_rules** | [**list[NicFirewallRule]**](NicFirewallRule.md) | List of all firewall rules for the specified NIC. | [optional] 
**target_group** | [**TargetGroup**](TargetGroup.md) |  | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.replica_nic import ReplicaNic

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaNic from a JSON string
replica_nic_instance = ReplicaNic.from_json(json)
# print the JSON string representation of the object
print(ReplicaNic.to_json())

# convert the object into a dict
replica_nic_dict = replica_nic_instance.to_dict()
# create an instance of ReplicaNic from a dict
replica_nic_from_dict = ReplicaNic.from_dict(replica_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


