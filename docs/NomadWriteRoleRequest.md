# NomadWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | **bool** | Boolean value describing if the token should be global or not. Defaults to false. | [optional] 
**policies** | **List[str]** | Comma-separated string or list of policies as previously created in Nomad. Required for &#39;client&#39; token. | [optional] 
**type** | **str** | Which type of token to create: &#39;client&#39; or &#39;management&#39;. If a &#39;management&#39; token, the \&quot;policies\&quot; parameter is not required. Defaults to &#39;client&#39;. | [optional] [default to 'client']

## Example

```python
from ahvac.models.nomad_write_role_request import NomadWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomadWriteRoleRequest from a JSON string
nomad_write_role_request_instance = NomadWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(NomadWriteRoleRequest.to_json())

# convert the object into a dict
nomad_write_role_request_dict = nomad_write_role_request_instance.to_dict()
# create an instance of NomadWriteRoleRequest from a dict
nomad_write_role_request_from_dict = NomadWriteRoleRequest.from_dict(nomad_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


