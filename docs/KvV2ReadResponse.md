# KvV2ReadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from ahvac.models.kv_v2_read_response import KvV2ReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KvV2ReadResponse from a JSON string
kv_v2_read_response_instance = KvV2ReadResponse.from_json(json)
# print the JSON string representation of the object
print(KvV2ReadResponse.to_json())

# convert the object into a dict
kv_v2_read_response_dict = kv_v2_read_response_instance.to_dict()
# create an instance of KvV2ReadResponse from a dict
kv_v2_read_response_from_dict = KvV2ReadResponse.from_dict(kv_v2_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


