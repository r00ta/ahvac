# GoogleCloudKmsConfigureKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_version** | **int** | Maximum allowed crypto key version. If set to a positive value, key versions greater than the given value are not permitted to be used. If set to 0 or a negative value, there is no maximum key version. | [optional] 
**min_version** | **int** | Minimum allowed crypto key version. If set to a positive value, key versions less than the given value are not permitted to be used. If set to 0 or a negative value, there is no minimum key version. This value only affects encryption/re-encryption, not decryption. To restrict old values from being decrypted, increase this value and then perform a trim operation. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_configure_key_request import GoogleCloudKmsConfigureKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsConfigureKeyRequest from a JSON string
google_cloud_kms_configure_key_request_instance = GoogleCloudKmsConfigureKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsConfigureKeyRequest.to_json())

# convert the object into a dict
google_cloud_kms_configure_key_request_dict = google_cloud_kms_configure_key_request_instance.to_dict()
# create an instance of GoogleCloudKmsConfigureKeyRequest from a dict
google_cloud_kms_configure_key_request_from_dict = GoogleCloudKmsConfigureKeyRequest.from_dict(google_cloud_kms_configure_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


