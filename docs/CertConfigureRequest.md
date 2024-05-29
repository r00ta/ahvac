# CertConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_binding** | **bool** | If set, during renewal, skips the matching of presented client identity with the client identity used during login. Defaults to false. | [optional] [default to False]
**enable_identity_alias_metadata** | **bool** | If set, metadata of the certificate including the metadata corresponding to allowed_metadata_extensions will be stored in the alias. Defaults to false. | [optional] [default to False]
**ocsp_cache_size** | **int** | The size of the in memory OCSP response cache, shared by all configured certs | [optional] [default to 100]

## Example

```python
from ahvac.models.cert_configure_request import CertConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertConfigureRequest from a JSON string
cert_configure_request_instance = CertConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(CertConfigureRequest.to_json())

# convert the object into a dict
cert_configure_request_dict = cert_configure_request_instance.to_dict()
# create an instance of CertConfigureRequest from a dict
cert_configure_request_from_dict = CertConfigureRequest.from_dict(cert_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


