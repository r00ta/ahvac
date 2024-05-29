# GoogleCloudWriteRolesetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | **str** | Bindings configuration string. | [optional] 
**project** | **str** | Name of the GCP project that this roleset&#39;s service account will belong to. | [optional] 
**secret_type** | **str** | Type of secret generated for this role set. Defaults to &#39;access_token&#39; | [optional] [default to 'access_token']
**token_scopes** | **List[str]** | List of OAuth scopes to assign to credentials generated under this role set | [optional] 

## Example

```python
from ahvac.models.google_cloud_write_roleset_request import GoogleCloudWriteRolesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudWriteRolesetRequest from a JSON string
google_cloud_write_roleset_request_instance = GoogleCloudWriteRolesetRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudWriteRolesetRequest.to_json())

# convert the object into a dict
google_cloud_write_roleset_request_dict = google_cloud_write_roleset_request_instance.to_dict()
# create an instance of GoogleCloudWriteRolesetRequest from a dict
google_cloud_write_roleset_request_from_dict = GoogleCloudWriteRolesetRequest.from_dict(google_cloud_write_roleset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


