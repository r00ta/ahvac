# GoogleCloudWriteImpersonatedAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_email** | **str** | Required. Email of the GCP service account to manage. Cannot be updated. | [optional] 
**token_scopes** | **List[str]** | List of OAuth scopes to assign to access tokens generated under this account. | [optional] 
**ttl** | **str** | Lifetime of the token for the impersonated account. | [optional] 

## Example

```python
from ahvac.models.google_cloud_write_impersonated_account_request import GoogleCloudWriteImpersonatedAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudWriteImpersonatedAccountRequest from a JSON string
google_cloud_write_impersonated_account_request_instance = GoogleCloudWriteImpersonatedAccountRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudWriteImpersonatedAccountRequest.to_json())

# convert the object into a dict
google_cloud_write_impersonated_account_request_dict = google_cloud_write_impersonated_account_request_instance.to_dict()
# create an instance of GoogleCloudWriteImpersonatedAccountRequest from a dict
google_cloud_write_impersonated_account_request_from_dict = GoogleCloudWriteImpersonatedAccountRequest.from_dict(google_cloud_write_impersonated_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


