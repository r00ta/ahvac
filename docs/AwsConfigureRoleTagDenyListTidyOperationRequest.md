# AwsConfigureRoleTagDenyListTidyOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_periodic_tidy** | **bool** | If set to &#39;true&#39;, disables the periodic tidying of deny listed entries. | [optional] [default to False]
**safety_buffer** | **str** | The amount of extra time that must have passed beyond the roletag expiration, before it is removed from the backend storage. Defaults to 4320h (180 days). | [optional] [default to '15552000']

## Example

```python
from ahvac.models.aws_configure_role_tag_deny_list_tidy_operation_request import AwsConfigureRoleTagDenyListTidyOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsConfigureRoleTagDenyListTidyOperationRequest from a JSON string
aws_configure_role_tag_deny_list_tidy_operation_request_instance = AwsConfigureRoleTagDenyListTidyOperationRequest.from_json(json)
# print the JSON string representation of the object
print(AwsConfigureRoleTagDenyListTidyOperationRequest.to_json())

# convert the object into a dict
aws_configure_role_tag_deny_list_tidy_operation_request_dict = aws_configure_role_tag_deny_list_tidy_operation_request_instance.to_dict()
# create an instance of AwsConfigureRoleTagDenyListTidyOperationRequest from a dict
aws_configure_role_tag_deny_list_tidy_operation_request_from_dict = AwsConfigureRoleTagDenyListTidyOperationRequest.from_dict(aws_configure_role_tag_deny_list_tidy_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


