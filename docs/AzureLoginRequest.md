# AzureLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | A signed JWT | [optional] 
**resource_group_name** | **str** | The resource group from the instance. | [optional] 
**resource_id** | **str** | The fully qualified ID of the resource, includingthe resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}. This value is ignored if vm_name or vmss_name is specified. | [optional] 
**role** | **str** | The token role. | [optional] 
**subscription_id** | **str** | The subscription id for the instance. | [optional] 
**vm_name** | **str** | The name of the virtual machine. This value is ignored if vmss_name is specified. | [optional] 
**vmss_name** | **str** | The name of the virtual machine scale set the instance is in. | [optional] 

## Example

```python
from ahvac.models.azure_login_request import AzureLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureLoginRequest from a JSON string
azure_login_request_instance = AzureLoginRequest.from_json(json)
# print the JSON string representation of the object
print(AzureLoginRequest.to_json())

# convert the object into a dict
azure_login_request_dict = azure_login_request_instance.to_dict()
# create an instance of AzureLoginRequest from a dict
azure_login_request_from_dict = AzureLoginRequest.from_dict(azure_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


