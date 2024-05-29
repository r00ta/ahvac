# AwsWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | Use role_arns or policy_arns instead. | [optional] 
**credential_type** | **str** | Type of credential to retrieve. Must be one of assumed_role, iam_user, or federation_token | [optional] 
**default_sts_ttl** | **str** | Default TTL for assumed_role and federation_token credential types when no TTL is explicitly requested with the credentials | [optional] 
**iam_groups** | **List[str]** | Names of IAM groups that generated IAM users will be added to. For a credential type of assumed_role or federation_token, the policies sent to the corresponding AWS call (sts:AssumeRole or sts:GetFederation) will be the policies from each group in iam_groups combined with the policy_document and policy_arns parameters. | [optional] 
**iam_tags** | **object** | IAM tags to be set for any users created by this role. These must be presented as Key-Value pairs. This can be represented as a map or a list of equal sign delimited key pairs. | [optional] 
**max_sts_ttl** | **str** | Max allowed TTL for assumed_role and federation_token credential types | [optional] 
**permissions_boundary_arn** | **str** | ARN of an IAM policy to attach as a permissions boundary on IAM user credentials; only valid when credential_type isiam_user | [optional] 
**policy** | **str** | Use policy_document instead. | [optional] 
**policy_arns** | **List[str]** | ARNs of AWS policies. Behavior varies by credential_type. When credential_type is iam_user, then it will attach the specified policies to the generated IAM user. When credential_type is assumed_role or federation_token, the policies will be passed as the PolicyArns parameter, acting as a filter on permissions available. | [optional] 
**policy_document** | **str** | JSON-encoded IAM policy document. Behavior varies by credential_type. When credential_type is iam_user, then it will attach the contents of the policy_document to the IAM user generated. When credential_type is assumed_role or federation_token, this will be passed in as the Policy parameter to the AssumeRole or GetFederationToken API call, acting as a filter on permissions available. | [optional] 
**role_arns** | **List[str]** | ARNs of AWS roles allowed to be assumed. Only valid when credential_type is assumed_role | [optional] 
**user_path** | **str** | Path for IAM User. Only valid when credential_type is iam_user | [optional] [default to '/']

## Example

```python
from ahvac.models.aws_write_role_request import AwsWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsWriteRoleRequest from a JSON string
aws_write_role_request_instance = AwsWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AwsWriteRoleRequest.to_json())

# convert the object into a dict
aws_write_role_request_dict = aws_write_role_request_instance.to_dict()
# create an instance of AwsWriteRoleRequest from a dict
aws_write_role_request_from_dict = AwsWriteRoleRequest.from_dict(aws_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


