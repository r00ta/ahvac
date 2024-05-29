# PkiPatchIssuerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain** | **List[str]** | CA Chain | [optional] 
**certificate** | **str** | Certificate | [optional] 
**crl_distribution_points** | **List[str]** | CRL Distribution Points | [optional] 
**enable_aia_url_templating** | **bool** | Whether or not templating is enabled for AIA fields | [optional] 
**issuer_id** | **str** | Issuer Id | [optional] 
**issuer_name** | **str** | Issuer Name | [optional] 
**issuing_certificates** | **List[str]** | Issuing Certificates | [optional] 
**key_id** | **str** | Key Id | [optional] 
**leaf_not_after_behavior** | **str** | Leaf Not After Behavior | [optional] 
**manual_chain** | **List[str]** | Manual Chain | [optional] 
**ocsp_servers** | **List[str]** | OCSP Servers | [optional] 
**revocation_signature_algorithm** | **str** | Revocation Signature Alogrithm | [optional] 
**revocation_time** | **int** |  | [optional] 
**revocation_time_rfc3339** | **str** |  | [optional] 
**revoked** | **bool** | Revoked | [optional] 
**usage** | **str** | Usage | [optional] 

## Example

```python
from ahvac.models.pki_patch_issuer_response import PkiPatchIssuerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiPatchIssuerResponse from a JSON string
pki_patch_issuer_response_instance = PkiPatchIssuerResponse.from_json(json)
# print the JSON string representation of the object
print(PkiPatchIssuerResponse.to_json())

# convert the object into a dict
pki_patch_issuer_response_dict = pki_patch_issuer_response_instance.to_dict()
# create an instance of PkiPatchIssuerResponse from a dict
pki_patch_issuer_response_from_dict = PkiPatchIssuerResponse.from_dict(pki_patch_issuer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


