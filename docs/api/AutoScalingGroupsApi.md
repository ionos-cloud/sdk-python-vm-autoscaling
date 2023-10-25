# AutoScalingGroupsApi

All URIs are relative to *https://api.ionos.com/autoscaling*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**groups_actions_find_by_id**](AutoScalingGroupsApi.md#groups_actions_find_by_id) | **GET** /groups/{groupId}/actions/{actionId} | Get Scaling Action Details by ID |
| [**groups_actions_get**](AutoScalingGroupsApi.md#groups_actions_get) | **GET** /groups/{groupId}/actions | Get Scaling Actions |
| [**groups_delete**](AutoScalingGroupsApi.md#groups_delete) | **DELETE** /groups/{groupId} | Delete a VM Auto Scaling Group by ID |
| [**groups_find_by_id**](AutoScalingGroupsApi.md#groups_find_by_id) | **GET** /groups/{groupId} | Get an Auto Scaling by ID |
| [**groups_get**](AutoScalingGroupsApi.md#groups_get) | **GET** /groups | Get VM Auto Scaling Groups |
| [**groups_post**](AutoScalingGroupsApi.md#groups_post) | **POST** /groups | Create a VM Auto Scaling Group |
| [**groups_put**](AutoScalingGroupsApi.md#groups_put) | **PUT** /groups/{groupId} | Update a VM Auto Scaling Group by ID |
| [**groups_servers_find_by_id**](AutoScalingGroupsApi.md#groups_servers_find_by_id) | **GET** /groups/{groupId}/servers/{serverId} | Get VM Auto Scaling Group Server by ID |
| [**groups_servers_get**](AutoScalingGroupsApi.md#groups_servers_get) | **GET** /groups/{groupId}/servers | Get VM Auto Scaling Group Servers |


# **groups_actions_find_by_id**
> Action groups_actions_find_by_id(action_id, group_id, depth=depth)

Get Scaling Action Details by ID

Retrieves the details of a scaling action specified by its ID. This operation returns metadata, properties, and the current status, for the specified scaling action

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **action_id** | **str**|  |  |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |

### Return type

[**Action**](../models/Action.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_actions_get**
> ActionCollection groups_actions_get(group_id, depth=depth, order_by=order_by)

Get Scaling Actions

Retrieves the list of the last Auto Scaling actions or jobs performed by the VM Auto Scaling.The actions are specified by its ID. Only the last 10 actions are available

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |
| **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**ActionCollection**](../models/ActionCollection.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_delete**
> groups_delete(group_id)

Delete a VM Auto Scaling Group by ID

Deletes the VM Auto Scaling Group specified by its ID.  >Deleting the associated servers and disks is currently not implemented.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |

### Return type

void (empty response body)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_find_by_id**
> Group groups_find_by_id(group_id, depth=depth)

Get an Auto Scaling by ID

Retrieves the VM Auto Scaling Group specified by its ID including the details.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |

### Return type

[**Group**](../models/Group.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_get**
> GroupCollection groups_get(depth=depth, order_by=order_by)

Get VM Auto Scaling Groups

Lists all VM Auto Scaling Groups of your account.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |
| **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**GroupCollection**](../models/GroupCollection.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_post**
> GroupPostResponse groups_post(group_post)

Create a VM Auto Scaling Group

Creates a VM Auto Scaling Group.   > Note that creating a group triggers the creation of two monitoring alarms for 'Scale-In' and 'Scale-Out' operations according to the 'Policy' settings.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_post** | [**GroupPost**](../models/GroupPost.md)|  |  |

### Return type

[**GroupPostResponse**](../models/GroupPostResponse.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **groups_put**
> Group groups_put(group_id, group_put)

Update a VM Auto Scaling Group by ID

Updates the VM Auto Scaling Group specified by its ID. The IDs assigned by the system when the resource is created, such as 'properties.datacenter.id' and 'backupunitId', are immutable and cannot be updated.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **group_put** | [**GroupPut**](../models/GroupPut.md)|  |  |

### Return type

[**Group**](../models/Group.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **groups_servers_find_by_id**
> Server groups_servers_find_by_id(group_id, server_id, depth=depth)

Get VM Auto Scaling Group Server by ID

Retrieves the properties of the server specified by its ID.  >Note that the server IDs of the VM Auto Scaling Groups are different from and do not match the VM server IDs in the data center.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **server_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |

### Return type

[**Server**](../models/Server.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_servers_get**
> ServerCollection groups_servers_get(group_id, depth=depth, order_by=order_by)

Get VM Auto Scaling Group Servers

Retrieves all servers associated with the VM Auto Scaling Group specified by its ID.   >Note that the server IDs of the VM Auto Scaling Groups are different from and do not match the VM server IDs in the data center.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |
| **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**ServerCollection**](../models/ServerCollection.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

