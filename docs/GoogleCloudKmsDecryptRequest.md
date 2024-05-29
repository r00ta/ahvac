# GoogleCloudKmsDecryptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_authenticated_data** | **str** | Optional data that was specified during encryption of this payload. | [optional] 
**ciphertext** | **str** | Ciphertext to decrypt as previously returned from an encrypt operation. This must be base64-encoded ciphertext as previously returned from an encrypt operation. | [optional] 
**key_version** | **int** | Integer version of the crypto key version to use for decryption. This is required for asymmetric keys. For symmetric keys, Cloud KMS will choose the correct version automatically. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_decrypt_request import GoogleCloudKmsDecryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsDecryptRequest from a JSON string
google_cloud_kms_decrypt_request_instance = GoogleCloudKmsDecryptRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsDecryptRequest.to_json())

# convert the object into a dict
google_cloud_kms_decrypt_request_dict = google_cloud_kms_decrypt_request_instance.to_dict()
# create an instance of GoogleCloudKmsDecryptRequest from a dict
google_cloud_kms_decrypt_request_from_dict = GoogleCloudKmsDecryptRequest.from_dict(google_cloud_kms_decrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


