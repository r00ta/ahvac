# RadiusConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dial_timeout** | **str** | Number of seconds before connect times out (default: 10) | [optional] [default to '10']
**host** | **str** | RADIUS server host | [optional] 
**nas_identifier** | **str** | RADIUS NAS Identifier field (optional) | [optional] [default to '']
**nas_port** | **int** | RADIUS NAS port field (default: 10) | [optional] [default to 10]
**port** | **int** | RADIUS server port (default: 1812) | [optional] [default to 1812]
**read_timeout** | **str** | Number of seconds before response times out (default: 10) | [optional] [default to '10']
**secret** | **str** | Secret shared with the RADIUS server | [optional] 
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **str** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies. This will apply to all tokens generated by this auth method, in addition to any configured for specific users. | [optional] 
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']
**unregistered_user_policies** | **str** | Comma-separated list of policies to grant upon successful RADIUS authentication of an unregistered user (default: empty) | [optional] [default to '']

## Example

```python
from ahvac.models.radius_configure_request import RadiusConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusConfigureRequest from a JSON string
radius_configure_request_instance = RadiusConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(RadiusConfigureRequest.to_json())

# convert the object into a dict
radius_configure_request_dict = radius_configure_request_instance.to_dict()
# create an instance of RadiusConfigureRequest from a dict
radius_configure_request_from_dict = RadiusConfigureRequest.from_dict(radius_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

