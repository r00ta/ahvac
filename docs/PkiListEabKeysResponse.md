# PkiListEabKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_info** | **object** | EAB details keyed by the eab key id | [optional] 
**keys** | **List[str]** | A list of unused eab keys | [optional] 

## Example

```python
from ahvac.models.pki_list_eab_keys_response import PkiListEabKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiListEabKeysResponse from a JSON string
pki_list_eab_keys_response_instance = PkiListEabKeysResponse.from_json(json)
# print the JSON string representation of the object
print(PkiListEabKeysResponse.to_json())

# convert the object into a dict
pki_list_eab_keys_response_dict = pki_list_eab_keys_response_instance.to_dict()
# create an instance of PkiListEabKeysResponse from a dict
pki_list_eab_keys_response_from_dict = PkiListEabKeysResponse.from_dict(pki_list_eab_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


