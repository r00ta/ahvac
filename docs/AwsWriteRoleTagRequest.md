# AwsWriteRoleTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_instance_migration** | **bool** | If set, allows migration of the underlying instance where the client resides. This keys off of pendingTime in the metadata document, so essentially, this disables the client nonce check whenever the instance is migrated to a new host and pendingTime is newer than the previously-remembered time. Use with caution. | [optional] [default to False]
**disallow_reauthentication** | **bool** | If set, only allows a single token to be granted per instance ID. In order to perform a fresh login, the entry in access list for the instance ID needs to be cleared using the &#39;auth/aws-ec2/identity-accesslist/&lt;instance_id&gt;&#39; endpoint. | [optional] [default to False]
**instance_id** | **str** | Instance ID for which this tag is intended for. If set, the created tag can only be used by the instance with the given ID. | [optional] 
**max_ttl** | **str** | If set, specifies the maximum allowed token lifetime. | [optional] [default to '0']
**policies** | **List[str]** | Policies to be associated with the tag. If set, must be a subset of the role&#39;s policies. If set, but set to an empty value, only the &#39;default&#39; policy will be given to issued tokens. | [optional] 

## Example

```python
from ahvac.models.aws_write_role_tag_request import AwsWriteRoleTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsWriteRoleTagRequest from a JSON string
aws_write_role_tag_request_instance = AwsWriteRoleTagRequest.from_json(json)
# print the JSON string representation of the object
print(AwsWriteRoleTagRequest.to_json())

# convert the object into a dict
aws_write_role_tag_request_dict = aws_write_role_tag_request_instance.to_dict()
# create an instance of AwsWriteRoleTagRequest from a dict
aws_write_role_tag_request_from_dict = AwsWriteRoleTagRequest.from_dict(aws_write_role_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


