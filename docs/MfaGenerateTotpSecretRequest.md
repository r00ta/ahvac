# MfaGenerateTotpSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_id** | **str** | The unique identifier for this MFA method. | 

## Example

```python
from ahvac.models.mfa_generate_totp_secret_request import MfaGenerateTotpSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaGenerateTotpSecretRequest from a JSON string
mfa_generate_totp_secret_request_instance = MfaGenerateTotpSecretRequest.from_json(json)
# print the JSON string representation of the object
print(MfaGenerateTotpSecretRequest.to_json())

# convert the object into a dict
mfa_generate_totp_secret_request_dict = mfa_generate_totp_secret_request_instance.to_dict()
# create an instance of MfaGenerateTotpSecretRequest from a dict
mfa_generate_totp_secret_request_from_dict = MfaGenerateTotpSecretRequest.from_dict(mfa_generate_totp_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


