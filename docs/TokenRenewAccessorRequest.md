# TokenRenewAccessorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessor** | **str** | Accessor of the token to renew (request body) | [optional] 
**increment** | **str** | The desired increment in seconds to the token expiration | [optional] [default to '0']

## Example

```python
from ahvac.models.token_renew_accessor_request import TokenRenewAccessorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRenewAccessorRequest from a JSON string
token_renew_accessor_request_instance = TokenRenewAccessorRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRenewAccessorRequest.to_json())

# convert the object into a dict
token_renew_accessor_request_dict = token_renew_accessor_request_instance.to_dict()
# create an instance of TokenRenewAccessorRequest from a dict
token_renew_accessor_request_from_dict = TokenRenewAccessorRequest.from_dict(token_renew_accessor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


