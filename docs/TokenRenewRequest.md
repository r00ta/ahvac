# TokenRenewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**increment** | **str** | The desired increment in seconds to the token expiration | [optional] [default to '0']
**token** | **str** | Token to renew (request body) | [optional] 

## Example

```python
from ahvac.models.token_renew_request import TokenRenewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRenewRequest from a JSON string
token_renew_request_instance = TokenRenewRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRenewRequest.to_json())

# convert the object into a dict
token_renew_request_dict = token_renew_request_instance.to_dict()
# create an instance of TokenRenewRequest from a dict
token_renew_request_from_dict = TokenRenewRequest.from_dict(token_renew_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


