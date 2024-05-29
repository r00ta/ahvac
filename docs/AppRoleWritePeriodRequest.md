# AppRoleWritePeriodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 

## Example

```python
from ahvac.models.app_role_write_period_request import AppRoleWritePeriodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoleWritePeriodRequest from a JSON string
app_role_write_period_request_instance = AppRoleWritePeriodRequest.from_json(json)
# print the JSON string representation of the object
print(AppRoleWritePeriodRequest.to_json())

# convert the object into a dict
app_role_write_period_request_dict = app_role_write_period_request_instance.to_dict()
# create an instance of AppRoleWritePeriodRequest from a dict
app_role_write_period_request_from_dict = AppRoleWritePeriodRequest.from_dict(app_role_write_period_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


