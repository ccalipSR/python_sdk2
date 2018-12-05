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


class CreateQueryTask(object):
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
        'query_id': 'int',
        'result_format': 'str',
        'source': 'str',
        'deferred': 'bool',
        'look_id': 'int',
        'dashboard_id': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'query_id': 'query_id',
        'result_format': 'result_format',
        'source': 'source',
        'deferred': 'deferred',
        'look_id': 'look_id',
        'dashboard_id': 'dashboard_id',
        'can': 'can'
    }

    def __init__(self, query_id=None, result_format=None, source=None, deferred=None, look_id=None, dashboard_id=None, can=None):  # noqa: E501
        """CreateQueryTask - a model defined in Swagger"""  # noqa: E501

        self._query_id = None
        self._result_format = None
        self._source = None
        self._deferred = None
        self._look_id = None
        self._dashboard_id = None
        self._can = None
        self.discriminator = None

        self.query_id = query_id
        self.result_format = result_format
        if source is not None:
            self.source = source
        if deferred is not None:
            self.deferred = deferred
        if look_id is not None:
            self.look_id = look_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if can is not None:
            self.can = can

    @property
    def query_id(self):
        """Gets the query_id of this CreateQueryTask.  # noqa: E501

        Id of query to run  # noqa: E501

        :return: The query_id of this CreateQueryTask.  # noqa: E501
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this CreateQueryTask.

        Id of query to run  # noqa: E501

        :param query_id: The query_id of this CreateQueryTask.  # noqa: E501
        :type: int
        """
        if query_id is None:
            raise ValueError("Invalid value for `query_id`, must not be `None`")  # noqa: E501

        self._query_id = query_id

    @property
    def result_format(self):
        """Gets the result_format of this CreateQueryTask.  # noqa: E501

        Desired result format  # noqa: E501

        :return: The result_format of this CreateQueryTask.  # noqa: E501
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        """Sets the result_format of this CreateQueryTask.

        Desired result format  # noqa: E501

        :param result_format: The result_format of this CreateQueryTask.  # noqa: E501
        :type: str
        """
        if result_format is None:
            raise ValueError("Invalid value for `result_format`, must not be `None`")  # noqa: E501

        self._result_format = result_format

    @property
    def source(self):
        """Gets the source of this CreateQueryTask.  # noqa: E501

        Source of query task  # noqa: E501

        :return: The source of this CreateQueryTask.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateQueryTask.

        Source of query task  # noqa: E501

        :param source: The source of this CreateQueryTask.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def deferred(self):
        """Gets the deferred of this CreateQueryTask.  # noqa: E501

        Create the task but defer execution  # noqa: E501

        :return: The deferred of this CreateQueryTask.  # noqa: E501
        :rtype: bool
        """
        return self._deferred

    @deferred.setter
    def deferred(self, deferred):
        """Sets the deferred of this CreateQueryTask.

        Create the task but defer execution  # noqa: E501

        :param deferred: The deferred of this CreateQueryTask.  # noqa: E501
        :type: bool
        """

        self._deferred = deferred

    @property
    def look_id(self):
        """Gets the look_id of this CreateQueryTask.  # noqa: E501

        Id of look associated with query.  # noqa: E501

        :return: The look_id of this CreateQueryTask.  # noqa: E501
        :rtype: int
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """Sets the look_id of this CreateQueryTask.

        Id of look associated with query.  # noqa: E501

        :param look_id: The look_id of this CreateQueryTask.  # noqa: E501
        :type: int
        """

        self._look_id = look_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this CreateQueryTask.  # noqa: E501

        Id of dashboard associated with query.  # noqa: E501

        :return: The dashboard_id of this CreateQueryTask.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this CreateQueryTask.

        Id of dashboard associated with query.  # noqa: E501

        :param dashboard_id: The dashboard_id of this CreateQueryTask.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def can(self):
        """Gets the can of this CreateQueryTask.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this CreateQueryTask.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this CreateQueryTask.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this CreateQueryTask.  # noqa: E501
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
        if not isinstance(other, CreateQueryTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
