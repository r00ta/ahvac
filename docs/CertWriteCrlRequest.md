# CertWriteCrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl** | **str** | The public CRL that should be trusted to attest to certificates&#39; validity statuses. May be DER or PEM encoded. Note: the expiration time is ignored; if the CRL is no longer valid, delete it using the same name as specified here. | [optional] 
**url** | **str** | The URL of a CRL distribution point. Only one of &#39;crl&#39; or &#39;url&#39; parameters should be specified. | [optional] 

## Example

```python
from ahvac.models.cert_write_crl_request import CertWriteCrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertWriteCrlRequest from a JSON string
cert_write_crl_request_instance = CertWriteCrlRequest.from_json(json)
# print the JSON string representation of the object
print(CertWriteCrlRequest.to_json())

# convert the object into a dict
cert_write_crl_request_dict = cert_write_crl_request_instance.to_dict()
# create an instance of CertWriteCrlRequest from a dict
cert_write_crl_request_from_dict = CertWriteCrlRequest.from_dict(cert_write_crl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


