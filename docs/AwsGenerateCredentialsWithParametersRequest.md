# AwsGenerateCredentialsWithParametersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_arn** | **str** | ARN of role to assume when credential_type is assumed_role | [optional] 
**role_session_name** | **str** | Session name to use when assuming role. Max chars: 64 | [optional] 
**ttl** | **str** | Lifetime of the returned credentials in seconds | [optional] [default to '3600']

## Example

```python
from ahvac.models.aws_generate_credentials_with_parameters_request import AwsGenerateCredentialsWithParametersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsGenerateCredentialsWithParametersRequest from a JSON string
aws_generate_credentials_with_parameters_request_instance = AwsGenerateCredentialsWithParametersRequest.from_json(json)
# print the JSON string representation of the object
print(AwsGenerateCredentialsWithParametersRequest.to_json())

# convert the object into a dict
aws_generate_credentials_with_parameters_request_dict = aws_generate_credentials_with_parameters_request_instance.to_dict()
# create an instance of AwsGenerateCredentialsWithParametersRequest from a dict
aws_generate_credentials_with_parameters_request_from_dict = AwsGenerateCredentialsWithParametersRequest.from_dict(aws_generate_credentials_with_parameters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


