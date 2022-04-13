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


class ParseErrorAllOf(object):
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

        'http_status': 'Int',

        'messages': 'list[ErrorMessageParse]',
    }

    attribute_map = {

        'http_status': 'httpStatus',

        'messages': 'messages',
    }

    def __init__(self, http_status=None, messages=None, local_vars_configuration=None):  # noqa: E501
        """ParseErrorAllOf - a model defined in OpenAPI"""  # noqa: E501
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
        """Gets the http_status of this ParseErrorAllOf.  # noqa: E501


        :return: The http_status of this ParseErrorAllOf.  # noqa: E501
        :rtype: Int
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this ParseErrorAllOf.


        :param http_status: The http_status of this ParseErrorAllOf.  # noqa: E501
        :type http_status: Int
        """

        self._http_status = http_status

    @property
    def messages(self):
        """Gets the messages of this ParseErrorAllOf.  # noqa: E501


        :return: The messages of this ParseErrorAllOf.  # noqa: E501
        :rtype: list[ErrorMessageParse]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ParseErrorAllOf.


        :param messages: The messages of this ParseErrorAllOf.  # noqa: E501
        :type messages: list[ErrorMessageParse]
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
        if not isinstance(other, ParseErrorAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParseErrorAllOf):
            return True

        return self.to_dict() != other.to_dict()
