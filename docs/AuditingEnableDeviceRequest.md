# AuditingEnableDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | User-friendly description for this audit backend. | [optional] 
**local** | **bool** | Mark the mount as a local mount, which is not replicated and is unaffected by replication. | [optional] [default to False]
**options** | **object** | Configuration options for the audit backend. | [optional] 
**type** | **str** | The type of the backend. Example: \&quot;mysql\&quot; | [optional] 

## Example

```python
from ahvac.models.auditing_enable_device_request import AuditingEnableDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditingEnableDeviceRequest from a JSON string
auditing_enable_device_request_instance = AuditingEnableDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(AuditingEnableDeviceRequest.to_json())

# convert the object into a dict
auditing_enable_device_request_dict = auditing_enable_device_request_instance.to_dict()
# create an instance of AuditingEnableDeviceRequest from a dict
auditing_enable_device_request_from_dict = AuditingEnableDeviceRequest.from_dict(auditing_enable_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


