# MfaWriteLoginEnforcementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_accessors** | **List[str]** | Array of auth mount accessor IDs | [optional] 
**auth_method_types** | **List[str]** | Array of auth mount types | [optional] 
**identity_entity_ids** | **List[str]** | Array of identity entity IDs | [optional] 
**identity_group_ids** | **List[str]** | Array of identity group IDs | [optional] 
**mfa_method_ids** | **List[str]** | Array of Method IDs that determine what methods will be enforced | 

## Example

```python
from ahvac.models.mfa_write_login_enforcement_request import MfaWriteLoginEnforcementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaWriteLoginEnforcementRequest from a JSON string
mfa_write_login_enforcement_request_instance = MfaWriteLoginEnforcementRequest.from_json(json)
# print the JSON string representation of the object
print(MfaWriteLoginEnforcementRequest.to_json())

# convert the object into a dict
mfa_write_login_enforcement_request_dict = mfa_write_login_enforcement_request_instance.to_dict()
# create an instance of MfaWriteLoginEnforcementRequest from a dict
mfa_write_login_enforcement_request_from_dict = MfaWriteLoginEnforcementRequest.from_dict(mfa_write_login_enforcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


