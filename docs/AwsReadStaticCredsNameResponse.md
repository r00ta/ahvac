# AwsReadStaticCredsNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | The access key of the AWS Credential | [optional] 
**secret_key** | **str** | The secret key of the AWS Credential | [optional] 

## Example

```python
from ahvac.models.aws_read_static_creds_name_response import AwsReadStaticCredsNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AwsReadStaticCredsNameResponse from a JSON string
aws_read_static_creds_name_response_instance = AwsReadStaticCredsNameResponse.from_json(json)
# print the JSON string representation of the object
print(AwsReadStaticCredsNameResponse.to_json())

# convert the object into a dict
aws_read_static_creds_name_response_dict = aws_read_static_creds_name_response_instance.to_dict()
# create an instance of AwsReadStaticCredsNameResponse from a dict
aws_read_static_creds_name_response_from_dict = AwsReadStaticCredsNameResponse.from_dict(aws_read_static_creds_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


