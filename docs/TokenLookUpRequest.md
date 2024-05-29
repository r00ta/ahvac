# TokenLookUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token to lookup | [optional] 

## Example

```python
from ahvac.models.token_look_up_request import TokenLookUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLookUpRequest from a JSON string
token_look_up_request_instance = TokenLookUpRequest.from_json(json)
# print the JSON string representation of the object
print(TokenLookUpRequest.to_json())

# convert the object into a dict
token_look_up_request_dict = token_look_up_request_instance.to_dict()
# create an instance of TokenLookUpRequest from a dict
token_look_up_request_from_dict = TokenLookUpRequest.from_dict(token_look_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


