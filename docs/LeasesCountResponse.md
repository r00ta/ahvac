# LeasesCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | **int** | Number of matching leases per mount | [optional] 
**lease_count** | **int** | Number of matching leases | [optional] 

## Example

```python
from ahvac.models.leases_count_response import LeasesCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesCountResponse from a JSON string
leases_count_response_instance = LeasesCountResponse.from_json(json)
# print the JSON string representation of the object
print(LeasesCountResponse.to_json())

# convert the object into a dict
leases_count_response_dict = leases_count_response_instance.to_dict()
# create an instance of LeasesCountResponse from a dict
leases_count_response_from_dict = LeasesCountResponse.from_dict(leases_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


