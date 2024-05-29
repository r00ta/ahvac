# TokenRevokeOrphanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token to revoke (request body) | [optional] 

## Example

```python
from ahvac.models.token_revoke_orphan_request import TokenRevokeOrphanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRevokeOrphanRequest from a JSON string
token_revoke_orphan_request_instance = TokenRevokeOrphanRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRevokeOrphanRequest.to_json())

# convert the object into a dict
token_revoke_orphan_request_dict = token_revoke_orphan_request_instance.to_dict()
# create an instance of TokenRevokeOrphanRequest from a dict
token_revoke_orphan_request_from_dict = TokenRevokeOrphanRequest.from_dict(token_revoke_orphan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


