# PkiWriteKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Key Id | [optional] 
**key_name** | **str** | Key Name | [optional] 
**key_type** | **str** | Key Type | [optional] 

## Example

```python
from ahvac.models.pki_write_key_response import PkiWriteKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiWriteKeyResponse from a JSON string
pki_write_key_response_instance = PkiWriteKeyResponse.from_json(json)
# print the JSON string representation of the object
print(PkiWriteKeyResponse.to_json())

# convert the object into a dict
pki_write_key_response_dict = pki_write_key_response_instance.to_dict()
# create an instance of PkiWriteKeyResponse from a dict
pki_write_key_response_from_dict = PkiWriteKeyResponse.from_dict(pki_write_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


