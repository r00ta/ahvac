# GithubLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | GitHub personal API token | [optional] 

## Example

```python
from ahvac.models.github_login_request import GithubLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubLoginRequest from a JSON string
github_login_request_instance = GithubLoginRequest.from_json(json)
# print the JSON string representation of the object
print(GithubLoginRequest.to_json())

# convert the object into a dict
github_login_request_dict = github_login_request_instance.to_dict()
# create an instance of GithubLoginRequest from a dict
github_login_request_from_dict = GithubLoginRequest.from_dict(github_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


