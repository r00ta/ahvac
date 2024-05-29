# RootTokenGenerationInitialize2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pgp_key** | **str** | Specifies a base64-encoded PGP public key. | [optional] 

## Example

```python
from ahvac.models.root_token_generation_initialize2_request import RootTokenGenerationInitialize2Request

# TODO update the JSON string below
json = "{}"
# create an instance of RootTokenGenerationInitialize2Request from a JSON string
root_token_generation_initialize2_request_instance = RootTokenGenerationInitialize2Request.from_json(json)
# print the JSON string representation of the object
print(RootTokenGenerationInitialize2Request.to_json())

# convert the object into a dict
root_token_generation_initialize2_request_dict = root_token_generation_initialize2_request_instance.to_dict()
# create an instance of RootTokenGenerationInitialize2Request from a dict
root_token_generation_initialize2_request_from_dict = RootTokenGenerationInitialize2Request.from_dict(root_token_generation_initialize2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


