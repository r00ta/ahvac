# LoggersUpdateVerbosityLevelForRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Log verbosity level. Supported values (in order of detail) are \&quot;trace\&quot;, \&quot;debug\&quot;, \&quot;info\&quot;, \&quot;warn\&quot;, and \&quot;error\&quot;. | [optional] 

## Example

```python
from ahvac.models.loggers_update_verbosity_level_for_request import LoggersUpdateVerbosityLevelForRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoggersUpdateVerbosityLevelForRequest from a JSON string
loggers_update_verbosity_level_for_request_instance = LoggersUpdateVerbosityLevelForRequest.from_json(json)
# print the JSON string representation of the object
print(LoggersUpdateVerbosityLevelForRequest.to_json())

# convert the object into a dict
loggers_update_verbosity_level_for_request_dict = loggers_update_verbosity_level_for_request_instance.to_dict()
# create an instance of LoggersUpdateVerbosityLevelForRequest from a dict
loggers_update_verbosity_level_for_request_from_dict = LoggersUpdateVerbosityLevelForRequest.from_dict(loggers_update_verbosity_level_for_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


