# PkiTidyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acme_account_safety_buffer** | **str** | The amount of time that must pass after creation that an account with no orders is marked revoked, and the amount of time after being marked revoked or deactivated. | [optional] [default to '2592000']
**issuer_safety_buffer** | **str** | The amount of extra time that must have passed beyond issuer&#39;s expiration before it is removed from the backend storage. Defaults to 8760 hours (1 year). | [optional] [default to '31536000']
**pause_duration** | **str** | The amount of time to wait between processing certificates. This allows operators to change the execution profile of tidy to take consume less resources by slowing down how long it takes to run. Note that the entire list of certificates will be stored in memory during the entire tidy operation, but resources to read/process/update existing entries will be spread out over a greater period of time. By default this is zero seconds. | [optional] [default to '0s']
**revocation_queue_safety_buffer** | **str** | The amount of time that must pass from the cross-cluster revocation request being initiated to when it will be slated for removal. Setting this too low may remove valid revocation requests before the owning cluster has a chance to process them, especially if the cluster is offline. | [optional] [default to '172800']
**safety_buffer** | **str** | The amount of extra time that must have passed beyond certificate expiration before it is removed from the backend storage and/or revocation list. Defaults to 72 hours. | [optional] [default to '259200']
**tidy_acme** | **bool** | Set to true to enable tidying ACME accounts, orders and authorizations. ACME orders are tidied (deleted) safety_buffer after the certificate associated with them expires, or after the order and relevant authorizations have expired if no certificate was produced. Authorizations are tidied with the corresponding order. When a valid ACME Account is at least acme_account_safety_buffer old, and has no remaining orders associated with it, the account is marked as revoked. After another acme_account_safety_buffer has passed from the revocation or deactivation date, a revoked or deactivated ACME account is deleted. | [optional] [default to False]
**tidy_cert_store** | **bool** | Set to true to enable tidying up the certificate store | [optional] 
**tidy_cross_cluster_revoked_certs** | **bool** | Set to true to enable tidying up the cross-cluster revoked certificate store. Only runs on the active primary node. | [optional] 
**tidy_expired_issuers** | **bool** | Set to true to automatically remove expired issuers past the issuer_safety_buffer. No keys will be removed as part of this operation. | [optional] 
**tidy_move_legacy_ca_bundle** | **bool** | Set to true to move the legacy ca_bundle from /config/ca_bundle to /config/ca_bundle.bak. This prevents downgrades to pre-Vault 1.11 versions (as older PKI engines do not know about the new multi-issuer storage layout), but improves the performance on seal wrapped PKI mounts. This will only occur if at least issuer_safety_buffer time has occurred after the initial storage migration. This backup is saved in case of an issue in future migrations. Operators may consider removing it via sys/raw if they desire. The backup will be removed via a DELETE /root call, but note that this removes ALL issuers within the mount (and is thus not desirable in most operational scenarios). | [optional] 
**tidy_revocation_list** | **bool** | Deprecated; synonym for &#39;tidy_revoked_certs | [optional] 
**tidy_revocation_queue** | **bool** | Set to true to remove stale revocation queue entries that haven&#39;t been confirmed by any active cluster. Only runs on the active primary node | [optional] [default to False]
**tidy_revoked_cert_issuer_associations** | **bool** | Set to true to validate issuer associations on revocation entries. This helps increase the performance of CRL building and OCSP responses. | [optional] 
**tidy_revoked_certs** | **bool** | Set to true to expire all revoked and expired certificates, removing them both from the CRL and from storage. The CRL will be rotated if this causes any values to be removed. | [optional] 

## Example

```python
from ahvac.models.pki_tidy_request import PkiTidyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiTidyRequest from a JSON string
pki_tidy_request_instance = PkiTidyRequest.from_json(json)
# print the JSON string representation of the object
print(PkiTidyRequest.to_json())

# convert the object into a dict
pki_tidy_request_dict = pki_tidy_request_instance.to_dict()
# create an instance of PkiTidyRequest from a dict
pki_tidy_request_from_dict = PkiTidyRequest.from_dict(pki_tidy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


