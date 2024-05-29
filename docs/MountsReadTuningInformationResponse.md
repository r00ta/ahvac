# MountsReadTuningInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_managed_keys** | **List[str]** |  | [optional] 
**allowed_response_headers** | **List[str]** | A list of headers to whitelist and allow a plugin to set on responses. | [optional] 
**audit_non_hmac_request_keys** | **List[str]** |  | [optional] 
**audit_non_hmac_response_keys** | **List[str]** |  | [optional] 
**default_lease_ttl** | **int** | The default lease TTL for this mount. | [optional] 
**description** | **str** | User-friendly description for this credential backend. | [optional] 
**external_entropy_access** | **bool** |  | [optional] 
**force_no_cache** | **bool** |  | [optional] 
**listing_visibility** | **str** |  | [optional] 
**max_lease_ttl** | **int** | The max lease TTL for this mount. | [optional] 
**options** | **object** | The options to pass into the backend. Should be a json object with string keys and values. | [optional] 
**passthrough_request_headers** | **List[str]** |  | [optional] 
**plugin_version** | **str** | The semantic version of the plugin to use, or image tag if oci_image is provided. | [optional] 
**token_type** | **str** | The type of token to issue (service or batch). | [optional] 
**user_lockout_counter_reset_duration** | **int** |  | [optional] 
**user_lockout_disable** | **bool** |  | [optional] 
**user_lockout_duration** | **int** |  | [optional] 
**user_lockout_threshold** | **int** |  | [optional] 

## Example

```python
from ahvac.models.mounts_read_tuning_information_response import MountsReadTuningInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MountsReadTuningInformationResponse from a JSON string
mounts_read_tuning_information_response_instance = MountsReadTuningInformationResponse.from_json(json)
# print the JSON string representation of the object
print(MountsReadTuningInformationResponse.to_json())

# convert the object into a dict
mounts_read_tuning_information_response_dict = mounts_read_tuning_information_response_instance.to_dict()
# create an instance of MountsReadTuningInformationResponse from a dict
mounts_read_tuning_information_response_from_dict = MountsReadTuningInformationResponse.from_dict(mounts_read_tuning_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


