# PkiIssuersImportBundleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pem_bundle** | **str** | PEM-format, concatenated unencrypted secret-key (optional) and certificates. | [optional] 

## Example

```python
from ahvac.models.pki_issuers_import_bundle_request import PkiIssuersImportBundleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuersImportBundleRequest from a JSON string
pki_issuers_import_bundle_request_instance = PkiIssuersImportBundleRequest.from_json(json)
# print the JSON string representation of the object
print(PkiIssuersImportBundleRequest.to_json())

# convert the object into a dict
pki_issuers_import_bundle_request_dict = pki_issuers_import_bundle_request_instance.to_dict()
# create an instance of PkiIssuersImportBundleRequest from a dict
pki_issuers_import_bundle_request_from_dict = PkiIssuersImportBundleRequest.from_dict(pki_issuers_import_bundle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


