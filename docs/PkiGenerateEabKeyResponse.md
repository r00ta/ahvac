# PkiGenerateEabKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_directory** | **str** | The ACME directory to which the key belongs | [optional] 
**created_on** | **datetime** | An RFC3339 formatted date time when the EAB token was created | [optional] 
**id** | **str** | The EAB key identifier | [optional] 
**key** | **str** | The EAB hmac key | [optional] 
**key_type** | **str** | The EAB key type | [optional] 

## Example

```python
from ahvac.models.pki_generate_eab_key_response import PkiGenerateEabKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiGenerateEabKeyResponse from a JSON string
pki_generate_eab_key_response_instance = PkiGenerateEabKeyResponse.from_json(json)
# print the JSON string representation of the object
print(PkiGenerateEabKeyResponse.to_json())

# convert the object into a dict
pki_generate_eab_key_response_dict = pki_generate_eab_key_response_instance.to_dict()
# create an instance of PkiGenerateEabKeyResponse from a dict
pki_generate_eab_key_response_from_dict = PkiGenerateEabKeyResponse.from_dict(pki_generate_eab_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


