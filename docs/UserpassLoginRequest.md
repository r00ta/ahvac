# UserpassLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for this user. | [optional] 

## Example

```python
from ahvac.models.userpass_login_request import UserpassLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserpassLoginRequest from a JSON string
userpass_login_request_instance = UserpassLoginRequest.from_json(json)
# print the JSON string representation of the object
print(UserpassLoginRequest.to_json())

# convert the object into a dict
userpass_login_request_dict = userpass_login_request_instance.to_dict()
# create an instance of UserpassLoginRequest from a dict
userpass_login_request_from_dict = UserpassLoginRequest.from_dict(userpass_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


