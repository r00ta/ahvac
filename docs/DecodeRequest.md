# DecodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoded_token** | **str** | Specifies the encoded token (result from generate-root). | [optional] 
**otp** | **str** | Specifies the otp code for decode. | [optional] 

## Example

```python
from ahvac.models.decode_request import DecodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRequest from a JSON string
decode_request_instance = DecodeRequest.from_json(json)
# print the JSON string representation of the object
print(DecodeRequest.to_json())

# convert the object into a dict
decode_request_dict = decode_request_instance.to_dict()
# create an instance of DecodeRequest from a dict
decode_request_from_dict = DecodeRequest.from_dict(decode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


