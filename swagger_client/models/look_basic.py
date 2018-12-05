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


class LookBasic(object):
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
        'title': 'str',
        'content_metadata_id': 'int',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'content_metadata_id': 'content_metadata_id',
        'can': 'can'
    }

    def __init__(self, id=None, title=None, content_metadata_id=None, can=None):  # noqa: E501
        """LookBasic - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._content_metadata_id = None
        self._can = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if content_metadata_id is not None:
            self.content_metadata_id = content_metadata_id
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this LookBasic.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this LookBasic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LookBasic.

        Unique Id  # noqa: E501

        :param id: The id of this LookBasic.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this LookBasic.  # noqa: E501

        Look Title  # noqa: E501

        :return: The title of this LookBasic.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LookBasic.

        Look Title  # noqa: E501

        :param title: The title of this LookBasic.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content_metadata_id(self):
        """Gets the content_metadata_id of this LookBasic.  # noqa: E501

        Id of content metadata  # noqa: E501

        :return: The content_metadata_id of this LookBasic.  # noqa: E501
        :rtype: int
        """
        return self._content_metadata_id

    @content_metadata_id.setter
    def content_metadata_id(self, content_metadata_id):
        """Sets the content_metadata_id of this LookBasic.

        Id of content metadata  # noqa: E501

        :param content_metadata_id: The content_metadata_id of this LookBasic.  # noqa: E501
        :type: int
        """

        self._content_metadata_id = content_metadata_id

    @property
    def can(self):
        """Gets the can of this LookBasic.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this LookBasic.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this LookBasic.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this LookBasic.  # noqa: E501
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
        if not isinstance(other, LookBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
