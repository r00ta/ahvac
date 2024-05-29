# OidcWriteAssignmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_ids** | **List[str]** | Comma separated string or array of identity entity IDs | [optional] 
**group_ids** | **List[str]** | Comma separated string or array of identity group IDs | [optional] 

## Example

```python
from ahvac.models.oidc_write_assignment_request import OidcWriteAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcWriteAssignmentRequest from a JSON string
oidc_write_assignment_request_instance = OidcWriteAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(OidcWriteAssignmentRequest.to_json())

# convert the object into a dict
oidc_write_assignment_request_dict = oidc_write_assignment_request_instance.to_dict()
# create an instance of OidcWriteAssignmentRequest from a dict
oidc_write_assignment_request_from_dict = OidcWriteAssignmentRequest.from_dict(oidc_write_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


