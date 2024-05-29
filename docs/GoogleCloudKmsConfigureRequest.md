# GoogleCloudKmsConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **str** | The credentials to use for authenticating to Google Cloud. Leave this blank to use the Default Application Credentials or instance metadata authentication. | [optional] 
**scopes** | **List[str]** | The list of full-URL scopes to request when authenticating. By default, this requests https://www.googleapis.com/auth/cloudkms. | [optional] 

## Example

```python
from ahvac.models.google_cloud_kms_configure_request import GoogleCloudKmsConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudKmsConfigureRequest from a JSON string
google_cloud_kms_configure_request_instance = GoogleCloudKmsConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudKmsConfigureRequest.to_json())

# convert the object into a dict
google_cloud_kms_configure_request_dict = google_cloud_kms_configure_request_instance.to_dict()
# create an instance of GoogleCloudKmsConfigureRequest from a dict
google_cloud_kms_configure_request_from_dict = GoogleCloudKmsConfigureRequest.from_dict(google_cloud_kms_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


