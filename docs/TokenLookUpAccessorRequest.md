# TokenLookUpAccessorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessor** | **str** | Accessor of the token to look up (request body) | [optional] 

## Example

```python
from ahvac.models.token_look_up_accessor_request import TokenLookUpAccessorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLookUpAccessorRequest from a JSON string
token_look_up_accessor_request_instance = TokenLookUpAccessorRequest.from_json(json)
# print the JSON string representation of the object
print(TokenLookUpAccessorRequest.to_json())

# convert the object into a dict
token_look_up_accessor_request_dict = token_look_up_accessor_request_instance.to_dict()
# create an instance of TokenLookUpAccessorRequest from a dict
token_look_up_accessor_request_from_dict = TokenLookUpAccessorRequest.from_dict(token_look_up_accessor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


