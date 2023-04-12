# coding: utf-8

"""
    VM Auto Scaling API

    The VM Auto Scaling Service enables IONOS clients to horizontally scale the number of VM replicas based on configured rules. You can use Auto Scaling to ensure that you have a sufficient number of replicas to handle your application loads at all times.  For this purpose, create an Auto Scaling group that contains the server replicas. The VM Auto Scaling Service ensures that the number of replicas in the group is always within the defined limits. For example, if the number of target replicas is specified, Auto Scaling maintains the specified number of replicas.   When scaling policies are set, Auto Scaling creates or deletes replicas according to the requirements of your applications. For each policy, specified 'scale-in' and 'scale-out' actions are performed when the corresponding thresholds are reached.  # noqa: E501

    The version of the OpenAPI document: 1-SDK.1
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_vm_autoscaling.configuration import Configuration


class ErrorReplicaValidateMessage(object):
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

        'error_code': 'str',

        'message': 'str',
    }

    attribute_map = {

        'error_code': 'errorCode',

        'message': 'message',
    }

    def __init__(self, error_code=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ErrorReplicaValidateMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_code = None
        self._message = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.message = message


    @property
    def error_code(self):
        """Gets the error_code of this ErrorReplicaValidateMessage.  # noqa: E501


        :return: The error_code of this ErrorReplicaValidateMessage.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ErrorReplicaValidateMessage.


        :param error_code: The error_code of this ErrorReplicaValidateMessage.  # noqa: E501
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this ErrorReplicaValidateMessage.  # noqa: E501


        :return: The message of this ErrorReplicaValidateMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorReplicaValidateMessage.


        :param message: The message of this ErrorReplicaValidateMessage.  # noqa: E501
        :type message: str
        """

        self._message = message
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
        if not isinstance(other, ErrorReplicaValidateMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorReplicaValidateMessage):
            return True

        return self.to_dict() != other.to_dict()
