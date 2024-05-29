# PkiWriteAcmeNewAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | ACME request &#39;payload&#39; value | [optional] 
**protected** | **str** | ACME request &#39;protected&#39; value | [optional] 
**signature** | **str** | ACME request &#39;signature&#39; value | [optional] 

## Example

```python
from ahvac.models.pki_write_acme_new_account_request import PkiWriteAcmeNewAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiWriteAcmeNewAccountRequest from a JSON string
pki_write_acme_new_account_request_instance = PkiWriteAcmeNewAccountRequest.from_json(json)
# print the JSON string representation of the object
print(PkiWriteAcmeNewAccountRequest.to_json())

# convert the object into a dict
pki_write_acme_new_account_request_dict = pki_write_acme_new_account_request_instance.to_dict()
# create an instance of PkiWriteAcmeNewAccountRequest from a dict
pki_write_acme_new_account_request_from_dict = PkiWriteAcmeNewAccountRequest.from_dict(pki_write_acme_new_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


