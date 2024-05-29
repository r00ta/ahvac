# AwsConfigureRootIamCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Access key with permission to create new keys. | [optional] 
**iam_endpoint** | **str** | Endpoint to custom IAM server URL | [optional] 
**max_retries** | **int** | Maximum number of retries for recoverable exceptions of AWS APIs | [optional] [default to -1]
**region** | **str** | Region for API calls. | [optional] 
**secret_key** | **str** | Secret key with permission to create new keys. | [optional] 
**sts_endpoint** | **str** | Endpoint to custom STS server URL | [optional] 
**username_template** | **str** | Template to generate custom IAM usernames | [optional] 

## Example

```python
from ahvac.models.aws_configure_root_iam_credentials_request import AwsConfigureRootIamCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsConfigureRootIamCredentialsRequest from a JSON string
aws_configure_root_iam_credentials_request_instance = AwsConfigureRootIamCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(AwsConfigureRootIamCredentialsRequest.to_json())

# convert the object into a dict
aws_configure_root_iam_credentials_request_dict = aws_configure_root_iam_credentials_request_instance.to_dict()
# create an instance of AwsConfigureRootIamCredentialsRequest from a dict
aws_configure_root_iam_credentials_request_from_dict = AwsConfigureRootIamCredentialsRequest.from_dict(aws_configure_root_iam_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


