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

from swagger_client.models.data_action_form_select_option import DataActionFormSelectOption  # noqa: F401,E501


class DataActionFormField(object):
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
        'name': 'str',
        'label': 'str',
        'description': 'str',
        'type': 'str',
        'default': 'str',
        'oauth_url': 'str',
        'required': 'bool',
        'options': 'list[DataActionFormSelectOption]'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'description': 'description',
        'type': 'type',
        'default': 'default',
        'oauth_url': 'oauth_url',
        'required': 'required',
        'options': 'options'
    }

    def __init__(self, name=None, label=None, description=None, type=None, default=None, oauth_url=None, required=None, options=None):  # noqa: E501
        """DataActionFormField - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._label = None
        self._description = None
        self._type = None
        self._default = None
        self._oauth_url = None
        self._required = None
        self._options = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if default is not None:
            self.default = default
        if oauth_url is not None:
            self.oauth_url = oauth_url
        if required is not None:
            self.required = required
        if options is not None:
            self.options = options

    @property
    def name(self):
        """Gets the name of this DataActionFormField.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this DataActionFormField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataActionFormField.

        Name  # noqa: E501

        :param name: The name of this DataActionFormField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this DataActionFormField.  # noqa: E501

        Human-readable label  # noqa: E501

        :return: The label of this DataActionFormField.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DataActionFormField.

        Human-readable label  # noqa: E501

        :param label: The label of this DataActionFormField.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this DataActionFormField.  # noqa: E501

        Description of field  # noqa: E501

        :return: The description of this DataActionFormField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataActionFormField.

        Description of field  # noqa: E501

        :param description: The description of this DataActionFormField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this DataActionFormField.  # noqa: E501

        Type of field.  # noqa: E501

        :return: The type of this DataActionFormField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataActionFormField.

        Type of field.  # noqa: E501

        :param type: The type of this DataActionFormField.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def default(self):
        """Gets the default of this DataActionFormField.  # noqa: E501

        Default value of the field.  # noqa: E501

        :return: The default of this DataActionFormField.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DataActionFormField.

        Default value of the field.  # noqa: E501

        :param default: The default of this DataActionFormField.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def oauth_url(self):
        """Gets the oauth_url of this DataActionFormField.  # noqa: E501

        The URL for an oauth link, if type is 'oauth_link'.  # noqa: E501

        :return: The oauth_url of this DataActionFormField.  # noqa: E501
        :rtype: str
        """
        return self._oauth_url

    @oauth_url.setter
    def oauth_url(self, oauth_url):
        """Sets the oauth_url of this DataActionFormField.

        The URL for an oauth link, if type is 'oauth_link'.  # noqa: E501

        :param oauth_url: The oauth_url of this DataActionFormField.  # noqa: E501
        :type: str
        """

        self._oauth_url = oauth_url

    @property
    def required(self):
        """Gets the required of this DataActionFormField.  # noqa: E501

        Whether or not the field is required. This is a user-interface hint. A user interface displaying this form should not submit it without a value for this field. The action server must also perform this validation.  # noqa: E501

        :return: The required of this DataActionFormField.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DataActionFormField.

        Whether or not the field is required. This is a user-interface hint. A user interface displaying this form should not submit it without a value for this field. The action server must also perform this validation.  # noqa: E501

        :param required: The required of this DataActionFormField.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def options(self):
        """Gets the options of this DataActionFormField.  # noqa: E501

        If the form type is 'select', a list of options to be selected from.  # noqa: E501

        :return: The options of this DataActionFormField.  # noqa: E501
        :rtype: list[DataActionFormSelectOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DataActionFormField.

        If the form type is 'select', a list of options to be selected from.  # noqa: E501

        :param options: The options of this DataActionFormField.  # noqa: E501
        :type: list[DataActionFormSelectOption]
        """

        self._options = options

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
        if not isinstance(other, DataActionFormField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
