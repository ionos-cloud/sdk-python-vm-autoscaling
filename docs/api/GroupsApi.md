# GroupsApi

All URIs are relative to *https://api.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**autoscaling_groups_actions_find_by_id**](GroupsApi.md#autoscaling_groups_actions_find_by_id) | **GET** /cloudapi/autoscaling/groups/{groupId}/actions/{actionId} | Retrieve action details |
| [**autoscaling_groups_actions_get**](GroupsApi.md#autoscaling_groups_actions_get) | **GET** /cloudapi/autoscaling/groups/{groupId}/actions | Retrieve last ten actions |
| [**autoscaling_groups_delete**](GroupsApi.md#autoscaling_groups_delete) | **DELETE** /cloudapi/autoscaling/groups/{groupId} | Delete autoscaling groups. |
| [**autoscaling_groups_find_by_id**](GroupsApi.md#autoscaling_groups_find_by_id) | **GET** /cloudapi/autoscaling/groups/{groupId} | Retrieve autoscaling groups by UUID |
| [**autoscaling_groups_get**](GroupsApi.md#autoscaling_groups_get) | **GET** /cloudapi/autoscaling/groups | List autoscaling groups |
| [**autoscaling_groups_post**](GroupsApi.md#autoscaling_groups_post) | **POST** /cloudapi/autoscaling/groups | Create autoscaling groups |
| [**autoscaling_groups_put**](GroupsApi.md#autoscaling_groups_put) | **PUT** /cloudapi/autoscaling/groups/{groupId} | Update autoscaling groups |
| [**autoscaling_groups_servers_find_by_id**](GroupsApi.md#autoscaling_groups_servers_find_by_id) | **GET** /cloudapi/autoscaling/groups/{groupId}/servers/{serverId} | Retrieve group servers by UUID |
| [**autoscaling_groups_servers_get**](GroupsApi.md#autoscaling_groups_servers_get) | **GET** /cloudapi/autoscaling/groups/{groupId}/servers | Retrieve autoscaling group servers |


# **autoscaling_groups_actions_find_by_id**
> Action autoscaling_groups_actions_find_by_id(action_id, group_id, depth=depth)

Retrieve action details

Retrieve the details, such as metadata, properties, and the current status, for the specified action.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
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
        # Retrieve action details
        api_response = api_instance.autoscaling_groups_actions_find_by_id(action_id, group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_actions_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **action_id** | [**str**](.md)|  |  |
| **group_id** | **str**|  |  |
| **depth** | **float**| Controls the detail depth of the response objects.    - depth&#x3D;0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth&#x3D;1: Direct properties and children references are included.    - depth&#x3D;2: Direct properties and children properties are included.    - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.    - depth&#x3D;... and so on   | [optional]  |

### Return type

[**Action**](../models/Action.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **autoscaling_groups_actions_get**
> ActionCollection autoscaling_groups_actions_get(group_id, depth=depth, order_by=order_by)

Retrieve last ten actions

Retrieve the scaling actions for the specified autoscaling group; presently, only the last ten actions are returned.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Retrieve last ten actions
        api_response = api_instance.autoscaling_groups_actions_get(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_actions_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| Controls the detail depth of the response objects.    - depth&#x3D;0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth&#x3D;1: Direct properties and children references are included.    - depth&#x3D;2: Direct properties and children properties are included.    - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.    - depth&#x3D;... and so on   | [optional]  |
| **order_by** | **str**| Define the property to be used for ordering the returned list; valid values are &#39;createdDate&#39; and &#39;lastModifiedDate&#39;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**ActionCollection**](../models/ActionCollection.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **autoscaling_groups_delete**
> autoscaling_groups_delete(group_id)

Delete autoscaling groups.

Delete the specified autoscaling group; deletion of the associated servers and volumes is presently not implemented.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Delete autoscaling groups.
        api_instance.autoscaling_groups_delete(group_id)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | [**str**](.md)|  |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **autoscaling_groups_find_by_id**
> Group autoscaling_groups_find_by_id(group_id, depth=depth)

Retrieve autoscaling groups by UUID

Retrieve the details for the autoscaling group with the specified UUID.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Retrieve autoscaling groups by UUID
        api_response = api_instance.autoscaling_groups_find_by_id(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| Controls the detail depth of the response objects.    - depth&#x3D;0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth&#x3D;1: Direct properties and children references are included.    - depth&#x3D;2: Direct properties and children properties are included.    - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.    - depth&#x3D;... and so on   | [optional]  |

### Return type

[**Group**](../models/Group.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **autoscaling_groups_get**
> GroupCollection autoscaling_groups_get(depth=depth, order_by=order_by)

List autoscaling groups

List all autoscaling groups for your account.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    try:
        # List autoscaling groups
        api_response = api_instance.autoscaling_groups_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **depth** | **float**| Controls the detail depth of the response objects.    - depth&#x3D;0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth&#x3D;1: Direct properties and children references are included.    - depth&#x3D;2: Direct properties and children properties are included.    - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.    - depth&#x3D;... and so on   | [optional]  |
| **order_by** | **str**| Define the property to be used for ordering the returned list; valid values are &#39;createdDate&#39; and &#39;lastModifiedDate&#39;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**GroupCollection**](../models/GroupCollection.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **autoscaling_groups_post**
> GroupPostResponse autoscaling_groups_post(group)

Create autoscaling groups

Create autoscaling groups with this POST method. Creation of a group will trigger the creation of two monitoring alarms, for ‘Scale In’ and ‘Scale Out’ operations, according to \"policy\" settings.   \"properties.name\" must not be null or blank.   \"properties.targetReplicaCount\" is optional attribute which must be >= minReplicaCount and <= maxReplicaCount if provided in the request body.   \"properties.minReplicaCount\" must be >= 0 and <= 200.   \"properties.maxReplicaCount\" must be >= 0 and <= 200.   \"properties.datacenter.id\" must be a valid data center ID.   \"properties.policy.metric\" must be one of: INSTANCE_CPU_UTILIZATION_AVERAGE, INSTANCE_NETWORK_IN_BYTES, INSTANCE_NETWORK_OUT_BYTES, INSTANCE_NETWORK_IN_PACKETS, INSTANCE_NETWORK_OUT_PACKETS.   \"properties.policy.unit\" must be one of:  PER_SECOND, PER_MINUTE, PER_HOUR, TOTAL.  TOTAL can be combined only with INSTANCE_CPU_UTILIZATION_AVERAGE.   \"properties.policy.range\" must be >= 2 minutes.   If \"properties.policy.unit\" is \"TOTAL\", then \"properties.policy.scaleOutThreshold - properties.policy.scaleInThreshold\" must be >= 40.    \"properties.policy.scaleInAction.amount\" (the same is true for \"properties.policy.scaleOutAction.amount\") must be:   in case of properties.policy.scaleInAction.amountType = ABSOLUTE: 1 <= properties.policy.scaleInAction.amount <= 10  in case of properties.policy.scaleInAction.amountType = PERCENTAGE: 1 <= properties.policy.scaleInAction.amount <= 200   \"properties.policy.scaleInAction.cooldownPeriod\" (the same is true for \"properties.policy.scaleOutAction.cooldownPeriod\") must be: >= 2 minutes and <= 24 hours with a default value of 5 minutes if not provided in the request payload or given with null, empty string or spaces.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group = ionoscloud_vm_autoscaling.Group() # Group | 
    try:
        # Create autoscaling groups
        api_response = api_instance.autoscaling_groups_post(group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group** | [**Group**](Group.md)|  |  |

### Return type

[**GroupPostResponse**](../models/GroupPostResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **autoscaling_groups_put**
> Group autoscaling_groups_put(group_id, group_update)

Update autoscaling groups

Update the specified autoscaling group. \"properties.datacenter.id\" is immutable after creation and cannot be updated.  The other validations are the same as when creating a group.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    group_update = ionoscloud_vm_autoscaling.GroupUpdate() # GroupUpdate | 
    try:
        # Update autoscaling groups
        api_response = api_instance.autoscaling_groups_put(group_id, group_update)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | [**str**](.md)|  |  |
| **group_update** | [**GroupUpdate**](GroupUpdate.md)|  |  |

### Return type

[**Group**](../models/Group.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **autoscaling_groups_servers_find_by_id**
> Server autoscaling_groups_servers_find_by_id(group_id, server_id, depth=depth)

Retrieve group servers by UUID

Retrieve the properties of the specificed server in autoscaling group.  Please note that the autoscaling group server IDs are distinct from, and do not match the VM server IDs in the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
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
        # Retrieve group servers by UUID
        api_response = api_instance.autoscaling_groups_servers_find_by_id(group_id, server_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_servers_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **server_id** | [**str**](.md)|  |  |
| **depth** | **float**| Controls the detail depth of the response objects.    - depth&#x3D;0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth&#x3D;1: Direct properties and children references are included.    - depth&#x3D;2: Direct properties and children properties are included.    - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.    - depth&#x3D;... and so on   | [optional]  |

### Return type

[**Server**](../models/Server.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **autoscaling_groups_servers_get**
> ServerCollection autoscaling_groups_servers_get(group_id, depth=depth, order_by=order_by)

Retrieve autoscaling group servers

Retrieve all servers, associated with the specified autoscaling group.  Please note that the autoscaling group server IDs are distinct from, and do not match the VM server IDs in the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.GroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    try:
        # Retrieve autoscaling group servers
        api_response = api_instance.autoscaling_groups_servers_get(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling GroupsApi.autoscaling_groups_servers_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**|  |  |
| **depth** | **float**| Controls the detail depth of the response objects.    - depth&#x3D;0: Only direct properties are included; children (such as executions or transitions) are not included.    - depth&#x3D;1: Direct properties and children references are included.    - depth&#x3D;2: Direct properties and children properties are included.    - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.    - depth&#x3D;... and so on   | [optional]  |
| **order_by** | **str**| Define the property to be used for ordering the returned list; valid values are &#39;createdDate&#39; and &#39;lastModifiedDate&#39;. | [optional] [default to &#39;createdDate&#39;] |

### Return type

[**ServerCollection**](../models/ServerCollection.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

