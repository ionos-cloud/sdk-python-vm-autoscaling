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


class GroupPostResponse(object):
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

        'metadata': 'Metadata',

        'properties': 'GroupProperties',

        'entities': 'GroupPostEntities',

        'started_actions': 'list[ActionResource]',
    }

    attribute_map = {

        'id': 'id',

        'type': 'type',

        'href': 'href',

        'metadata': 'metadata',

        'properties': 'properties',

        'entities': 'entities',

        'started_actions': 'startedActions',
    }

    def __init__(self, id=None, type=None, href=None, metadata=None, properties=None, entities=None, started_actions=None, local_vars_configuration=None):  # noqa: E501
        """GroupPostResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._href = None
        self._metadata = None
        self._properties = None
        self._entities = None
        self._started_actions = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        if href is not None:
            self.href = href
        if metadata is not None:
            self.metadata = metadata
        self.properties = properties
        if entities is not None:
            self.entities = entities
        if started_actions is not None:
            self.started_actions = started_actions


    @property
    def id(self):
        """Gets the id of this GroupPostResponse.  # noqa: E501

        The unique resource identifier.  # noqa: E501

        :return: The id of this GroupPostResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupPostResponse.

        The unique resource identifier.  # noqa: E501

        :param id: The id of this GroupPostResponse.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this GroupPostResponse.  # noqa: E501

        The resource type.  # noqa: E501

        :return: The type of this GroupPostResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupPostResponse.

        The resource type.  # noqa: E501

        :param type: The type of this GroupPostResponse.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def href(self):
        """Gets the href of this GroupPostResponse.  # noqa: E501

        The absolute URL to the resource's representation.  # noqa: E501

        :return: The href of this GroupPostResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this GroupPostResponse.

        The absolute URL to the resource's representation.  # noqa: E501

        :param href: The href of this GroupPostResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def metadata(self):
        """Gets the metadata of this GroupPostResponse.  # noqa: E501


        :return: The metadata of this GroupPostResponse.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GroupPostResponse.


        :param metadata: The metadata of this GroupPostResponse.  # noqa: E501
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def properties(self):
        """Gets the properties of this GroupPostResponse.  # noqa: E501


        :return: The properties of this GroupPostResponse.  # noqa: E501
        :rtype: GroupProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GroupPostResponse.


        :param properties: The properties of this GroupPostResponse.  # noqa: E501
        :type properties: GroupProperties
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def entities(self):
        """Gets the entities of this GroupPostResponse.  # noqa: E501


        :return: The entities of this GroupPostResponse.  # noqa: E501
        :rtype: GroupPostEntities
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this GroupPostResponse.


        :param entities: The entities of this GroupPostResponse.  # noqa: E501
        :type entities: GroupPostEntities
        """

        self._entities = entities

    @property
    def started_actions(self):
        """Gets the started_actions of this GroupPostResponse.  # noqa: E501

        Any background activity caused by this request. You can use this to track the progress of such activities.  # noqa: E501

        :return: The started_actions of this GroupPostResponse.  # noqa: E501
        :rtype: list[ActionResource]
        """
        return self._started_actions

    @started_actions.setter
    def started_actions(self, started_actions):
        """Sets the started_actions of this GroupPostResponse.

        Any background activity caused by this request. You can use this to track the progress of such activities.  # noqa: E501

        :param started_actions: The started_actions of this GroupPostResponse.  # noqa: E501
        :type started_actions: list[ActionResource]
        """

        self._started_actions = started_actions
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
        if not isinstance(other, GroupPostResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupPostResponse):
            return True

        return self.to_dict() != other.to_dict()
