# PkiRootSignSelfIssuedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Certificate | [optional] 
**issuing_ca** | **str** | Issuing CA | [optional] 

## Example

```python
from ahvac.models.pki_root_sign_self_issued_response import PkiRootSignSelfIssuedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRootSignSelfIssuedResponse from a JSON string
pki_root_sign_self_issued_response_instance = PkiRootSignSelfIssuedResponse.from_json(json)
# print the JSON string representation of the object
print(PkiRootSignSelfIssuedResponse.to_json())

# convert the object into a dict
pki_root_sign_self_issued_response_dict = pki_root_sign_self_issued_response_instance.to_dict()
# create an instance of PkiRootSignSelfIssuedResponse from a dict
pki_root_sign_self_issued_response_from_dict = PkiRootSignSelfIssuedResponse.from_dict(pki_root_sign_self_issued_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


