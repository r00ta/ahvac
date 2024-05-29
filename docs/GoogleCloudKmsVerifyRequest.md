# GoogleCloudKmsVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | Digest to verify. This digest must use the same SHA algorithm as the underlying Cloud KMS key. The digest must be the base64-encoded binary value. This field is required. | [optional] 
**key_version** | **int** | Integer version of the crypto key version to use for verification. This field is required. | [optional] 
**signature** | **str** | Base64-encoded signature to use for verification. This field is required. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_verify_request import GoogleCloudKmsVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsVerifyRequest from a JSON string
google_cloud_kms_verify_request_instance = GoogleCloudKmsVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsVerifyRequest.to_json())

# convert the object into a dict
google_cloud_kms_verify_request_dict = google_cloud_kms_verify_request_instance.to_dict()
# create an instance of GoogleCloudKmsVerifyRequest from a dict
google_cloud_kms_verify_request_from_dict = GoogleCloudKmsVerifyRequest.from_dict(google_cloud_kms_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


