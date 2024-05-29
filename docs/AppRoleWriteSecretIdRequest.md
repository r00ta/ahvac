# AppRoleWriteSecretIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_list** | **List[str]** | Comma separated string or list of CIDR blocks enforcing secret IDs to be used from specific set of IP addresses. If &#39;bound_cidr_list&#39; is set on the role, then the list of CIDR blocks listed here should be a subset of the CIDR blocks listed on the role. | [optional] 
**metadata** | **str** | Metadata to be tied to the SecretID. This should be a JSON formatted string containing the metadata in key value pairs. | [optional] 
**num_uses** | **int** | Number of times this SecretID can be used, after which the SecretID expires. Overrides secret_id_num_uses role option when supplied. May not be higher than role&#39;s secret_id_num_uses. | [optional] 
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**ttl** | **str** | Duration in seconds after which this SecretID expires. Overrides secret_id_ttl role option when supplied. May not be longer than role&#39;s secret_id_ttl. | [optional] 

## Example

```python
from ahvac.models.app_role_write_secret_id_request import AppRoleWriteSecretIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWriteSecretIdRequest from a JSON string
app_role_write_secret_id_request_instance = AppRoleWriteSecretIdRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWriteSecretIdRequest.to_json())

# convert the object into a dict
app_role_write_secret_id_request_dict = app_role_write_secret_id_request_instance.to_dict()
# create an instance of AppRoleWriteSecretIdRequest from a dict
app_role_write_secret_id_request_from_dict = AppRoleWriteSecretIdRequest.from_dict(app_role_write_secret_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


