# ionoscloud_vm_autoscaling.AutoScalingGroupsApi

All URIs are relative to *https://api.ionos.com/autoscaling*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_actions_find_by_id**](AutoScalingGroupsApi.md#groups_actions_find_by_id) | **GET** /groups/{groupId}/actions/{actionId} | Get Scaling Action Details by ID
[**groups_actions_get**](AutoScalingGroupsApi.md#groups_actions_get) | **GET** /groups/{groupId}/actions | Get Scaling Actions
[**groups_delete**](AutoScalingGroupsApi.md#groups_delete) | **DELETE** /groups/{groupId} | Delete a VM Auto Scaling Group by ID
[**groups_find_by_id**](AutoScalingGroupsApi.md#groups_find_by_id) | **GET** /groups/{groupId} | Get an Auto Scaling by ID
[**groups_get**](AutoScalingGroupsApi.md#groups_get) | **GET** /groups | Get VM Auto Scaling Groups
[**groups_post**](AutoScalingGroupsApi.md#groups_post) | **POST** /groups | Create a VM Auto Scaling Group
[**groups_put**](AutoScalingGroupsApi.md#groups_put) | **PUT** /groups/{groupId} | Update a VM Auto Scaling Group by ID
[**groups_servers_find_by_id**](AutoScalingGroupsApi.md#groups_servers_find_by_id) | **GET** /groups/{groupId}/servers/{serverId} | Get VM Auto Scaling Group Server by ID
[**groups_servers_get**](AutoScalingGroupsApi.md#groups_servers_get) | **GET** /groups/{groupId}/servers | Get VM Auto Scaling Group Servers


# **groups_actions_find_by_id**
> Action groups_actions_find_by_id(action_id, group_id, depth=depth)

Get Scaling Action Details by ID

Retrieves the details of a scaling action specified by its ID. This operation returns metadata, properties, and the current status, for the specified scaling action

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.action import Action
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    action_id = 'action_id_example' # str | 
    group_id = 'group_id_example' # str | 
    depth = 0 # float | With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.   (optional) (default to 0)

    try:
        # Get Scaling Action Details by ID
        api_response = api_instance.groups_actions_find_by_id(action_id, group_id, depth=depth)
        print("The response of AutoScalingGroupsApi->groups_actions_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_actions_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 
 **group_id** | **str**|  | 
 **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional] [default to 0]

### Return type

[**Action**](Action.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_actions_get**
> ActionCollection groups_actions_get(group_id, depth=depth, order_by=order_by)

Get Scaling Actions

Retrieves the list of the last Auto Scaling actions or jobs performed by the VM Auto Scaling.The actions are specified by its ID. Only the last 10 actions are available

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.action_collection import ActionCollection
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    depth = 0 # float | With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.   (optional) (default to 0)
    order_by = 'createdDate' # str | Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``. (optional) (default to 'createdDate')

    try:
        # Get Scaling Actions
        api_response = api_instance.groups_actions_get(group_id, depth=depth, order_by=order_by)
        print("The response of AutoScalingGroupsApi->groups_actions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_actions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional] [default to 0]
 **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;]

### Return type

[**ActionCollection**](ActionCollection.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_delete**
> groups_delete(group_id)

Delete a VM Auto Scaling Group by ID

Deletes the VM Auto Scaling Group specified by its ID.

>Deleting the associated servers and disks is currently not implemented.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Delete a VM Auto Scaling Group by ID
        api_instance.groups_delete(group_id)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content. The deletion was successful. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_find_by_id**
> Group groups_find_by_id(group_id, depth=depth)

Get an Auto Scaling by ID

Retrieves the VM Auto Scaling Group specified by its ID including the details.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.group import Group
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    depth = 0 # float | With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.   (optional) (default to 0)

    try:
        # Get an Auto Scaling by ID
        api_response = api_instance.groups_find_by_id(group_id, depth=depth)
        print("The response of AutoScalingGroupsApi->groups_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional] [default to 0]

### Return type

[**Group**](Group.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> GroupCollection groups_get(depth=depth, order_by=order_by)

Get VM Auto Scaling Groups

Lists all VM Auto Scaling Groups of your account.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.group_collection import GroupCollection
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    depth = 0 # float | With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.   (optional) (default to 0)
    order_by = 'createdDate' # str | Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``. (optional) (default to 'createdDate')

    try:
        # Get VM Auto Scaling Groups
        api_response = api_instance.groups_get(depth=depth, order_by=order_by)
        print("The response of AutoScalingGroupsApi->groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional] [default to 0]
 **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;]

### Return type

[**GroupCollection**](GroupCollection.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_post**
> GroupPostResponse groups_post(group_post)

Create a VM Auto Scaling Group

Creates a VM Auto Scaling Group. 

> Note that creating a group triggers the creation of two monitoring alarms for 'Scale-In' and 'Scale-Out' operations according to the 'Policy' settings.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.group_post import GroupPost
from ionoscloud_vm_autoscaling.models.group_post_response import GroupPostResponse
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    group_post = ionoscloud_vm_autoscaling.GroupPost() # GroupPost | 

    try:
        # Create a VM Auto Scaling Group
        api_response = api_instance.groups_post(group_post)
        print("The response of AutoScalingGroupsApi->groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_post** | [**GroupPost**](GroupPost.md)|  | 

### Return type

[**GroupPostResponse**](GroupPostResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_put**
> Group groups_put(group_id, group_put)

Update a VM Auto Scaling Group by ID

Updates the VM Auto Scaling Group specified by its ID. The IDs assigned by the system when the resource is created, such as 'properties.datacenter.id' and 'backupunitId', are immutable and cannot be updated.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.group import Group
from ionoscloud_vm_autoscaling.models.group_put import GroupPut
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    group_put = ionoscloud_vm_autoscaling.GroupPut() # GroupPut | 

    try:
        # Update a VM Auto Scaling Group by ID
        api_response = api_instance.groups_put(group_id, group_put)
        print("The response of AutoScalingGroupsApi->groups_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **group_put** | [**GroupPut**](GroupPut.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_servers_find_by_id**
> Server groups_servers_find_by_id(group_id, server_id, depth=depth)

Get VM Auto Scaling Group Server by ID

Retrieves the properties of the server specified by its ID.

>Note that the server IDs of the VM Auto Scaling Groups are different from and do not match the VM server IDs in the data center.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.server import Server
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    server_id = 'server_id_example' # str | 
    depth = 0 # float | With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.   (optional) (default to 0)

    try:
        # Get VM Auto Scaling Group Server by ID
        api_response = api_instance.groups_servers_find_by_id(group_id, server_id, depth=depth)
        print("The response of AutoScalingGroupsApi->groups_servers_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_servers_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **server_id** | **str**|  | 
 **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional] [default to 0]

### Return type

[**Server**](Server.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_servers_get**
> ServerCollection groups_servers_get(group_id, depth=depth, order_by=order_by)

Get VM Auto Scaling Group Servers

Retrieves all servers associated with the VM Auto Scaling Group specified by its ID. 

>Note that the server IDs of the VM Auto Scaling Groups are different from and do not match the VM server IDs in the data center.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_vm_autoscaling
from ionoscloud_vm_autoscaling.models.server_collection import ServerCollection
from ionoscloud_vm_autoscaling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/autoscaling
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_vm_autoscaling.Configuration(
    host = "https://api.ionos.com/autoscaling"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_vm_autoscaling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_vm_autoscaling.AutoScalingGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    depth = 0 # float | With this parameter, you control the level of detail of the response objects:    - ``0``: Only direct properties are included; children (such as executions or transitions) are not considered.    - ``1``: Direct properties and children references are included.    - ``2``: Direct properties and children properties are included.    - ``3``: Direct properties and children properties and children's children are included.    - etc.   (optional) (default to 0)
    order_by = 'createdDate' # str | Use this parameter to specify by which the returned list should be sorted. Valid values are: ``createdDate`` and ``lastModifiedDate``. (optional) (default to 'createdDate')

    try:
        # Get VM Auto Scaling Group Servers
        api_response = api_instance.groups_servers_get(group_id, depth=depth, order_by=order_by)
        print("The response of AutoScalingGroupsApi->groups_servers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoScalingGroupsApi->groups_servers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **depth** | **float**| With this parameter, you control the level of detail of the response objects:    - &#x60;&#x60;0&#x60;&#x60;: Only direct properties are included; children (such as executions or transitions) are not considered.    - &#x60;&#x60;1&#x60;&#x60;: Direct properties and children references are included.    - &#x60;&#x60;2&#x60;&#x60;: Direct properties and children properties are included.    - &#x60;&#x60;3&#x60;&#x60;: Direct properties and children properties and children&#39;s children are included.    - etc.   | [optional] [default to 0]
 **order_by** | **str**| Use this parameter to specify by which the returned list should be sorted. Valid values are: &#x60;&#x60;createdDate&#x60;&#x60; and &#x60;&#x60;lastModifiedDate&#x60;&#x60;. | [optional] [default to &#39;createdDate&#39;]

### Return type

[**ServerCollection**](ServerCollection.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

