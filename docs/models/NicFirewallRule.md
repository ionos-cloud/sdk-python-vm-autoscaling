# NicFirewallRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the firewall rule. | [optional] 
**protocol** | **str** | The protocol for the rule. The property cannot be modified after its creation (not allowed in update requests). | 
**source_mac** | **str** | Only traffic originating from the respective MAC address is permitted. Valid format: &#39;aa:bb:cc:dd:ee:ff&#39;. The value &#39;null&#39; allows traffic from any MAC address. | [optional] 
**source_ip** | **str** | Only traffic originating from the respective IPv4 address is permitted. The value &#39;null&#39; allows traffic from any IP address. | [optional] 
**target_ip** | **str** | If the target NIC has multiple IP addresses, only the traffic directed to the respective IP address of the NIC is allowed. The value &#39;null&#39; allows traffic to any target IP address. | [optional] 
**icmp_code** | **int** | Sets the allowed code (from 0 to 254) when ICMP protocol is selected. The value &#39;null&#39;&#39; allows all codes. | [optional] 
**icmp_type** | **int** | Sets the allowed type (from 0 to 254) if the protocol ICMP is selected. The value &#39;null&#39; allows all types. | [optional] 
**port_range_start** | **int** | Sets the initial range of the allowed port (from 1 to 65535) if the protocol TCP or UDP is selected. The value &#39;null&#39; for &#39;portRangeStart&#39; and &#39;portRangeEnd&#39; allows all ports. | [optional] 
**port_range_end** | **int** | Sets the end range of the allowed port (from 1 to 65535) if the protocol TCP or UDP is selected. The value &#39;null&#39; for &#39;portRangeStart&#39; and &#39;portRangeEnd&#39; allows all ports. | [optional] 
**type** | **str** | The firewall rule type. If not specified, the default value &#39;INGRESS&#39; is used. | [optional] 

## Example

```python
from ionoscloud_vm_autoscaling.models.nic_firewall_rule import NicFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of NicFirewallRule from a JSON string
nic_firewall_rule_instance = NicFirewallRule.from_json(json)
# print the JSON string representation of the object
print(NicFirewallRule.to_json())

# convert the object into a dict
nic_firewall_rule_dict = nic_firewall_rule_instance.to_dict()
# create an instance of NicFirewallRule from a dict
nic_firewall_rule_from_dict = NicFirewallRule.from_dict(nic_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


