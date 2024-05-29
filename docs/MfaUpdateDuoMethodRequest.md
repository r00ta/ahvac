# MfaUpdateDuoMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_hostname** | **str** | API host name for Duo. | [optional] 
**integration_key** | **str** | Integration key for Duo. | [optional] 
**method_name** | **str** | The unique name identifier for this MFA method. | [optional] 
**push_info** | **str** | Push information for Duo. | [optional] 
**secret_key** | **str** | Secret key for Duo. | [optional] 
**use_passcode** | **bool** | If true, the user is reminded to use the passcode upon MFA validation. This option does not enforce using the passcode. Defaults to false. | [optional] 
**username_format** | **str** | A template string for mapping Identity names to MFA method names. Values to subtitute should be placed in {{}}. For example, \&quot;{{alias.name}}@example.com\&quot;. Currently-supported mappings: alias.name: The name returned by the mount configured via the mount_accessor parameter If blank, the Alias&#39;s name field will be used as-is. | [optional] 

## Example

```python
from ahvac.models.mfa_update_duo_method_request import MfaUpdateDuoMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaUpdateDuoMethodRequest from a JSON string
mfa_update_duo_method_request_instance = MfaUpdateDuoMethodRequest.from_json(json)
# print the JSON string representation of the object
print(MfaUpdateDuoMethodRequest.to_json())

# convert the object into a dict
mfa_update_duo_method_request_dict = mfa_update_duo_method_request_instance.to_dict()
# create an instance of MfaUpdateDuoMethodRequest from a dict
mfa_update_duo_method_request_from_dict = MfaUpdateDuoMethodRequest.from_dict(mfa_update_duo_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


