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
from swagger_client.api.project_api import ProjectApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.project_api.ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_git_branches(self):
        """Test case for all_git_branches

        Get All Git Branches  # noqa: E501
        """
        pass

    def test_all_git_connection_tests(self):
        """Test case for all_git_connection_tests

        Get All Git Connection Tests  # noqa: E501
        """
        pass

    def test_all_project_files(self):
        """Test case for all_project_files

        Get All Project Files  # noqa: E501
        """
        pass

    def test_all_projects(self):
        """Test case for all_projects

        Get All Projects  # noqa: E501
        """
        pass

    def test_create_git_branch(self):
        """Test case for create_git_branch

        Checkout New Git Branch  # noqa: E501
        """
        pass

    def test_create_git_deploy_key(self):
        """Test case for create_git_deploy_key

        Create Deploy Key  # noqa: E501
        """
        pass

    def test_create_project(self):
        """Test case for create_project

        Create Project  # noqa: E501
        """
        pass

    def test_delete_git_branch(self):
        """Test case for delete_git_branch

        Delete a Git Branch  # noqa: E501
        """
        pass

    def test_find_git_branch(self):
        """Test case for find_git_branch

        Find a Git Branch  # noqa: E501
        """
        pass

    def test_git_branch(self):
        """Test case for git_branch

        Get Active Git Branch  # noqa: E501
        """
        pass

    def test_git_deploy_key(self):
        """Test case for git_deploy_key

        Git Deploy Key  # noqa: E501
        """
        pass

    def test_project(self):
        """Test case for project

        Get Project  # noqa: E501
        """
        pass

    def test_project_file(self):
        """Test case for project_file

        Get Project File  # noqa: E501
        """
        pass

    def test_project_validation_results(self):
        """Test case for project_validation_results

        Cached Project Validation Results  # noqa: E501
        """
        pass

    def test_project_workspace(self):
        """Test case for project_workspace

        Get Project Workspace  # noqa: E501
        """
        pass

    def test_reset_project_to_production(self):
        """Test case for reset_project_to_production

        Reset To Production  # noqa: E501
        """
        pass

    def test_reset_project_to_remote(self):
        """Test case for reset_project_to_remote

        Reset To Remote  # noqa: E501
        """
        pass

    def test_run_git_connection_test(self):
        """Test case for run_git_connection_test

        Run Git Connection Test  # noqa: E501
        """
        pass

    def test_update_git_branch(self):
        """Test case for update_git_branch

        Update Project Git Branch  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update Project  # noqa: E501
        """
        pass

    def test_validate_project(self):
        """Test case for validate_project

        Validate Project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
