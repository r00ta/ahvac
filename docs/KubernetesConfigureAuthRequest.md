# KubernetesConfigureAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_iss_validation** | **bool** | Disable JWT issuer validation (Deprecated, will be removed in a future release) | [optional] [default to True]
**disable_local_ca_jwt** | **bool** | Disable defaulting to the local CA cert and service account JWT when running in a Kubernetes pod | [optional] [default to False]
**issuer** | **str** | Optional JWT issuer. If no issuer is specified, then this plugin will use kubernetes.io/serviceaccount as the default issuer. (Deprecated, will be removed in a future release) | [optional] 
**kubernetes_ca_cert** | **str** | PEM encoded CA cert for use by the TLS client used to talk with the API. | [optional] 
**kubernetes_host** | **str** | Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server. | [optional] 
**pem_keys** | **List[str]** | Optional list of PEM-formated public keys or certificates used to verify the signatures of kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys. | [optional] 
**token_reviewer_jwt** | **str** | A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API. | [optional] 

## Example

```python
from ahvac.models.kubernetes_configure_auth_request import KubernetesConfigureAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesConfigureAuthRequest from a JSON string
kubernetes_configure_auth_request_instance = KubernetesConfigureAuthRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesConfigureAuthRequest.to_json())

# convert the object into a dict
kubernetes_configure_auth_request_dict = kubernetes_configure_auth_request_instance.to_dict()
# create an instance of KubernetesConfigureAuthRequest from a dict
kubernetes_configure_auth_request_from_dict = KubernetesConfigureAuthRequest.from_dict(kubernetes_configure_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


