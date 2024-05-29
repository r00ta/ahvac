# TokenRevokeAccessorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessor** | **str** | Accessor of the token (request body) | [optional] 

## Example

```python
from ahvac.models.token_revoke_accessor_request import TokenRevokeAccessorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRevokeAccessorRequest from a JSON string
token_revoke_accessor_request_instance = TokenRevokeAccessorRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRevokeAccessorRequest.to_json())

# convert the object into a dict
token_revoke_accessor_request_dict = token_revoke_accessor_request_instance.to_dict()
# create an instance of TokenRevokeAccessorRequest from a dict
token_revoke_accessor_request_from_dict = TokenRevokeAccessorRequest.from_dict(token_revoke_accessor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


