# GoogleCloudLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | A signed JWT. This is either a self-signed service account JWT (&#39;iam&#39; roles only) or a GCE identity metadata token (&#39;iam&#39;, &#39;gce&#39; roles). | [optional] 
**role** | **str** | Name of the role against which the login is being attempted. Required. | [optional] 

## Example

```python
from ahvac.models.google_cloud_login_request import GoogleCloudLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudLoginRequest from a JSON string
google_cloud_login_request_instance = GoogleCloudLoginRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudLoginRequest.to_json())

# convert the object into a dict
google_cloud_login_request_dict = google_cloud_login_request_instance.to_dict()
# create an instance of GoogleCloudLoginRequest from a dict
google_cloud_login_request_from_dict = GoogleCloudLoginRequest.from_dict(google_cloud_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


