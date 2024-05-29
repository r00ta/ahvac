# PkiReadRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_any_name** | **bool** | If set, clients can request certificates for any domain, regardless of allowed_domains restrictions. See the documentation for more information. | [optional] 
**allow_bare_domains** | **bool** | If set, clients can request certificates for the base domains themselves, e.g. \&quot;example.com\&quot; of domains listed in allowed_domains. This is a separate option as in some cases this can be considered a security threat. See the documentation for more information. | [optional] 
**allow_glob_domains** | **bool** | If set, domains specified in allowed_domains can include shell-style glob patterns, e.g. \&quot;ftp*.example.com\&quot;. See the documentation for more information. | [optional] 
**allow_ip_sans** | **bool** | If set, IP Subject Alternative Names are allowed. Any valid IP is accepted and No authorization checking is performed. | [optional] 
**allow_localhost** | **bool** | Whether to allow \&quot;localhost\&quot; and \&quot;localdomain\&quot; as a valid common name in a request, independent of allowed_domains value. | [optional] 
**allow_subdomains** | **bool** | If set, clients can request certificates for subdomains of domains listed in allowed_domains, including wildcard subdomains. See the documentation for more information. | [optional] 
**allow_token_displayname** | **bool** | Whether to allow \&quot;localhost\&quot; and \&quot;localdomain\&quot; as a valid common name in a request, independent of allowed_domains value. | [optional] 
**allow_wildcard_certificates** | **bool** | If set, allows certificates with wildcards in the common name to be issued, conforming to RFC 6125&#39;s Section 6.4.3; e.g., \&quot;*.example.net\&quot; or \&quot;b*z.example.net\&quot;. See the documentation for more information. | [optional] 
**allowed_domains** | **List[str]** | Specifies the domains this role is allowed to issue certificates for. This is used with the allow_bare_domains, allow_subdomains, and allow_glob_domains to determine matches for the common name, DNS-typed SAN entries, and Email-typed SAN entries of certificates. See the documentation for more information. This parameter accepts a comma-separated string or list of domains. | [optional] 
**allowed_domains_template** | **bool** | If set, Allowed domains can be specified using identity template policies. Non-templated domains are also permitted. | [optional] 
**allowed_other_sans** | **List[str]** | If set, an array of allowed other names to put in SANs. These values support globbing and must be in the format &lt;oid&gt;;&lt;type&gt;:&lt;value&gt;. Currently only \&quot;utf8\&quot; is a valid type. All values, including globbing values, must use this syntax, with the exception being a single \&quot;*\&quot; which allows any OID and any value (but type must still be utf8). | [optional] 
**allowed_serial_numbers** | **List[str]** | If set, an array of allowed serial numbers to put in Subject. These values support globbing. | [optional] 
**allowed_uri_sans** | **List[str]** | If set, an array of allowed URIs for URI Subject Alternative Names. Any valid URI is accepted, these values support globbing. | [optional] 
**allowed_uri_sans_template** | **bool** | If set, Allowed URI SANs can be specified using identity template policies. Non-templated URI SANs are also permitted. | [optional] 
**allowed_user_ids** | **List[str]** | If set, an array of allowed user-ids to put in user system login name specified here: https://www.rfc-editor.org/rfc/rfc1274#section-9.3.1 | [optional] 
**basic_constraints_valid_for_non_ca** | **bool** | Mark Basic Constraints valid when issuing non-CA certificates. | [optional] 
**client_flag** | **bool** | If set, certificates are flagged for client auth use. Defaults to true. See also RFC 5280 Section 4.2.1.12. | [optional] 
**cn_validations** | **List[str]** | List of allowed validations to run against the Common Name field. Values can include &#39;email&#39; to validate the CN is a email address, &#39;hostname&#39; to validate the CN is a valid hostname (potentially including wildcards). When multiple validations are specified, these take OR semantics (either email OR hostname are allowed). The special value &#39;disabled&#39; allows disabling all CN name validations, allowing for arbitrary non-Hostname, non-Email address CNs. | [optional] 
**code_signing_flag** | **bool** | If set, certificates are flagged for code signing use. Defaults to false. See also RFC 5280 Section 4.2.1.12. | [optional] 
**country** | **List[str]** | If set, Country will be set to this value in certificates issued by this role. | [optional] 
**email_protection_flag** | **bool** | If set, certificates are flagged for email protection use. Defaults to false. See also RFC 5280 Section 4.2.1.12. | [optional] 
**enforce_hostnames** | **bool** | If set, only valid host names are allowed for CN and DNS SANs, and the host part of email addresses. Defaults to true. | [optional] 
**ext_key_usage** | **List[str]** | A comma-separated string or list of extended key usages. Valid values can be found at https://golang.org/pkg/crypto/x509/#ExtKeyUsage -- simply drop the \&quot;ExtKeyUsage\&quot; part of the name. To remove all key usages from being set, set this value to an empty list. See also RFC 5280 Section 4.2.1.12. | [optional] 
**ext_key_usage_oids** | **List[str]** | A comma-separated string or list of extended key usage oids. | [optional] 
**generate_lease** | **bool** | If set, certificates issued/signed against this role will have Vault leases attached to them. Defaults to \&quot;false\&quot;. Certificates can be added to the CRL by \&quot;vault revoke &lt;lease_id&gt;\&quot; when certificates are associated with leases. It can also be done using the \&quot;pki/revoke\&quot; endpoint. However, when lease generation is disabled, invoking \&quot;pki/revoke\&quot; would be the only way to add the certificates to the CRL. When large number of certificates are generated with long lifetimes, it is recommended that lease generation be disabled, as large amount of leases adversely affect the startup time of Vault. | [optional] 
**issuer_ref** | **str** | Reference to the issuer used to sign requests serviced by this role. | [optional] 
**key_bits** | **int** | The number of bits to use. Allowed values are 0 (universal default); with rsa key_type: 2048 (default), 3072, or 4096; with ec key_type: 224, 256 (default), 384, or 521; ignored with ed25519. | [optional] 
**key_type** | **str** | The type of key to use; defaults to RSA. \&quot;rsa\&quot; \&quot;ec\&quot;, \&quot;ed25519\&quot; and \&quot;any\&quot; are the only valid values. | [optional] 
**key_usage** | **List[str]** | A comma-separated string or list of key usages (not extended key usages). Valid values can be found at https://golang.org/pkg/crypto/x509/#KeyUsage -- simply drop the \&quot;KeyUsage\&quot; part of the name. To remove all key usages from being set, set this value to an empty list. See also RFC 5280 Section 4.2.1.3. | [optional] 
**locality** | **List[str]** | If set, Locality will be set to this value in certificates issued by this role. | [optional] 
**max_ttl** | **int** | The maximum allowed lease duration. If not set, defaults to the system maximum lease TTL. | [optional] 
**no_store** | **bool** | If set, certificates issued/signed against this role will not be stored in the storage backend. This can improve performance when issuing large numbers of certificates. However, certificates issued in this way cannot be enumerated or revoked, so this option is recommended only for certificates that are non-sensitive, or extremely short-lived. This option implies a value of \&quot;false\&quot; for \&quot;generate_lease\&quot;. | [optional] 
**not_after** | **str** | Set the not after field of the certificate with specified date value. The value format should be given in UTC format YYYY-MM-ddTHH:MM:SSZ. | [optional] 
**not_before_duration** | **int** | The duration in seconds before now which the certificate needs to be backdated by. | [optional] 
**organization** | **List[str]** | If set, O (Organization) will be set to this value in certificates issued by this role. | [optional] 
**ou** | **List[str]** | If set, OU (OrganizationalUnit) will be set to this value in certificates issued by this role. | [optional] 
**policy_identifiers** | **List[str]** | A comma-separated string or list of policy OIDs, or a JSON list of qualified policy information, which must include an oid, and may include a notice and/or cps url, using the form [{\&quot;oid\&quot;&#x3D;\&quot;1.3.6.1.4.1.7.8\&quot;,\&quot;notice\&quot;&#x3D;\&quot;I am a user Notice\&quot;}, {\&quot;oid\&quot;&#x3D;\&quot;1.3.6.1.4.1.44947.1.2.4 \&quot;,\&quot;cps\&quot;&#x3D;\&quot;https://example.com\&quot;}]. | [optional] 
**postal_code** | **List[str]** | If set, Postal Code will be set to this value in certificates issued by this role. | [optional] 
**province** | **List[str]** | If set, Province will be set to this value in certificates issued by this role. | [optional] 
**require_cn** | **bool** | If set to false, makes the &#39;common_name&#39; field optional while generating a certificate. | [optional] 
**server_flag** | **bool** | If set, certificates are flagged for server auth use. Defaults to true. See also RFC 5280 Section 4.2.1.12. | [optional] [default to True]
**signature_bits** | **int** | The number of bits to use in the signature algorithm; accepts 256 for SHA-2-256, 384 for SHA-2-384, and 512 for SHA-2-512. Defaults to 0 to automatically detect based on key length (SHA-2-256 for RSA keys, and matching the curve size for NIST P-Curves). | [optional] 
**street_address** | **List[str]** | If set, Street Address will be set to this value in certificates issued by this role. | [optional] 
**ttl** | **int** | The lease duration (validity period of the certificate) if no specific lease duration is requested. The lease duration controls the expiration of certificates issued by this backend. Defaults to the system default value or the value of max_ttl, whichever is shorter. | [optional] 
**use_csr_common_name** | **bool** | If set, when used with a signing profile, the common name in the CSR will be used. This does *not* include any requested Subject Alternative Names; use use_csr_sans for that. Defaults to true. | [optional] 
**use_csr_sans** | **bool** | If set, when used with a signing profile, the SANs in the CSR will be used. This does *not* include the Common Name (cn); use use_csr_common_name for that. Defaults to true. | [optional] 
**use_pss** | **bool** | Whether or not to use PSS signatures when using a RSA key-type issuer. Defaults to false. | [optional] 

## Example

```python
from ahvac.models.pki_read_role_response import PkiReadRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadRoleResponse from a JSON string
pki_read_role_response_instance = PkiReadRoleResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadRoleResponse.to_json())

# convert the object into a dict
pki_read_role_response_dict = pki_read_role_response_instance.to_dict()
# create an instance of PkiReadRoleResponse from a dict
pki_read_role_response_from_dict = PkiReadRoleResponse.from_dict(pki_read_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


