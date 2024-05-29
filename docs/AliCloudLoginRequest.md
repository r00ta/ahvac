# AliCloudLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_request_headers** | **str** | The request headers. This must include the headers over which AliCloud has included a signature. | [optional] 
**identity_request_url** | **str** | Base64-encoded full URL against which to make the AliCloud request. | [optional] 
**role** | **str** | Name of the role against which the login is being attempted. If &#39;role&#39; is not specified, then the login endpoint looks for a role name in the ARN returned by the GetCallerIdentity request. If a matching role is not found, login fails. | 

## Example

```python
from ahvac.models.ali_cloud_login_request import AliCloudLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AliCloudLoginRequest from a JSON string
ali_cloud_login_request_instance = AliCloudLoginRequest.from_json(json)
# print the JSON string representation of the object
print(AliCloudLoginRequest.to_json())

# convert the object into a dict
ali_cloud_login_request_dict = ali_cloud_login_request_instance.to_dict()
# create an instance of AliCloudLoginRequest from a dict
ali_cloud_login_request_from_dict = AliCloudLoginRequest.from_dict(ali_cloud_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


