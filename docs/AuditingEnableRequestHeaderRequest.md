# AuditingEnableRequestHeaderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hmac** | **bool** |  | [optional] 

## Example

```python
from ahvac.models.auditing_enable_request_header_request import AuditingEnableRequestHeaderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditingEnableRequestHeaderRequest from a JSON string
auditing_enable_request_header_request_instance = AuditingEnableRequestHeaderRequest.from_json(json)
# print the JSON string representation of the object
print(AuditingEnableRequestHeaderRequest.to_json())

# convert the object into a dict
auditing_enable_request_header_request_dict = auditing_enable_request_header_request_instance.to_dict()
# create an instance of AuditingEnableRequestHeaderRequest from a dict
auditing_enable_request_header_request_from_dict = AuditingEnableRequestHeaderRequest.from_dict(auditing_enable_request_header_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


