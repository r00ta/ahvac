# TokenLookUpSelf2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token to look up (unused, does not need to be set) | [optional] 

## Example

```python
from ahvac.models.token_look_up_self2_request import TokenLookUpSelf2Request

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLookUpSelf2Request from a JSON string
token_look_up_self2_request_instance = TokenLookUpSelf2Request.from_json(json)
# print the JSON string representation of the object
print(TokenLookUpSelf2Request.to_json())

# convert the object into a dict
token_look_up_self2_request_dict = token_look_up_self2_request_instance.to_dict()
# create an instance of TokenLookUpSelf2Request from a dict
token_look_up_self2_request_from_dict = TokenLookUpSelf2Request.from_dict(token_look_up_self2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


