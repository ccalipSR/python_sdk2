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
from swagger_client.api.content_api import ContentApi  # noqa: E501
from swagger_client.rest import ApiException


class TestContentApi(unittest.TestCase):
    """ContentApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.content_api.ContentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_content_metadata_accesss(self):
        """Test case for all_content_metadata_accesss

        Get All Content Metadata Accesss  # noqa: E501
        """
        pass

    def test_all_content_metadatas(self):
        """Test case for all_content_metadatas

        Get All Content Metadatas  # noqa: E501
        """
        pass

    def test_content_favorite(self):
        """Test case for content_favorite

        Get Favorite Content  # noqa: E501
        """
        pass

    def test_content_metadata(self):
        """Test case for content_metadata

        Get Content Metadata  # noqa: E501
        """
        pass

    def test_create_content_favorite(self):
        """Test case for create_content_favorite

        Create Favorite Content  # noqa: E501
        """
        pass

    def test_create_content_metadata_access(self):
        """Test case for create_content_metadata_access

        Create Content Metadata Access  # noqa: E501
        """
        pass

    def test_delete_content_favorite(self):
        """Test case for delete_content_favorite

        Delete Favorite Content  # noqa: E501
        """
        pass

    def test_delete_content_metadata_access(self):
        """Test case for delete_content_metadata_access

        Delete Content Metadata Access  # noqa: E501
        """
        pass

    def test_search_content_favorites(self):
        """Test case for search_content_favorites

        Search Favorite Contents  # noqa: E501
        """
        pass

    def test_search_content_views(self):
        """Test case for search_content_views

        Search Content Views  # noqa: E501
        """
        pass

    def test_update_content_metadata(self):
        """Test case for update_content_metadata

        Update Content Metadata  # noqa: E501
        """
        pass

    def test_update_content_metadata_access(self):
        """Test case for update_content_metadata_access

        Update Content Metadata Access  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
