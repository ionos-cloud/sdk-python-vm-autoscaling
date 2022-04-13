# DocumentationApi

All URIs are relative to *https://api.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**autoscaling_openapi_json_get**](DocumentationApi.md#autoscaling_openapi_json_get) | **GET** /cloudapi/autoscaling/openapi.json | Retrieve VM autoscaling OpenAPI spec (JSON) |
| [**autoscaling_openapi_yaml_get**](DocumentationApi.md#autoscaling_openapi_yaml_get) | **GET** /cloudapi/autoscaling/openapi.yaml | Retrieve VM autoscaling OpenAPI spec (YAML) |


# **autoscaling_openapi_json_get**
> autoscaling_openapi_json_get()

Retrieve VM autoscaling OpenAPI spec (JSON)

Retrieve the OpenAPI specification in JSON format.

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
    api_instance = ionoscloud_vm_autoscaling.DocumentationApi(api_client)
    try:
        # Retrieve VM autoscaling OpenAPI spec (JSON)
        api_instance.autoscaling_openapi_json_get()
    except ApiException as e:
        print('Exception when calling DocumentationApi.autoscaling_openapi_json_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

# **autoscaling_openapi_yaml_get**
> autoscaling_openapi_yaml_get()

Retrieve VM autoscaling OpenAPI spec (YAML)

Retrieve the OpenAPI specification in YAML format (auto-generated from the JSON).

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
    api_instance = ionoscloud_vm_autoscaling.DocumentationApi(api_client)
    try:
        # Retrieve VM autoscaling OpenAPI spec (YAML)
        api_instance.autoscaling_openapi_yaml_get()
    except ApiException as e:
        print('Exception when calling DocumentationApi.autoscaling_openapi_yaml_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

