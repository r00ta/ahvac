# MountsEnableSecretsEngineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Configuration for this mount, such as default_lease_ttl and max_lease_ttl. | [optional] 
**description** | **str** | User-friendly description for this mount. | [optional] 
**external_entropy_access** | **bool** | Whether to give the mount access to Vault&#39;s external entropy. | [optional] [default to False]
**local** | **bool** | Mark the mount as a local mount, which is not replicated and is unaffected by replication. | [optional] [default to False]
**options** | **object** | The options to pass into the backend. Should be a json object with string keys and values. | [optional] 
**plugin_name** | **str** | Name of the plugin to mount based from the name registered in the plugin catalog. | [optional] 
**plugin_version** | **str** | The semantic version of the plugin to use, or image tag if oci_image is provided. | [optional] 
**seal_wrap** | **bool** | Whether to turn on seal wrapping for the mount. | [optional] [default to False]
**type** | **str** | The type of the backend. Example: \&quot;passthrough\&quot; | [optional] 

## Example

```python
from ahvac.models.mounts_enable_secrets_engine_request import MountsEnableSecretsEngineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MountsEnableSecretsEngineRequest from a JSON string
mounts_enable_secrets_engine_request_instance = MountsEnableSecretsEngineRequest.from_json(json)
# print the JSON string representation of the object
print(MountsEnableSecretsEngineRequest.to_json())

# convert the object into a dict
mounts_enable_secrets_engine_request_dict = mounts_enable_secrets_engine_request_instance.to_dict()
# create an instance of MountsEnableSecretsEngineRequest from a dict
mounts_enable_secrets_engine_request_from_dict = MountsEnableSecretsEngineRequest.from_dict(mounts_enable_secrets_engine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


