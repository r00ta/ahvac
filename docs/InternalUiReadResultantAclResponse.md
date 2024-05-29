# InternalUiReadResultantAclResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact_paths** | **object** |  | [optional] 
**glob_paths** | **object** |  | [optional] 
**root** | **bool** |  | [optional] 

## Example

```python
from ahvac.models.internal_ui_read_resultant_acl_response import InternalUiReadResultantAclResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalUiReadResultantAclResponse from a JSON string
internal_ui_read_resultant_acl_response_instance = InternalUiReadResultantAclResponse.from_json(json)
# print the JSON string representation of the object
print(InternalUiReadResultantAclResponse.to_json())

# convert the object into a dict
internal_ui_read_resultant_acl_response_dict = internal_ui_read_resultant_acl_response_instance.to_dict()
# create an instance of InternalUiReadResultantAclResponse from a dict
internal_ui_read_resultant_acl_response_from_dict = InternalUiReadResultantAclResponse.from_dict(internal_ui_read_resultant_acl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


