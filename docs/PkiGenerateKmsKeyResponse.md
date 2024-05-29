# PkiGenerateKmsKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | ID assigned to this key. | [optional] 
**key_name** | **str** | Name assigned to this key. | [optional] 
**key_type** | **str** | The type of key to use; defaults to RSA. \&quot;rsa\&quot; \&quot;ec\&quot; and \&quot;ed25519\&quot; are the only valid values. | [optional] 
**private_key** | **str** | The private key string | [optional] 

## Example

```python
from ahvac.models.pki_generate_kms_key_response import PkiGenerateKmsKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiGenerateKmsKeyResponse from a JSON string
pki_generate_kms_key_response_instance = PkiGenerateKmsKeyResponse.from_json(json)
# print the JSON string representation of the object
print(PkiGenerateKmsKeyResponse.to_json())

# convert the object into a dict
pki_generate_kms_key_response_dict = pki_generate_kms_key_response_instance.to_dict()
# create an instance of PkiGenerateKmsKeyResponse from a dict
pki_generate_kms_key_response_from_dict = PkiGenerateKmsKeyResponse.from_dict(pki_generate_kms_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


