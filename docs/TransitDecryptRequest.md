# TransitDecryptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_data** | **str** | When using an AEAD cipher mode, such as AES-GCM, this parameter allows passing associated data (AD/AAD) into the encryption function; this data must be passed on subsequent decryption requests but can be transited in plaintext. On successful decryption, both the ciphertext and the associated data are attested not to have been tampered with. | [optional] 
**batch_input** | **List[object]** | Specifies a list of items to be decrypted in a single batch. When this parameter is set, if the parameters &#39;ciphertext&#39;, &#39;context&#39; and &#39;nonce&#39; are also set, they will be ignored. Any batch output will preserve the order of the batch input. | [optional] 
**ciphertext** | **str** | The ciphertext to decrypt, provided as returned by encrypt. | [optional] 
**context** | **str** | Base64 encoded context for key derivation. Required if key derivation is enabled. | [optional] 
**nonce** | **str** | Base64 encoded nonce value used during encryption. Must be provided if convergent encryption is enabled for this key and the key was generated with Vault 0.6.1. Not required for keys created in 0.6.2+. | [optional] 
**partial_failure_response_code** | **int** | Ordinarily, if a batch item fails to decrypt due to a bad input, but other batch items succeed, the HTTP response code is 400 (Bad Request). Some applications may want to treat partial failures differently. Providing the parameter returns the given response code integer instead of a 400 in this case. If all values fail HTTP 400 is still returned. | [optional] 

## Example

```python
from ahvac.models.transit_decrypt_request import TransitDecryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitDecryptRequest from a JSON string
transit_decrypt_request_instance = TransitDecryptRequest.from_json(json)
# print the JSON string representation of the object
print(TransitDecryptRequest.to_json())

# convert the object into a dict
transit_decrypt_request_dict = transit_decrypt_request_instance.to_dict()
# create an instance of TransitDecryptRequest from a dict
transit_decrypt_request_from_dict = TransitDecryptRequest.from_dict(transit_decrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


