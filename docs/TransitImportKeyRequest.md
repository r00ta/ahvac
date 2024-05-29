# TransitImportKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_plaintext_backup** | **bool** | Enables taking a backup of the named key in plaintext format. Once set, this cannot be disabled. | [optional] 
**allow_rotation** | **bool** | True if the imported key may be rotated within Vault; false otherwise. | [optional] 
**auto_rotate_period** | **str** | Amount of time the key should live before being automatically rotated. A value of 0 (default) disables automatic rotation for the key. | [optional] [default to '0']
**ciphertext** | **str** | The base64-encoded ciphertext of the keys. The AES key should be encrypted using OAEP with the wrapping key and then concatenated with the import key, wrapped by the AES key. | [optional] 
**context** | **str** | Base64 encoded context for key derivation. When reading a key with key derivation enabled, if the key type supports public keys, this will return the public key for the given context. | [optional] 
**derived** | **bool** | Enables key derivation mode. This allows for per-transaction unique keys for encryption operations. | [optional] 
**exportable** | **bool** | Enables keys to be exportable. This allows for all the valid keys in the key ring to be exported. | [optional] 
**hash_function** | **str** | The hash function used as a random oracle in the OAEP wrapping of the user-generated, ephemeral AES key. Can be one of \&quot;SHA1\&quot;, \&quot;SHA224\&quot;, \&quot;SHA256\&quot; (default), \&quot;SHA384\&quot;, or \&quot;SHA512\&quot; | [optional] [default to 'SHA256']
**public_key** | **str** | The plaintext PEM public key to be imported. If \&quot;ciphertext\&quot; is set, this field is ignored. | [optional] 
**type** | **str** | The type of key being imported. Currently, \&quot;aes128-gcm96\&quot; (symmetric), \&quot;aes256-gcm96\&quot; (symmetric), \&quot;ecdsa-p256\&quot; (asymmetric), \&quot;ecdsa-p384\&quot; (asymmetric), \&quot;ecdsa-p521\&quot; (asymmetric), \&quot;ed25519\&quot; (asymmetric), \&quot;rsa-2048\&quot; (asymmetric), \&quot;rsa-3072\&quot; (asymmetric), \&quot;rsa-4096\&quot; (asymmetric) are supported. Defaults to \&quot;aes256-gcm96\&quot;. | [optional] [default to 'aes256-gcm96']

## Example

```python
from ahvac.models.transit_import_key_request import TransitImportKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitImportKeyRequest from a JSON string
transit_import_key_request_instance = TransitImportKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitImportKeyRequest.to_json())

# convert the object into a dict
transit_import_key_request_dict = transit_import_key_request_instance.to_dict()
# create an instance of TransitImportKeyRequest from a dict
transit_import_key_request_from_dict = TransitImportKeyRequest.from_dict(transit_import_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


