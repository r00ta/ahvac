# RateLimitQuotasReadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_interval** | **int** |  | [optional] 
**inheritable** | **bool** |  | [optional] 
**interval** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**role** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ahvac.models.rate_limit_quotas_read_response import RateLimitQuotasReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitQuotasReadResponse from a JSON string
rate_limit_quotas_read_response_instance = RateLimitQuotasReadResponse.from_json(json)
# print the JSON string representation of the object
print(RateLimitQuotasReadResponse.to_json())

# convert the object into a dict
rate_limit_quotas_read_response_dict = rate_limit_quotas_read_response_instance.to_dict()
# create an instance of RateLimitQuotasReadResponse from a dict
rate_limit_quotas_read_response_from_dict = RateLimitQuotasReadResponse.from_dict(rate_limit_quotas_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


