# ReplicaNic

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **lan** | **int** | The LAN ID of this replica NIC. |  |
| **name** | **str** | The replica NIC name. |  |
| **dhcp** | **bool** | DHCP for this replica NIC. This is an optional attribute with the default value &#39;TRUE&#39; if not specified in the request payload or as null. | [optional]  |
| **firewall_active** | **bool** | Activate or deactivate the firewall. By default, an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, IP addresses and ports. | [optional]  |
| **firewall_type** | **str** | The type of firewall rules that will be allowed on the NIC. If not specified, the default INGRESS value is used. | [optional]  |
| **flow_logs** | [**list[NicFlowLog]**](NicFlowLog.md) | List of all flow logs for the specified NIC. | [optional]  |
| **firewall_rules** | [**list[NicFirewallRule]**](NicFirewallRule.md) | List of all firewall rules for the specified NIC. | [optional]  |
| **target_group** | [**TargetGroup**](TargetGroup.md) |  | [optional]  |


