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


class CredentialsLookerOpenid(object):
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
        'email': 'str',
        'created_at': 'str',
        'logged_in_at': 'str',
        'logged_in_ip': 'str',
        'is_disabled': 'bool',
        'type': 'str',
        'url': 'str',
        'user_url': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'email': 'email',
        'created_at': 'created_at',
        'logged_in_at': 'logged_in_at',
        'logged_in_ip': 'logged_in_ip',
        'is_disabled': 'is_disabled',
        'type': 'type',
        'url': 'url',
        'user_url': 'user_url',
        'can': 'can'
    }

    def __init__(self, email=None, created_at=None, logged_in_at=None, logged_in_ip=None, is_disabled=None, type=None, url=None, user_url=None, can=None):  # noqa: E501
        """CredentialsLookerOpenid - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._created_at = None
        self._logged_in_at = None
        self._logged_in_ip = None
        self._is_disabled = None
        self._type = None
        self._url = None
        self._user_url = None
        self._can = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if created_at is not None:
            self.created_at = created_at
        if logged_in_at is not None:
            self.logged_in_at = logged_in_at
        if logged_in_ip is not None:
            self.logged_in_ip = logged_in_ip
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if user_url is not None:
            self.user_url = user_url
        if can is not None:
            self.can = can

    @property
    def email(self):
        """Gets the email of this CredentialsLookerOpenid.  # noqa: E501

        EMail address used for user login  # noqa: E501

        :return: The email of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CredentialsLookerOpenid.

        EMail address used for user login  # noqa: E501

        :param email: The email of this CredentialsLookerOpenid.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def created_at(self):
        """Gets the created_at of this CredentialsLookerOpenid.  # noqa: E501

        Timestamp for the creation of this credential  # noqa: E501

        :return: The created_at of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CredentialsLookerOpenid.

        Timestamp for the creation of this credential  # noqa: E501

        :param created_at: The created_at of this CredentialsLookerOpenid.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def logged_in_at(self):
        """Gets the logged_in_at of this CredentialsLookerOpenid.  # noqa: E501

        Timestamp for most recent login using credential  # noqa: E501

        :return: The logged_in_at of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: str
        """
        return self._logged_in_at

    @logged_in_at.setter
    def logged_in_at(self, logged_in_at):
        """Sets the logged_in_at of this CredentialsLookerOpenid.

        Timestamp for most recent login using credential  # noqa: E501

        :param logged_in_at: The logged_in_at of this CredentialsLookerOpenid.  # noqa: E501
        :type: str
        """

        self._logged_in_at = logged_in_at

    @property
    def logged_in_ip(self):
        """Gets the logged_in_ip of this CredentialsLookerOpenid.  # noqa: E501

        IP address of client for most recent login using credential  # noqa: E501

        :return: The logged_in_ip of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: str
        """
        return self._logged_in_ip

    @logged_in_ip.setter
    def logged_in_ip(self, logged_in_ip):
        """Sets the logged_in_ip of this CredentialsLookerOpenid.

        IP address of client for most recent login using credential  # noqa: E501

        :param logged_in_ip: The logged_in_ip of this CredentialsLookerOpenid.  # noqa: E501
        :type: str
        """

        self._logged_in_ip = logged_in_ip

    @property
    def is_disabled(self):
        """Gets the is_disabled of this CredentialsLookerOpenid.  # noqa: E501

        Has this credential been disabled?  # noqa: E501

        :return: The is_disabled of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this CredentialsLookerOpenid.

        Has this credential been disabled?  # noqa: E501

        :param is_disabled: The is_disabled of this CredentialsLookerOpenid.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def type(self):
        """Gets the type of this CredentialsLookerOpenid.  # noqa: E501

        Short name for the type of this kind of credential  # noqa: E501

        :return: The type of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CredentialsLookerOpenid.

        Short name for the type of this kind of credential  # noqa: E501

        :param type: The type of this CredentialsLookerOpenid.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this CredentialsLookerOpenid.  # noqa: E501

        Link to get this item  # noqa: E501

        :return: The url of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CredentialsLookerOpenid.

        Link to get this item  # noqa: E501

        :param url: The url of this CredentialsLookerOpenid.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user_url(self):
        """Gets the user_url of this CredentialsLookerOpenid.  # noqa: E501

        Link to get this user  # noqa: E501

        :return: The user_url of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: str
        """
        return self._user_url

    @user_url.setter
    def user_url(self, user_url):
        """Sets the user_url of this CredentialsLookerOpenid.

        Link to get this user  # noqa: E501

        :param user_url: The user_url of this CredentialsLookerOpenid.  # noqa: E501
        :type: str
        """

        self._user_url = user_url

    @property
    def can(self):
        """Gets the can of this CredentialsLookerOpenid.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this CredentialsLookerOpenid.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this CredentialsLookerOpenid.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this CredentialsLookerOpenid.  # noqa: E501
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
        if not isinstance(other, CredentialsLookerOpenid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other