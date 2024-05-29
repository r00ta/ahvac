# KvV2ReadSubkeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**subkeys** | **object** |  | [optional] 

## Example

```python
from ahvac.models.kv_v2_read_subkeys_response import KvV2ReadSubkeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2ReadSubkeysResponse from a JSON string
kv_v2_read_subkeys_response_instance = KvV2ReadSubkeysResponse.from_json(json)
# print the JSON string representation of the object
print(KvV2ReadSubkeysResponse.to_json())

# convert the object into a dict
kv_v2_read_subkeys_response_dict = kv_v2_read_subkeys_response_instance.to_dict()
# create an instance of KvV2ReadSubkeysResponse from a dict
kv_v2_read_subkeys_response_from_dict = KvV2ReadSubkeysResponse.from_dict(kv_v2_read_subkeys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


