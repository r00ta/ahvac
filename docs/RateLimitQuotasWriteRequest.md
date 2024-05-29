# RateLimitQuotasWriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_interval** | **str** | If set, when a client reaches a rate limit threshold, the client will be prohibited from any further requests until after the &#39;block_interval&#39; has elapsed. | [optional] 
**inheritable** | **bool** | Whether all child namespaces can inherit this namespace quota. | [optional] 
**interval** | **str** | The duration to enforce rate limiting for (default &#39;1s&#39;). | [optional] 
**path** | **str** | Path of the mount or namespace to apply the quota. A blank path configures a global quota. For example namespace1/ adds a quota to a full namespace, namespace1/auth/userpass adds a quota to userpass in namespace1. | [optional] 
**rate** | **float** | The maximum number of requests in a given interval to be allowed by the quota rule. The &#39;rate&#39; must be positive. | [optional] 
**role** | **str** | Login role to apply this quota to. Note that when set, path must be configured to a valid auth method with a concept of roles. | [optional] 
**type** | **str** | Type of the quota rule. | [optional] 

## Example

```python
from ahvac.models.rate_limit_quotas_write_request import RateLimitQuotasWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitQuotasWriteRequest from a JSON string
rate_limit_quotas_write_request_instance = RateLimitQuotasWriteRequest.from_json(json)
# print the JSON string representation of the object
print(RateLimitQuotasWriteRequest.to_json())

# convert the object into a dict
rate_limit_quotas_write_request_dict = rate_limit_quotas_write_request_instance.to_dict()
# create an instance of RateLimitQuotasWriteRequest from a dict
rate_limit_quotas_write_request_from_dict = RateLimitQuotasWriteRequest.from_dict(rate_limit_quotas_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


