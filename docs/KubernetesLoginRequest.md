# KubernetesLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | A signed JWT for authenticating a service account. This field is required. | [optional] 
**role** | **str** | Name of the role against which the login is being attempted. This field is required | [optional] 

## Example

```python
from ahvac.models.kubernetes_login_request import KubernetesLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesLoginRequest from a JSON string
kubernetes_login_request_instance = KubernetesLoginRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesLoginRequest.to_json())

# convert the object into a dict
kubernetes_login_request_dict = kubernetes_login_request_instance.to_dict()
# create an instance of KubernetesLoginRequest from a dict
kubernetes_login_request_from_dict = KubernetesLoginRequest.from_dict(kubernetes_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


