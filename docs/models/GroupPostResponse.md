# GroupPostResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **str** | The resource&#39;s unique identifier | [readonly]  |
| **type** | **str** | The type of object that has been created | [optional] [readonly]  |
| **href** | **str** | URL to the object representation (absolute path) | [optional] [readonly]  |
| **metadata** | [**Metadata**](Metadata.md) |  | [optional]  |
| **properties** | [**GroupProperties**](GroupProperties.md) |  |  |
| **entities** | [**GroupEntities**](GroupEntities.md) |  | [optional]  |
| **started_actions** | [**list[ActionResource]**](ActionResource.md) | Any background activity caused by this request. This allows the caller to track the progress of such activity. | [optional] [readonly]  |


