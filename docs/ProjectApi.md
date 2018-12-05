# swagger_client.ProjectApi

All URIs are relative to *https://shoprunner.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_git_branches**](ProjectApi.md#all_git_branches) | **GET** /projects/{project_id}/git_branches | Get All Git Branches
[**all_git_connection_tests**](ProjectApi.md#all_git_connection_tests) | **GET** /projects/{project_id}/git_connection_tests | Get All Git Connection Tests
[**all_project_files**](ProjectApi.md#all_project_files) | **GET** /projects/{project_id}/files | Get All Project Files
[**all_projects**](ProjectApi.md#all_projects) | **GET** /projects | Get All Projects
[**create_git_branch**](ProjectApi.md#create_git_branch) | **POST** /projects/{project_id}/git_branch | Checkout New Git Branch
[**create_git_deploy_key**](ProjectApi.md#create_git_deploy_key) | **POST** /projects/{project_id}/git/deploy_key | Create Deploy Key
[**create_project**](ProjectApi.md#create_project) | **POST** /projects | Create Project
[**delete_git_branch**](ProjectApi.md#delete_git_branch) | **DELETE** /projects/{project_id}/git_branch/{branch_name} | Delete a Git Branch
[**find_git_branch**](ProjectApi.md#find_git_branch) | **GET** /projects/{project_id}/git_branch/{branch_name} | Find a Git Branch
[**git_branch**](ProjectApi.md#git_branch) | **GET** /projects/{project_id}/git_branch | Get Active Git Branch
[**git_deploy_key**](ProjectApi.md#git_deploy_key) | **GET** /projects/{project_id}/git/deploy_key | Git Deploy Key
[**project**](ProjectApi.md#project) | **GET** /projects/{project_id} | Get Project
[**project_file**](ProjectApi.md#project_file) | **GET** /projects/{project_id}/files/file | Get Project File
[**project_validation_results**](ProjectApi.md#project_validation_results) | **GET** /projects/{project_id}/validate | Cached Project Validation Results
[**project_workspace**](ProjectApi.md#project_workspace) | **GET** /projects/{project_id}/current_workspace | Get Project Workspace
[**reset_project_to_production**](ProjectApi.md#reset_project_to_production) | **POST** /projects/{project_id}/reset_to_production | Reset To Production
[**reset_project_to_remote**](ProjectApi.md#reset_project_to_remote) | **POST** /projects/{project_id}/reset_to_remote | Reset To Remote
[**run_git_connection_test**](ProjectApi.md#run_git_connection_test) | **GET** /projects/{project_id}/git_connection_tests/{test_id} | Run Git Connection Test
[**update_git_branch**](ProjectApi.md#update_git_branch) | **PUT** /projects/{project_id}/git_branch | Update Project Git Branch
[**update_project**](ProjectApi.md#update_project) | **PATCH** /projects/{project_id} | Update Project
[**validate_project**](ProjectApi.md#validate_project) | **POST** /projects/{project_id}/validate | Validate Project


# **all_git_branches**
> list[GitBranch] all_git_branches(project_id)

Get All Git Branches

### Get All Git Branches  Returns a list of git branches in the project repository 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id

try:
    # Get All Git Branches
    api_response = api_instance.all_git_branches(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->all_git_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[GitBranch]**](GitBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_git_connection_tests**
> list[GitConnectionTest] all_git_connection_tests(project_id)

Get All Git Connection Tests

### Get All Git Connection Tests  Returns a list of tests which can be run against a project's git connection. Call [Run Git Connection Test](#!/Project/run_git_connection_test) to execute each test in sequence.  Tests are ordered by increasing specificity. Tests should be run in the order returned because later tests require functionality tested by tests earlier in the test list.  For example, a late-stage test for write access is meaningless if connecting to the git server (an early test) is failing. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id

try:
    # Get All Git Connection Tests
    api_response = api_instance.all_git_connection_tests(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->all_git_connection_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[GitConnectionTest]**](GitConnectionTest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_project_files**
> list[ProjectFile] all_project_files(project_id, fields=fields)

Get All Project Files

### Get All Project Files  Returns a list of the files in the project 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Get All Project Files
    api_response = api_instance.all_project_files(project_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->all_project_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**list[ProjectFile]**](ProjectFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_projects**
> list[Project] all_projects(fields=fields)

Get All Projects

### Get All Projects  Returns all projects visible to the current user 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Get All Projects
    api_response = api_instance.all_projects(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->all_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_git_branch**
> GitBranch create_git_branch(project_id, body=body)

Checkout New Git Branch

### Create and Checkout a Git Branch  Creates and checks out a new branch in the given project repository Only allowed in development mode   - Call `update_session` to select the 'dev' workspace.  Optionally specify a branch name, tag name or commit SHA as the start point in the ref field.   If no ref is specified, HEAD of the current branch will be used as the start point for the new branch.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
body = swagger_client.GitBranch() # GitBranch | Git Branch (optional)

try:
    # Checkout New Git Branch
    api_response = api_instance.create_git_branch(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_git_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **body** | [**GitBranch**](GitBranch.md)| Git Branch | [optional] 

### Return type

[**GitBranch**](GitBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_git_deploy_key**
> str create_git_deploy_key(project_id)

Create Deploy Key

### Create Git Deploy Key  Create a public/private key pair for authenticating ssh git requests from Looker to a remote git repository for a particular Looker project.  Returns the public key of the generated ssh key pair.  Copy this public key to your remote git repository's ssh keys configuration so that the remote git service can validate and accept git requests from the Looker server. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id

try:
    # Create Deploy Key
    api_response = api_instance.create_git_deploy_key(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_git_deploy_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(body=body)

Create Project

### Create A Project  dev mode required. - Call `update_session` to select the 'dev' workspace.  `name` is required. `git_remote_url` is not allowed. To configure Git for the newly created project, follow the instructions in `update_project`.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.Project() # Project | Project (optional)

try:
    # Create Project
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Project**](Project.md)| Project | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_git_branch**
> str delete_git_branch(project_id, branch_name)

Delete a Git Branch

### Delete the specified Git Branch  Delete git branch specified in branch_name path param from local and remote of specified project repository 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
branch_name = 'branch_name_example' # str | Branch Name

try:
    # Delete a Git Branch
    api_response = api_instance.delete_git_branch(project_id, branch_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_git_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **branch_name** | **str**| Branch Name | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_git_branch**
> GitBranch find_git_branch(project_id, branch_name)

Find a Git Branch

### Get the specified Git Branch  Returns the git branch specified in branch_name path param if it exists in the given project repository 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
branch_name = 'branch_name_example' # str | Branch Name

try:
    # Find a Git Branch
    api_response = api_instance.find_git_branch(project_id, branch_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->find_git_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **branch_name** | **str**| Branch Name | 

### Return type

[**GitBranch**](GitBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **git_branch**
> GitBranch git_branch(project_id)

Get Active Git Branch

### Get the Current Git Branch  Returns the git branch currently checked out in the given project repository 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id

try:
    # Get Active Git Branch
    api_response = api_instance.git_branch(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->git_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**GitBranch**](GitBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **git_deploy_key**
> str git_deploy_key(project_id)

Git Deploy Key

### Git Deploy Key  Returns the ssh public key previously created for a project's git repository. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id

try:
    # Git Deploy Key
    api_response = api_instance.git_deploy_key(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->git_deploy_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project**
> Project project(project_id, fields=fields)

Get Project

### Get A Project  Returns the project with the given project id 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Get Project
    api_response = api_instance.project(project_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_file**
> ProjectFile project_file(project_id, file_id, fields=fields)

Get Project File

### Get Project File Info  Returns information about a file in the project 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
file_id = 'file_id_example' # str | File Id
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Get Project File
    api_response = api_instance.project_file(project_id, file_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **file_id** | **str**| File Id | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_validation_results**
> ProjectValidationCache project_validation_results(project_id, fields=fields)

Cached Project Validation Results

### Get Cached Project Validation Results  Returns the cached results of a previous project validation calculation, if any. Returns http status 204 No Content if no validation results exist.  Validating the content of all the files in a project can be computationally intensive for large projects. Use this API to simply fetch the results of the most recent project validation rather than revalidating the entire project from scratch.  A value of `\"stale\": true` in the response indicates that the project has changed since the cached validation results were computed. The cached validation results may no longer reflect the current state of the project. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Cached Project Validation Results
    api_response = api_instance.project_validation_results(project_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project_validation_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**ProjectValidationCache**](ProjectValidationCache.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_workspace**
> ProjectWorkspace project_workspace(project_id, fields=fields)

Get Project Workspace

### Get Project Workspace  Returns information about the state of the project files in the currently selected workspace 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Get Project Workspace
    api_response = api_instance.project_workspace(project_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->project_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**ProjectWorkspace**](ProjectWorkspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_project_to_production**
> str reset_project_to_production(project_id)

Reset To Production

### Reset a project to the revision of the project that is in production.  **DANGER** this will delete any changes that have not been pushed to a remote repository. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Id of project

try:
    # Reset To Production
    api_response = api_instance.reset_project_to_production(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->reset_project_to_production: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of project | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_project_to_remote**
> str reset_project_to_remote(project_id)

Reset To Remote

### Reset a project development branch to the revision of the project that is on the remote.  **DANGER** this will delete any changes that have not been pushed to a remote repository. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Id of project

try:
    # Reset To Remote
    api_response = api_instance.reset_project_to_remote(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->reset_project_to_remote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of project | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_git_connection_test**
> GitConnectionTestResult run_git_connection_test(project_id, test_id)

Run Git Connection Test

### Run a git connection test  Run the named test on the git service used by this project and return the result. This is intended to help debug git connections when things do not work properly, to give more helpful information about why a git url is not working with Looker.  Tests should be run in the order they are returned by [Get All Git Connection Tests](#!/Project/all_git_connection_tests). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
test_id = 'test_id_example' # str | Test Id

try:
    # Run Git Connection Test
    api_response = api_instance.run_git_connection_test(project_id, test_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->run_git_connection_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **test_id** | **str**| Test Id | 

### Return type

[**GitConnectionTestResult**](GitConnectionTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_branch**
> GitBranch update_git_branch(project_id, body)

Update Project Git Branch

### Checkout and/or reset --hard an existing Git Branch  Only allowed in development mode   - Call `update_session` to select the 'dev' workspace.  Checkout an existing branch if name field is different from the name of the currently checked out branch.  Optionally specify a branch name, tag name or commit SHA to which the branch should be reset.   **DANGER** hard reset will be force pushed to the remote. Unsaved changes and commits may be permanently lost.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
body = swagger_client.GitBranch() # GitBranch | Git Branch

try:
    # Update Project Git Branch
    api_response = api_instance.update_git_branch(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_git_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **body** | [**GitBranch**](GitBranch.md)| Git Branch | 

### Return type

[**GitBranch**](GitBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(project_id, body, fields=fields)

Update Project

### Update Project Configuration  Apply changes to a project's configuration.   #### Configuring Git for a Project  To set up a Looker project with a remote git repository, follow these steps:  1. Call `update_session` to select the 'dev' workspace. 1. Call `create_git_deploy_key` to create a new deploy key for the project 1. Copy the deploy key text into the remote git repository's ssh key configuration 1. Call `update_project` to set project's `git_remote_url` ()and `git_service_name`, if necessary).  When you modify a project's `git_remote_url`, Looker connects to the remote repository to fetch metadata. The remote git repository MUST be configured with the Looker-generated deploy key for this project prior to setting the project's `git_remote_url`.  To set up a Looker project with a git repository residing on the Looker server (a 'bare' git repo): 1. Call `update_session` to select the 'dev' workspace. 1. Call `update_project` setting `git_remote_url` to nil and `git_service_name` to \"bare\".  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
body = swagger_client.Project() # Project | Project
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Update Project
    api_response = api_instance.update_project(project_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **body** | [**Project**](Project.md)| Project | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_project**
> ProjectValidation validate_project(project_id, fields=fields)

Validate Project

### Validate Project  Performs lint validation of all lookml files in the project. Returns a list of errors found, if any.  Validating the content of all the files in a project can be computationally intensive for large projects. For best performance, call `validate_project(project_id)` only when you really want to recompute project validation. To quickly display the results of the most recent project validation (without recomputing), use `project_validation_results(project_id)` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_id = 'project_id_example' # str | Project Id
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Validate Project
    api_response = api_instance.validate_project(project_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->validate_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**ProjectValidation**](ProjectValidation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

