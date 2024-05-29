# GoogleCloudKmsReencryptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_authenticated_data** | **str** | Optional data that, if specified, must also be provided during decryption. | [optional] 
**ciphertext** | **str** | Ciphertext to be re-encrypted to the latest key version. This must be ciphertext that Vault previously generated for this named key. | [optional] 
**key_version** | **int** | Integer version of the crypto key version to use for the new encryption. If unspecified, this defaults to the latest active crypto key version. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_reencrypt_request import GoogleCloudKmsReencryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsReencryptRequest from a JSON string
google_cloud_kms_reencrypt_request_instance = GoogleCloudKmsReencryptRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsReencryptRequest.to_json())

# convert the object into a dict
google_cloud_kms_reencrypt_request_dict = google_cloud_kms_reencrypt_request_instance.to_dict()
# create an instance of GoogleCloudKmsReencryptRequest from a dict
google_cloud_kms_reencrypt_request_from_dict = GoogleCloudKmsReencryptRequest.from_dict(google_cloud_kms_reencrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


