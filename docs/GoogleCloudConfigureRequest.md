# GoogleCloudConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **str** | GCP IAM service account credentials JSON with permissions to create new service accounts and set IAM policies | [optional] 
**max_ttl** | **str** | Maximum time a service account key is valid for. If &lt;&#x3D; 0, will use system default. | [optional] 
**ttl** | **str** | Default lease for generated keys. If &lt;&#x3D; 0, will use system default. | [optional] 

## Example

```python
from ahvac.models.google_cloud_configure_request import GoogleCloudConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudConfigureRequest from a JSON string
google_cloud_configure_request_instance = GoogleCloudConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudConfigureRequest.to_json())

# convert the object into a dict
google_cloud_configure_request_dict = google_cloud_configure_request_instance.to_dict()
# create an instance of GoogleCloudConfigureRequest from a dict
google_cloud_configure_request_from_dict = GoogleCloudConfigureRequest.from_dict(google_cloud_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


