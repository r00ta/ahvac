# PkiIssuersImportCertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pem_bundle** | **str** | PEM-format, concatenated unencrypted secret-key (optional) and certificates. | [optional] 

## Example

```python
from ahvac.models.pki_issuers_import_cert_request import PkiIssuersImportCertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuersImportCertRequest from a JSON string
pki_issuers_import_cert_request_instance = PkiIssuersImportCertRequest.from_json(json)
# print the JSON string representation of the object
print(PkiIssuersImportCertRequest.to_json())

# convert the object into a dict
pki_issuers_import_cert_request_dict = pki_issuers_import_cert_request_instance.to_dict()
# create an instance of PkiIssuersImportCertRequest from a dict
pki_issuers_import_cert_request_from_dict = PkiIssuersImportCertRequest.from_dict(pki_issuers_import_cert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


