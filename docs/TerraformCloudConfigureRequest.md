# TerraformCloudConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address to access Terraform Cloud or Enterprise. Default is \&quot;https://app.terraform.io\&quot;. | [optional] [default to 'https://app.terraform.io']
**base_path** | **str** | The base path for the Terraform Cloud or Enterprise API. Default is \&quot;/api/v2/\&quot;. | [optional] [default to '/api/v2/']
**token** | **str** | The token to access Terraform Cloud | 

## Example

```python
from ahvac.models.terraform_cloud_configure_request import TerraformCloudConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerraformCloudConfigureRequest from a JSON string
terraform_cloud_configure_request_instance = TerraformCloudConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(TerraformCloudConfigureRequest.to_json())

# convert the object into a dict
terraform_cloud_configure_request_dict = terraform_cloud_configure_request_instance.to_dict()
# create an instance of TerraformCloudConfigureRequest from a dict
terraform_cloud_configure_request_from_dict = TerraformCloudConfigureRequest.from_dict(terraform_cloud_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


