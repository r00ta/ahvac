# PkiGenerateExportedKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_bits** | **int** | The number of bits to use. Allowed values are 0 (universal default); with rsa key_type: 2048 (default), 3072, or 4096; with ec key_type: 224, 256 (default), 384, or 521; ignored with ed25519. | [optional] [default to 0]
**key_name** | **str** | Optional name to be used for this key | [optional] 
**key_type** | **str** | The type of key to use; defaults to RSA. \&quot;rsa\&quot; \&quot;ec\&quot; and \&quot;ed25519\&quot; are the only valid values. | [optional] [default to 'rsa']
**managed_key_id** | **str** | The name of the managed key to use when the exported type is kms. When kms type is the key type, this field or managed_key_name is required. Ignored for other types. | [optional] 
**managed_key_name** | **str** | The name of the managed key to use when the exported type is kms. When kms type is the key type, this field or managed_key_id is required. Ignored for other types. | [optional] 

## Example

```python
from ahvac.models.pki_generate_exported_key_request import PkiGenerateExportedKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiGenerateExportedKeyRequest from a JSON string
pki_generate_exported_key_request_instance = PkiGenerateExportedKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PkiGenerateExportedKeyRequest.to_json())

# convert the object into a dict
pki_generate_exported_key_request_dict = pki_generate_exported_key_request_instance.to_dict()
# create an instance of PkiGenerateExportedKeyRequest from a dict
pki_generate_exported_key_request_from_dict = PkiGenerateExportedKeyRequest.from_dict(pki_generate_exported_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


