# MfaAdminGenerateTotpSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Entity ID on which the generated secret needs to get stored. | 
**method_id** | **str** | The unique identifier for this MFA method. | 

## Example

```python
from ahvac.models.mfa_admin_generate_totp_secret_request import MfaAdminGenerateTotpSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaAdminGenerateTotpSecretRequest from a JSON string
mfa_admin_generate_totp_secret_request_instance = MfaAdminGenerateTotpSecretRequest.from_json(json)
# print the JSON string representation of the object
print(MfaAdminGenerateTotpSecretRequest.to_json())

# convert the object into a dict
mfa_admin_generate_totp_secret_request_dict = mfa_admin_generate_totp_secret_request_instance.to_dict()
# create an instance of MfaAdminGenerateTotpSecretRequest from a dict
mfa_admin_generate_totp_secret_request_from_dict = MfaAdminGenerateTotpSecretRequest.from_dict(mfa_admin_generate_totp_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


