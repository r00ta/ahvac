# TotpValidateCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | TOTP code to be validated. | [optional] 

## Example

```python
from ahvac.models.totp_validate_code_request import TotpValidateCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TotpValidateCodeRequest from a JSON string
totp_validate_code_request_instance = TotpValidateCodeRequest.from_json(json)
# print the JSON string representation of the object
print(TotpValidateCodeRequest.to_json())

# convert the object into a dict
totp_validate_code_request_dict = totp_validate_code_request_instance.to_dict()
# create an instance of TotpValidateCodeRequest from a dict
totp_validate_code_request_from_dict = TotpValidateCodeRequest.from_dict(totp_validate_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


