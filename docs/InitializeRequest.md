# InitializeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pgp_keys** | **List[str]** | Specifies an array of PGP public keys used to encrypt the output unseal keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as &#x60;secret_shares&#x60;. | [optional] 
**recovery_pgp_keys** | **List[str]** | Specifies an array of PGP public keys used to encrypt the output recovery keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as &#x60;recovery_shares&#x60;. | [optional] 
**recovery_shares** | **int** | Specifies the number of shares to split the recovery key into. | [optional] 
**recovery_threshold** | **int** | Specifies the number of shares required to reconstruct the recovery key. This must be less than or equal to &#x60;recovery_shares&#x60;. | [optional] 
**root_token_pgp_key** | **str** | Specifies a PGP public key used to encrypt the initial root token. The key must be base64-encoded from its original binary representation. | [optional] 
**secret_shares** | **int** | Specifies the number of shares to split the unseal key into. | [optional] 
**secret_threshold** | **int** | Specifies the number of shares required to reconstruct the unseal key. This must be less than or equal secret_shares. If using Vault HSM with auto-unsealing, this value must be the same as &#x60;secret_shares&#x60;. | [optional] 
**stored_shares** | **int** | Specifies the number of shares that should be encrypted by the HSM and stored for auto-unsealing. Currently must be the same as &#x60;secret_shares&#x60;. | [optional] 

## Example

```python
from ahvac.models.initialize_request import InitializeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeRequest from a JSON string
initialize_request_instance = InitializeRequest.from_json(json)
# print the JSON string representation of the object
print(InitializeRequest.to_json())

# convert the object into a dict
initialize_request_dict = initialize_request_instance.to_dict()
# create an instance of InitializeRequest from a dict
initialize_request_from_dict = InitializeRequest.from_dict(initialize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


