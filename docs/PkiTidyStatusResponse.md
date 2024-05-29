# PkiTidyStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_account_deleted_count** | **int** | The number of revoked acme accounts removed | [optional] 
**acme_account_revoked_count** | **int** | The number of unused acme accounts revoked | [optional] 
**acme_account_safety_buffer** | **int** | Safety buffer after creation after which accounts lacking orders are revoked | [optional] 
**acme_orders_deleted_count** | **int** | The number of expired, unused acme orders removed | [optional] 
**cert_store_deleted_count** | **int** | The number of certificate storage entries deleted | [optional] 
**cross_revoked_cert_deleted_count** | **int** |  | [optional] 
**current_cert_store_count** | **int** | The number of revoked certificate entries deleted | [optional] 
**current_revoked_cert_count** | **int** | The number of revoked certificate entries deleted | [optional] 
**error** | **str** | The error message | [optional] 
**internal_backend_uuid** | **str** |  | [optional] 
**issuer_safety_buffer** | **int** | Issuer safety buffer | [optional] 
**last_auto_tidy_finished** | **str** | Time the last auto-tidy operation finished | [optional] 
**message** | **str** | Message of the operation | [optional] 
**missing_issuer_cert_count** | **int** |  | [optional] 
**pause_duration** | **str** | Duration to pause between tidying certificates | [optional] 
**revocation_queue_deleted_count** | **int** |  | [optional] 
**revocation_queue_safety_buffer** | **int** | Revocation queue safety buffer | [optional] 
**revoked_cert_deleted_count** | **int** | The number of revoked certificate entries deleted | [optional] 
**safety_buffer** | **int** | Safety buffer time duration | [optional] 
**state** | **str** | One of Inactive, Running, Finished, or Error | [optional] 
**tidy_acme** | **bool** | Tidy Unused Acme Accounts, and Orders | [optional] 
**tidy_cert_store** | **bool** | Tidy certificate store | [optional] 
**tidy_cross_cluster_revoked_certs** | **bool** | Tidy the cross-cluster revoked certificate store | [optional] 
**tidy_expired_issuers** | **bool** | Tidy expired issuers | [optional] 
**tidy_move_legacy_ca_bundle** | **bool** |  | [optional] 
**tidy_revocation_queue** | **bool** |  | [optional] 
**tidy_revoked_cert_issuer_associations** | **bool** | Tidy revoked certificate issuer associations | [optional] 
**tidy_revoked_certs** | **bool** | Tidy revoked certificates | [optional] 
**time_finished** | **str** | Time the operation finished | [optional] 
**time_started** | **str** | Time the operation started | [optional] 
**total_acme_account_count** | **int** | Total number of acme accounts iterated over | [optional] 

## Example

```python
from ahvac.models.pki_tidy_status_response import PkiTidyStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiTidyStatusResponse from a JSON string
pki_tidy_status_response_instance = PkiTidyStatusResponse.from_json(json)
# print the JSON string representation of the object
print(PkiTidyStatusResponse.to_json())

# convert the object into a dict
pki_tidy_status_response_dict = pki_tidy_status_response_instance.to_dict()
# create an instance of PkiTidyStatusResponse from a dict
pki_tidy_status_response_from_dict = PkiTidyStatusResponse.from_dict(pki_tidy_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


