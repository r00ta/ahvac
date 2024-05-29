# RootTokenGenerationUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** |  | [optional] 
**encoded_root_token** | **str** |  | [optional] 
**encoded_token** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 
**otp** | **str** |  | [optional] 
**otp_length** | **int** |  | [optional] 
**pgp_fingerprint** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**required** | **int** |  | [optional] 
**started** | **bool** |  | [optional] 

## Example

```python
from ahvac.models.root_token_generation_update_response import RootTokenGenerationUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RootTokenGenerationUpdateResponse from a JSON string
root_token_generation_update_response_instance = RootTokenGenerationUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RootTokenGenerationUpdateResponse.to_json())

# convert the object into a dict
root_token_generation_update_response_dict = root_token_generation_update_response_instance.to_dict()
# create an instance of RootTokenGenerationUpdateResponse from a dict
root_token_generation_update_response_from_dict = RootTokenGenerationUpdateResponse.from_dict(root_token_generation_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


