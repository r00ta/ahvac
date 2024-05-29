# OidcIntrospectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Optional client_id to verify | [optional] 
**token** | **str** | Token to verify | [optional] 

## Example

```python
from ahvac.models.oidc_introspect_request import OidcIntrospectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OidcIntrospectRequest from a JSON string
oidc_introspect_request_instance = OidcIntrospectRequest.from_json(json)
# print the JSON string representation of the object
print(OidcIntrospectRequest.to_json())

# convert the object into a dict
oidc_introspect_request_dict = oidc_introspect_request_instance.to_dict()
# create an instance of OidcIntrospectRequest from a dict
oidc_introspect_request_from_dict = OidcIntrospectRequest.from_dict(oidc_introspect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


