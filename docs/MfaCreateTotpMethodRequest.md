# MfaCreateTotpMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The hashing algorithm used to generate the TOTP token. Options include SHA1, SHA256 and SHA512. | [optional] [default to 'SHA1']
**digits** | **int** | The number of digits in the generated TOTP token. This value can either be 6 or 8. | [optional] [default to 6]
**issuer** | **str** | The name of the key&#39;s issuing organization. | [optional] 
**key_size** | **int** | Determines the size in bytes of the generated key. | [optional] [default to 20]
**max_validation_attempts** | **int** | Max number of allowed validation attempts. | [optional] 
**method_name** | **str** | The unique name identifier for this MFA method. | [optional] 
**period** | **str** | The length of time used to generate a counter for the TOTP token calculation. | [optional] [default to '30']
**qr_size** | **int** | The pixel size of the generated square QR code. | [optional] [default to 200]
**skew** | **int** | The number of delay periods that are allowed when validating a TOTP token. This value can either be 0 or 1. | [optional] [default to 1]

## Example

```python
from ahvac.models.mfa_create_totp_method_request import MfaCreateTotpMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaCreateTotpMethodRequest from a JSON string
mfa_create_totp_method_request_instance = MfaCreateTotpMethodRequest.from_json(json)
# print the JSON string representation of the object
print(MfaCreateTotpMethodRequest.to_json())

# convert the object into a dict
mfa_create_totp_method_request_dict = mfa_create_totp_method_request_instance.to_dict()
# create an instance of MfaCreateTotpMethodRequest from a dict
mfa_create_totp_method_request_from_dict = MfaCreateTotpMethodRequest.from_dict(mfa_create_totp_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


