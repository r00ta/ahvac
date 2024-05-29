# AwsConfigureClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | AWS Access Key ID for the account used to make AWS API requests. | [optional] [default to '']
**allowed_sts_header_values** | **List[str]** | List of additional headers that are allowed to be in AWS STS request headers | [optional] 
**endpoint** | **str** | URL to override the default generated endpoint for making AWS EC2 API calls. | [optional] [default to '']
**iam_endpoint** | **str** | URL to override the default generated endpoint for making AWS IAM API calls. | [optional] [default to '']
**iam_server_id_header_value** | **str** | Value to require in the X-Vault-AWS-IAM-Server-ID request header | [optional] [default to '']
**max_retries** | **int** | Maximum number of retries for recoverable exceptions of AWS APIs | [optional] [default to -1]
**secret_key** | **str** | AWS Secret Access Key for the account used to make AWS API requests. | [optional] [default to '']
**sts_endpoint** | **str** | URL to override the default generated endpoint for making AWS STS API calls. | [optional] [default to '']
**sts_region** | **str** | The region ID for the sts_endpoint, if set. | [optional] [default to '']
**use_sts_region_from_client** | **bool** | Uses the STS region from client requests for making AWS STS API calls. | [optional] [default to False]

## Example

```python
from ahvac.models.aws_configure_client_request import AwsConfigureClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsConfigureClientRequest from a JSON string
aws_configure_client_request_instance = AwsConfigureClientRequest.from_json(json)
# print the JSON string representation of the object
print(AwsConfigureClientRequest.to_json())

# convert the object into a dict
aws_configure_client_request_dict = aws_configure_client_request_instance.to_dict()
# create an instance of AwsConfigureClientRequest from a dict
aws_configure_client_request_from_dict = AwsConfigureClientRequest.from_dict(aws_configure_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


