# PkiImportKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | Optional name to be used for this key | [optional] 
**pem_bundle** | **str** | PEM-format, unencrypted secret key | [optional] 

## Example

```python
from ahvac.models.pki_import_key_request import PkiImportKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiImportKeyRequest from a JSON string
pki_import_key_request_instance = PkiImportKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PkiImportKeyRequest.to_json())

# convert the object into a dict
pki_import_key_request_dict = pki_import_key_request_instance.to_dict()
# create an instance of PkiImportKeyRequest from a dict
pki_import_key_request_from_dict = PkiImportKeyRequest.from_dict(pki_import_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


