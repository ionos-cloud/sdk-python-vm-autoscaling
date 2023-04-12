# GroupsApi

All URIs are relative to *https://api.ionos.com/cloudapi/autoscaling*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**groups_actions_find_by_id**](GroupsApi.md#groups_actions_find_by_id) | **GET** /groups/{groupId}/actions/{actionId} | Get Scaling Action Details by ID |
| [**groups_actions_get**](GroupsApi.md#groups_actions_get) | **GET** /groups/{groupId}/actions | Get Scaling Actions |
| [**groups_delete**](GroupsApi.md#groups_delete) | **DELETE** /groups/{groupId} | Delete an Auto Scaling Group by ID |
| [**groups_find_by_id**](GroupsApi.md#groups_find_by_id) | **GET** /groups/{groupId} | Get an Auto Scaling by ID |
| [**groups_get**](GroupsApi.md#groups_get) | **GET** /groups | Get Auto Scaling Groups |
| [**groups_post**](GroupsApi.md#groups_post) | **POST** /groups | Create an Auto Scaling Group |
| [**groups_put**](GroupsApi.md#groups_put) | **PUT** /groups/{groupId} | Update an Auto Scaling Group by ID |
| [**groups_servers_find_by_id**](GroupsApi.md#groups_servers_find_by_id) | **GET** /groups/{groupId}/servers/{serverId} | Get Auto Scaling Group Server by ID |
| [**groups_servers_get**](GroupsApi.md#groups_servers_get) | **GET** /groups/{groupId}/servers | Get Auto Scaling Group Servers |


# **groups_actions_find_by_id**
> Action groups_actions_find_by_id(action_id, group_id, depth=depth)

Get Scaling Action Details by ID

Retrieves the details of a scaling action specified by its ID. This operation returns metadata, properties, and the current status, for the specified scaling action

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    action_id = 'action_id_example' # str | 
    group_id = 'group_id_example' # str | 
    try:
        # Get Scaling Action Details by ID
        api_response = api_instance.groups_actions_find_by_id(action_id, group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_actions_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **action_id** | [**str**](../models/.md)|  |  |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |

### Return type

[**Action**](../models/Action.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_actions_get**
> ActionCollection groups_actions_get(group_id, depth=depth, order_by=order_by)

Get Scaling Actions

Retrieves the list of the scaling actions for the Auto Scaling group specified by its ID.    >Note that currently, only the last ten actions are returned.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Get Scaling Actions
        api_response = api_instance.groups_actions_get(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_actions_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |
| **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**ActionCollection**](../models/ActionCollection.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_delete**
> groups_delete(group_id)

Delete an Auto Scaling Group by ID

Deletes the Auto Scaling group specified by its ID.  >Deleting the associated servers and disks is currently not implemented.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Delete an Auto Scaling Group by ID
        api_instance.groups_delete(group_id)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | [**str**](../models/.md)|  |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_find_by_id**
> Group groups_find_by_id(group_id, depth=depth)

Get an Auto Scaling by ID

Retrieves the Auto Scaling group specified by its ID including the details.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Get an Auto Scaling by ID
        api_response = api_instance.groups_find_by_id(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |

### Return type

[**Group**](../models/Group.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_get**
> GroupCollection groups_get(depth=depth, order_by=order_by)

Get Auto Scaling Groups

Lists all Auto Scaling groups of your account.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    try:
        # Get Auto Scaling Groups
        api_response = api_instance.groups_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |
| **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**GroupCollection**](../models/GroupCollection.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_post**
> GroupPostResponse groups_post(group_post)

Create an Auto Scaling Group

Creates an Auto Scaling group.   > Note that creating a group triggers the creation of two monitoring alarms for 'Scale-In' and 'Scale-Out' operations according to the 'Policy' settings.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_post = ionoscloud_vm_autoscaling.GroupPost() # GroupPost | 
    try:
        # Create an Auto Scaling Group
        api_response = api_instance.groups_post(group_post)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_post** | [**GroupPost**](../models/GroupPost.md)|  |  |

### Return type

[**GroupPostResponse**](../models/GroupPostResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **groups_put**
> Group groups_put(group_id, group_put)

Update an Auto Scaling Group by ID

Updates the Auto Scaling group specified by its ID. The IDs assigned by the system when the resource is created, such as 'properties.datacenter.id' and 'backupunitId', are immutable and cannot be updated.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    group_put = ionoscloud_vm_autoscaling.GroupPut() # GroupPut | 
    try:
        # Update an Auto Scaling Group by ID
        api_response = api_instance.groups_put(group_id, group_put)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | [**str**](../models/.md)|  |  |
| **group_put** | [**GroupPut**](../models/GroupPut.md)|  |  |

### Return type

[**Group**](../models/Group.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **groups_servers_find_by_id**
> Server groups_servers_find_by_id(group_id, server_id, depth=depth)

Get Auto Scaling Group Server by ID

Retrieves the properties of the server specified by its ID.  >Note that the server IDs of the Auto Scaling groups are different from and do not match the VM server IDs in the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    server_id = 'server_id_example' # str | 
    try:
        # Get Auto Scaling Group Server by ID
        api_response = api_instance.groups_servers_find_by_id(group_id, server_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_servers_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **server_id** | [**str**](../models/.md)|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |

### Return type

[**Server**](../models/Server.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **groups_servers_get**
> ServerCollection groups_servers_get(group_id, depth=depth, order_by=order_by)

Get Auto Scaling Group Servers

Retrieves all servers associated with the Auto Scaling group specified by its ID.   >Note that the server IDs of the Auto Scaling groups are different from and do not match the VM server IDs in the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/autoscaling
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com/cloudapi/autoscaling',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Get Auto Scaling Group Servers
        api_response = api_instance.groups_servers_get(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.groups_servers_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional]  |
| **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**ServerCollection**](../models/ServerCollection.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

