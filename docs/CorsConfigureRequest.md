# CorsConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_headers** | **List[str]** | A comma-separated string or array of strings indicating headers that are allowed on cross-origin requests. | [optional] 
**allowed_origins** | **List[str]** | A comma-separated string or array of strings indicating origins that may make cross-origin requests. | [optional] 
**enable** | **bool** | Enables or disables CORS headers on requests. | [optional] 

## Example

```python
from ahvac.models.cors_configure_request import CorsConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CorsConfigureRequest from a JSON string
cors_configure_request_instance = CorsConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(CorsConfigureRequest.to_json())

# convert the object into a dict
cors_configure_request_dict = cors_configure_request_instance.to_dict()
# create an instance of CorsConfigureRequest from a dict
cors_configure_request_from_dict = CorsConfigureRequest.from_dict(cors_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


