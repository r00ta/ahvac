# PkiReadKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Key Id | [optional] 
**key_name** | **str** | Key Name | [optional] 
**key_type** | **str** | Key Type | [optional] 
**managed_key_id** | **str** | Managed Key Id | [optional] 
**managed_key_name** | **str** | Managed Key Name | [optional] 
**subject_key_id** | **str** | RFC 5280 Subject Key Identifier of the public counterpart | [optional] 

## Example

```python
from ahvac.models.pki_read_key_response import PkiReadKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadKeyResponse from a JSON string
pki_read_key_response_instance = PkiReadKeyResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadKeyResponse.to_json())

# convert the object into a dict
pki_read_key_response_dict = pki_read_key_response_instance.to_dict()
# create an instance of PkiReadKeyResponse from a dict
pki_read_key_response_from_dict = PkiReadKeyResponse.from_dict(pki_read_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


