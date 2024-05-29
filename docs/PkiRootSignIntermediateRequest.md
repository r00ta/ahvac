# PkiRootSignIntermediateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_names** | **str** | The requested Subject Alternative Names, if any, in a comma-delimited list. May contain both DNS names and email addresses. | [optional] 
**common_name** | **str** | The requested common name; if you want more than one, specify the alternative names in the alt_names map. If not specified when signing, the common name will be taken from the CSR; other names must still be specified in alt_names or ip_sans. | [optional] 
**country** | **List[str]** | If set, Country will be set to this value. | [optional] 
**csr** | **str** | PEM-format CSR to be signed. | [optional] [default to '']
**exclude_cn_from_sans** | **bool** | If true, the Common Name will not be included in DNS or Email Subject Alternate Names. Defaults to false (CN is included). | [optional] [default to False]
**format** | **str** | Format for returned data. Can be \&quot;pem\&quot;, \&quot;der\&quot;, or \&quot;pem_bundle\&quot;. If \&quot;pem_bundle\&quot;, any private key and issuing cert will be appended to the certificate pem. If \&quot;der\&quot;, the value will be base64 encoded. Defaults to \&quot;pem\&quot;. | [optional] [default to 'pem']
**ip_sans** | **List[str]** | The requested IP SANs, if any, in a comma-delimited list | [optional] 
**issuer_name** | **str** | Provide a name to the generated or existing issuer, the name must be unique across all issuers and not be the reserved value &#39;default&#39; | [optional] 
**issuer_ref** | **str** | Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [optional] [default to 'default']
**locality** | **List[str]** | If set, Locality will be set to this value. | [optional] 
**max_path_length** | **int** | The maximum allowable path length | [optional] [default to -1]
**not_after** | **str** | Set the not after field of the certificate with specified date value. The value format should be given in UTC format YYYY-MM-ddTHH:MM:SSZ | [optional] 
**not_before_duration** | **str** | The duration before now which the certificate needs to be backdated by. | [optional] [default to '30']
**organization** | **List[str]** | If set, O (Organization) will be set to this value. | [optional] 
**other_sans** | **List[str]** | Requested other SANs, in an array with the format &lt;oid&gt;;UTF8:&lt;utf8 string value&gt; for each entry. | [optional] 
**ou** | **List[str]** | If set, OU (OrganizationalUnit) will be set to this value. | [optional] 
**permitted_dns_domains** | **List[str]** | Domains for which this certificate is allowed to sign or issue child certificates. If set, all DNS names (subject and alt) on child certs must be exact matches or subsets of the given domains (see https://tools.ietf.org/html/rfc5280#section-4.2.1.10). | [optional] 
**postal_code** | **List[str]** | If set, Postal Code will be set to this value. | [optional] 
**private_key_format** | **str** | Format for the returned private key. Generally the default will be controlled by the \&quot;format\&quot; parameter as either base64-encoded DER or PEM-encoded DER. However, this can be set to \&quot;pkcs8\&quot; to have the returned private key contain base64-encoded pkcs8 or PEM-encoded pkcs8 instead. Defaults to \&quot;der\&quot;. | [optional] [default to 'der']
**province** | **List[str]** | If set, Province will be set to this value. | [optional] 
**serial_number** | **str** | The Subject&#39;s requested serial number, if any. See RFC 4519 Section 2.31 &#39;serialNumber&#39; for a description of this field. If you want more than one, specify alternative names in the alt_names map using OID 2.5.4.5. This has no impact on the final certificate&#39;s Serial Number field. | [optional] 
**signature_bits** | **int** | The number of bits to use in the signature algorithm; accepts 256 for SHA-2-256, 384 for SHA-2-384, and 512 for SHA-2-512. Defaults to 0 to automatically detect based on key length (SHA-2-256 for RSA keys, and matching the curve size for NIST P-Curves). | [optional] [default to 0]
**skid** | **str** | Value for the Subject Key Identifier field (RFC 5280 Section 4.2.1.2). This value should ONLY be used when cross-signing to mimic the existing certificate&#39;s SKID value; this is necessary to allow certain TLS implementations (such as OpenSSL) which use SKID/AKID matches in chain building to restrict possible valid chains. Specified as a string in hex format. Default is empty, allowing Vault to automatically calculate the SKID according to method one in the above RFC section. | [optional] [default to '']
**street_address** | **List[str]** | If set, Street Address will be set to this value. | [optional] 
**ttl** | **str** | The requested Time To Live for the certificate; sets the expiration date. If not specified the role default, backend default, or system default TTL is used, in that order. Cannot be larger than the mount max TTL. Note: this only has an effect when generating a CA cert or signing a CA cert, not when generating a CSR for an intermediate CA. | [optional] 
**uri_sans** | **List[str]** | The requested URI SANs, if any, in a comma-delimited list. | [optional] 
**use_csr_values** | **bool** | If true, then: 1) Subject information, including names and alternate names, will be preserved from the CSR rather than using values provided in the other parameters to this path; 2) Any key usages requested in the CSR will be added to the basic set of key usages used for CA certs signed by this path; for instance, the non-repudiation flag; 3) Extensions requested in the CSR will be copied into the issued certificate. | [optional] [default to False]
**use_pss** | **bool** | Whether or not to use PSS signatures when using a RSA key-type issuer. Defaults to false. | [optional] [default to False]

## Example

```python
from ahvac.models.pki_root_sign_intermediate_request import PkiRootSignIntermediateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRootSignIntermediateRequest from a JSON string
pki_root_sign_intermediate_request_instance = PkiRootSignIntermediateRequest.from_json(json)
# print the JSON string representation of the object
print(PkiRootSignIntermediateRequest.to_json())

# convert the object into a dict
pki_root_sign_intermediate_request_dict = pki_root_sign_intermediate_request_instance.to_dict()
# create an instance of PkiRootSignIntermediateRequest from a dict
pki_root_sign_intermediate_request_from_dict = PkiRootSignIntermediateRequest.from_dict(pki_root_sign_intermediate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


