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

from swagger_client.models.api_version_element import ApiVersionElement  # noqa: F401,E501


class ApiVersion(object):
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
        'looker_release_version': 'str',
        'current_version': 'ApiVersionElement',
        'supported_versions': 'list[ApiVersionElement]',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'looker_release_version': 'looker_release_version',
        'current_version': 'current_version',
        'supported_versions': 'supported_versions',
        'can': 'can'
    }

    def __init__(self, looker_release_version=None, current_version=None, supported_versions=None, can=None):  # noqa: E501
        """ApiVersion - a model defined in Swagger"""  # noqa: E501

        self._looker_release_version = None
        self._current_version = None
        self._supported_versions = None
        self._can = None
        self.discriminator = None

        if looker_release_version is not None:
            self.looker_release_version = looker_release_version
        if current_version is not None:
            self.current_version = current_version
        if supported_versions is not None:
            self.supported_versions = supported_versions
        if can is not None:
            self.can = can

    @property
    def looker_release_version(self):
        """Gets the looker_release_version of this ApiVersion.  # noqa: E501

        Current Looker release version number  # noqa: E501

        :return: The looker_release_version of this ApiVersion.  # noqa: E501
        :rtype: str
        """
        return self._looker_release_version

    @looker_release_version.setter
    def looker_release_version(self, looker_release_version):
        """Sets the looker_release_version of this ApiVersion.

        Current Looker release version number  # noqa: E501

        :param looker_release_version: The looker_release_version of this ApiVersion.  # noqa: E501
        :type: str
        """

        self._looker_release_version = looker_release_version

    @property
    def current_version(self):
        """Gets the current_version of this ApiVersion.  # noqa: E501

        Current version for this Looker instance  # noqa: E501

        :return: The current_version of this ApiVersion.  # noqa: E501
        :rtype: ApiVersionElement
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this ApiVersion.

        Current version for this Looker instance  # noqa: E501

        :param current_version: The current_version of this ApiVersion.  # noqa: E501
        :type: ApiVersionElement
        """

        self._current_version = current_version

    @property
    def supported_versions(self):
        """Gets the supported_versions of this ApiVersion.  # noqa: E501

        Array of versions supported by this Looker instance  # noqa: E501

        :return: The supported_versions of this ApiVersion.  # noqa: E501
        :rtype: list[ApiVersionElement]
        """
        return self._supported_versions

    @supported_versions.setter
    def supported_versions(self, supported_versions):
        """Sets the supported_versions of this ApiVersion.

        Array of versions supported by this Looker instance  # noqa: E501

        :param supported_versions: The supported_versions of this ApiVersion.  # noqa: E501
        :type: list[ApiVersionElement]
        """

        self._supported_versions = supported_versions

    @property
    def can(self):
        """Gets the can of this ApiVersion.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this ApiVersion.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this ApiVersion.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this ApiVersion.  # noqa: E501
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
        if not isinstance(other, ApiVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
