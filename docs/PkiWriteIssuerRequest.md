# PkiWriteIssuerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl_distribution_points** | **List[str]** | Comma-separated list of URLs to be used for the CRL distribution points attribute. See also RFC 5280 Section 4.2.1.13. | [optional] 
**enable_aia_url_templating** | **bool** | Whether or not to enabling templating of the above AIA fields. When templating is enabled the special values &#39;{{issuer_id}}&#39;, &#39;{{cluster_path}}&#39;, &#39;{{cluster_aia_path}}&#39; are available, but the addresses are not checked for URL validity until issuance time. Using &#39;{{cluster_path}}&#39; requires /config/cluster&#39;s &#39;path&#39; member to be set on all PR Secondary clusters and using &#39;{{cluster_aia_path}}&#39; requires /config/cluster&#39;s &#39;aia_path&#39; member to be set on all PR secondary clusters. | [optional] [default to False]
**issuer_name** | **str** | Provide a name to the generated or existing issuer, the name must be unique across all issuers and not be the reserved value &#39;default&#39; | [optional] 
**issuing_certificates** | **List[str]** | Comma-separated list of URLs to be used for the issuing certificate attribute. See also RFC 5280 Section 4.2.2.1. | [optional] 
**leaf_not_after_behavior** | **str** | Behavior of leaf&#39;s NotAfter fields: \&quot;err\&quot; to error if the computed NotAfter date exceeds that of this issuer; \&quot;truncate\&quot; to silently truncate to that of this issuer; or \&quot;permit\&quot; to allow this issuance to succeed (with NotAfter exceeding that of an issuer). Note that not all values will results in certificates that can be validated through the entire validity period. It is suggested to use \&quot;truncate\&quot; for intermediate CAs and \&quot;permit\&quot; only for root CAs. | [optional] [default to 'err']
**manual_chain** | **List[str]** | Chain of issuer references to use to build this issuer&#39;s computed CAChain field, when non-empty. | [optional] 
**ocsp_servers** | **List[str]** | Comma-separated list of URLs to be used for the OCSP servers attribute. See also RFC 5280 Section 4.2.2.1. | [optional] 
**revocation_signature_algorithm** | **str** | Which x509.SignatureAlgorithm name to use for signing CRLs. This parameter allows differentiation between PKCS#1v1.5 and PSS keys and choice of signature hash algorithm. The default (empty string) value is for Go to select the signature algorithm. This can fail if the underlying key does not support the requested signature algorithm, which may not be known at modification time (such as with PKCS#11 managed RSA keys). | [optional] [default to '']
**usage** | **List[str]** | Comma-separated list (or string slice) of usages for this issuer; valid values are \&quot;read-only\&quot;, \&quot;issuing-certificates\&quot;, \&quot;crl-signing\&quot;, and \&quot;ocsp-signing\&quot;. Multiple values may be specified. Read-only is implicit and always set. | [optional] [default to ["read-only","issuing-certificates","crl-signing","ocsp-signing"]]

## Example

```python
from ahvac.models.pki_write_issuer_request import PkiWriteIssuerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiWriteIssuerRequest from a JSON string
pki_write_issuer_request_instance = PkiWriteIssuerRequest.from_json(json)
# print the JSON string representation of the object
print(PkiWriteIssuerRequest.to_json())

# convert the object into a dict
pki_write_issuer_request_dict = pki_write_issuer_request_instance.to_dict()
# create an instance of PkiWriteIssuerRequest from a dict
pki_write_issuer_request_from_dict = PkiWriteIssuerRequest.from_dict(pki_write_issuer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


