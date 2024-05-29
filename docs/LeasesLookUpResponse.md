# LeasesLookUpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | A list of lease ids | [optional] 

## Example

```python
from ahvac.models.leases_look_up_response import LeasesLookUpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesLookUpResponse from a JSON string
leases_look_up_response_instance = LeasesLookUpResponse.from_json(json)
# print the JSON string representation of the object
print(LeasesLookUpResponse.to_json())

# convert the object into a dict
leases_look_up_response_dict = leases_look_up_response_instance.to_dict()
# create an instance of LeasesLookUpResponse from a dict
leases_look_up_response_from_dict = LeasesLookUpResponse.from_dict(leases_look_up_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


