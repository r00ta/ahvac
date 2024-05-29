# PkiReadCrlConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_rebuild** | **bool** | If set to true, enables automatic rebuilding of the CRL | [optional] 
**auto_rebuild_grace_period** | **str** | The time before the CRL expires to automatically rebuild it, when enabled. Must be shorter than the CRL expiry. Defaults to 12h. | [optional] 
**cross_cluster_revocation** | **bool** | Whether to enable a global, cross-cluster revocation queue. Must be used with auto_rebuild&#x3D;true. | [optional] 
**delta_rebuild_interval** | **str** | The time between delta CRL rebuilds if a new revocation has occurred. Must be shorter than the CRL expiry. Defaults to 15m. | [optional] 
**disable** | **bool** | If set to true, disables generating the CRL entirely. | [optional] 
**enable_delta** | **bool** | Whether to enable delta CRLs between authoritative CRL rebuilds | [optional] 
**expiry** | **str** | The amount of time the generated CRL should be valid; defaults to 72 hours | [optional] 
**ocsp_disable** | **bool** | If set to true, ocsp unauthorized responses will be returned. | [optional] 
**ocsp_expiry** | **str** | The amount of time an OCSP response will be valid (controls the NextUpdate field); defaults to 12 hours | [optional] 
**unified_crl** | **bool** | If set to true enables global replication of revocation entries, also enabling unified versions of OCSP and CRLs if their respective features are enabled. disable for CRLs and ocsp_disable for OCSP. | [optional] 
**unified_crl_on_existing_paths** | **bool** | If set to true, existing CRL and OCSP paths will return the unified CRL instead of a response based on cluster-local data | [optional] 

## Example

```python
from ahvac.models.pki_read_crl_configuration_response import PkiReadCrlConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadCrlConfigurationResponse from a JSON string
pki_read_crl_configuration_response_instance = PkiReadCrlConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadCrlConfigurationResponse.to_json())

# convert the object into a dict
pki_read_crl_configuration_response_dict = pki_read_crl_configuration_response_instance.to_dict()
# create an instance of PkiReadCrlConfigurationResponse from a dict
pki_read_crl_configuration_response_from_dict = PkiReadCrlConfigurationResponse.from_dict(pki_read_crl_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


