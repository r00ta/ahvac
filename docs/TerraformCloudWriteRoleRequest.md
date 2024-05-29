# TerraformCloudWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_ttl** | **str** | Maximum time for role. If not set or set to 0, will use system default. | [optional] 
**organization** | **str** | Name of the Terraform Cloud or Enterprise organization | [optional] 
**team_id** | **str** | ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx) | [optional] 
**ttl** | **str** | Default lease for generated credentials. If not set or set to 0, will use system default. | [optional] 
**user_id** | **str** | ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx) | [optional] 

## Example

```python
from ahvac.models.terraform_cloud_write_role_request import TerraformCloudWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerraformCloudWriteRoleRequest from a JSON string
terraform_cloud_write_role_request_instance = TerraformCloudWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(TerraformCloudWriteRoleRequest.to_json())

# convert the object into a dict
terraform_cloud_write_role_request_dict = terraform_cloud_write_role_request_instance.to_dict()
# create an instance of TerraformCloudWriteRoleRequest from a dict
terraform_cloud_write_role_request_from_dict = TerraformCloudWriteRoleRequest.from_dict(terraform_cloud_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


