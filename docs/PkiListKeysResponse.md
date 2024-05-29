# PkiListKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_info** | **object** | Key info with issuer name | [optional] 
**keys** | **List[str]** | A list of keys | [optional] 

## Example

```python
from ahvac.models.pki_list_keys_response import PkiListKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiListKeysResponse from a JSON string
pki_list_keys_response_instance = PkiListKeysResponse.from_json(json)
# print the JSON string representation of the object
print(PkiListKeysResponse.to_json())

# convert the object into a dict
pki_list_keys_response_dict = pki_list_keys_response_instance.to_dict()
# create an instance of PkiListKeysResponse from a dict
pki_list_keys_response_from_dict = PkiListKeysResponse.from_dict(pki_list_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


