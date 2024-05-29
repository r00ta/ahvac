# GoogleCloudKmsRegisterKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_key** | **str** | Full resource ID of the crypto key including the project, location, key ring, and crypto key like \&quot;projects/%s/locations/%s/keyRings/%s/cryptoKeys/%s\&quot;. This crypto key must already exist in Google Cloud KMS unless verify is set to \&quot;false\&quot;. | [optional] 
**verify** | **bool** | Verify that the given Google Cloud KMS crypto key exists and is accessible before creating the storage entry in Vault. Set this to \&quot;false\&quot; if the key will not exist at creation time. | [optional] [default to True]

## Example

```python
from ahvac.models.google_cloud_kms_register_key_request import GoogleCloudKmsRegisterKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsRegisterKeyRequest from a JSON string
google_cloud_kms_register_key_request_instance = GoogleCloudKmsRegisterKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsRegisterKeyRequest.to_json())

# convert the object into a dict
google_cloud_kms_register_key_request_dict = google_cloud_kms_register_key_request_instance.to_dict()
# create an instance of GoogleCloudKmsRegisterKeyRequest from a dict
google_cloud_kms_register_key_request_from_dict = GoogleCloudKmsRegisterKeyRequest.from_dict(google_cloud_kms_register_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


