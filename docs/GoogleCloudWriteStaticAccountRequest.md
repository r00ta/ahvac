# GoogleCloudWriteStaticAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | **str** | Bindings configuration string. | [optional] 
**secret_type** | **str** | Type of secret generated for this account. Cannot be updated. Defaults to \&quot;access_token\&quot; | [optional] [default to 'access_token']
**service_account_email** | **str** | Required. Email of the GCP service account to manage. Cannot be updated. | [optional] 
**token_scopes** | **List[str]** | List of OAuth scopes to assign to access tokens generated under this account. Ignored if \&quot;secret_type\&quot; is not \&quot;\&quot;access_token\&quot;\&quot; | [optional] 

## Example

```python
from ahvac.models.google_cloud_write_static_account_request import GoogleCloudWriteStaticAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudWriteStaticAccountRequest from a JSON string
google_cloud_write_static_account_request_instance = GoogleCloudWriteStaticAccountRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudWriteStaticAccountRequest.to_json())

# convert the object into a dict
google_cloud_write_static_account_request_dict = google_cloud_write_static_account_request_instance.to_dict()
# create an instance of GoogleCloudWriteStaticAccountRequest from a dict
google_cloud_write_static_account_request_from_dict = GoogleCloudWriteStaticAccountRequest.from_dict(google_cloud_write_static_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


