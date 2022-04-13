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


class MetadataBasic(object):
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

        'created_date': 'datetime',

        'etag': 'str',

        'last_modified_date': 'datetime',

        'state': 'MetadataState',
    }

    attribute_map = {

        'created_date': 'createdDate',

        'etag': 'etag',

        'last_modified_date': 'lastModifiedDate',

        'state': 'state',
    }

    def __init__(self, created_date=None, etag=None, last_modified_date=None, state=None, local_vars_configuration=None):  # noqa: E501
        """MetadataBasic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_date = None
        self._etag = None
        self._last_modified_date = None
        self._state = None
        self.discriminator = None

        self.created_date = created_date
        self.etag = etag
        self.last_modified_date = last_modified_date
        self.state = state


    @property
    def created_date(self):
        """Gets the created_date of this MetadataBasic.  # noqa: E501

        When the resource was created.  # noqa: E501

        :return: The created_date of this MetadataBasic.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this MetadataBasic.

        When the resource was created.  # noqa: E501

        :param created_date: The created_date of this MetadataBasic.  # noqa: E501
        :type created_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_date is None:  # noqa: E501
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def etag(self):
        """Gets the etag of this MetadataBasic.  # noqa: E501

        Resource etag  # noqa: E501

        :return: The etag of this MetadataBasic.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this MetadataBasic.

        Resource etag  # noqa: E501

        :param etag: The etag of this MetadataBasic.  # noqa: E501
        :type etag: str
        """
        if self.local_vars_configuration.client_side_validation and etag is None:  # noqa: E501
            raise ValueError("Invalid value for `etag`, must not be `None`")  # noqa: E501

        self._etag = etag

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this MetadataBasic.  # noqa: E501

        When the resource was last modified.  # noqa: E501

        :return: The last_modified_date of this MetadataBasic.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this MetadataBasic.

        When the resource was last modified.  # noqa: E501

        :param last_modified_date: The last_modified_date of this MetadataBasic.  # noqa: E501
        :type last_modified_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_date is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_date`, must not be `None`")  # noqa: E501

        self._last_modified_date = last_modified_date

    @property
    def state(self):
        """Gets the state of this MetadataBasic.  # noqa: E501


        :return: The state of this MetadataBasic.  # noqa: E501
        :rtype: MetadataState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MetadataBasic.


        :param state: The state of this MetadataBasic.  # noqa: E501
        :type state: MetadataState
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state
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
        if not isinstance(other, MetadataBasic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetadataBasic):
            return True

        return self.to_dict() != other.to_dict()
