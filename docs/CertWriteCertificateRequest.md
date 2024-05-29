# CertWriteCertificateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_common_names** | **List[str]** | A comma-separated list of names. At least one must exist in the Common Name. Supports globbing. | [optional] 
**allowed_dns_sans** | **List[str]** | A comma-separated list of DNS names. At least one must exist in the SANs. Supports globbing. | [optional] 
**allowed_email_sans** | **List[str]** | A comma-separated list of Email Addresses. At least one must exist in the SANs. Supports globbing. | [optional] 
**allowed_metadata_extensions** | **List[str]** | A comma-separated string or array of oid extensions. Upon successful authentication, these extensions will be added as metadata if they are present in the certificate. The metadata key will be the string consisting of the oid numbers separated by a dash (-) instead of a dot (.) to allow usage in ACL templates. | [optional] 
**allowed_names** | **List[str]** | A comma-separated list of names. At least one must exist in either the Common Name or SANs. Supports globbing. This parameter is deprecated, please use allowed_common_names, allowed_dns_sans, allowed_email_sans, allowed_uri_sans. | [optional] 
**allowed_organizational_units** | **List[str]** | A comma-separated list of Organizational Units names. At least one must exist in the OU field. | [optional] 
**allowed_uri_sans** | **List[str]** | A comma-separated list of URIs. At least one must exist in the SANs. Supports globbing. | [optional] 
**bound_cidrs** | **List[str]** | Use \&quot;token_bound_cidrs\&quot; instead. If this and \&quot;token_bound_cidrs\&quot; are both specified, only \&quot;token_bound_cidrs\&quot; will be used. | [optional] 
**certificate** | **str** | The public certificate that should be trusted. Must be x509 PEM encoded. | [optional] 
**display_name** | **str** | The display name to use for clients using this certificate. | [optional] 
**lease** | **int** | Use \&quot;token_ttl\&quot; instead. If this and \&quot;token_ttl\&quot; are both specified, only \&quot;token_ttl\&quot; will be used. | [optional] 
**max_ttl** | **str** | Use \&quot;token_max_ttl\&quot; instead. If this and \&quot;token_max_ttl\&quot; are both specified, only \&quot;token_max_ttl\&quot; will be used. | [optional] 
**ocsp_ca_certificates** | **str** | Any additional CA certificates needed to communicate with OCSP servers | [optional] 
**ocsp_enabled** | **bool** | Whether to attempt OCSP verification of certificates at login | [optional] 
**ocsp_fail_open** | **bool** | If set to true, if an OCSP revocation cannot be made successfully, login will proceed rather than failing. If false, failing to get an OCSP status fails the request. | [optional] [default to False]
**ocsp_query_all_servers** | **bool** | If set to true, rather than accepting the first successful OCSP response, query all servers and consider the certificate valid only if all servers agree. | [optional] [default to False]
**ocsp_servers_override** | **List[str]** | A comma-separated list of OCSP server addresses. If unset, the OCSP server is determined from the AuthorityInformationAccess extension on the certificate being inspected. | [optional] 
**period** | **str** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**required_extensions** | **List[str]** | A comma-separated string or array of extensions formatted as \&quot;oid:value\&quot;. Expects the extension value to be some type of ASN1 encoded string. All values much match. Supports globbing on \&quot;value\&quot;. | [optional] 
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **str** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']
**ttl** | **str** | Use \&quot;token_ttl\&quot; instead. If this and \&quot;token_ttl\&quot; are both specified, only \&quot;token_ttl\&quot; will be used. | [optional] 

## Example

```python
from ahvac.models.cert_write_certificate_request import CertWriteCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertWriteCertificateRequest from a JSON string
cert_write_certificate_request_instance = CertWriteCertificateRequest.from_json(json)
# print the JSON string representation of the object
print(CertWriteCertificateRequest.to_json())

# convert the object into a dict
cert_write_certificate_request_dict = cert_write_certificate_request_instance.to_dict()
# create an instance of CertWriteCertificateRequest from a dict
cert_write_certificate_request_from_dict = CertWriteCertificateRequest.from_dict(cert_write_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


