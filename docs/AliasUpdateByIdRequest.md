# AliasUpdateByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_id** | **str** | Entity ID to which this alias should be tied to | [optional] 
**entity_id** | **str** | Entity ID to which this alias should be tied to. This field is deprecated in favor of &#39;canonical_id&#39;. | [optional] 
**mount_accessor** | **str** | Mount accessor to which this alias belongs to | [optional] 
**name** | **str** | Name of the alias | [optional] 

## Example

```python
from ahvac.models.alias_update_by_id_request import AliasUpdateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AliasUpdateByIdRequest from a JSON string
alias_update_by_id_request_instance = AliasUpdateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(AliasUpdateByIdRequest.to_json())

# convert the object into a dict
alias_update_by_id_request_dict = alias_update_by_id_request_instance.to_dict()
# create an instance of AliasUpdateByIdRequest from a dict
alias_update_by_id_request_from_dict = AliasUpdateByIdRequest.from_dict(alias_update_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


