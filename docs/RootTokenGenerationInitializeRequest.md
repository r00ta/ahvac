# RootTokenGenerationInitializeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pgp_key** | **str** | Specifies a base64-encoded PGP public key. | [optional] 

## Example

```python
from ahvac.models.root_token_generation_initialize_request import RootTokenGenerationInitializeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RootTokenGenerationInitializeRequest from a JSON string
root_token_generation_initialize_request_instance = RootTokenGenerationInitializeRequest.from_json(json)
# print the JSON string representation of the object
print(RootTokenGenerationInitializeRequest.to_json())

# convert the object into a dict
root_token_generation_initialize_request_dict = root_token_generation_initialize_request_instance.to_dict()
# create an instance of RootTokenGenerationInitializeRequest from a dict
root_token_generation_initialize_request_from_dict = RootTokenGenerationInitializeRequest.from_dict(root_token_generation_initialize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


