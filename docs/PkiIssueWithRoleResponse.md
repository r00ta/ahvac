# PkiIssueWithRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **List[str]** | Certificate Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**expiration** | **int** | Time of expiration | [optional] 
**issuing_ca** | **str** | Issuing Certificate Authority | [optional] 
**private_key** | **str** | Private key | [optional] 
**private_key_type** | **str** | Private key type | [optional] 
**serial_number** | **str** | Serial Number | [optional] 

## Example

```python
from ahvac.models.pki_issue_with_role_response import PkiIssueWithRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssueWithRoleResponse from a JSON string
pki_issue_with_role_response_instance = PkiIssueWithRoleResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssueWithRoleResponse.to_json())

# convert the object into a dict
pki_issue_with_role_response_dict = pki_issue_with_role_response_instance.to_dict()
# create an instance of PkiIssueWithRoleResponse from a dict
pki_issue_with_role_response_from_dict = PkiIssueWithRoleResponse.from_dict(pki_issue_with_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


