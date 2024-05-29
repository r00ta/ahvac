# PkiConfigureAutoTidyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_account_safety_buffer** | **int** | Safety buffer after creation after which accounts lacking orders are revoked | [optional] 
**enabled** | **bool** | Specifies whether automatic tidy is enabled or not | [optional] 
**interval_duration** | **int** | Specifies the duration between automatic tidy operation | [optional] 
**issuer_safety_buffer** | **int** | Issuer safety buffer | [optional] 
**maintain_stored_certificate_counts** | **bool** |  | [optional] 
**pause_duration** | **str** | Duration to pause between tidying certificates | [optional] 
**publish_stored_certificate_count_metrics** | **bool** |  | [optional] 
**revocation_queue_safety_buffer** | **int** |  | [optional] 
**safety_buffer** | **int** | Safety buffer time duration | [optional] 
**tidy_acme** | **bool** | Tidy Unused Acme Accounts, and Orders | [optional] 
**tidy_cert_store** | **bool** | Specifies whether to tidy up the certificate store | [optional] 
**tidy_cross_cluster_revoked_certs** | **bool** | Tidy the cross-cluster revoked certificate store | [optional] 
**tidy_expired_issuers** | **bool** | Specifies whether tidy expired issuers | [optional] 
**tidy_move_legacy_ca_bundle** | **bool** |  | [optional] 
**tidy_revocation_queue** | **bool** |  | [optional] 
**tidy_revoked_cert_issuer_associations** | **bool** | Specifies whether to associate revoked certificates with their corresponding issuers | [optional] 
**tidy_revoked_certs** | **bool** | Specifies whether to remove all invalid and expired certificates from storage | [optional] 

## Example

```python
from ahvac.models.pki_configure_auto_tidy_response import PkiConfigureAutoTidyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureAutoTidyResponse from a JSON string
pki_configure_auto_tidy_response_instance = PkiConfigureAutoTidyResponse.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureAutoTidyResponse.to_json())

# convert the object into a dict
pki_configure_auto_tidy_response_dict = pki_configure_auto_tidy_response_instance.to_dict()
# create an instance of PkiConfigureAutoTidyResponse from a dict
pki_configure_auto_tidy_response_from_dict = PkiConfigureAutoTidyResponse.from_dict(pki_configure_auto_tidy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


