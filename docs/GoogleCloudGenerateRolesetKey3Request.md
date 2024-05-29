# GoogleCloudGenerateRolesetKey3Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_algorithm** | **str** | Private key algorithm for service account key - defaults to KEY_ALG_RSA_2048\&quot; | [optional] [default to 'KEY_ALG_RSA_2048']
**key_type** | **str** | Private key type for service account key - defaults to TYPE_GOOGLE_CREDENTIALS_FILE\&quot; | [optional] [default to 'TYPE_GOOGLE_CREDENTIALS_FILE']
**ttl** | **str** | Lifetime of the service account key | [optional] 

## Example

```python
from ahvac.models.google_cloud_generate_roleset_key3_request import GoogleCloudGenerateRolesetKey3Request

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudGenerateRolesetKey3Request from a JSON string
google_cloud_generate_roleset_key3_request_instance = GoogleCloudGenerateRolesetKey3Request.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudGenerateRolesetKey3Request.to_json())

# convert the object into a dict
google_cloud_generate_roleset_key3_request_dict = google_cloud_generate_roleset_key3_request_instance.to_dict()
# create an instance of GoogleCloudGenerateRolesetKey3Request from a dict
google_cloud_generate_roleset_key3_request_from_dict = GoogleCloudGenerateRolesetKey3Request.from_dict(google_cloud_generate_roleset_key3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


