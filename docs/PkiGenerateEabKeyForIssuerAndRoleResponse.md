# PkiGenerateEabKeyForIssuerAndRoleResponse


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
from ahvac.models.pki_generate_eab_key_for_issuer_and_role_response import PkiGenerateEabKeyForIssuerAndRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiGenerateEabKeyForIssuerAndRoleResponse from a JSON string
pki_generate_eab_key_for_issuer_and_role_response_instance = PkiGenerateEabKeyForIssuerAndRoleResponse.from_json(json)
# print the JSON string representation of the object
print(PkiGenerateEabKeyForIssuerAndRoleResponse.to_json())

# convert the object into a dict
pki_generate_eab_key_for_issuer_and_role_response_dict = pki_generate_eab_key_for_issuer_and_role_response_instance.to_dict()
# create an instance of PkiGenerateEabKeyForIssuerAndRoleResponse from a dict
pki_generate_eab_key_for_issuer_and_role_response_from_dict = PkiGenerateEabKeyForIssuerAndRoleResponse.from_dict(pki_generate_eab_key_for_issuer_and_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


