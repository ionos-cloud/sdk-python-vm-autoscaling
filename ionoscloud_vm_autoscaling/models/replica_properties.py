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


class ReplicaProperties(object):
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

        'availability_zone': 'AvailabilityZone',

        'cores': 'int',

        'cpu_family': 'CpuFamily',

        'nics': 'list[ReplicaNic]',

        'ram': 'int',
    }

    attribute_map = {

        'availability_zone': 'availabilityZone',

        'cores': 'cores',

        'cpu_family': 'cpuFamily',

        'nics': 'nics',

        'ram': 'ram',
    }

    def __init__(self, availability_zone=None, cores=None, cpu_family=None, nics=None, ram=None, local_vars_configuration=None):  # noqa: E501
        """ReplicaProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._availability_zone = None
        self._cores = None
        self._cpu_family = None
        self._nics = None
        self._ram = None
        self.discriminator = None

        self.availability_zone = availability_zone
        self.cores = cores
        if cpu_family is not None:
            self.cpu_family = cpu_family
        if nics is not None:
            self.nics = nics
        self.ram = ram


    @property
    def availability_zone(self):
        """Gets the availability_zone of this ReplicaProperties.  # noqa: E501


        :return: The availability_zone of this ReplicaProperties.  # noqa: E501
        :rtype: AvailabilityZone
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ReplicaProperties.


        :param availability_zone: The availability_zone of this ReplicaProperties.  # noqa: E501
        :type availability_zone: AvailabilityZone
        """
        if self.local_vars_configuration.client_side_validation and availability_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `availability_zone`, must not be `None`")  # noqa: E501

        self._availability_zone = availability_zone

    @property
    def cores(self):
        """Gets the cores of this ReplicaProperties.  # noqa: E501

        The total number of cores for the VMs.  # noqa: E501

        :return: The cores of this ReplicaProperties.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this ReplicaProperties.

        The total number of cores for the VMs.  # noqa: E501

        :param cores: The cores of this ReplicaProperties.  # noqa: E501
        :type cores: int
        """
        if self.local_vars_configuration.client_side_validation and cores is None:  # noqa: E501
            raise ValueError("Invalid value for `cores`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < 1):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cores = cores

    @property
    def cpu_family(self):
        """Gets the cpu_family of this ReplicaProperties.  # noqa: E501


        :return: The cpu_family of this ReplicaProperties.  # noqa: E501
        :rtype: CpuFamily
        """
        return self._cpu_family

    @cpu_family.setter
    def cpu_family(self, cpu_family):
        """Sets the cpu_family of this ReplicaProperties.


        :param cpu_family: The cpu_family of this ReplicaProperties.  # noqa: E501
        :type cpu_family: CpuFamily
        """

        self._cpu_family = cpu_family

    @property
    def nics(self):
        """Gets the nics of this ReplicaProperties.  # noqa: E501

        List of NICs associated with this Replica.  # noqa: E501

        :return: The nics of this ReplicaProperties.  # noqa: E501
        :rtype: list[ReplicaNic]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this ReplicaProperties.

        List of NICs associated with this Replica.  # noqa: E501

        :param nics: The nics of this ReplicaProperties.  # noqa: E501
        :type nics: list[ReplicaNic]
        """

        self._nics = nics

    @property
    def ram(self):
        """Gets the ram of this ReplicaProperties.  # noqa: E501

        The amount of memory for the VMs in MB, e.g. 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB.  # noqa: E501

        :return: The ram of this ReplicaProperties.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ReplicaProperties.

        The amount of memory for the VMs in MB, e.g. 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB.  # noqa: E501

        :param ram: The ram of this ReplicaProperties.  # noqa: E501
        :type ram: int
        """
        if self.local_vars_configuration.client_side_validation and ram is None:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501

        self._ram = ram
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
        if not isinstance(other, ReplicaProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplicaProperties):
            return True

        return self.to_dict() != other.to_dict()
