# PkiSignWithRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_names** | **str** | The requested Subject Alternative Names, if any, in a comma-delimited list. If email protection is enabled for the role, this may contain email addresses. | [optional] 
**common_name** | **str** | The requested common name; if you want more than one, specify the alternative names in the alt_names map. If email protection is enabled in the role, this may be an email address. | [optional] 
**csr** | **str** | PEM-format CSR to be signed. | [optional] [default to '']
**exclude_cn_from_sans** | **bool** | If true, the Common Name will not be included in DNS or Email Subject Alternate Names. Defaults to false (CN is included). | [optional] [default to False]
**format** | **str** | Format for returned data. Can be \&quot;pem\&quot;, \&quot;der\&quot;, or \&quot;pem_bundle\&quot;. If \&quot;pem_bundle\&quot;, any private key and issuing cert will be appended to the certificate pem. If \&quot;der\&quot;, the value will be base64 encoded. Defaults to \&quot;pem\&quot;. | [optional] [default to 'pem']
**ip_sans** | **List[str]** | The requested IP SANs, if any, in a comma-delimited list | [optional] 
**issuer_ref** | **str** | Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [optional] [default to 'default']
**not_after** | **str** | Set the not after field of the certificate with specified date value. The value format should be given in UTC format YYYY-MM-ddTHH:MM:SSZ | [optional] 
**other_sans** | **List[str]** | Requested other SANs, in an array with the format &lt;oid&gt;;UTF8:&lt;utf8 string value&gt; for each entry. | [optional] 
**private_key_format** | **str** | Format for the returned private key. Generally the default will be controlled by the \&quot;format\&quot; parameter as either base64-encoded DER or PEM-encoded DER. However, this can be set to \&quot;pkcs8\&quot; to have the returned private key contain base64-encoded pkcs8 or PEM-encoded pkcs8 instead. Defaults to \&quot;der\&quot;. | [optional] [default to 'der']
**remove_roots_from_chain** | **bool** | Whether or not to remove self-signed CA certificates in the output of the ca_chain field. | [optional] [default to False]
**serial_number** | **str** | The Subject&#39;s requested serial number, if any. See RFC 4519 Section 2.31 &#39;serialNumber&#39; for a description of this field. If you want more than one, specify alternative names in the alt_names map using OID 2.5.4.5. This has no impact on the final certificate&#39;s Serial Number field. | [optional] 
**ttl** | **str** | The requested Time To Live for the certificate; sets the expiration date. If not specified the role default, backend default, or system default TTL is used, in that order. Cannot be larger than the role max TTL. | [optional] 
**uri_sans** | **List[str]** | The requested URI SANs, if any, in a comma-delimited list. | [optional] 
**user_ids** | **List[str]** | The requested user_ids value to place in the subject, if any, in a comma-delimited list. Restricted by allowed_user_ids. Any values are added with OID 0.9.2342.19200300.100.1.1. | [optional] 

## Example

```python
from ahvac.models.pki_sign_with_role_request import PkiSignWithRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiSignWithRoleRequest from a JSON string
pki_sign_with_role_request_instance = PkiSignWithRoleRequest.from_json(json)
# print the JSON string representation of the object
print(PkiSignWithRoleRequest.to_json())

# convert the object into a dict
pki_sign_with_role_request_dict = pki_sign_with_role_request_instance.to_dict()
# create an instance of PkiSignWithRoleRequest from a dict
pki_sign_with_role_request_from_dict = PkiSignWithRoleRequest.from_dict(pki_sign_with_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


