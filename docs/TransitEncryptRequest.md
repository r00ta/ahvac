# TransitEncryptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_data** | **str** | When using an AEAD cipher mode, such as AES-GCM, this parameter allows passing associated data (AD/AAD) into the encryption function; this data must be passed on subsequent decryption requests but can be transited in plaintext. On successful decryption, both the ciphertext and the associated data are attested not to have been tampered with. | [optional] 
**batch_input** | **List[object]** | Specifies a list of items to be encrypted in a single batch. When this parameter is set, if the parameters &#39;plaintext&#39;, &#39;context&#39; and &#39;nonce&#39; are also set, they will be ignored. Any batch output will preserve the order of the batch input. | [optional] 
**context** | **str** | Base64 encoded context for key derivation. Required if key derivation is enabled | [optional] 
**convergent_encryption** | **bool** | This parameter will only be used when a key is expected to be created. Whether to support convergent encryption. This is only supported when using a key with key derivation enabled and will require all requests to carry both a context and 96-bit (12-byte) nonce. The given nonce will be used in place of a randomly generated nonce. As a result, when the same context and nonce are supplied, the same ciphertext is generated. It is *very important* when using this mode that you ensure that all nonces are unique for a given context. Failing to do so will severely impact the ciphertext&#39;s security. | [optional] 
**key_version** | **int** | The version of the key to use for encryption. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional] 
**nonce** | **str** | Base64 encoded nonce value. Must be provided if convergent encryption is enabled for this key and the key was generated with Vault 0.6.1. Not required for keys created in 0.6.2+. The value must be exactly 96 bits (12 bytes) long and the user must ensure that for any given context (and thus, any given encryption key) this nonce value is **never reused**. | [optional] 
**partial_failure_response_code** | **int** | Ordinarily, if a batch item fails to encrypt due to a bad input, but other batch items succeed, the HTTP response code is 400 (Bad Request). Some applications may want to treat partial failures differently. Providing the parameter returns the given response code integer instead of a 400 in this case. If all values fail HTTP 400 is still returned. | [optional] 
**plaintext** | **str** | Base64 encoded plaintext value to be encrypted | [optional] 
**type** | **str** | This parameter is required when encryption key is expected to be created. When performing an upsert operation, the type of key to create. Currently, \&quot;aes128-gcm96\&quot; (symmetric) and \&quot;aes256-gcm96\&quot; (symmetric) are the only types supported. Defaults to \&quot;aes256-gcm96\&quot;. | [optional] [default to 'aes256-gcm96']

## Example

```python
from ahvac.models.transit_encrypt_request import TransitEncryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitEncryptRequest from a JSON string
transit_encrypt_request_instance = TransitEncryptRequest.from_json(json)
# print the JSON string representation of the object
print(TransitEncryptRequest.to_json())

# convert the object into a dict
transit_encrypt_request_dict = transit_encrypt_request_instance.to_dict()
# create an instance of TransitEncryptRequest from a dict
transit_encrypt_request_from_dict = TransitEncryptRequest.from_dict(transit_encrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


