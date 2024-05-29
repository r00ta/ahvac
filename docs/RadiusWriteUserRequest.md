# RadiusWriteUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | **List[str]** | Comma-separated list of policies associated to the user. | [optional] 

## Example

```python
from ahvac.models.radius_write_user_request import RadiusWriteUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusWriteUserRequest from a JSON string
radius_write_user_request_instance = RadiusWriteUserRequest.from_json(json)
# print the JSON string representation of the object
print(RadiusWriteUserRequest.to_json())

# convert the object into a dict
radius_write_user_request_dict = radius_write_user_request_instance.to_dict()
# create an instance of RadiusWriteUserRequest from a dict
radius_write_user_request_from_dict = RadiusWriteUserRequest.from_dict(radius_write_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


