# LeasesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | **int** | Number of matching leases per mount | [optional] 
**lease_count** | **int** | Number of matching leases | [optional] 

## Example

```python
from ahvac.models.leases_list_response import LeasesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesListResponse from a JSON string
leases_list_response_instance = LeasesListResponse.from_json(json)
# print the JSON string representation of the object
print(LeasesListResponse.to_json())

# convert the object into a dict
leases_list_response_dict = leases_list_response_instance.to_dict()
# create an instance of LeasesListResponse from a dict
leases_list_response_from_dict = LeasesListResponse.from_dict(leases_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


