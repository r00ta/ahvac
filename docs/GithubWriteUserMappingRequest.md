# GithubWriteUserMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value for users mapping | [optional] 

## Example

```python
from ahvac.models.github_write_user_mapping_request import GithubWriteUserMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubWriteUserMappingRequest from a JSON string
github_write_user_mapping_request_instance = GithubWriteUserMappingRequest.from_json(json)
# print the JSON string representation of the object
print(GithubWriteUserMappingRequest.to_json())

# convert the object into a dict
github_write_user_mapping_request_dict = github_write_user_mapping_request_instance.to_dict()
# create an instance of GithubWriteUserMappingRequest from a dict
github_write_user_mapping_request_from_dict = GithubWriteUserMappingRequest.from_dict(github_write_user_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


