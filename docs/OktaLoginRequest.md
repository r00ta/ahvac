# OktaLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** | Nonce provided if performing login that requires number verification challenge. Logins through the vault login CLI command will automatically generate a nonce. | [optional] 
**password** | **str** | Password for this user. | [optional] 
**provider** | **str** | Preferred factor provider. | [optional] 
**totp** | **str** | TOTP passcode. | [optional] 

## Example

```python
from ahvac.models.okta_login_request import OktaLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OktaLoginRequest from a JSON string
okta_login_request_instance = OktaLoginRequest.from_json(json)
# print the JSON string representation of the object
print(OktaLoginRequest.to_json())

# convert the object into a dict
okta_login_request_dict = okta_login_request_instance.to_dict()
# create an instance of OktaLoginRequest from a dict
okta_login_request_from_dict = OktaLoginRequest.from_dict(okta_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


