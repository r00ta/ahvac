# MountsTuneConfigurationParametersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_managed_keys** | **List[str]** |  | [optional] 
**allowed_response_headers** | **List[str]** | A list of headers to whitelist and allow a plugin to set on responses. | [optional] 
**audit_non_hmac_request_keys** | **List[str]** | The list of keys in the request data object that will not be HMAC&#39;ed by audit devices. | [optional] 
**audit_non_hmac_response_keys** | **List[str]** | The list of keys in the response data object that will not be HMAC&#39;ed by audit devices. | [optional] 
**default_lease_ttl** | **str** | The default lease TTL for this mount. | [optional] 
**description** | **str** | User-friendly description for this credential backend. | [optional] 
**listing_visibility** | **str** | Determines the visibility of the mount in the UI-specific listing endpoint. Accepted value are &#39;unauth&#39; and &#39;hidden&#39;, with the empty default (&#39;&#39;) behaving like &#39;hidden&#39;. | [optional] 
**max_lease_ttl** | **str** | The max lease TTL for this mount. | [optional] 
**options** | **object** | The options to pass into the backend. Should be a json object with string keys and values. | [optional] 
**passthrough_request_headers** | **List[str]** | A list of headers to whitelist and pass from the request to the plugin. | [optional] 
**plugin_version** | **str** | The semantic version of the plugin to use, or image tag if oci_image is provided. | [optional] 
**token_type** | **str** | The type of token to issue (service or batch). | [optional] 
**user_lockout_config** | **object** | The user lockout configuration to pass into the backend. Should be a json object with string keys and values. | [optional] 

## Example

```python
from ahvac.models.mounts_tune_configuration_parameters_request import MountsTuneConfigurationParametersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MountsTuneConfigurationParametersRequest from a JSON string
mounts_tune_configuration_parameters_request_instance = MountsTuneConfigurationParametersRequest.from_json(json)
# print the JSON string representation of the object
print(MountsTuneConfigurationParametersRequest.to_json())

# convert the object into a dict
mounts_tune_configuration_parameters_request_dict = mounts_tune_configuration_parameters_request_instance.to_dict()
# create an instance of MountsTuneConfigurationParametersRequest from a dict
mounts_tune_configuration_parameters_request_from_dict = MountsTuneConfigurationParametersRequest.from_dict(mounts_tune_configuration_parameters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


