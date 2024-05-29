# InternalUiListEnabledFeatureFlagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_flags** | **List[str]** |  | [optional] 

## Example

```python
from ahvac.models.internal_ui_list_enabled_feature_flags_response import InternalUiListEnabledFeatureFlagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalUiListEnabledFeatureFlagsResponse from a JSON string
internal_ui_list_enabled_feature_flags_response_instance = InternalUiListEnabledFeatureFlagsResponse.from_json(json)
# print the JSON string representation of the object
print(InternalUiListEnabledFeatureFlagsResponse.to_json())

# convert the object into a dict
internal_ui_list_enabled_feature_flags_response_dict = internal_ui_list_enabled_feature_flags_response_instance.to_dict()
# create an instance of InternalUiListEnabledFeatureFlagsResponse from a dict
internal_ui_list_enabled_feature_flags_response_from_dict = InternalUiListEnabledFeatureFlagsResponse.from_dict(internal_ui_list_enabled_feature_flags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


