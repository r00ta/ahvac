# PkiIssuersGenerateIntermediateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_basic_constraints** | **bool** | Whether to add a Basic Constraints extension with CA: true. Only needed as a workaround in some compatibility scenarios with Active Directory Certificate Services. | [optional] 
**alt_names** | **str** | The requested Subject Alternative Names, if any, in a comma-delimited list. May contain both DNS names and email addresses. | [optional] 
**common_name** | **str** | The requested common name; if you want more than one, specify the alternative names in the alt_names map. If not specified when signing, the common name will be taken from the CSR; other names must still be specified in alt_names or ip_sans. | [optional] 
**country** | **List[str]** | If set, Country will be set to this value. | [optional] 
**exclude_cn_from_sans** | **bool** | If true, the Common Name will not be included in DNS or Email Subject Alternate Names. Defaults to false (CN is included). | [optional] [default to False]
**format** | **str** | Format for returned data. Can be \&quot;pem\&quot;, \&quot;der\&quot;, or \&quot;pem_bundle\&quot;. If \&quot;pem_bundle\&quot;, any private key and issuing cert will be appended to the certificate pem. If \&quot;der\&quot;, the value will be base64 encoded. Defaults to \&quot;pem\&quot;. | [optional] [default to 'pem']
**ip_sans** | **List[str]** | The requested IP SANs, if any, in a comma-delimited list | [optional] 
**key_bits** | **int** | The number of bits to use. Allowed values are 0 (universal default); with rsa key_type: 2048 (default), 3072, or 4096; with ec key_type: 224, 256 (default), 384, or 521; ignored with ed25519. | [optional] [default to 0]
**key_name** | **str** | Provide a name to the generated or existing key, the name must be unique across all keys and not be the reserved value &#39;default&#39; | [optional] 
**key_ref** | **str** | Reference to a existing key; either \&quot;default\&quot; for the configured default key, an identifier or the name assigned to the key. | [optional] [default to 'default']
**key_type** | **str** | The type of key to use; defaults to RSA. \&quot;rsa\&quot; \&quot;ec\&quot; and \&quot;ed25519\&quot; are the only valid values. | [optional] [default to 'rsa']
**locality** | **List[str]** | If set, Locality will be set to this value. | [optional] 
**managed_key_id** | **str** | The name of the managed key to use when the exported type is kms. When kms type is the key type, this field or managed_key_name is required. Ignored for other types. | [optional] 
**managed_key_name** | **str** | The name of the managed key to use when the exported type is kms. When kms type is the key type, this field or managed_key_id is required. Ignored for other types. | [optional] 
**not_after** | **str** | Set the not after field of the certificate with specified date value. The value format should be given in UTC format YYYY-MM-ddTHH:MM:SSZ | [optional] 
**not_before_duration** | **str** | The duration before now which the certificate needs to be backdated by. | [optional] [default to '30']
**organization** | **List[str]** | If set, O (Organization) will be set to this value. | [optional] 
**other_sans** | **List[str]** | Requested other SANs, in an array with the format &lt;oid&gt;;UTF8:&lt;utf8 string value&gt; for each entry. | [optional] 
**ou** | **List[str]** | If set, OU (OrganizationalUnit) will be set to this value. | [optional] 
**postal_code** | **List[str]** | If set, Postal Code will be set to this value. | [optional] 
**private_key_format** | **str** | Format for the returned private key. Generally the default will be controlled by the \&quot;format\&quot; parameter as either base64-encoded DER or PEM-encoded DER. However, this can be set to \&quot;pkcs8\&quot; to have the returned private key contain base64-encoded pkcs8 or PEM-encoded pkcs8 instead. Defaults to \&quot;der\&quot;. | [optional] [default to 'der']
**province** | **List[str]** | If set, Province will be set to this value. | [optional] 
**serial_number** | **str** | The Subject&#39;s requested serial number, if any. See RFC 4519 Section 2.31 &#39;serialNumber&#39; for a description of this field. If you want more than one, specify alternative names in the alt_names map using OID 2.5.4.5. This has no impact on the final certificate&#39;s Serial Number field. | [optional] 
**signature_bits** | **int** | The number of bits to use in the signature algorithm; accepts 256 for SHA-2-256, 384 for SHA-2-384, and 512 for SHA-2-512. Defaults to 0 to automatically detect based on key length (SHA-2-256 for RSA keys, and matching the curve size for NIST P-Curves). | [optional] [default to 0]
**street_address** | **List[str]** | If set, Street Address will be set to this value. | [optional] 
**ttl** | **str** | The requested Time To Live for the certificate; sets the expiration date. If not specified the role default, backend default, or system default TTL is used, in that order. Cannot be larger than the mount max TTL. Note: this only has an effect when generating a CA cert or signing a CA cert, not when generating a CSR for an intermediate CA. | [optional] 
**uri_sans** | **List[str]** | The requested URI SANs, if any, in a comma-delimited list. | [optional] 

## Example

```python
from ahvac.models.pki_issuers_generate_intermediate_request import PkiIssuersGenerateIntermediateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuersGenerateIntermediateRequest from a JSON string
pki_issuers_generate_intermediate_request_instance = PkiIssuersGenerateIntermediateRequest.from_json(json)
# print the JSON string representation of the object
print(PkiIssuersGenerateIntermediateRequest.to_json())

# convert the object into a dict
pki_issuers_generate_intermediate_request_dict = pki_issuers_generate_intermediate_request_instance.to_dict()
# create an instance of PkiIssuersGenerateIntermediateRequest from a dict
pki_issuers_generate_intermediate_request_from_dict = PkiIssuersGenerateIntermediateRequest.from_dict(pki_issuers_generate_intermediate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


