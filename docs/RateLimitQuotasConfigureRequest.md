# RateLimitQuotasConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_rate_limit_audit_logging** | **bool** | If set, starts audit logging of requests that get rejected due to rate limit quota rule violations. | [optional] 
**enable_rate_limit_response_headers** | **bool** | If set, additional rate limit quota HTTP headers will be added to responses. | [optional] 
**rate_limit_exempt_paths** | **List[str]** | Specifies the list of exempt paths from all rate limit quotas. If empty no paths will be exempt. | [optional] 

## Example

```python
from ahvac.models.rate_limit_quotas_configure_request import RateLimitQuotasConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitQuotasConfigureRequest from a JSON string
rate_limit_quotas_configure_request_instance = RateLimitQuotasConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(RateLimitQuotasConfigureRequest.to_json())

# convert the object into a dict
rate_limit_quotas_configure_request_dict = rate_limit_quotas_configure_request_instance.to_dict()
# create an instance of RateLimitQuotasConfigureRequest from a dict
rate_limit_quotas_configure_request_from_dict = RateLimitQuotasConfigureRequest.from_dict(rate_limit_quotas_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


