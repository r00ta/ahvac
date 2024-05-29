# KubernetesConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_local_ca_jwt** | **bool** | Disable defaulting to the local CA certificate and service account JWT when running in a Kubernetes pod. | [optional] [default to False]
**kubernetes_ca_cert** | **str** | PEM encoded CA certificate to use to verify the Kubernetes API server certificate. Defaults to the local pod&#39;s CA if found. | [optional] 
**kubernetes_host** | **str** | Kubernetes API URL to connect to. Defaults to https://$KUBERNETES_SERVICE_HOST:KUBERNETES_SERVICE_PORT if those environment variables are set. | [optional] 
**service_account_jwt** | **str** | The JSON web token of the service account used by the secret engine to manage Kubernetes credentials. Defaults to the local pod&#39;s JWT if found. | [optional] 

## Example

```python
from ahvac.models.kubernetes_configure_request import KubernetesConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesConfigureRequest from a JSON string
kubernetes_configure_request_instance = KubernetesConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesConfigureRequest.to_json())

# convert the object into a dict
kubernetes_configure_request_dict = kubernetes_configure_request_instance.to_dict()
# create an instance of KubernetesConfigureRequest from a dict
kubernetes_configure_request_from_dict = KubernetesConfigureRequest.from_dict(kubernetes_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


