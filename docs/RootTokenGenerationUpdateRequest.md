# RootTokenGenerationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies a single unseal key share. | [optional] 
**nonce** | **str** | Specifies the nonce of the attempt. | [optional] 

## Example

```python
from ahvac.models.root_token_generation_update_request import RootTokenGenerationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RootTokenGenerationUpdateRequest from a JSON string
root_token_generation_update_request_instance = RootTokenGenerationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RootTokenGenerationUpdateRequest.to_json())

# convert the object into a dict
root_token_generation_update_request_dict = root_token_generation_update_request_instance.to_dict()
# create an instance of RootTokenGenerationUpdateRequest from a dict
root_token_generation_update_request_from_dict = RootTokenGenerationUpdateRequest.from_dict(root_token_generation_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


