# AppRoleLookUpSecretIdByAccessorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_list** | **List[str]** | List of CIDR blocks enforcing secret IDs to be used from specific set of IP addresses. If &#39;bound_cidr_list&#39; is set on the role, then the list of CIDR blocks listed here should be a subset of the CIDR blocks listed on the role. | [optional] 
**creation_time** | **datetime** |  | [optional] 
**expiration_time** | **datetime** |  | [optional] 
**last_updated_time** | **datetime** |  | [optional] 
**metadata** | **object** |  | [optional] 
**secret_id_accessor** | **str** | Accessor of the secret ID | [optional] 
**secret_id_num_uses** | **int** | Number of times a secret ID can access the role, after which the secret ID will expire. | [optional] 
**secret_id_ttl** | **str** | Duration in seconds after which the issued secret ID expires. | [optional] 
**token_bound_cidrs** | **List[str]** | List of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token. Should be a subset of the token CIDR blocks listed on the role, if any. | [optional] 

## Example

```python
from ahvac.models.app_role_look_up_secret_id_by_accessor_response import AppRoleLookUpSecretIdByAccessorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleLookUpSecretIdByAccessorResponse from a JSON string
app_role_look_up_secret_id_by_accessor_response_instance = AppRoleLookUpSecretIdByAccessorResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoleLookUpSecretIdByAccessorResponse.to_json())

# convert the object into a dict
app_role_look_up_secret_id_by_accessor_response_dict = app_role_look_up_secret_id_by_accessor_response_instance.to_dict()
# create an instance of AppRoleLookUpSecretIdByAccessorResponse from a dict
app_role_look_up_secret_id_by_accessor_response_from_dict = AppRoleLookUpSecretIdByAccessorResponse.from_dict(app_role_look_up_secret_id_by_accessor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


