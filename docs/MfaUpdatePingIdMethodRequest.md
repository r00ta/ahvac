# MfaUpdatePingIdMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_name** | **str** | The unique name identifier for this MFA method. | [optional] 
**settings_file_base64** | **str** | The settings file provided by Ping, Base64-encoded. This must be a settings file suitable for third-party clients, not the PingID SDK or PingFederate. | [optional] 
**username_format** | **str** | A template string for mapping Identity names to MFA method names. Values to subtitute should be placed in {{}}. For example, \&quot;{{alias.name}}@example.com\&quot;. Currently-supported mappings: alias.name: The name returned by the mount configured via the mount_accessor parameter If blank, the Alias&#39;s name field will be used as-is. | [optional] 

## Example

```python
from ahvac.models.mfa_update_ping_id_method_request import MfaUpdatePingIdMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MfaUpdatePingIdMethodRequest from a JSON string
mfa_update_ping_id_method_request_instance = MfaUpdatePingIdMethodRequest.from_json(json)
# print the JSON string representation of the object
print(MfaUpdatePingIdMethodRequest.to_json())

# convert the object into a dict
mfa_update_ping_id_method_request_dict = mfa_update_ping_id_method_request_instance.to_dict()
# create an instance of MfaUpdatePingIdMethodRequest from a dict
mfa_update_ping_id_method_request_from_dict = MfaUpdatePingIdMethodRequest.from_dict(mfa_update_ping_id_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


