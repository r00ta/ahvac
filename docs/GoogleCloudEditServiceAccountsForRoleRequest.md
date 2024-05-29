# GoogleCloudEditServiceAccountsForRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **List[str]** | Service-account emails or IDs to add. | [optional] 
**remove** | **List[str]** | Service-account emails or IDs to remove. | [optional] 

## Example

```python
from ahvac.models.google_cloud_edit_service_accounts_for_role_request import GoogleCloudEditServiceAccountsForRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudEditServiceAccountsForRoleRequest from a JSON string
google_cloud_edit_service_accounts_for_role_request_instance = GoogleCloudEditServiceAccountsForRoleRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudEditServiceAccountsForRoleRequest.to_json())

# convert the object into a dict
google_cloud_edit_service_accounts_for_role_request_dict = google_cloud_edit_service_accounts_for_role_request_instance.to_dict()
# create an instance of GoogleCloudEditServiceAccountsForRoleRequest from a dict
google_cloud_edit_service_accounts_for_role_request_from_dict = GoogleCloudEditServiceAccountsForRoleRequest.from_dict(google_cloud_edit_service_accounts_for_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


