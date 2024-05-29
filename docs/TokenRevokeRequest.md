# TokenRevokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token to revoke (request body) | [optional] 

## Example

```python
from ahvac.models.token_revoke_request import TokenRevokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRevokeRequest from a JSON string
token_revoke_request_instance = TokenRevokeRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRevokeRequest.to_json())

# convert the object into a dict
token_revoke_request_dict = token_revoke_request_instance.to_dict()
# create an instance of TokenRevokeRequest from a dict
token_revoke_request_from_dict = TokenRevokeRequest.from_dict(token_revoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


