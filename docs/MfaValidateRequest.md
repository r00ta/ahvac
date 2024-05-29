# MfaValidateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_payload** | **object** | A map from MFA method ID to a slice of passcodes or an empty slice if the method does not use passcodes | 
**mfa_request_id** | **str** | ID for this MFA request | 

## Example

```python
from ahvac.models.mfa_validate_request import MfaValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaValidateRequest from a JSON string
mfa_validate_request_instance = MfaValidateRequest.from_json(json)
# print the JSON string representation of the object
print(MfaValidateRequest.to_json())

# convert the object into a dict
mfa_validate_request_dict = mfa_validate_request_instance.to_dict()
# create an instance of MfaValidateRequest from a dict
mfa_validate_request_from_dict = MfaValidateRequest.from_dict(mfa_validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


