# PkiListIssuersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_info** | **object** | Key info with issuer name | [optional] 
**keys** | **List[str]** | A list of keys | [optional] 

## Example

```python
from ahvac.models.pki_list_issuers_response import PkiListIssuersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiListIssuersResponse from a JSON string
pki_list_issuers_response_instance = PkiListIssuersResponse.from_json(json)
# print the JSON string representation of the object
print(PkiListIssuersResponse.to_json())

# convert the object into a dict
pki_list_issuers_response_dict = pki_list_issuers_response_instance.to_dict()
# create an instance of PkiListIssuersResponse from a dict
pki_list_issuers_response_from_dict = PkiListIssuersResponse.from_dict(pki_list_issuers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


