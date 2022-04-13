# coding: utf-8

"""
    VM Auto Scaling service (CloudAPI)

    VM Auto Scaling service enables IONOS clients to horizontally scale the number of VM instances, based on configured rules. Use Auto Scaling to ensure you will have a sufficient number of instances to handle your application loads at all times.  Create an Auto Scaling group that contains the server instances; Auto Scaling service will ensure that the number of instances in the group is always within these limits.  When target replica count is specified, Auto Scaling will maintain the set number on instances.  When scaling policies are specified, Auto Scaling will create or delete instances based on the demands of your applications. For each policy, specified scale-in and scale-out actions are performed whenever the corresponding thresholds are met.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_vm_autoscaling.configuration import Configuration


class ReplicaVolumePost(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {

        'image': 'str',

        'name': 'str',

        'size': 'int',

        'ssh_keys': 'list[str]',

        'type': 'VolumeHwType',

        'user_data': 'str',

        'bus': 'BusType',

        'image_password': 'str',
    }

    attribute_map = {

        'image': 'image',

        'name': 'name',

        'size': 'size',

        'ssh_keys': 'sshKeys',

        'type': 'type',

        'user_data': 'userData',

        'bus': 'bus',

        'image_password': 'imagePassword',
    }

    def __init__(self, image=None, name=None, size=None, ssh_keys=None, type=None, user_data=None, bus=None, image_password=None, local_vars_configuration=None):  # noqa: E501
        """ReplicaVolumePost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._image = None
        self._name = None
        self._size = None
        self._ssh_keys = None
        self._type = None
        self._user_data = None
        self._bus = None
        self._image_password = None
        self.discriminator = None

        self.image = image
        self.name = name
        self.size = size
        if ssh_keys is not None:
            self.ssh_keys = ssh_keys
        self.type = type
        if user_data is not None:
            self.user_data = user_data
        if bus is not None:
            self.bus = bus
        if image_password is not None:
            self.image_password = image_password


    @property
    def image(self):
        """Gets the image of this ReplicaVolumePost.  # noqa: E501

        The image installed on the volume. Only the UUID of the image is presently supported.  # noqa: E501

        :return: The image of this ReplicaVolumePost.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ReplicaVolumePost.

        The image installed on the volume. Only the UUID of the image is presently supported.  # noqa: E501

        :param image: The image of this ReplicaVolumePost.  # noqa: E501
        :type image: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image is not None and not re.search(r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}', image)):  # noqa: E501
            raise ValueError(r"Invalid value for `image`, must be a follow pattern or equal to `/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/`")  # noqa: E501

        self._image = image

    @property
    def name(self):
        """Gets the name of this ReplicaVolumePost.  # noqa: E501

        Name of the replica volume.  # noqa: E501

        :return: The name of this ReplicaVolumePost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReplicaVolumePost.

        Name of the replica volume.  # noqa: E501

        :param name: The name of this ReplicaVolumePost.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this ReplicaVolumePost.  # noqa: E501

        User-defined size for this replica volume in GB.  # noqa: E501

        :return: The size of this ReplicaVolumePost.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ReplicaVolumePost.

        User-defined size for this replica volume in GB.  # noqa: E501

        :param size: The size of this ReplicaVolumePost.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < 1):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._size = size

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this ReplicaVolumePost.  # noqa: E501

        Ssh keys that has access to the volume.  # noqa: E501

        :return: The ssh_keys of this ReplicaVolumePost.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this ReplicaVolumePost.

        Ssh keys that has access to the volume.  # noqa: E501

        :param ssh_keys: The ssh_keys of this ReplicaVolumePost.  # noqa: E501
        :type ssh_keys: list[str]
        """

        self._ssh_keys = ssh_keys

    @property
    def type(self):
        """Gets the type of this ReplicaVolumePost.  # noqa: E501


        :return: The type of this ReplicaVolumePost.  # noqa: E501
        :rtype: VolumeHwType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReplicaVolumePost.


        :param type: The type of this ReplicaVolumePost.  # noqa: E501
        :type type: VolumeHwType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def user_data(self):
        """Gets the user_data of this ReplicaVolumePost.  # noqa: E501

        user-data (Cloud Init) for this replica volume.  # noqa: E501

        :return: The user_data of this ReplicaVolumePost.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ReplicaVolumePost.

        user-data (Cloud Init) for this replica volume.  # noqa: E501

        :param user_data: The user_data of this ReplicaVolumePost.  # noqa: E501
        :type user_data: str
        """

        self._user_data = user_data

    @property
    def bus(self):
        """Gets the bus of this ReplicaVolumePost.  # noqa: E501


        :return: The bus of this ReplicaVolumePost.  # noqa: E501
        :rtype: BusType
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """Sets the bus of this ReplicaVolumePost.


        :param bus: The bus of this ReplicaVolumePost.  # noqa: E501
        :type bus: BusType
        """

        self._bus = bus

    @property
    def image_password(self):
        """Gets the image_password of this ReplicaVolumePost.  # noqa: E501

        Image password for this replica volume.  # noqa: E501

        :return: The image_password of this ReplicaVolumePost.  # noqa: E501
        :rtype: str
        """
        return self._image_password

    @image_password.setter
    def image_password(self, image_password):
        """Sets the image_password of this ReplicaVolumePost.

        Image password for this replica volume.  # noqa: E501

        :param image_password: The image_password of this ReplicaVolumePost.  # noqa: E501
        :type image_password: str
        """

        self._image_password = image_password
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReplicaVolumePost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplicaVolumePost):
            return True

        return self.to_dict() != other.to_dict()
