# GroupPostResponse

A group of virtual servers where the number of replicas can be scaled automatically.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **str** | The unique resource identifier. | [readonly]  |
| **type** | **str** | The resource type. | [optional] [readonly]  |
| **href** | **str** | The absolute URL to the resource&#39;s representation. | [optional] [readonly]  |
| **metadata** | [**Metadata**](Metadata.md) |  | [optional]  |
| **properties** | [**GroupProperties**](GroupProperties.md) |  |  |
| **entities** | [**GroupPostEntities**](GroupPostEntities.md) |  | [optional]  |
| **started_actions** | [**list[ActionResource]**](ActionResource.md) | Any background activity caused by this request. You can use this to track the progress of such activities. | [optional] [readonly]  |


