# PkiReadIssuerDerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **List[str]** | CA Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**issuer_id** | **str** | Issuer Id | [optional] 
**issuer_name** | **str** | Issuer Name | [optional] 

## Example

```python
from ahvac.models.pki_read_issuer_der_response import PkiReadIssuerDerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadIssuerDerResponse from a JSON string
pki_read_issuer_der_response_instance = PkiReadIssuerDerResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadIssuerDerResponse.to_json())

# convert the object into a dict
pki_read_issuer_der_response_dict = pki_read_issuer_der_response_instance.to_dict()
# create an instance of PkiReadIssuerDerResponse from a dict
pki_read_issuer_der_response_from_dict = PkiReadIssuerDerResponse.from_dict(pki_read_issuer_der_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


