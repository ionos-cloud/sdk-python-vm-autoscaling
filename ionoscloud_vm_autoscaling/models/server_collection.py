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


class ServerCollection(object):
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

        'id': 'str',

        'type': 'str',

        'href': 'str',

        'items': 'list[Server]',
    }

    attribute_map = {

        'id': 'id',

        'type': 'type',

        'href': 'href',

        'items': 'items',
    }

    def __init__(self, id=None, type=None, href=None, items=None, local_vars_configuration=None):  # noqa: E501
        """ServerCollection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._href = None
        self._items = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items


    @property
    def id(self):
        """Gets the id of this ServerCollection.  # noqa: E501

        The resource's unique identifier  # noqa: E501

        :return: The id of this ServerCollection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerCollection.

        The resource's unique identifier  # noqa: E501

        :param id: The id of this ServerCollection.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this ServerCollection.  # noqa: E501

        The type of object that has been created  # noqa: E501

        :return: The type of this ServerCollection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerCollection.

        The type of object that has been created  # noqa: E501

        :param type: The type of this ServerCollection.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def href(self):
        """Gets the href of this ServerCollection.  # noqa: E501

        URL to the object representation (absolute path)  # noqa: E501

        :return: The href of this ServerCollection.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ServerCollection.

        URL to the object representation (absolute path)  # noqa: E501

        :param href: The href of this ServerCollection.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this ServerCollection.  # noqa: E501


        :return: The items of this ServerCollection.  # noqa: E501
        :rtype: list[Server]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ServerCollection.


        :param items: The items of this ServerCollection.  # noqa: E501
        :type items: list[Server]
        """

        self._items = items
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
        if not isinstance(other, ServerCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerCollection):
            return True

        return self.to_dict() != other.to_dict()
