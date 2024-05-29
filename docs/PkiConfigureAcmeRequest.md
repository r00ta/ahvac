# PkiConfigureAcmeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_role_ext_key_usage** | **bool** | whether the ExtKeyUsage field from a role is used, defaults to false meaning that certificate will be signed with ServerAuth. | [optional] [default to False]
**allowed_issuers** | **List[str]** | which issuers are allowed for use with ACME; by default, this will only be the primary (default) issuer | [optional] [default to ["*"]]
**allowed_roles** | **List[str]** | which roles are allowed for use with ACME; by default via &#39;*&#39;, these will be all roles including sign-verbatim; when concrete role names are specified, any default_directory_policy role must be included to allow usage of the default acme directories under /pki/acme/directory and /pki/issuer/:issuer_id/acme/directory. | [optional] [default to ["*"]]
**default_directory_policy** | **str** | the policy to be used for non-role-qualified ACME requests; by default ACME issuance will be otherwise unrestricted, equivalent to the sign-verbatim endpoint; one may also specify a role to use as this policy, as \&quot;role:&lt;role_name&gt;\&quot;, the specified role must be allowed by allowed_roles | [optional] [default to 'sign-verbatim']
**dns_resolver** | **str** | DNS resolver to use for domain resolution on this mount. Defaults to using the default system resolver. Must be in the format &lt;host&gt;:&lt;port&gt;, with both parts mandatory. | [optional] [default to '']
**eab_policy** | **str** | Specify the policy to use for external account binding behaviour, &#39;not-required&#39;, &#39;new-account-required&#39; or &#39;always-required&#39; | [optional] [default to 'always-required']
**enabled** | **bool** | whether ACME is enabled, defaults to false meaning that clusters will by default not get ACME support | [optional] [default to False]

## Example

```python
from ahvac.models.pki_configure_acme_request import PkiConfigureAcmeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureAcmeRequest from a JSON string
pki_configure_acme_request_instance = PkiConfigureAcmeRequest.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureAcmeRequest.to_json())

# convert the object into a dict
pki_configure_acme_request_dict = pki_configure_acme_request_instance.to_dict()
# create an instance of PkiConfigureAcmeRequest from a dict
pki_configure_acme_request_from_dict = PkiConfigureAcmeRequest.from_dict(pki_configure_acme_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


