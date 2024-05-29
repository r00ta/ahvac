# CentrifyConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | OAuth2 App ID | [optional] [default to 'vault_io_integration']
**client_id** | **str** | OAuth2 Client ID | [optional] 
**client_secret** | **str** | OAuth2 Client Secret | [optional] 
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**scope** | **str** | OAuth2 App Scope | [optional] [default to 'vault_io_integration']
**service_url** | **str** | Service URL (https://&lt;tenant&gt;.my.centrify.com) | [optional] 
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']

## Example

```python
from ahvac.models.centrify_configure_request import CentrifyConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CentrifyConfigureRequest from a JSON string
centrify_configure_request_instance = CentrifyConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(CentrifyConfigureRequest.to_json())

# convert the object into a dict
centrify_configure_request_dict = centrify_configure_request_instance.to_dict()
# create an instance of CentrifyConfigureRequest from a dict
centrify_configure_request_from_dict = CentrifyConfigureRequest.from_dict(centrify_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


