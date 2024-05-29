# PkiRevokeIssuerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **List[str]** | Certificate Authority Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**crl_distribution_points** | **List[str]** | Specifies the URL values for the CRL Distribution Points field | [optional] 
**issuer_id** | **str** | ID of the issuer | [optional] 
**issuer_name** | **str** | Name of the issuer | [optional] 
**issuing_certificates** | **List[str]** | Specifies the URL values for the Issuing Certificate field | [optional] 
**key_id** | **str** | ID of the Key | [optional] 
**leaf_not_after_behavior** | **str** |  | [optional] 
**manual_chain** | **List[str]** | Manual Chain | [optional] 
**ocsp_servers** | **List[str]** | Specifies the URL values for the OCSP Servers field | [optional] 
**revocation_signature_algorithm** | **str** | Which signature algorithm to use when building CRLs | [optional] 
**revocation_time** | **int** | Time of revocation | [optional] 
**revocation_time_rfc3339** | **datetime** | RFC formatted time of revocation | [optional] 
**revoked** | **bool** | Whether the issuer was revoked | [optional] 
**usage** | **str** | Allowed usage | [optional] 

## Example

```python
from ahvac.models.pki_revoke_issuer_response import PkiRevokeIssuerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRevokeIssuerResponse from a JSON string
pki_revoke_issuer_response_instance = PkiRevokeIssuerResponse.from_json(json)
# print the JSON string representation of the object
print(PkiRevokeIssuerResponse.to_json())

# convert the object into a dict
pki_revoke_issuer_response_dict = pki_revoke_issuer_response_instance.to_dict()
# create an instance of PkiRevokeIssuerResponse from a dict
pki_revoke_issuer_response_from_dict = PkiRevokeIssuerResponse.from_dict(pki_revoke_issuer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


