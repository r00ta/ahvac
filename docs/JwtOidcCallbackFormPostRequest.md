# JwtOidcCallbackFormPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_nonce** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**id_token** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from ahvac.models.jwt_oidc_callback_form_post_request import JwtOidcCallbackFormPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JwtOidcCallbackFormPostRequest from a JSON string
jwt_oidc_callback_form_post_request_instance = JwtOidcCallbackFormPostRequest.from_json(json)
# print the JSON string representation of the object
print(JwtOidcCallbackFormPostRequest.to_json())

# convert the object into a dict
jwt_oidc_callback_form_post_request_dict = jwt_oidc_callback_form_post_request_instance.to_dict()
# create an instance of JwtOidcCallbackFormPostRequest from a dict
jwt_oidc_callback_form_post_request_from_dict = JwtOidcCallbackFormPostRequest.from_dict(jwt_oidc_callback_form_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


