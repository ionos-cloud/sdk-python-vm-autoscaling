# ReplicaVolumePost

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **image** | **str** | The image installed on the volume. Only the UUID of the image is presently supported. |  |
| **name** | **str** | Name of the replica volume. |  |
| **size** | **int** | User-defined size for this replica volume in GB. |  |
| **ssh_keys** | **list[str]** | Ssh keys that has access to the volume. | [optional]  |
| **type** | [**VolumeHwType**](VolumeHwType.md) |  |  |
| **user_data** | **str** | user-data (Cloud Init) for this replica volume. | [optional]  |
| **bus** | [**BusType**](BusType.md) |  | [optional]  |
| **image_password** | **str** | Image password for this replica volume. | [optional]  |


