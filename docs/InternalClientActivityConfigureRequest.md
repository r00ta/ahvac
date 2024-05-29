# InternalClientActivityConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_report_months** | **int** | Number of months to report if no start date specified. | [optional] [default to 12]
**enabled** | **str** | Enable or disable collection of client count: enable, disable, or default. | [optional] [default to 'default']
**retention_months** | **int** | Number of months of client data to retain. Setting to 0 will clear all existing data. | [optional] [default to 24]

## Example

```python
from ahvac.models.internal_client_activity_configure_request import InternalClientActivityConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalClientActivityConfigureRequest from a JSON string
internal_client_activity_configure_request_instance = InternalClientActivityConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(InternalClientActivityConfigureRequest.to_json())

# convert the object into a dict
internal_client_activity_configure_request_dict = internal_client_activity_configure_request_instance.to_dict()
# create an instance of InternalClientActivityConfigureRequest from a dict
internal_client_activity_configure_request_from_dict = InternalClientActivityConfigureRequest.from_dict(internal_client_activity_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


