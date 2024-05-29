# RekeyAttemptInitializeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **bool** | Specifies if using PGP-encrypted keys, whether Vault should also store a plaintext backup of the PGP-encrypted keys. | [optional] 
**pgp_keys** | **List[str]** | Specifies an array of PGP public keys used to encrypt the output unseal keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as secret_shares. | [optional] 
**require_verification** | **bool** | Turns on verification functionality | [optional] 
**secret_shares** | **int** | Specifies the number of shares to split the unseal key into. | [optional] 
**secret_threshold** | **int** | Specifies the number of shares required to reconstruct the unseal key. This must be less than or equal secret_shares. If using Vault HSM with auto-unsealing, this value must be the same as secret_shares. | [optional] 

## Example

```python
from ahvac.models.rekey_attempt_initialize_request import RekeyAttemptInitializeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyAttemptInitializeRequest from a JSON string
rekey_attempt_initialize_request_instance = RekeyAttemptInitializeRequest.from_json(json)
# print the JSON string representation of the object
print(RekeyAttemptInitializeRequest.to_json())

# convert the object into a dict
rekey_attempt_initialize_request_dict = rekey_attempt_initialize_request_instance.to_dict()
# create an instance of RekeyAttemptInitializeRequest from a dict
rekey_attempt_initialize_request_from_dict = RekeyAttemptInitializeRequest.from_dict(rekey_attempt_initialize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


