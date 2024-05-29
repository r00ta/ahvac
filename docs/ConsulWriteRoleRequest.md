# ConsulWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consul_namespace** | **str** | Indicates which namespace that the token will be created within. Defaults to &#39;default&#39;. Available in Consul 1.7 and above. | [optional] 
**consul_policies** | **List[str]** | List of policies to attach to the token. Either \&quot;consul_policies\&quot; or \&quot;consul_roles\&quot; are required for Consul 1.5 and above, or just \&quot;consul_policies\&quot; if using Consul 1.4. | [optional] 
**consul_roles** | **List[str]** | List of Consul roles to attach to the token. Either \&quot;policies\&quot; or \&quot;consul_roles\&quot; are required for Consul 1.5 and above. | [optional] 
**lease** | **str** | Use \&quot;ttl\&quot; instead. | [optional] 
**local** | **bool** | Indicates that the token should not be replicated globally and instead be local to the current datacenter. Available in Consul 1.4 and above. | [optional] 
**max_ttl** | **str** | Max TTL for the Consul token created from the role. | [optional] 
**node_identities** | **List[str]** | List of Node Identities to attach to the token. Available in Consul 1.8.1 or above. | [optional] 
**partition** | **str** | Indicates which admin partition that the token will be created within. Defaults to &#39;default&#39;. Available in Consul 1.11 and above. | [optional] 
**policies** | **List[str]** | Use \&quot;consul_policies\&quot; instead. | [optional] 
**policy** | **str** | Policy document, base64 encoded. Required for &#39;client&#39; tokens. Required for Consul pre-1.4. | [optional] 
**service_identities** | **List[str]** | List of Service Identities to attach to the token, separated by semicolons. Available in Consul 1.5 or above. | [optional] 
**token_type** | **str** | Which type of token to create: &#39;client&#39; or &#39;management&#39;. If a &#39;management&#39; token, the \&quot;policy\&quot;, \&quot;policies\&quot;, and \&quot;consul_roles\&quot; parameters are not required. Defaults to &#39;client&#39;. | [optional] [default to 'client']
**ttl** | **str** | TTL for the Consul token created from the role. | [optional] 

## Example

```python
from ahvac.models.consul_write_role_request import ConsulWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsulWriteRoleRequest from a JSON string
consul_write_role_request_instance = ConsulWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(ConsulWriteRoleRequest.to_json())

# convert the object into a dict
consul_write_role_request_dict = consul_write_role_request_instance.to_dict()
# create an instance of ConsulWriteRoleRequest from a dict
consul_write_role_request_from_dict = ConsulWriteRoleRequest.from_dict(consul_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


