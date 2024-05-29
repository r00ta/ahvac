# GoogleCloudKmsSignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | Digest to sign. This digest must use the same SHA algorithm as the underlying Cloud KMS key. The digest must be the base64-encoded binary value. This field is required. | [optional] 
**key_version** | **int** | Integer version of the crypto key version to use for signing. This field is required. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_sign_request import GoogleCloudKmsSignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsSignRequest from a JSON string
google_cloud_kms_sign_request_instance = GoogleCloudKmsSignRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsSignRequest.to_json())

# convert the object into a dict
google_cloud_kms_sign_request_dict = google_cloud_kms_sign_request_instance.to_dict()
# create an instance of GoogleCloudKmsSignRequest from a dict
google_cloud_kms_sign_request_from_dict = GoogleCloudKmsSignRequest.from_dict(google_cloud_kms_sign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


