# AwsTidyIdentityAccessListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**safety_buffer** | **str** | The amount of extra time that must have passed beyond the identity&#39;s expiration, before it is removed from the backend storage. | [optional] [default to '259200']

## Example

```python
from ahvac.models.aws_tidy_identity_access_list_request import AwsTidyIdentityAccessListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTidyIdentityAccessListRequest from a JSON string
aws_tidy_identity_access_list_request_instance = AwsTidyIdentityAccessListRequest.from_json(json)
# print the JSON string representation of the object
print(AwsTidyIdentityAccessListRequest.to_json())

# convert the object into a dict
aws_tidy_identity_access_list_request_dict = aws_tidy_identity_access_list_request_instance.to_dict()
# create an instance of AwsTidyIdentityAccessListRequest from a dict
aws_tidy_identity_access_list_request_from_dict = AwsTidyIdentityAccessListRequest.from_dict(aws_tidy_identity_access_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


