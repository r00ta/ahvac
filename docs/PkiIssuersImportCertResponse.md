# PkiIssuersImportCertResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_issuers** | **List[str]** | Existing issuers specified as part of the import bundle of this request | [optional] 
**existing_keys** | **List[str]** | Existing keys specified as part of the import bundle of this request | [optional] 
**imported_issuers** | **List[str]** | Net-new issuers imported as a part of this request | [optional] 
**imported_keys** | **List[str]** | Net-new keys imported as a part of this request | [optional] 
**mapping** | **object** | A mapping of issuer_id to key_id for all issuers included in this request | [optional] 

## Example

```python
from ahvac.models.pki_issuers_import_cert_response import PkiIssuersImportCertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuersImportCertResponse from a JSON string
pki_issuers_import_cert_response_instance = PkiIssuersImportCertResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuersImportCertResponse.to_json())

# convert the object into a dict
pki_issuers_import_cert_response_dict = pki_issuers_import_cert_response_instance.to_dict()
# create an instance of PkiIssuersImportCertResponse from a dict
pki_issuers_import_cert_response_from_dict = PkiIssuersImportCertResponse.from_dict(pki_issuers_import_cert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


