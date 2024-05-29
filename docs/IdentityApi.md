# ahvac.IdentityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alias_create**](IdentityApi.md#alias_create) | **POST** /identity/alias | Create a new alias.
[**alias_delete_by_id**](IdentityApi.md#alias_delete_by_id) | **DELETE** /identity/alias/id/{id} | 
[**alias_list_by_id**](IdentityApi.md#alias_list_by_id) | **GET** /identity/alias/id/ | List all the alias IDs.
[**alias_read_by_id**](IdentityApi.md#alias_read_by_id) | **GET** /identity/alias/id/{id} | 
[**alias_update_by_id**](IdentityApi.md#alias_update_by_id) | **POST** /identity/alias/id/{id} | 
[**entity_batch_delete**](IdentityApi.md#entity_batch_delete) | **POST** /identity/entity/batch-delete | Delete all of the entities provided
[**entity_create**](IdentityApi.md#entity_create) | **POST** /identity/entity | Create a new entity
[**entity_create_alias**](IdentityApi.md#entity_create_alias) | **POST** /identity/entity-alias | Create a new alias.
[**entity_delete_alias_by_id**](IdentityApi.md#entity_delete_alias_by_id) | **DELETE** /identity/entity-alias/id/{id} | 
[**entity_delete_by_id**](IdentityApi.md#entity_delete_by_id) | **DELETE** /identity/entity/id/{id} | 
[**entity_delete_by_name**](IdentityApi.md#entity_delete_by_name) | **DELETE** /identity/entity/name/{name} | 
[**entity_list_aliases_by_id**](IdentityApi.md#entity_list_aliases_by_id) | **GET** /identity/entity-alias/id/ | List all the alias IDs.
[**entity_list_by_id**](IdentityApi.md#entity_list_by_id) | **GET** /identity/entity/id/ | List all the entity IDs
[**entity_list_by_name**](IdentityApi.md#entity_list_by_name) | **GET** /identity/entity/name/ | List all the entity names
[**entity_look_up**](IdentityApi.md#entity_look_up) | **POST** /identity/lookup/entity | Query entities based on various properties.
[**entity_merge**](IdentityApi.md#entity_merge) | **POST** /identity/entity/merge | Merge two or more entities together
[**entity_read_alias_by_id**](IdentityApi.md#entity_read_alias_by_id) | **GET** /identity/entity-alias/id/{id} | 
[**entity_read_by_id**](IdentityApi.md#entity_read_by_id) | **GET** /identity/entity/id/{id} | 
[**entity_read_by_name**](IdentityApi.md#entity_read_by_name) | **GET** /identity/entity/name/{name} | 
[**entity_update_alias_by_id**](IdentityApi.md#entity_update_alias_by_id) | **POST** /identity/entity-alias/id/{id} | 
[**entity_update_by_id**](IdentityApi.md#entity_update_by_id) | **POST** /identity/entity/id/{id} | 
[**entity_update_by_name**](IdentityApi.md#entity_update_by_name) | **POST** /identity/entity/name/{name} | 
[**group_create**](IdentityApi.md#group_create) | **POST** /identity/group | 
[**group_create_alias**](IdentityApi.md#group_create_alias) | **POST** /identity/group-alias | Creates a new group alias, or updates an existing one.
[**group_delete_alias_by_id**](IdentityApi.md#group_delete_alias_by_id) | **DELETE** /identity/group-alias/id/{id} | 
[**group_delete_by_id**](IdentityApi.md#group_delete_by_id) | **DELETE** /identity/group/id/{id} | 
[**group_delete_by_name**](IdentityApi.md#group_delete_by_name) | **DELETE** /identity/group/name/{name} | 
[**group_list_aliases_by_id**](IdentityApi.md#group_list_aliases_by_id) | **GET** /identity/group-alias/id/ | List all the group alias IDs.
[**group_list_by_id**](IdentityApi.md#group_list_by_id) | **GET** /identity/group/id/ | List all the group IDs.
[**group_list_by_name**](IdentityApi.md#group_list_by_name) | **GET** /identity/group/name/ | 
[**group_look_up**](IdentityApi.md#group_look_up) | **POST** /identity/lookup/group | Query groups based on various properties.
[**group_read_alias_by_id**](IdentityApi.md#group_read_alias_by_id) | **GET** /identity/group-alias/id/{id} | 
[**group_read_by_id**](IdentityApi.md#group_read_by_id) | **GET** /identity/group/id/{id} | 
[**group_read_by_name**](IdentityApi.md#group_read_by_name) | **GET** /identity/group/name/{name} | 
[**group_update_alias_by_id**](IdentityApi.md#group_update_alias_by_id) | **POST** /identity/group-alias/id/{id} | 
[**group_update_by_id**](IdentityApi.md#group_update_by_id) | **POST** /identity/group/id/{id} | 
[**group_update_by_name**](IdentityApi.md#group_update_by_name) | **POST** /identity/group/name/{name} | 
[**mfa_admin_destroy_totp_secret**](IdentityApi.md#mfa_admin_destroy_totp_secret) | **POST** /identity/mfa/method/totp/admin-destroy | Destroys a TOTP secret for the given MFA method ID on the given entity
[**mfa_admin_generate_totp_secret**](IdentityApi.md#mfa_admin_generate_totp_secret) | **POST** /identity/mfa/method/totp/admin-generate | Update or create TOTP secret for the given method ID on the given entity.
[**mfa_create_duo_method**](IdentityApi.md#mfa_create_duo_method) | **POST** /identity/mfa/method/duo | Create the given MFA method
[**mfa_create_okta_method**](IdentityApi.md#mfa_create_okta_method) | **POST** /identity/mfa/method/okta | Create the given MFA method
[**mfa_create_ping_id_method**](IdentityApi.md#mfa_create_ping_id_method) | **POST** /identity/mfa/method/pingid | Create the given MFA method
[**mfa_create_totp_method**](IdentityApi.md#mfa_create_totp_method) | **POST** /identity/mfa/method/totp | Create the given MFA method
[**mfa_delete_duo_method**](IdentityApi.md#mfa_delete_duo_method) | **DELETE** /identity/mfa/method/duo/{method_id} | Delete the given MFA method
[**mfa_delete_login_enforcement**](IdentityApi.md#mfa_delete_login_enforcement) | **DELETE** /identity/mfa/login-enforcement/{name} | Delete a login enforcement
[**mfa_delete_okta_method**](IdentityApi.md#mfa_delete_okta_method) | **DELETE** /identity/mfa/method/okta/{method_id} | Delete the given MFA method
[**mfa_delete_ping_id_method**](IdentityApi.md#mfa_delete_ping_id_method) | **DELETE** /identity/mfa/method/pingid/{method_id} | Delete the given MFA method
[**mfa_delete_totp_method**](IdentityApi.md#mfa_delete_totp_method) | **DELETE** /identity/mfa/method/totp/{method_id} | Delete the given MFA method
[**mfa_generate_totp_secret**](IdentityApi.md#mfa_generate_totp_secret) | **POST** /identity/mfa/method/totp/generate | Update or create TOTP secret for the given method ID on the given entity.
[**mfa_list_duo_methods**](IdentityApi.md#mfa_list_duo_methods) | **GET** /identity/mfa/method/duo/ | List MFA method configurations for the given MFA method
[**mfa_list_login_enforcements**](IdentityApi.md#mfa_list_login_enforcements) | **GET** /identity/mfa/login-enforcement/ | List login enforcements
[**mfa_list_methods**](IdentityApi.md#mfa_list_methods) | **GET** /identity/mfa/method/ | List MFA method configurations for all MFA methods
[**mfa_list_okta_methods**](IdentityApi.md#mfa_list_okta_methods) | **GET** /identity/mfa/method/okta/ | List MFA method configurations for the given MFA method
[**mfa_list_ping_id_methods**](IdentityApi.md#mfa_list_ping_id_methods) | **GET** /identity/mfa/method/pingid/ | List MFA method configurations for the given MFA method
[**mfa_list_totp_methods**](IdentityApi.md#mfa_list_totp_methods) | **GET** /identity/mfa/method/totp/ | List MFA method configurations for the given MFA method
[**mfa_read_duo_method**](IdentityApi.md#mfa_read_duo_method) | **GET** /identity/mfa/method/duo/{method_id} | Read the current configuration for the given MFA method
[**mfa_read_login_enforcement**](IdentityApi.md#mfa_read_login_enforcement) | **GET** /identity/mfa/login-enforcement/{name} | Read the current login enforcement
[**mfa_read_method**](IdentityApi.md#mfa_read_method) | **GET** /identity/mfa/method/{method_id} | Read the current configuration for the given ID regardless of the MFA method type
[**mfa_read_okta_method**](IdentityApi.md#mfa_read_okta_method) | **GET** /identity/mfa/method/okta/{method_id} | Read the current configuration for the given MFA method
[**mfa_read_ping_id_method**](IdentityApi.md#mfa_read_ping_id_method) | **GET** /identity/mfa/method/pingid/{method_id} | Read the current configuration for the given MFA method
[**mfa_read_totp_method**](IdentityApi.md#mfa_read_totp_method) | **GET** /identity/mfa/method/totp/{method_id} | Read the current configuration for the given MFA method
[**mfa_update_duo_method**](IdentityApi.md#mfa_update_duo_method) | **POST** /identity/mfa/method/duo/{method_id} | Update the configuration for the given MFA method
[**mfa_update_okta_method**](IdentityApi.md#mfa_update_okta_method) | **POST** /identity/mfa/method/okta/{method_id} | Update the configuration for the given MFA method
[**mfa_update_ping_id_method**](IdentityApi.md#mfa_update_ping_id_method) | **POST** /identity/mfa/method/pingid/{method_id} | Update the configuration for the given MFA method
[**mfa_update_totp_method**](IdentityApi.md#mfa_update_totp_method) | **POST** /identity/mfa/method/totp/{method_id} | Update the configuration for the given MFA method
[**mfa_write_login_enforcement**](IdentityApi.md#mfa_write_login_enforcement) | **POST** /identity/mfa/login-enforcement/{name} | Create or update a login enforcement
[**oidc_configure**](IdentityApi.md#oidc_configure) | **POST** /identity/oidc/config | 
[**oidc_delete_assignment**](IdentityApi.md#oidc_delete_assignment) | **DELETE** /identity/oidc/assignment/{name} | 
[**oidc_delete_client**](IdentityApi.md#oidc_delete_client) | **DELETE** /identity/oidc/client/{name} | 
[**oidc_delete_key**](IdentityApi.md#oidc_delete_key) | **DELETE** /identity/oidc/key/{name} | CRUD operations for OIDC keys.
[**oidc_delete_provider**](IdentityApi.md#oidc_delete_provider) | **DELETE** /identity/oidc/provider/{name} | 
[**oidc_delete_role**](IdentityApi.md#oidc_delete_role) | **DELETE** /identity/oidc/role/{name} | CRUD operations on OIDC Roles
[**oidc_delete_scope**](IdentityApi.md#oidc_delete_scope) | **DELETE** /identity/oidc/scope/{name} | 
[**oidc_generate_token**](IdentityApi.md#oidc_generate_token) | **GET** /identity/oidc/token/{name} | Generate an OIDC token
[**oidc_introspect**](IdentityApi.md#oidc_introspect) | **POST** /identity/oidc/introspect | Verify the authenticity of an OIDC token
[**oidc_list_assignments**](IdentityApi.md#oidc_list_assignments) | **GET** /identity/oidc/assignment/ | 
[**oidc_list_clients**](IdentityApi.md#oidc_list_clients) | **GET** /identity/oidc/client/ | 
[**oidc_list_keys**](IdentityApi.md#oidc_list_keys) | **GET** /identity/oidc/key/ | List OIDC keys
[**oidc_list_providers**](IdentityApi.md#oidc_list_providers) | **GET** /identity/oidc/provider/ | 
[**oidc_list_roles**](IdentityApi.md#oidc_list_roles) | **GET** /identity/oidc/role/ | List configured OIDC roles
[**oidc_list_scopes**](IdentityApi.md#oidc_list_scopes) | **GET** /identity/oidc/scope/ | 
[**oidc_provider_authorize**](IdentityApi.md#oidc_provider_authorize) | **GET** /identity/oidc/provider/{name}/authorize | 
[**oidc_provider_authorize_with_parameters**](IdentityApi.md#oidc_provider_authorize_with_parameters) | **POST** /identity/oidc/provider/{name}/authorize | 
[**oidc_provider_token**](IdentityApi.md#oidc_provider_token) | **POST** /identity/oidc/provider/{name}/token | 
[**oidc_provider_user_info**](IdentityApi.md#oidc_provider_user_info) | **GET** /identity/oidc/provider/{name}/userinfo | 
[**oidc_provider_user_info2**](IdentityApi.md#oidc_provider_user_info2) | **POST** /identity/oidc/provider/{name}/userinfo | 
[**oidc_read_assignment**](IdentityApi.md#oidc_read_assignment) | **GET** /identity/oidc/assignment/{name} | 
[**oidc_read_client**](IdentityApi.md#oidc_read_client) | **GET** /identity/oidc/client/{name} | 
[**oidc_read_configuration**](IdentityApi.md#oidc_read_configuration) | **GET** /identity/oidc/config | 
[**oidc_read_key**](IdentityApi.md#oidc_read_key) | **GET** /identity/oidc/key/{name} | CRUD operations for OIDC keys.
[**oidc_read_open_id_configuration**](IdentityApi.md#oidc_read_open_id_configuration) | **GET** /identity/oidc/.well-known/openid-configuration | Query OIDC configurations
[**oidc_read_provider**](IdentityApi.md#oidc_read_provider) | **GET** /identity/oidc/provider/{name} | 
[**oidc_read_provider_open_id_configuration**](IdentityApi.md#oidc_read_provider_open_id_configuration) | **GET** /identity/oidc/provider/{name}/.well-known/openid-configuration | 
[**oidc_read_provider_public_keys**](IdentityApi.md#oidc_read_provider_public_keys) | **GET** /identity/oidc/provider/{name}/.well-known/keys | 
[**oidc_read_public_keys**](IdentityApi.md#oidc_read_public_keys) | **GET** /identity/oidc/.well-known/keys | Retrieve public keys
[**oidc_read_role**](IdentityApi.md#oidc_read_role) | **GET** /identity/oidc/role/{name} | CRUD operations on OIDC Roles
[**oidc_read_scope**](IdentityApi.md#oidc_read_scope) | **GET** /identity/oidc/scope/{name} | 
[**oidc_rotate_key**](IdentityApi.md#oidc_rotate_key) | **POST** /identity/oidc/key/{name}/rotate | Rotate a named OIDC key.
[**oidc_write_assignment**](IdentityApi.md#oidc_write_assignment) | **POST** /identity/oidc/assignment/{name} | 
[**oidc_write_client**](IdentityApi.md#oidc_write_client) | **POST** /identity/oidc/client/{name} | 
[**oidc_write_key**](IdentityApi.md#oidc_write_key) | **POST** /identity/oidc/key/{name} | CRUD operations for OIDC keys.
[**oidc_write_provider**](IdentityApi.md#oidc_write_provider) | **POST** /identity/oidc/provider/{name} | 
[**oidc_write_role**](IdentityApi.md#oidc_write_role) | **POST** /identity/oidc/role/{name} | CRUD operations on OIDC Roles
[**oidc_write_scope**](IdentityApi.md#oidc_write_scope) | **POST** /identity/oidc/scope/{name} | 
[**persona_create**](IdentityApi.md#persona_create) | **POST** /identity/persona | Create a new alias.
[**persona_delete_by_id**](IdentityApi.md#persona_delete_by_id) | **DELETE** /identity/persona/id/{id} | 
[**persona_list_by_id**](IdentityApi.md#persona_list_by_id) | **GET** /identity/persona/id/ | List all the alias IDs.
[**persona_read_by_id**](IdentityApi.md#persona_read_by_id) | **GET** /identity/persona/id/{id} | 
[**persona_update_by_id**](IdentityApi.md#persona_update_by_id) | **POST** /identity/persona/id/{id} | 


# **alias_create**
> alias_create(alias_create_request)

Create a new alias.

### Example


```python
import ahvac
from ahvac.models.alias_create_request import AliasCreateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    alias_create_request = ahvac.AliasCreateRequest() # AliasCreateRequest | 

    try:
        # Create a new alias.
        await api_instance.alias_create(alias_create_request)
    except Exception as e:
        print("Exception when calling IdentityApi->alias_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias_create_request** | [**AliasCreateRequest**](AliasCreateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alias_delete_by_id**
> alias_delete_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the alias

    try:
        await api_instance.alias_delete_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->alias_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alias_list_by_id**
> StandardListResponse alias_list_by_id(list)

List all the alias IDs.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List all the alias IDs.
        api_response = await api_instance.alias_list_by_id(list)
        print("The response of IdentityApi->alias_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->alias_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alias_read_by_id**
> alias_read_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the alias

    try:
        await api_instance.alias_read_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->alias_read_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alias_update_by_id**
> alias_update_by_id(id, alias_update_by_id_request)



### Example


```python
import ahvac
from ahvac.models.alias_update_by_id_request import AliasUpdateByIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the alias
    alias_update_by_id_request = ahvac.AliasUpdateByIdRequest() # AliasUpdateByIdRequest | 

    try:
        await api_instance.alias_update_by_id(id, alias_update_by_id_request)
    except Exception as e:
        print("Exception when calling IdentityApi->alias_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 
 **alias_update_by_id_request** | [**AliasUpdateByIdRequest**](AliasUpdateByIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_batch_delete**
> entity_batch_delete(entity_batch_delete_request)

Delete all of the entities provided

### Example


```python
import ahvac
from ahvac.models.entity_batch_delete_request import EntityBatchDeleteRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    entity_batch_delete_request = ahvac.EntityBatchDeleteRequest() # EntityBatchDeleteRequest | 

    try:
        # Delete all of the entities provided
        await api_instance.entity_batch_delete(entity_batch_delete_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_batch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_batch_delete_request** | [**EntityBatchDeleteRequest**](EntityBatchDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_create**
> entity_create(entity_create_request)

Create a new entity

### Example


```python
import ahvac
from ahvac.models.entity_create_request import EntityCreateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    entity_create_request = ahvac.EntityCreateRequest() # EntityCreateRequest | 

    try:
        # Create a new entity
        await api_instance.entity_create(entity_create_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_create_request** | [**EntityCreateRequest**](EntityCreateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_create_alias**
> entity_create_alias(entity_create_alias_request)

Create a new alias.

### Example


```python
import ahvac
from ahvac.models.entity_create_alias_request import EntityCreateAliasRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    entity_create_alias_request = ahvac.EntityCreateAliasRequest() # EntityCreateAliasRequest | 

    try:
        # Create a new alias.
        await api_instance.entity_create_alias(entity_create_alias_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_create_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_create_alias_request** | [**EntityCreateAliasRequest**](EntityCreateAliasRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_delete_alias_by_id**
> entity_delete_alias_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the alias

    try:
        await api_instance.entity_delete_alias_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_delete_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_delete_by_id**
> entity_delete_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the entity. If set, updates the corresponding existing entity.

    try:
        await api_instance.entity_delete_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the entity. If set, updates the corresponding existing entity. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_delete_by_name**
> entity_delete_by_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the entity

    try:
        await api_instance.entity_delete_by_name(name)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_delete_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the entity | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_list_aliases_by_id**
> StandardListResponse entity_list_aliases_by_id(list)

List all the alias IDs.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List all the alias IDs.
        api_response = await api_instance.entity_list_aliases_by_id(list)
        print("The response of IdentityApi->entity_list_aliases_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_list_aliases_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_list_by_id**
> StandardListResponse entity_list_by_id(list)

List all the entity IDs

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List all the entity IDs
        api_response = await api_instance.entity_list_by_id(list)
        print("The response of IdentityApi->entity_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_list_by_name**
> StandardListResponse entity_list_by_name(list)

List all the entity names

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List all the entity names
        api_response = await api_instance.entity_list_by_name(list)
        print("The response of IdentityApi->entity_list_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_list_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_look_up**
> entity_look_up(entity_look_up_request)

Query entities based on various properties.

### Example


```python
import ahvac
from ahvac.models.entity_look_up_request import EntityLookUpRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    entity_look_up_request = ahvac.EntityLookUpRequest() # EntityLookUpRequest | 

    try:
        # Query entities based on various properties.
        await api_instance.entity_look_up(entity_look_up_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_look_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_look_up_request** | [**EntityLookUpRequest**](EntityLookUpRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_merge**
> entity_merge(entity_merge_request)

Merge two or more entities together

### Example


```python
import ahvac
from ahvac.models.entity_merge_request import EntityMergeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    entity_merge_request = ahvac.EntityMergeRequest() # EntityMergeRequest | 

    try:
        # Merge two or more entities together
        await api_instance.entity_merge(entity_merge_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_merge_request** | [**EntityMergeRequest**](EntityMergeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_read_alias_by_id**
> entity_read_alias_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the alias

    try:
        await api_instance.entity_read_alias_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_read_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_read_by_id**
> entity_read_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the entity. If set, updates the corresponding existing entity.

    try:
        await api_instance.entity_read_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_read_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the entity. If set, updates the corresponding existing entity. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_read_by_name**
> entity_read_by_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the entity

    try:
        await api_instance.entity_read_by_name(name)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_read_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the entity | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_update_alias_by_id**
> entity_update_alias_by_id(id, entity_update_alias_by_id_request)



### Example


```python
import ahvac
from ahvac.models.entity_update_alias_by_id_request import EntityUpdateAliasByIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the alias
    entity_update_alias_by_id_request = ahvac.EntityUpdateAliasByIdRequest() # EntityUpdateAliasByIdRequest | 

    try:
        await api_instance.entity_update_alias_by_id(id, entity_update_alias_by_id_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_update_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 
 **entity_update_alias_by_id_request** | [**EntityUpdateAliasByIdRequest**](EntityUpdateAliasByIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_update_by_id**
> entity_update_by_id(id, entity_update_by_id_request)



### Example


```python
import ahvac
from ahvac.models.entity_update_by_id_request import EntityUpdateByIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the entity. If set, updates the corresponding existing entity.
    entity_update_by_id_request = ahvac.EntityUpdateByIdRequest() # EntityUpdateByIdRequest | 

    try:
        await api_instance.entity_update_by_id(id, entity_update_by_id_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the entity. If set, updates the corresponding existing entity. | 
 **entity_update_by_id_request** | [**EntityUpdateByIdRequest**](EntityUpdateByIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_update_by_name**
> entity_update_by_name(name, entity_update_by_name_request)



### Example


```python
import ahvac
from ahvac.models.entity_update_by_name_request import EntityUpdateByNameRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the entity
    entity_update_by_name_request = ahvac.EntityUpdateByNameRequest() # EntityUpdateByNameRequest | 

    try:
        await api_instance.entity_update_by_name(name, entity_update_by_name_request)
    except Exception as e:
        print("Exception when calling IdentityApi->entity_update_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the entity | 
 **entity_update_by_name_request** | [**EntityUpdateByNameRequest**](EntityUpdateByNameRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_create**
> group_create(group_create_request)



### Example


```python
import ahvac
from ahvac.models.group_create_request import GroupCreateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    group_create_request = ahvac.GroupCreateRequest() # GroupCreateRequest | 

    try:
        await api_instance.group_create(group_create_request)
    except Exception as e:
        print("Exception when calling IdentityApi->group_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_create_request** | [**GroupCreateRequest**](GroupCreateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_create_alias**
> group_create_alias(group_create_alias_request)

Creates a new group alias, or updates an existing one.

### Example


```python
import ahvac
from ahvac.models.group_create_alias_request import GroupCreateAliasRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    group_create_alias_request = ahvac.GroupCreateAliasRequest() # GroupCreateAliasRequest | 

    try:
        # Creates a new group alias, or updates an existing one.
        await api_instance.group_create_alias(group_create_alias_request)
    except Exception as e:
        print("Exception when calling IdentityApi->group_create_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_create_alias_request** | [**GroupCreateAliasRequest**](GroupCreateAliasRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete_alias_by_id**
> group_delete_alias_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the group alias.

    try:
        await api_instance.group_delete_alias_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->group_delete_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group alias. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete_by_id**
> group_delete_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the group. If set, updates the corresponding existing group.

    try:
        await api_instance.group_delete_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->group_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group. If set, updates the corresponding existing group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete_by_name**
> group_delete_by_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the group.

    try:
        await api_instance.group_delete_by_name(name)
    except Exception as e:
        print("Exception when calling IdentityApi->group_delete_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_list_aliases_by_id**
> StandardListResponse group_list_aliases_by_id(list)

List all the group alias IDs.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List all the group alias IDs.
        api_response = await api_instance.group_list_aliases_by_id(list)
        print("The response of IdentityApi->group_list_aliases_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->group_list_aliases_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_list_by_id**
> StandardListResponse group_list_by_id(list)

List all the group IDs.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List all the group IDs.
        api_response = await api_instance.group_list_by_id(list)
        print("The response of IdentityApi->group_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->group_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_list_by_name**
> StandardListResponse group_list_by_name(list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.group_list_by_name(list)
        print("The response of IdentityApi->group_list_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->group_list_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_look_up**
> group_look_up(group_look_up_request)

Query groups based on various properties.

### Example


```python
import ahvac
from ahvac.models.group_look_up_request import GroupLookUpRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    group_look_up_request = ahvac.GroupLookUpRequest() # GroupLookUpRequest | 

    try:
        # Query groups based on various properties.
        await api_instance.group_look_up(group_look_up_request)
    except Exception as e:
        print("Exception when calling IdentityApi->group_look_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_look_up_request** | [**GroupLookUpRequest**](GroupLookUpRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_read_alias_by_id**
> group_read_alias_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the group alias.

    try:
        await api_instance.group_read_alias_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->group_read_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group alias. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_read_by_id**
> group_read_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the group. If set, updates the corresponding existing group.

    try:
        await api_instance.group_read_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->group_read_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group. If set, updates the corresponding existing group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_read_by_name**
> group_read_by_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the group.

    try:
        await api_instance.group_read_by_name(name)
    except Exception as e:
        print("Exception when calling IdentityApi->group_read_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_update_alias_by_id**
> group_update_alias_by_id(id, group_update_alias_by_id_request)



### Example


```python
import ahvac
from ahvac.models.group_update_alias_by_id_request import GroupUpdateAliasByIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the group alias.
    group_update_alias_by_id_request = ahvac.GroupUpdateAliasByIdRequest() # GroupUpdateAliasByIdRequest | 

    try:
        await api_instance.group_update_alias_by_id(id, group_update_alias_by_id_request)
    except Exception as e:
        print("Exception when calling IdentityApi->group_update_alias_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group alias. | 
 **group_update_alias_by_id_request** | [**GroupUpdateAliasByIdRequest**](GroupUpdateAliasByIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_update_by_id**
> group_update_by_id(id, group_update_by_id_request)



### Example


```python
import ahvac
from ahvac.models.group_update_by_id_request import GroupUpdateByIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the group. If set, updates the corresponding existing group.
    group_update_by_id_request = ahvac.GroupUpdateByIdRequest() # GroupUpdateByIdRequest | 

    try:
        await api_instance.group_update_by_id(id, group_update_by_id_request)
    except Exception as e:
        print("Exception when calling IdentityApi->group_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group. If set, updates the corresponding existing group. | 
 **group_update_by_id_request** | [**GroupUpdateByIdRequest**](GroupUpdateByIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_update_by_name**
> group_update_by_name(name, group_update_by_name_request)



### Example


```python
import ahvac
from ahvac.models.group_update_by_name_request import GroupUpdateByNameRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the group.
    group_update_by_name_request = ahvac.GroupUpdateByNameRequest() # GroupUpdateByNameRequest | 

    try:
        await api_instance.group_update_by_name(name, group_update_by_name_request)
    except Exception as e:
        print("Exception when calling IdentityApi->group_update_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the group. | 
 **group_update_by_name_request** | [**GroupUpdateByNameRequest**](GroupUpdateByNameRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_admin_destroy_totp_secret**
> mfa_admin_destroy_totp_secret(mfa_admin_destroy_totp_secret_request)

Destroys a TOTP secret for the given MFA method ID on the given entity

### Example


```python
import ahvac
from ahvac.models.mfa_admin_destroy_totp_secret_request import MfaAdminDestroyTotpSecretRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    mfa_admin_destroy_totp_secret_request = ahvac.MfaAdminDestroyTotpSecretRequest() # MfaAdminDestroyTotpSecretRequest | 

    try:
        # Destroys a TOTP secret for the given MFA method ID on the given entity
        await api_instance.mfa_admin_destroy_totp_secret(mfa_admin_destroy_totp_secret_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_admin_destroy_totp_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_admin_destroy_totp_secret_request** | [**MfaAdminDestroyTotpSecretRequest**](MfaAdminDestroyTotpSecretRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_admin_generate_totp_secret**
> mfa_admin_generate_totp_secret(mfa_admin_generate_totp_secret_request)

Update or create TOTP secret for the given method ID on the given entity.

### Example


```python
import ahvac
from ahvac.models.mfa_admin_generate_totp_secret_request import MfaAdminGenerateTotpSecretRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    mfa_admin_generate_totp_secret_request = ahvac.MfaAdminGenerateTotpSecretRequest() # MfaAdminGenerateTotpSecretRequest | 

    try:
        # Update or create TOTP secret for the given method ID on the given entity.
        await api_instance.mfa_admin_generate_totp_secret(mfa_admin_generate_totp_secret_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_admin_generate_totp_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_admin_generate_totp_secret_request** | [**MfaAdminGenerateTotpSecretRequest**](MfaAdminGenerateTotpSecretRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_create_duo_method**
> mfa_create_duo_method(mfa_create_duo_method_request)

Create the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_create_duo_method_request import MfaCreateDuoMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    mfa_create_duo_method_request = ahvac.MfaCreateDuoMethodRequest() # MfaCreateDuoMethodRequest | 

    try:
        # Create the given MFA method
        await api_instance.mfa_create_duo_method(mfa_create_duo_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_create_duo_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_create_duo_method_request** | [**MfaCreateDuoMethodRequest**](MfaCreateDuoMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_create_okta_method**
> mfa_create_okta_method(mfa_create_okta_method_request)

Create the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_create_okta_method_request import MfaCreateOktaMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    mfa_create_okta_method_request = ahvac.MfaCreateOktaMethodRequest() # MfaCreateOktaMethodRequest | 

    try:
        # Create the given MFA method
        await api_instance.mfa_create_okta_method(mfa_create_okta_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_create_okta_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_create_okta_method_request** | [**MfaCreateOktaMethodRequest**](MfaCreateOktaMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_create_ping_id_method**
> mfa_create_ping_id_method(mfa_create_ping_id_method_request)

Create the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_create_ping_id_method_request import MfaCreatePingIdMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    mfa_create_ping_id_method_request = ahvac.MfaCreatePingIdMethodRequest() # MfaCreatePingIdMethodRequest | 

    try:
        # Create the given MFA method
        await api_instance.mfa_create_ping_id_method(mfa_create_ping_id_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_create_ping_id_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_create_ping_id_method_request** | [**MfaCreatePingIdMethodRequest**](MfaCreatePingIdMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_create_totp_method**
> mfa_create_totp_method(mfa_create_totp_method_request)

Create the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_create_totp_method_request import MfaCreateTotpMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    mfa_create_totp_method_request = ahvac.MfaCreateTotpMethodRequest() # MfaCreateTotpMethodRequest | 

    try:
        # Create the given MFA method
        await api_instance.mfa_create_totp_method(mfa_create_totp_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_create_totp_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_create_totp_method_request** | [**MfaCreateTotpMethodRequest**](MfaCreateTotpMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_delete_duo_method**
> mfa_delete_duo_method(method_id)

Delete the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Delete the given MFA method
        await api_instance.mfa_delete_duo_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_delete_duo_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_delete_login_enforcement**
> mfa_delete_login_enforcement(name)

Delete a login enforcement

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name for this login enforcement configuration

    try:
        # Delete a login enforcement
        await api_instance.mfa_delete_login_enforcement(name)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_delete_login_enforcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for this login enforcement configuration | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_delete_okta_method**
> mfa_delete_okta_method(method_id)

Delete the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Delete the given MFA method
        await api_instance.mfa_delete_okta_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_delete_okta_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_delete_ping_id_method**
> mfa_delete_ping_id_method(method_id)

Delete the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Delete the given MFA method
        await api_instance.mfa_delete_ping_id_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_delete_ping_id_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_delete_totp_method**
> mfa_delete_totp_method(method_id)

Delete the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Delete the given MFA method
        await api_instance.mfa_delete_totp_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_delete_totp_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_generate_totp_secret**
> mfa_generate_totp_secret(mfa_generate_totp_secret_request)

Update or create TOTP secret for the given method ID on the given entity.

### Example


```python
import ahvac
from ahvac.models.mfa_generate_totp_secret_request import MfaGenerateTotpSecretRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    mfa_generate_totp_secret_request = ahvac.MfaGenerateTotpSecretRequest() # MfaGenerateTotpSecretRequest | 

    try:
        # Update or create TOTP secret for the given method ID on the given entity.
        await api_instance.mfa_generate_totp_secret(mfa_generate_totp_secret_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_generate_totp_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_generate_totp_secret_request** | [**MfaGenerateTotpSecretRequest**](MfaGenerateTotpSecretRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_list_duo_methods**
> StandardListResponse mfa_list_duo_methods(list)

List MFA method configurations for the given MFA method

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List MFA method configurations for the given MFA method
        api_response = await api_instance.mfa_list_duo_methods(list)
        print("The response of IdentityApi->mfa_list_duo_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_list_duo_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_list_login_enforcements**
> StandardListResponse mfa_list_login_enforcements(list)

List login enforcements

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List login enforcements
        api_response = await api_instance.mfa_list_login_enforcements(list)
        print("The response of IdentityApi->mfa_list_login_enforcements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_list_login_enforcements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_list_methods**
> StandardListResponse mfa_list_methods(list)

List MFA method configurations for all MFA methods

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List MFA method configurations for all MFA methods
        api_response = await api_instance.mfa_list_methods(list)
        print("The response of IdentityApi->mfa_list_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_list_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_list_okta_methods**
> StandardListResponse mfa_list_okta_methods(list)

List MFA method configurations for the given MFA method

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List MFA method configurations for the given MFA method
        api_response = await api_instance.mfa_list_okta_methods(list)
        print("The response of IdentityApi->mfa_list_okta_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_list_okta_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_list_ping_id_methods**
> StandardListResponse mfa_list_ping_id_methods(list)

List MFA method configurations for the given MFA method

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List MFA method configurations for the given MFA method
        api_response = await api_instance.mfa_list_ping_id_methods(list)
        print("The response of IdentityApi->mfa_list_ping_id_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_list_ping_id_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_list_totp_methods**
> StandardListResponse mfa_list_totp_methods(list)

List MFA method configurations for the given MFA method

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List MFA method configurations for the given MFA method
        api_response = await api_instance.mfa_list_totp_methods(list)
        print("The response of IdentityApi->mfa_list_totp_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_list_totp_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_read_duo_method**
> mfa_read_duo_method(method_id)

Read the current configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Read the current configuration for the given MFA method
        await api_instance.mfa_read_duo_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_read_duo_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_read_login_enforcement**
> mfa_read_login_enforcement(name)

Read the current login enforcement

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name for this login enforcement configuration

    try:
        # Read the current login enforcement
        await api_instance.mfa_read_login_enforcement(name)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_read_login_enforcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for this login enforcement configuration | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_read_method**
> mfa_read_method(method_id)

Read the current configuration for the given ID regardless of the MFA method type

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Read the current configuration for the given ID regardless of the MFA method type
        await api_instance.mfa_read_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_read_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_read_okta_method**
> mfa_read_okta_method(method_id)

Read the current configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Read the current configuration for the given MFA method
        await api_instance.mfa_read_okta_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_read_okta_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_read_ping_id_method**
> mfa_read_ping_id_method(method_id)

Read the current configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Read the current configuration for the given MFA method
        await api_instance.mfa_read_ping_id_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_read_ping_id_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_read_totp_method**
> mfa_read_totp_method(method_id)

Read the current configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.

    try:
        # Read the current configuration for the given MFA method
        await api_instance.mfa_read_totp_method(method_id)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_read_totp_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_update_duo_method**
> mfa_update_duo_method(method_id, mfa_update_duo_method_request)

Update the configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_update_duo_method_request import MfaUpdateDuoMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.
    mfa_update_duo_method_request = ahvac.MfaUpdateDuoMethodRequest() # MfaUpdateDuoMethodRequest | 

    try:
        # Update the configuration for the given MFA method
        await api_instance.mfa_update_duo_method(method_id, mfa_update_duo_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_update_duo_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 
 **mfa_update_duo_method_request** | [**MfaUpdateDuoMethodRequest**](MfaUpdateDuoMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_update_okta_method**
> mfa_update_okta_method(method_id, mfa_update_okta_method_request)

Update the configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_update_okta_method_request import MfaUpdateOktaMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.
    mfa_update_okta_method_request = ahvac.MfaUpdateOktaMethodRequest() # MfaUpdateOktaMethodRequest | 

    try:
        # Update the configuration for the given MFA method
        await api_instance.mfa_update_okta_method(method_id, mfa_update_okta_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_update_okta_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 
 **mfa_update_okta_method_request** | [**MfaUpdateOktaMethodRequest**](MfaUpdateOktaMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_update_ping_id_method**
> mfa_update_ping_id_method(method_id, mfa_update_ping_id_method_request)

Update the configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_update_ping_id_method_request import MfaUpdatePingIdMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.
    mfa_update_ping_id_method_request = ahvac.MfaUpdatePingIdMethodRequest() # MfaUpdatePingIdMethodRequest | 

    try:
        # Update the configuration for the given MFA method
        await api_instance.mfa_update_ping_id_method(method_id, mfa_update_ping_id_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_update_ping_id_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 
 **mfa_update_ping_id_method_request** | [**MfaUpdatePingIdMethodRequest**](MfaUpdatePingIdMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_update_totp_method**
> mfa_update_totp_method(method_id, mfa_update_totp_method_request)

Update the configuration for the given MFA method

### Example


```python
import ahvac
from ahvac.models.mfa_update_totp_method_request import MfaUpdateTotpMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    method_id = 'method_id_example' # str | The unique identifier for this MFA method.
    mfa_update_totp_method_request = ahvac.MfaUpdateTotpMethodRequest() # MfaUpdateTotpMethodRequest | 

    try:
        # Update the configuration for the given MFA method
        await api_instance.mfa_update_totp_method(method_id, mfa_update_totp_method_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_update_totp_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_id** | **str**| The unique identifier for this MFA method. | 
 **mfa_update_totp_method_request** | [**MfaUpdateTotpMethodRequest**](MfaUpdateTotpMethodRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_write_login_enforcement**
> mfa_write_login_enforcement(name, mfa_write_login_enforcement_request)

Create or update a login enforcement

### Example


```python
import ahvac
from ahvac.models.mfa_write_login_enforcement_request import MfaWriteLoginEnforcementRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name for this login enforcement configuration
    mfa_write_login_enforcement_request = ahvac.MfaWriteLoginEnforcementRequest() # MfaWriteLoginEnforcementRequest | 

    try:
        # Create or update a login enforcement
        await api_instance.mfa_write_login_enforcement(name, mfa_write_login_enforcement_request)
    except Exception as e:
        print("Exception when calling IdentityApi->mfa_write_login_enforcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for this login enforcement configuration | 
 **mfa_write_login_enforcement_request** | [**MfaWriteLoginEnforcementRequest**](MfaWriteLoginEnforcementRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_configure**
> oidc_configure(oidc_configure_request)



### Example


```python
import ahvac
from ahvac.models.oidc_configure_request import OidcConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    oidc_configure_request = ahvac.OidcConfigureRequest() # OidcConfigureRequest | 

    try:
        await api_instance.oidc_configure(oidc_configure_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oidc_configure_request** | [**OidcConfigureRequest**](OidcConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_delete_assignment**
> oidc_delete_assignment(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the assignment

    try:
        await api_instance.oidc_delete_assignment(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_delete_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_delete_client**
> oidc_delete_client(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the client.

    try:
        await api_instance.oidc_delete_client(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_delete_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the client. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_delete_key**
> oidc_delete_key(name)

CRUD operations for OIDC keys.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the key

    try:
        # CRUD operations for OIDC keys.
        await api_instance.oidc_delete_key(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_delete_provider**
> oidc_delete_provider(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider

    try:
        await api_instance.oidc_delete_provider(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_delete_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_delete_role**
> oidc_delete_role(name)

CRUD operations on OIDC Roles

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the role

    try:
        # CRUD operations on OIDC Roles
        await api_instance.oidc_delete_role(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_delete_scope**
> oidc_delete_scope(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the scope

    try:
        await api_instance.oidc_delete_scope(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_delete_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the scope | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_generate_token**
> oidc_generate_token(name)

Generate an OIDC token

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the role

    try:
        # Generate an OIDC token
        await api_instance.oidc_generate_token(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_generate_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_introspect**
> oidc_introspect(oidc_introspect_request)

Verify the authenticity of an OIDC token

### Example


```python
import ahvac
from ahvac.models.oidc_introspect_request import OidcIntrospectRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    oidc_introspect_request = ahvac.OidcIntrospectRequest() # OidcIntrospectRequest | 

    try:
        # Verify the authenticity of an OIDC token
        await api_instance.oidc_introspect(oidc_introspect_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_introspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oidc_introspect_request** | [**OidcIntrospectRequest**](OidcIntrospectRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_list_assignments**
> StandardListResponse oidc_list_assignments(list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.oidc_list_assignments(list)
        print("The response of IdentityApi->oidc_list_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_list_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_list_clients**
> StandardListResponse oidc_list_clients(list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.oidc_list_clients(list)
        print("The response of IdentityApi->oidc_list_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_list_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_list_keys**
> StandardListResponse oidc_list_keys(list)

List OIDC keys

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List OIDC keys
        api_response = await api_instance.oidc_list_keys(list)
        print("The response of IdentityApi->oidc_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_list_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_list_providers**
> StandardListResponse oidc_list_providers(list, allowed_client_id=allowed_client_id)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`
    allowed_client_id = '' # str | Filters the list of OIDC providers to those that allow the given client ID in their set of allowed_client_ids. (optional) (default to '')

    try:
        api_response = await api_instance.oidc_list_providers(list, allowed_client_id=allowed_client_id)
        print("The response of IdentityApi->oidc_list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_list_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 
 **allowed_client_id** | **str**| Filters the list of OIDC providers to those that allow the given client ID in their set of allowed_client_ids. | [optional] [default to &#39;&#39;]

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_list_roles**
> StandardListResponse oidc_list_roles(list)

List configured OIDC roles

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List configured OIDC roles
        api_response = await api_instance.oidc_list_roles(list)
        print("The response of IdentityApi->oidc_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_list_scopes**
> StandardListResponse oidc_list_scopes(list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.oidc_list_scopes(list)
        print("The response of IdentityApi->oidc_list_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_list_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_provider_authorize**
> oidc_provider_authorize(name, client_id=client_id, code_challenge=code_challenge, code_challenge_method=code_challenge_method, max_age=max_age, nonce=nonce, redirect_uri=redirect_uri, response_type=response_type, scope=scope, state=state)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider
    client_id = 'client_id_example' # str | The ID of the requesting client. (optional)
    code_challenge = 'code_challenge_example' # str | The code challenge derived from the code verifier. (optional)
    code_challenge_method = 'plain' # str | The method that was used to derive the code challenge. The following methods are supported: 'S256', 'plain'. Defaults to 'plain'. (optional) (default to 'plain')
    max_age = 56 # int | The allowable elapsed time in seconds since the last time the end-user was actively authenticated. (optional)
    nonce = 'nonce_example' # str | The value that will be returned in the ID token nonce claim after a token exchange. (optional)
    redirect_uri = 'redirect_uri_example' # str | The redirection URI to which the response will be sent. (optional)
    response_type = 'response_type_example' # str | The OIDC authentication flow to be used. The following response types are supported: 'code' (optional)
    scope = 'scope_example' # str | A space-delimited, case-sensitive list of scopes to be requested. The 'openid' scope is required. (optional)
    state = 'state_example' # str | The value used to maintain state between the authentication request and client. (optional)

    try:
        await api_instance.oidc_provider_authorize(name, client_id=client_id, code_challenge=code_challenge, code_challenge_method=code_challenge_method, max_age=max_age, nonce=nonce, redirect_uri=redirect_uri, response_type=response_type, scope=scope, state=state)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_provider_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 
 **client_id** | **str**| The ID of the requesting client. | [optional] 
 **code_challenge** | **str**| The code challenge derived from the code verifier. | [optional] 
 **code_challenge_method** | **str**| The method that was used to derive the code challenge. The following methods are supported: &#39;S256&#39;, &#39;plain&#39;. Defaults to &#39;plain&#39;. | [optional] [default to &#39;plain&#39;]
 **max_age** | **int**| The allowable elapsed time in seconds since the last time the end-user was actively authenticated. | [optional] 
 **nonce** | **str**| The value that will be returned in the ID token nonce claim after a token exchange. | [optional] 
 **redirect_uri** | **str**| The redirection URI to which the response will be sent. | [optional] 
 **response_type** | **str**| The OIDC authentication flow to be used. The following response types are supported: &#39;code&#39; | [optional] 
 **scope** | **str**| A space-delimited, case-sensitive list of scopes to be requested. The &#39;openid&#39; scope is required. | [optional] 
 **state** | **str**| The value used to maintain state between the authentication request and client. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_provider_authorize_with_parameters**
> oidc_provider_authorize_with_parameters(name, oidc_provider_authorize_with_parameters_request)



### Example


```python
import ahvac
from ahvac.models.oidc_provider_authorize_with_parameters_request import OidcProviderAuthorizeWithParametersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider
    oidc_provider_authorize_with_parameters_request = ahvac.OidcProviderAuthorizeWithParametersRequest() # OidcProviderAuthorizeWithParametersRequest | 

    try:
        await api_instance.oidc_provider_authorize_with_parameters(name, oidc_provider_authorize_with_parameters_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_provider_authorize_with_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 
 **oidc_provider_authorize_with_parameters_request** | [**OidcProviderAuthorizeWithParametersRequest**](OidcProviderAuthorizeWithParametersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_provider_token**
> oidc_provider_token(name, oidc_provider_token_request)



### Example


```python
import ahvac
from ahvac.models.oidc_provider_token_request import OidcProviderTokenRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider
    oidc_provider_token_request = ahvac.OidcProviderTokenRequest() # OidcProviderTokenRequest | 

    try:
        await api_instance.oidc_provider_token(name, oidc_provider_token_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_provider_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 
 **oidc_provider_token_request** | [**OidcProviderTokenRequest**](OidcProviderTokenRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_provider_user_info**
> oidc_provider_user_info(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider

    try:
        await api_instance.oidc_provider_user_info(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_provider_user_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_provider_user_info2**
> oidc_provider_user_info2(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider

    try:
        await api_instance.oidc_provider_user_info2(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_provider_user_info2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_assignment**
> oidc_read_assignment(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the assignment

    try:
        await api_instance.oidc_read_assignment(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_client**
> oidc_read_client(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the client.

    try:
        await api_instance.oidc_read_client(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the client. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_configuration**
> oidc_read_configuration()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)

    try:
        await api_instance.oidc_read_configuration()
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_key**
> oidc_read_key(name)

CRUD operations for OIDC keys.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the key

    try:
        # CRUD operations for OIDC keys.
        await api_instance.oidc_read_key(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_open_id_configuration**
> oidc_read_open_id_configuration()

Query OIDC configurations

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)

    try:
        # Query OIDC configurations
        await api_instance.oidc_read_open_id_configuration()
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_open_id_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_provider**
> oidc_read_provider(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider

    try:
        await api_instance.oidc_read_provider(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_provider_open_id_configuration**
> oidc_read_provider_open_id_configuration(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider

    try:
        await api_instance.oidc_read_provider_open_id_configuration(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_provider_open_id_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_provider_public_keys**
> oidc_read_provider_public_keys(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider

    try:
        await api_instance.oidc_read_provider_public_keys(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_provider_public_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_public_keys**
> oidc_read_public_keys()

Retrieve public keys

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)

    try:
        # Retrieve public keys
        await api_instance.oidc_read_public_keys()
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_public_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_role**
> oidc_read_role(name)

CRUD operations on OIDC Roles

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the role

    try:
        # CRUD operations on OIDC Roles
        await api_instance.oidc_read_role(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_read_scope**
> oidc_read_scope(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the scope

    try:
        await api_instance.oidc_read_scope(name)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_read_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the scope | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_rotate_key**
> oidc_rotate_key(name, oidc_rotate_key_request)

Rotate a named OIDC key.

### Example


```python
import ahvac
from ahvac.models.oidc_rotate_key_request import OidcRotateKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the key
    oidc_rotate_key_request = ahvac.OidcRotateKeyRequest() # OidcRotateKeyRequest | 

    try:
        # Rotate a named OIDC key.
        await api_instance.oidc_rotate_key(name, oidc_rotate_key_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_rotate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **oidc_rotate_key_request** | [**OidcRotateKeyRequest**](OidcRotateKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_write_assignment**
> oidc_write_assignment(name, oidc_write_assignment_request)



### Example


```python
import ahvac
from ahvac.models.oidc_write_assignment_request import OidcWriteAssignmentRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the assignment
    oidc_write_assignment_request = ahvac.OidcWriteAssignmentRequest() # OidcWriteAssignmentRequest | 

    try:
        await api_instance.oidc_write_assignment(name, oidc_write_assignment_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_write_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the assignment | 
 **oidc_write_assignment_request** | [**OidcWriteAssignmentRequest**](OidcWriteAssignmentRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_write_client**
> oidc_write_client(name, oidc_write_client_request)



### Example


```python
import ahvac
from ahvac.models.oidc_write_client_request import OidcWriteClientRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the client.
    oidc_write_client_request = ahvac.OidcWriteClientRequest() # OidcWriteClientRequest | 

    try:
        await api_instance.oidc_write_client(name, oidc_write_client_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_write_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the client. | 
 **oidc_write_client_request** | [**OidcWriteClientRequest**](OidcWriteClientRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_write_key**
> oidc_write_key(name, oidc_write_key_request)

CRUD operations for OIDC keys.

### Example


```python
import ahvac
from ahvac.models.oidc_write_key_request import OidcWriteKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the key
    oidc_write_key_request = ahvac.OidcWriteKeyRequest() # OidcWriteKeyRequest | 

    try:
        # CRUD operations for OIDC keys.
        await api_instance.oidc_write_key(name, oidc_write_key_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_write_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **oidc_write_key_request** | [**OidcWriteKeyRequest**](OidcWriteKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_write_provider**
> oidc_write_provider(name, oidc_write_provider_request)



### Example


```python
import ahvac
from ahvac.models.oidc_write_provider_request import OidcWriteProviderRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the provider
    oidc_write_provider_request = ahvac.OidcWriteProviderRequest() # OidcWriteProviderRequest | 

    try:
        await api_instance.oidc_write_provider(name, oidc_write_provider_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_write_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the provider | 
 **oidc_write_provider_request** | [**OidcWriteProviderRequest**](OidcWriteProviderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_write_role**
> oidc_write_role(name, oidc_write_role_request)

CRUD operations on OIDC Roles

### Example


```python
import ahvac
from ahvac.models.oidc_write_role_request import OidcWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the role
    oidc_write_role_request = ahvac.OidcWriteRoleRequest() # OidcWriteRoleRequest | 

    try:
        # CRUD operations on OIDC Roles
        await api_instance.oidc_write_role(name, oidc_write_role_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **oidc_write_role_request** | [**OidcWriteRoleRequest**](OidcWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_write_scope**
> oidc_write_scope(name, oidc_write_scope_request)



### Example


```python
import ahvac
from ahvac.models.oidc_write_scope_request import OidcWriteScopeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    name = 'name_example' # str | Name of the scope
    oidc_write_scope_request = ahvac.OidcWriteScopeRequest() # OidcWriteScopeRequest | 

    try:
        await api_instance.oidc_write_scope(name, oidc_write_scope_request)
    except Exception as e:
        print("Exception when calling IdentityApi->oidc_write_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the scope | 
 **oidc_write_scope_request** | [**OidcWriteScopeRequest**](OidcWriteScopeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persona_create**
> persona_create(persona_create_request)

Create a new alias.

### Example


```python
import ahvac
from ahvac.models.persona_create_request import PersonaCreateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    persona_create_request = ahvac.PersonaCreateRequest() # PersonaCreateRequest | 

    try:
        # Create a new alias.
        await api_instance.persona_create(persona_create_request)
    except Exception as e:
        print("Exception when calling IdentityApi->persona_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persona_create_request** | [**PersonaCreateRequest**](PersonaCreateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persona_delete_by_id**
> persona_delete_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the persona

    try:
        await api_instance.persona_delete_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->persona_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the persona | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persona_list_by_id**
> StandardListResponse persona_list_by_id(list)

List all the alias IDs.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List all the alias IDs.
        api_response = await api_instance.persona_list_by_id(list)
        print("The response of IdentityApi->persona_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->persona_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persona_read_by_id**
> persona_read_by_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the persona

    try:
        await api_instance.persona_read_by_id(id)
    except Exception as e:
        print("Exception when calling IdentityApi->persona_read_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the persona | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persona_update_by_id**
> persona_update_by_id(id, persona_update_by_id_request)



### Example


```python
import ahvac
from ahvac.models.persona_update_by_id_request import PersonaUpdateByIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.IdentityApi(api_client)
    id = 'id_example' # str | ID of the persona
    persona_update_by_id_request = ahvac.PersonaUpdateByIdRequest() # PersonaUpdateByIdRequest | 

    try:
        await api_instance.persona_update_by_id(id, persona_update_by_id_request)
    except Exception as e:
        print("Exception when calling IdentityApi->persona_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the persona | 
 **persona_update_by_id_request** | [**PersonaUpdateByIdRequest**](PersonaUpdateByIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

