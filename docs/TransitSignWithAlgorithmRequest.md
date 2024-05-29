# TransitSignWithAlgorithmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Deprecated: use \&quot;hash_algorithm\&quot; instead. | [optional] [default to 'sha2-256']
**batch_input** | **List[object]** | Specifies a list of items for processing. When this parameter is set, any supplied &#39;input&#39; or &#39;context&#39; parameters will be ignored. Responses are returned in the &#39;batch_results&#39; array component of the &#39;data&#39; element of the response. Any batch output will preserve the order of the batch input | [optional] 
**context** | **str** | Base64 encoded context for key derivation. Required if key derivation is enabled; currently only available with ed25519 keys. | [optional] 
**hash_algorithm** | **str** | Hash algorithm to use (POST body parameter). Valid values are: * sha1 * sha2-224 * sha2-256 * sha2-384 * sha2-512 * sha3-224 * sha3-256 * sha3-384 * sha3-512 * none Defaults to \&quot;sha2-256\&quot;. Not valid for all key types, including ed25519. Using none requires setting prehashed&#x3D;true and signature_algorithm&#x3D;pkcs1v15, yielding a PKCSv1_5_NoOID instead of the usual PKCSv1_5_DERnull signature. | [optional] [default to 'sha2-256']
**input** | **str** | The base64-encoded input data | [optional] 
**key_version** | **int** | The version of the key to use for signing. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional] 
**marshaling_algorithm** | **str** | The method by which to marshal the signature. The default is &#39;asn1&#39; which is used by openssl and X.509. It can also be set to &#39;jws&#39; which is used for JWT signatures; setting it to this will also cause the encoding of the signature to be url-safe base64 instead of using standard base64 encoding. Currently only valid for ECDSA P-256 key types\&quot;. | [optional] [default to 'asn1']
**prehashed** | **bool** | Set to &#39;true&#39; when the input is already hashed. If the key type is &#39;rsa-2048&#39;, &#39;rsa-3072&#39; or &#39;rsa-4096&#39;, then the algorithm used to hash the input should be indicated by the &#39;algorithm&#39; parameter. | [optional] 
**salt_length** | **str** | The salt length used to sign. Currently only applies to the RSA PSS signature scheme. Options are &#39;auto&#39; (the default used by Golang, causing the salt to be as large as possible when signing), &#39;hash&#39; (causes the salt length to equal the length of the hash used in the signature), or an integer between the minimum and the maximum permissible salt lengths for the given RSA key size. Defaults to &#39;auto&#39;. | [optional] [default to 'auto']
**signature_algorithm** | **str** | The signature algorithm to use for signing. Currently only applies to RSA key types. Options are &#39;pss&#39; or &#39;pkcs1v15&#39;. Defaults to &#39;pss&#39; | [optional] 

## Example

```python
from ahvac.models.transit_sign_with_algorithm_request import TransitSignWithAlgorithmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitSignWithAlgorithmRequest from a JSON string
transit_sign_with_algorithm_request_instance = TransitSignWithAlgorithmRequest.from_json(json)
# print the JSON string representation of the object
print(TransitSignWithAlgorithmRequest.to_json())

# convert the object into a dict
transit_sign_with_algorithm_request_dict = transit_sign_with_algorithm_request_instance.to_dict()
# create an instance of TransitSignWithAlgorithmRequest from a dict
transit_sign_with_algorithm_request_from_dict = TransitSignWithAlgorithmRequest.from_dict(transit_sign_with_algorithm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


