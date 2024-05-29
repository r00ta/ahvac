# RateLimitQuotasReadConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_rate_limit_audit_logging** | **bool** |  | [optional] 
**enable_rate_limit_response_headers** | **bool** |  | [optional] 
**rate_limit_exempt_paths** | **List[str]** |  | [optional] 

## Example

```python
from ahvac.models.rate_limit_quotas_read_configuration_response import RateLimitQuotasReadConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitQuotasReadConfigurationResponse from a JSON string
rate_limit_quotas_read_configuration_response_instance = RateLimitQuotasReadConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(RateLimitQuotasReadConfigurationResponse.to_json())

# convert the object into a dict
rate_limit_quotas_read_configuration_response_dict = rate_limit_quotas_read_configuration_response_instance.to_dict()
# create an instance of RateLimitQuotasReadConfigurationResponse from a dict
rate_limit_quotas_read_configuration_response_from_dict = RateLimitQuotasReadConfigurationResponse.from_dict(rate_limit_quotas_read_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


