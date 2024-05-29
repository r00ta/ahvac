# GoogleCloudKmsWriteKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Algorithm to use for encryption, decryption, or signing. The value depends on the key purpose. The value cannot be changed after creation. For a key purpose of \&quot;encrypt_decrypt\&quot;, the valid values are: - symmetric_encryption (default) For a key purpose of \&quot;asymmetric_sign\&quot;, valid values are: - rsa_sign_pss_2048_sha256 - rsa_sign_pss_3072_sha256 - rsa_sign_pss_4096_sha256 - rsa_sign_pkcs1_2048_sha256 - rsa_sign_pkcs1_3072_sha256 - rsa_sign_pkcs1_4096_sha256 - ec_sign_p256_sha256 - ec_sign_p384_sha384 For a key purpose of \&quot;asymmetric_decrypt\&quot;, valid values are: - rsa_decrypt_oaep_2048_sha256 - rsa_decrypt_oaep_3072_sha256 - rsa_decrypt_oaep_4096_sha256 | [optional] 
**crypto_key** | **str** | Name of the crypto key to use. If the given crypto key does not exist, Vault will try to create it. This defaults to the name of the key given to Vault as the parameter if unspecified. | [optional] 
**key_ring** | **str** | Full Google Cloud resource ID of the key ring with the project and location (e.g. projects/my-project/locations/global/keyRings/my-keyring). If the given key ring does not exist, Vault will try to create it during a create operation. | [optional] 
**labels** | **object** | Arbitrary key&#x3D;value label to apply to the crypto key. To specify multiple labels, specify this argument multiple times (e.g. labels&#x3D;\&quot;a&#x3D;b\&quot; labels&#x3D;\&quot;c&#x3D;d\&quot;). | [optional] 
**protection_level** | **str** | Level of protection to use for the key management. Valid values are \&quot;software\&quot; and \&quot;hsm\&quot;. The default value is \&quot;software\&quot;. The value cannot be changed after creation. | [optional] 
**purpose** | **str** | Purpose of the key. Valid options are \&quot;asymmetric_decrypt\&quot;, \&quot;asymmetric_sign\&quot;, and \&quot;encrypt_decrypt\&quot;. The default value is \&quot;encrypt_decrypt\&quot;. The value cannot be changed after creation. | [optional] 
**rotation_period** | **str** | Amount of time between crypto key version rotations. This is specified as a time duration value like 72h (72 hours). The smallest possible value is 24h. This value only applies to keys with a purpose of \&quot;encrypt_decrypt\&quot;. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_write_key_request import GoogleCloudKmsWriteKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsWriteKeyRequest from a JSON string
google_cloud_kms_write_key_request_instance = GoogleCloudKmsWriteKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsWriteKeyRequest.to_json())

# convert the object into a dict
google_cloud_kms_write_key_request_dict = google_cloud_kms_write_key_request_instance.to_dict()
# create an instance of GoogleCloudKmsWriteKeyRequest from a dict
google_cloud_kms_write_key_request_from_dict = GoogleCloudKmsWriteKeyRequest.from_dict(google_cloud_kms_write_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


