# PkiReadIssuerJsonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **List[str]** | CA Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**issuer_id** | **str** | Issuer Id | [optional] 
**issuer_name** | **str** | Issuer Name | [optional] 

## Example

```python
from ahvac.models.pki_read_issuer_json_response import PkiReadIssuerJsonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadIssuerJsonResponse from a JSON string
pki_read_issuer_json_response_instance = PkiReadIssuerJsonResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadIssuerJsonResponse.to_json())

# convert the object into a dict
pki_read_issuer_json_response_dict = pki_read_issuer_json_response_instance.to_dict()
# create an instance of PkiReadIssuerJsonResponse from a dict
pki_read_issuer_json_response_from_dict = PkiReadIssuerJsonResponse.from_dict(pki_read_issuer_json_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


