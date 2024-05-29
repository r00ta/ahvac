# RadiusLoginWithUsernameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for this user. | [optional] 
**username** | **str** | Username to be used for login. (POST request body) | [optional] 

## Example

```python
from ahvac.models.radius_login_with_username_request import RadiusLoginWithUsernameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusLoginWithUsernameRequest from a JSON string
radius_login_with_username_request_instance = RadiusLoginWithUsernameRequest.from_json(json)
# print the JSON string representation of the object
print(RadiusLoginWithUsernameRequest.to_json())

# convert the object into a dict
radius_login_with_username_request_dict = radius_login_with_username_request_instance.to_dict()
# create an instance of RadiusLoginWithUsernameRequest from a dict
radius_login_with_username_request_from_dict = RadiusLoginWithUsernameRequest.from_dict(radius_login_with_username_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


