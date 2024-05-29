# AliCloudConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Access key with appropriate permissions. | [optional] 
**secret_key** | **str** | Secret key with appropriate permissions. | [optional] 

## Example

```python
from ahvac.models.ali_cloud_configure_request import AliCloudConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AliCloudConfigureRequest from a JSON string
ali_cloud_configure_request_instance = AliCloudConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(AliCloudConfigureRequest.to_json())

# convert the object into a dict
ali_cloud_configure_request_dict = ali_cloud_configure_request_instance.to_dict()
# create an instance of AliCloudConfigureRequest from a dict
ali_cloud_configure_request_from_dict = AliCloudConfigureRequest.from_dict(ali_cloud_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


