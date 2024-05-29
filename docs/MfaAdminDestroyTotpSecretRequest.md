# MfaAdminDestroyTotpSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Identifier of the entity from which the MFA method secret needs to be removed. | 
**method_id** | **str** | The unique identifier for this MFA method. | 

## Example

```python
from ahvac.models.mfa_admin_destroy_totp_secret_request import MfaAdminDestroyTotpSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaAdminDestroyTotpSecretRequest from a JSON string
mfa_admin_destroy_totp_secret_request_instance = MfaAdminDestroyTotpSecretRequest.from_json(json)
# print the JSON string representation of the object
print(MfaAdminDestroyTotpSecretRequest.to_json())

# convert the object into a dict
mfa_admin_destroy_totp_secret_request_dict = mfa_admin_destroy_totp_secret_request_instance.to_dict()
# create an instance of MfaAdminDestroyTotpSecretRequest from a dict
mfa_admin_destroy_totp_secret_request_from_dict = MfaAdminDestroyTotpSecretRequest.from_dict(mfa_admin_destroy_totp_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


