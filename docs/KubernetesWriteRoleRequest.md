# KubernetesWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_kubernetes_namespace_selector** | **str** | A label selector for Kubernetes namespaces in which credentials can be generated. Accepts either a JSON or YAML object. If set with allowed_kubernetes_namespaces, the conditions are conjuncted. | [optional] 
**allowed_kubernetes_namespaces** | **List[str]** | A list of the Kubernetes namespaces in which credentials can be generated. If set to \&quot;*\&quot; all namespaces are allowed. | [optional] 
**extra_annotations** | **object** | Additional annotations to apply to all generated Kubernetes objects. | [optional] 
**extra_labels** | **object** | Additional labels to apply to all generated Kubernetes objects. | [optional] 
**generated_role_rules** | **str** | The Role or ClusterRole rules to use when generating a role. Accepts either a JSON or YAML object. If set, the entire chain of Kubernetes objects will be generated. | [optional] 
**kubernetes_role_name** | **str** | The pre-existing Role or ClusterRole to bind a generated service account to. If set, Kubernetes token, service account, and role binding objects will be created. | [optional] 
**kubernetes_role_type** | **str** | Specifies whether the Kubernetes role is a Role or ClusterRole. | [optional] [default to 'Role']
**name_template** | **str** | The name template to use when generating service accounts, roles and role bindings. If unset, a default template is used. | [optional] 
**service_account_name** | **str** | The pre-existing service account to generate tokens for. Mutually exclusive with all role parameters. If set, only a Kubernetes service account token will be created. | [optional] 
**token_default_audiences** | **List[str]** | The default audiences for generated Kubernetes service account tokens. If not set or set to \&quot;\&quot;, will use k8s cluster default. | [optional] 
**token_default_ttl** | **str** | The default ttl for generated Kubernetes service account tokens. If not set or set to 0, will use system default. | [optional] 
**token_max_ttl** | **str** | The maximum ttl for generated Kubernetes service account tokens. If not set or set to 0, will use system default. | [optional] 

## Example

```python
from ahvac.models.kubernetes_write_role_request import KubernetesWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesWriteRoleRequest from a JSON string
kubernetes_write_role_request_instance = KubernetesWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesWriteRoleRequest.to_json())

# convert the object into a dict
kubernetes_write_role_request_dict = kubernetes_write_role_request_instance.to_dict()
# create an instance of KubernetesWriteRoleRequest from a dict
kubernetes_write_role_request_from_dict = KubernetesWriteRoleRequest.from_dict(kubernetes_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


