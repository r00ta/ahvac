# AliCloudWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_policies** | **str** | JSON of policies to be dynamically applied to users of this role. | [optional] 
**max_ttl** | **str** | The maximum allowed lifetime of tokens issued using this role. | [optional] 
**remote_policies** | **List[str]** | The name and type of each remote policy to be applied. Example: \&quot;name:AliyunRDSReadOnlyAccess,type:System\&quot;. | [optional] 
**role_arn** | **str** | ARN of the role to be assumed. If provided, inline_policies and remote_policies should be blank. At creation time, this role must have configured trusted actors, and the access key and secret that will be used to assume the role (in /config) must qualify as a trusted actor. | [optional] 
**ttl** | **str** | Duration in seconds after which the issued token should expire. Defaults to 0, in which case the value will fallback to the system/mount defaults. | [optional] 

## Example

```python
from ahvac.models.ali_cloud_write_role_request import AliCloudWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AliCloudWriteRoleRequest from a JSON string
ali_cloud_write_role_request_instance = AliCloudWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AliCloudWriteRoleRequest.to_json())

# convert the object into a dict
ali_cloud_write_role_request_dict = ali_cloud_write_role_request_instance.to_dict()
# create an instance of AliCloudWriteRoleRequest from a dict
ali_cloud_write_role_request_from_dict = AliCloudWriteRoleRequest.from_dict(ali_cloud_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


