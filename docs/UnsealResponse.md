# UnsealResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**hcp_link_resource_id** | **str** |  | [optional] 
**hcp_link_status** | **str** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**migration** | **bool** |  | [optional] 
**n** | **int** |  | [optional] 
**nonce** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**recovery_seal** | **bool** |  | [optional] 
**sealed** | **bool** |  | [optional] 
**storage_type** | **str** |  | [optional] 
**t** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from ahvac.models.unseal_response import UnsealResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnsealResponse from a JSON string
unseal_response_instance = UnsealResponse.from_json(json)
# print the JSON string representation of the object
print(UnsealResponse.to_json())

# convert the object into a dict
unseal_response_dict = unseal_response_instance.to_dict()
# create an instance of UnsealResponse from a dict
unseal_response_from_dict = UnsealResponse.from_dict(unseal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


