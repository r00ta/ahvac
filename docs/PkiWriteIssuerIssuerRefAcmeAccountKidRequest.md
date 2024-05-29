# PkiWriteIssuerIssuerRefAcmeAccountKidRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | ACME request &#39;payload&#39; value | [optional] 
**protected** | **str** | ACME request &#39;protected&#39; value | [optional] 
**signature** | **str** | ACME request &#39;signature&#39; value | [optional] 

## Example

```python
from ahvac.models.pki_write_issuer_issuer_ref_acme_account_kid_request import PkiWriteIssuerIssuerRefAcmeAccountKidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiWriteIssuerIssuerRefAcmeAccountKidRequest from a JSON string
pki_write_issuer_issuer_ref_acme_account_kid_request_instance = PkiWriteIssuerIssuerRefAcmeAccountKidRequest.from_json(json)
# print the JSON string representation of the object
print(PkiWriteIssuerIssuerRefAcmeAccountKidRequest.to_json())

# convert the object into a dict
pki_write_issuer_issuer_ref_acme_account_kid_request_dict = pki_write_issuer_issuer_ref_acme_account_kid_request_instance.to_dict()
# create an instance of PkiWriteIssuerIssuerRefAcmeAccountKidRequest from a dict
pki_write_issuer_issuer_ref_acme_account_kid_request_from_dict = PkiWriteIssuerIssuerRefAcmeAccountKidRequest.from_dict(pki_write_issuer_issuer_ref_acme_account_kid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


