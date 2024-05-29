# JwtLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | The signed JWT to validate. | [optional] 
**role** | **str** | The role to log in against. | [optional] 

## Example

```python
from ahvac.models.jwt_login_request import JwtLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtLoginRequest from a JSON string
jwt_login_request_instance = JwtLoginRequest.from_json(json)
# print the JSON string representation of the object
print(JwtLoginRequest.to_json())

# convert the object into a dict
jwt_login_request_dict = jwt_login_request_instance.to_dict()
# create an instance of JwtLoginRequest from a dict
jwt_login_request_from_dict = JwtLoginRequest.from_dict(jwt_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


