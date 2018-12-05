# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@looker.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Group(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'user_count': 'int',
        'contains_current_user': 'bool',
        'externally_managed': 'bool',
        'include_by_default': 'bool',
        'external_group_id': 'str',
        'can_add_to_content_metadata': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_count': 'user_count',
        'contains_current_user': 'contains_current_user',
        'externally_managed': 'externally_managed',
        'include_by_default': 'include_by_default',
        'external_group_id': 'external_group_id',
        'can_add_to_content_metadata': 'can_add_to_content_metadata',
        'can': 'can'
    }

    def __init__(self, id=None, name=None, user_count=None, contains_current_user=None, externally_managed=None, include_by_default=None, external_group_id=None, can_add_to_content_metadata=None, can=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._user_count = None
        self._contains_current_user = None
        self._externally_managed = None
        self._include_by_default = None
        self._external_group_id = None
        self._can_add_to_content_metadata = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_count is not None:
            self.user_count = user_count
        if contains_current_user is not None:
            self.contains_current_user = contains_current_user
        if externally_managed is not None:
            self.externally_managed = externally_managed
        if include_by_default is not None:
            self.include_by_default = include_by_default
        if external_group_id is not None:
            self.external_group_id = external_group_id
        if can_add_to_content_metadata is not None:
            self.can_add_to_content_metadata = can_add_to_content_metadata
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        Unique Id  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        Name of group  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        Name of group  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_count(self):
        """Gets the user_count of this Group.  # noqa: E501

        Number of users included in this group  # noqa: E501

        :return: The user_count of this Group.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this Group.

        Number of users included in this group  # noqa: E501

        :param user_count: The user_count of this Group.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def contains_current_user(self):
        """Gets the contains_current_user of this Group.  # noqa: E501

        Currently logged in user is group member  # noqa: E501

        :return: The contains_current_user of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._contains_current_user

    @contains_current_user.setter
    def contains_current_user(self, contains_current_user):
        """Sets the contains_current_user of this Group.

        Currently logged in user is group member  # noqa: E501

        :param contains_current_user: The contains_current_user of this Group.  # noqa: E501
        :type: bool
        """

        self._contains_current_user = contains_current_user

    @property
    def externally_managed(self):
        """Gets the externally_managed of this Group.  # noqa: E501

        Group membership controlled outside of Looker  # noqa: E501

        :return: The externally_managed of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """Sets the externally_managed of this Group.

        Group membership controlled outside of Looker  # noqa: E501

        :param externally_managed: The externally_managed of this Group.  # noqa: E501
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def include_by_default(self):
        """Gets the include_by_default of this Group.  # noqa: E501

        New users are added to this group by default  # noqa: E501

        :return: The include_by_default of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._include_by_default

    @include_by_default.setter
    def include_by_default(self, include_by_default):
        """Sets the include_by_default of this Group.

        New users are added to this group by default  # noqa: E501

        :param include_by_default: The include_by_default of this Group.  # noqa: E501
        :type: bool
        """

        self._include_by_default = include_by_default

    @property
    def external_group_id(self):
        """Gets the external_group_id of this Group.  # noqa: E501

        External Id group if embed group  # noqa: E501

        :return: The external_group_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._external_group_id

    @external_group_id.setter
    def external_group_id(self, external_group_id):
        """Sets the external_group_id of this Group.

        External Id group if embed group  # noqa: E501

        :param external_group_id: The external_group_id of this Group.  # noqa: E501
        :type: str
        """

        self._external_group_id = external_group_id

    @property
    def can_add_to_content_metadata(self):
        """Gets the can_add_to_content_metadata of this Group.  # noqa: E501

        Group can be used in content access controls  # noqa: E501

        :return: The can_add_to_content_metadata of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._can_add_to_content_metadata

    @can_add_to_content_metadata.setter
    def can_add_to_content_metadata(self, can_add_to_content_metadata):
        """Sets the can_add_to_content_metadata of this Group.

        Group can be used in content access controls  # noqa: E501

        :param can_add_to_content_metadata: The can_add_to_content_metadata of this Group.  # noqa: E501
        :type: bool
        """

        self._can_add_to_content_metadata = can_add_to_content_metadata

    @property
    def can(self):
        """Gets the can of this Group.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this Group.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this Group.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this Group.  # noqa: E501
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other