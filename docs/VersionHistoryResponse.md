# VersionHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_info** | **object** |  | [optional] 
**keys** | **List[str]** |  | [optional] 

## Example

```python
from ahvac.models.version_history_response import VersionHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionHistoryResponse from a JSON string
version_history_response_instance = VersionHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(VersionHistoryResponse.to_json())

# convert the object into a dict
version_history_response_dict = version_history_response_instance.to_dict()
# create an instance of VersionHistoryResponse from a dict
version_history_response_from_dict = VersionHistoryResponse.from_dict(version_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


