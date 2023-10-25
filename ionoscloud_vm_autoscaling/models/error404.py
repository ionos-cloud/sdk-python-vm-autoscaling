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


class Error404(object):
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

        'http_status': 'int',

        'messages': 'list[Error404Message]',
    }

    attribute_map = {

        'http_status': 'httpStatus',

        'messages': 'messages',
    }

    def __init__(self, http_status=None, messages=None, local_vars_configuration=None):  # noqa: E501
        """Error404 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._http_status = None
        self._messages = None
        self.discriminator = None

        if http_status is not None:
            self.http_status = http_status
        if messages is not None:
            self.messages = messages


    @property
    def http_status(self):
        """Gets the http_status of this Error404.  # noqa: E501


        :return: The http_status of this Error404.  # noqa: E501
        :rtype: int
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this Error404.


        :param http_status: The http_status of this Error404.  # noqa: E501
        :type http_status: int
        """

        self._http_status = http_status

    @property
    def messages(self):
        """Gets the messages of this Error404.  # noqa: E501


        :return: The messages of this Error404.  # noqa: E501
        :rtype: list[Error404Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Error404.


        :param messages: The messages of this Error404.  # noqa: E501
        :type messages: list[Error404Message]
        """

        self._messages = messages
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
        if not isinstance(other, Error404):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error404):
            return True

        return self.to_dict() != other.to_dict()
