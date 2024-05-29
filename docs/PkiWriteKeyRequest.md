# PkiWriteKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | Human-readable name for this key. | [optional] 

## Example

```python
from ahvac.models.pki_write_key_request import PkiWriteKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiWriteKeyRequest from a JSON string
pki_write_key_request_instance = PkiWriteKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PkiWriteKeyRequest.to_json())

# convert the object into a dict
pki_write_key_request_dict = pki_write_key_request_instance.to_dict()
# create an instance of PkiWriteKeyRequest from a dict
pki_write_key_request_from_dict = PkiWriteKeyRequest.from_dict(pki_write_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


