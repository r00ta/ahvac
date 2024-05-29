# KubernetesGenerateCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **List[str]** | The intended audiences of the generated credentials | [optional] 
**cluster_role_binding** | **bool** | If true, generate a ClusterRoleBinding to grant permissions across the whole cluster instead of within a namespace. Requires the Vault role to have kubernetes_role_type set to ClusterRole. | [optional] 
**kubernetes_namespace** | **str** | The name of the Kubernetes namespace in which to generate the credentials | 
**ttl** | **str** | The TTL of the generated credentials | [optional] 

## Example

```python
from ahvac.models.kubernetes_generate_credentials_request import KubernetesGenerateCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesGenerateCredentialsRequest from a JSON string
kubernetes_generate_credentials_request_instance = KubernetesGenerateCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesGenerateCredentialsRequest.to_json())

# convert the object into a dict
kubernetes_generate_credentials_request_dict = kubernetes_generate_credentials_request_instance.to_dict()
# create an instance of KubernetesGenerateCredentialsRequest from a dict
kubernetes_generate_credentials_request_from_dict = KubernetesGenerateCredentialsRequest.from_dict(kubernetes_generate_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


