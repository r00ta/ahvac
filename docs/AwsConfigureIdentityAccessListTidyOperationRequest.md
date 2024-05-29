# AwsConfigureIdentityAccessListTidyOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_periodic_tidy** | **bool** | If set to &#39;true&#39;, disables the periodic tidying of the &#39;identity-accesslist/&lt;instance_id&gt;&#39; entries. | [optional] [default to False]
**safety_buffer** | **str** | The amount of extra time that must have passed beyond the identity&#39;s expiration, before it is removed from the backend storage. | [optional] [default to '259200']

## Example

```python
from ahvac.models.aws_configure_identity_access_list_tidy_operation_request import AwsConfigureIdentityAccessListTidyOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsConfigureIdentityAccessListTidyOperationRequest from a JSON string
aws_configure_identity_access_list_tidy_operation_request_instance = AwsConfigureIdentityAccessListTidyOperationRequest.from_json(json)
# print the JSON string representation of the object
print(AwsConfigureIdentityAccessListTidyOperationRequest.to_json())

# convert the object into a dict
aws_configure_identity_access_list_tidy_operation_request_dict = aws_configure_identity_access_list_tidy_operation_request_instance.to_dict()
# create an instance of AwsConfigureIdentityAccessListTidyOperationRequest from a dict
aws_configure_identity_access_list_tidy_operation_request_from_dict = AwsConfigureIdentityAccessListTidyOperationRequest.from_dict(aws_configure_identity_access_list_tidy_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


