# GithubWriteTeamMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value for teams mapping | [optional] 

## Example

```python
from ahvac.models.github_write_team_mapping_request import GithubWriteTeamMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubWriteTeamMappingRequest from a JSON string
github_write_team_mapping_request_instance = GithubWriteTeamMappingRequest.from_json(json)
# print the JSON string representation of the object
print(GithubWriteTeamMappingRequest.to_json())

# convert the object into a dict
github_write_team_mapping_request_dict = github_write_team_mapping_request_instance.to_dict()
# create an instance of GithubWriteTeamMappingRequest from a dict
github_write_team_mapping_request_from_dict = GithubWriteTeamMappingRequest.from_dict(github_write_team_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


