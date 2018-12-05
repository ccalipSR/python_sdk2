# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@looker.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.group_api import GroupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.group_api.GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_group_group(self):
        """Test case for add_group_group

        Add a Group to Group  # noqa: E501
        """
        pass

    def test_add_group_user(self):
        """Test case for add_group_user

        Add a User to Group  # noqa: E501
        """
        pass

    def test_all_group_groups(self):
        """Test case for all_group_groups

        Get All Groups in Group  # noqa: E501
        """
        pass

    def test_all_group_users(self):
        """Test case for all_group_users

        Get All Users in Group  # noqa: E501
        """
        pass

    def test_all_groups(self):
        """Test case for all_groups

        Get All Groups  # noqa: E501
        """
        pass

    def test_create_group(self):
        """Test case for create_group

        Create Group  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete Group  # noqa: E501
        """
        pass

    def test_delete_group_from_group(self):
        """Test case for delete_group_from_group

        Deletes a Group from Group  # noqa: E501
        """
        pass

    def test_delete_group_user(self):
        """Test case for delete_group_user

        Remove a User from Group  # noqa: E501
        """
        pass

    def test_delete_user_attribute_group_value(self):
        """Test case for delete_user_attribute_group_value

        Delete User Attribute Group Value  # noqa: E501
        """
        pass

    def test_group(self):
        """Test case for group

        Get Group  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Update Group  # noqa: E501
        """
        pass

    def test_update_user_attribute_group_value(self):
        """Test case for update_user_attribute_group_value

        Set User Attribute Group Value  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
