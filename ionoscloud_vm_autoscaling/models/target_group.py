# coding: utf-8

"""
    VM Auto Scaling API

    The VM Auto Scaling Service enables IONOS clients to horizontally scale the number of VM replicas based on configured rules. You can use VM Auto Scaling to ensure that you have a sufficient number of replicas to handle your application loads at all times.  For this purpose, create a VM Auto Scaling Group that contains the server replicas. The VM Auto Scaling Service ensures that the number of replicas in the group is always within the defined limits.   When scaling policies are set, VM Auto Scaling creates or deletes replicas according to the requirements of your applications. For each policy, specified 'scale-in' and 'scale-out' actions are performed when the corresponding thresholds are reached.  # noqa: E501

    The version of the OpenAPI document: 1-SDK.1
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_vm_autoscaling.configuration import Configuration


class TargetGroup(object):
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

        'target_group_id': 'str',

        'port': 'int',

        'weight': 'int',
    }

    attribute_map = {

        'target_group_id': 'targetGroupId',

        'port': 'port',

        'weight': 'weight',
    }

    def __init__(self, target_group_id=None, port=None, weight=None, local_vars_configuration=None):  # noqa: E501
        """TargetGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_group_id = None
        self._port = None
        self._weight = None
        self.discriminator = None

        self.target_group_id = target_group_id
        self.port = port
        self.weight = weight


    @property
    def target_group_id(self):
        """Gets the target_group_id of this TargetGroup.  # noqa: E501

        id  # noqa: E501

        :return: The target_group_id of this TargetGroup.  # noqa: E501
        :rtype: str
        """
        return self._target_group_id

    @target_group_id.setter
    def target_group_id(self, target_group_id):
        """Sets the target_group_id of this TargetGroup.

        id  # noqa: E501

        :param target_group_id: The target_group_id of this TargetGroup.  # noqa: E501
        :type target_group_id: str
        """
        if self.local_vars_configuration.client_side_validation and target_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_group_id`, must not be `None`")  # noqa: E501

        self._target_group_id = target_group_id

    @property
    def port(self):
        """Gets the port of this TargetGroup.  # noqa: E501

        port  # noqa: E501

        :return: The port of this TargetGroup.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TargetGroup.

        port  # noqa: E501

        :param port: The port of this TargetGroup.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def weight(self):
        """Gets the weight of this TargetGroup.  # noqa: E501

        weight  # noqa: E501

        :return: The weight of this TargetGroup.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this TargetGroup.

        weight  # noqa: E501

        :param weight: The weight of this TargetGroup.  # noqa: E501
        :type weight: int
        """
        if self.local_vars_configuration.client_side_validation and weight is None:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight
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
        if not isinstance(other, TargetGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetGroup):
            return True

        return self.to_dict() != other.to_dict()
