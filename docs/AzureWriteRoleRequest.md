# AzureWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_object_id** | **str** | Application Object ID to use for static service principal credentials. | [optional] 
**azure_groups** | **str** | JSON list of Azure groups to add the service principal to. | [optional] 
**azure_roles** | **str** | JSON list of Azure roles to assign. | [optional] 
**max_ttl** | **str** | Maximum time a service principal. If not set or set to 0, will use system default. | [optional] 
**permanently_delete** | **bool** | Indicates whether new application objects should be permanently deleted. If not set, objects will not be permanently deleted. | [optional] [default to False]
**persist_app** | **bool** | Persist the app between generated credentials. Useful if the app needs to maintain owner ship of resources it creates | [optional] [default to False]
**ttl** | **str** | Default lease for generated credentials. If not set or set to 0, will use system default. | [optional] 

## Example

```python
from ahvac.models.azure_write_role_request import AzureWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureWriteRoleRequest from a JSON string
azure_write_role_request_instance = AzureWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AzureWriteRoleRequest.to_json())

# convert the object into a dict
azure_write_role_request_dict = azure_write_role_request_instance.to_dict()
# create an instance of AzureWriteRoleRequest from a dict
azure_write_role_request_from_dict = AzureWriteRoleRequest.from_dict(azure_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


