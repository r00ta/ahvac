# UnsealRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies a single unseal key share. This is required unless reset is true. | [optional] 
**reset** | **bool** | Specifies if previously-provided unseal keys are discarded and the unseal process is reset. | [optional] 

## Example

```python
from ahvac.models.unseal_request import UnsealRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnsealRequest from a JSON string
unseal_request_instance = UnsealRequest.from_json(json)
# print the JSON string representation of the object
print(UnsealRequest.to_json())

# convert the object into a dict
unseal_request_dict = unseal_request_instance.to_dict()
# create an instance of UnsealRequest from a dict
unseal_request_from_dict = UnsealRequest.from_dict(unseal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


