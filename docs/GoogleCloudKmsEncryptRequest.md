# GoogleCloudKmsEncryptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_authenticated_data** | **str** | Optional base64-encoded data that, if specified, must also be provided to decrypt this payload. | [optional] 
**key_version** | **int** | Integer version of the crypto key version to use for encryption. If unspecified, this defaults to the latest active crypto key version. | [optional] 
**plaintext** | **str** | Plaintext value to be encrypted. This can be a string or binary, but the size is limited. See the Google Cloud KMS documentation for information on size limitations by key types. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_encrypt_request import GoogleCloudKmsEncryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsEncryptRequest from a JSON string
google_cloud_kms_encrypt_request_instance = GoogleCloudKmsEncryptRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsEncryptRequest.to_json())

# convert the object into a dict
google_cloud_kms_encrypt_request_dict = google_cloud_kms_encrypt_request_instance.to_dict()
# create an instance of GoogleCloudKmsEncryptRequest from a dict
google_cloud_kms_encrypt_request_from_dict = GoogleCloudKmsEncryptRequest.from_dict(google_cloud_kms_encrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


