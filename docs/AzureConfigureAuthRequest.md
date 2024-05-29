# AzureConfigureAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The OAuth2 client id to connection to Azure. This value can also be provided with the AZURE_CLIENT_ID environment variable. | [optional] 
**client_secret** | **str** | The OAuth2 client secret to connection to Azure. This value can also be provided with the AZURE_CLIENT_SECRET environment variable. | [optional] 
**environment** | **str** | The Azure environment name. If not provided, AzurePublicCloud is used. This value can also be provided with the AZURE_ENVIRONMENT environment variable. | [optional] 
**resource** | **str** | The resource URL for the vault application in Azure Active Directory. This value can also be provided with the AZURE_AD_RESOURCE environment variable. | [optional] 
**root_password_ttl** | **str** | The TTL of the root password in Azure. This can be either a number of seconds or a time formatted duration (ex: 24h, 48ds) | [optional] [default to '15768000000000000']
**tenant_id** | **str** | The tenant id for the Azure Active Directory. This is sometimes referred to as Directory ID in AD. This value can also be provided with the AZURE_TENANT_ID environment variable. | [optional] 

## Example

```python
from ahvac.models.azure_configure_auth_request import AzureConfigureAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureConfigureAuthRequest from a JSON string
azure_configure_auth_request_instance = AzureConfigureAuthRequest.from_json(json)
# print the JSON string representation of the object
print(AzureConfigureAuthRequest.to_json())

# convert the object into a dict
azure_configure_auth_request_dict = azure_configure_auth_request_instance.to_dict()
# create an instance of AzureConfigureAuthRequest from a dict
azure_configure_auth_request_from_dict = AzureConfigureAuthRequest.from_dict(azure_configure_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


