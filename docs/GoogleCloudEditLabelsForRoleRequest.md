# GoogleCloudEditLabelsForRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **List[str]** | BoundLabels to add (in $key:$value) | [optional] 
**remove** | **List[str]** | Label key values to remove | [optional] 

## Example

```python
from ahvac.models.google_cloud_edit_labels_for_role_request import GoogleCloudEditLabelsForRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudEditLabelsForRoleRequest from a JSON string
google_cloud_edit_labels_for_role_request_instance = GoogleCloudEditLabelsForRoleRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudEditLabelsForRoleRequest.to_json())

# convert the object into a dict
google_cloud_edit_labels_for_role_request_dict = google_cloud_edit_labels_for_role_request_instance.to_dict()
# create an instance of GoogleCloudEditLabelsForRoleRequest from a dict
google_cloud_edit_labels_for_role_request_from_dict = GoogleCloudEditLabelsForRoleRequest.from_dict(google_cloud_edit_labels_for_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


