# SealStatusResponse


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
from ahvac.models.seal_status_response import SealStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SealStatusResponse from a JSON string
seal_status_response_instance = SealStatusResponse.from_json(json)
# print the JSON string representation of the object
print(SealStatusResponse.to_json())

# convert the object into a dict
seal_status_response_dict = seal_status_response_instance.to_dict()
# create an instance of SealStatusResponse from a dict
seal_status_response_from_dict = SealStatusResponse.from_dict(seal_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


