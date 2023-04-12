# ReplicaVolumePost

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **image** | **str** | The image installed on the disk. Currently, only the UUID of the image is supported.  &gt;Note that either &#39;image&#39; or &#39;imageAlias&#39; must be specified, but not both. | [optional]  |
| **image_alias** | **str** | The image installed on the volume. Must be an &#39;imageAlias&#39; as specified via the images API. Note that one of &#39;image&#39; or &#39;imageAlias&#39; must be set, but not both. | [optional]  |
| **name** | **str** | The replica volume name. |  |
| **size** | **int** | The size of this replica volume in GB. |  |
| **ssh_keys** | **list[str]** | The SSH keys of this volume. | [optional]  |
| **type** | [**VolumeHwType**](VolumeHwType.md) |  |  |
| **user_data** | **str** | The user data (Cloud Init) for this replica volume. | [optional]  |
| **bus** | [**BusType**](BusType.md) |  | [optional]  |
| **backupunit_id** | **str** | The ID of the backup unit that the user has access to. The property is immutable and is only allowed to be set on creation of a new a volume. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; in conjunction with this property. | [optional]  |
| **boot_order** | **str** | Determines whether the volume will be used as a boot volume. Set to NONE, the volume will not be used as boot volume. Set to PRIMARY, the volume will be used as boot volume and set to AUTO will delegate the decision to the provisioning engine to decide whether to use the voluem as boot volume. Notice that exactly one volume can be set to PRIMARY or all of them set to AUTO. |  |
| **image_password** | **str** | The image password for this replica volume. | [optional]  |


