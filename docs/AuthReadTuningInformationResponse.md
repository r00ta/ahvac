# AuthReadTuningInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_managed_keys** | **List[str]** |  | [optional] 
**allowed_response_headers** | **List[str]** |  | [optional] 
**audit_non_hmac_request_keys** | **List[str]** |  | [optional] 
**audit_non_hmac_response_keys** | **List[str]** |  | [optional] 
**default_lease_ttl** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**external_entropy_access** | **bool** |  | [optional] 
**force_no_cache** | **bool** |  | [optional] 
**listing_visibility** | **str** |  | [optional] 
**max_lease_ttl** | **int** |  | [optional] 
**options** | **object** |  | [optional] 
**passthrough_request_headers** | **List[str]** |  | [optional] 
**plugin_version** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**user_lockout_counter_reset_duration** | **int** |  | [optional] 
**user_lockout_disable** | **bool** |  | [optional] 
**user_lockout_duration** | **int** |  | [optional] 
**user_lockout_threshold** | **int** |  | [optional] 

## Example

```python
from ahvac.models.auth_read_tuning_information_response import AuthReadTuningInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthReadTuningInformationResponse from a JSON string
auth_read_tuning_information_response_instance = AuthReadTuningInformationResponse.from_json(json)
# print the JSON string representation of the object
print(AuthReadTuningInformationResponse.to_json())

# convert the object into a dict
auth_read_tuning_information_response_dict = auth_read_tuning_information_response_instance.to_dict()
# create an instance of AuthReadTuningInformationResponse from a dict
auth_read_tuning_information_response_from_dict = AuthReadTuningInformationResponse.from_dict(auth_read_tuning_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


