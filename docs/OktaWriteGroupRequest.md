# OktaWriteGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | **List[str]** | Comma-separated list of policies associated to the group. | [optional] 

## Example

```python
from ahvac.models.okta_write_group_request import OktaWriteGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OktaWriteGroupRequest from a JSON string
okta_write_group_request_instance = OktaWriteGroupRequest.from_json(json)
# print the JSON string representation of the object
print(OktaWriteGroupRequest.to_json())

# convert the object into a dict
okta_write_group_request_dict = okta_write_group_request_instance.to_dict()
# create an instance of OktaWriteGroupRequest from a dict
okta_write_group_request_from_dict = OktaWriteGroupRequest.from_dict(okta_write_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


