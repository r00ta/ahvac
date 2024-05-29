# MfaUpdateOktaMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** | Okta API key. | [optional] 
**base_url** | **str** | The base domain to use for the Okta API. When not specified in the configuration, \&quot;okta.com\&quot; is used. | [optional] 
**method_name** | **str** | The unique name identifier for this MFA method. | [optional] 
**org_name** | **str** | Name of the organization to be used in the Okta API. | [optional] 
**primary_email** | **bool** | If true, the username will only match the primary email for the account. Defaults to false. | [optional] 
**production** | **bool** | (DEPRECATED) Use base_url instead. | [optional] 
**username_format** | **str** | A template string for mapping Identity names to MFA method names. Values to substitute should be placed in {{}}. For example, \&quot;{{entity.name}}@example.com\&quot;. If blank, the Entity&#39;s name field will be used as-is. | [optional] 

## Example

```python
from ahvac.models.mfa_update_okta_method_request import MfaUpdateOktaMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaUpdateOktaMethodRequest from a JSON string
mfa_update_okta_method_request_instance = MfaUpdateOktaMethodRequest.from_json(json)
# print the JSON string representation of the object
print(MfaUpdateOktaMethodRequest.to_json())

# convert the object into a dict
mfa_update_okta_method_request_dict = mfa_update_okta_method_request_instance.to_dict()
# create an instance of MfaUpdateOktaMethodRequest from a dict
mfa_update_okta_method_request_from_dict = MfaUpdateOktaMethodRequest.from_dict(mfa_update_okta_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


