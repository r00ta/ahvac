# LoggersUpdateVerbosityLevelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Log verbosity level. Supported values (in order of detail) are \&quot;trace\&quot;, \&quot;debug\&quot;, \&quot;info\&quot;, \&quot;warn\&quot;, and \&quot;error\&quot;. | [optional] 

## Example

```python
from ahvac.models.loggers_update_verbosity_level_request import LoggersUpdateVerbosityLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoggersUpdateVerbosityLevelRequest from a JSON string
loggers_update_verbosity_level_request_instance = LoggersUpdateVerbosityLevelRequest.from_json(json)
# print the JSON string representation of the object
print(LoggersUpdateVerbosityLevelRequest.to_json())

# convert the object into a dict
loggers_update_verbosity_level_request_dict = loggers_update_verbosity_level_request_instance.to_dict()
# create an instance of LoggersUpdateVerbosityLevelRequest from a dict
loggers_update_verbosity_level_request_from_dict = LoggersUpdateVerbosityLevelRequest.from_dict(loggers_update_verbosity_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


