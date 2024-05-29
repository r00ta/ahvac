# AwsWriteStsRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sts_role** | **str** | AWS ARN for STS role to be assumed when interacting with the account specified. The Vault server must have permissions to assume this role. | [optional] 

## Example

```python
from ahvac.models.aws_write_sts_role_request import AwsWriteStsRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsWriteStsRoleRequest from a JSON string
aws_write_sts_role_request_instance = AwsWriteStsRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AwsWriteStsRoleRequest.to_json())

# convert the object into a dict
aws_write_sts_role_request_dict = aws_write_sts_role_request_instance.to_dict()
# create an instance of AwsWriteStsRoleRequest from a dict
aws_write_sts_role_request_from_dict = AwsWriteStsRoleRequest.from_dict(aws_write_sts_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


