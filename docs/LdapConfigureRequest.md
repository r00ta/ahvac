# LdapConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_group_search** | **bool** | Use anonymous binds when performing LDAP group searches (if true the initial credentials will still be used for the initial connection test). | [optional] [default to False]
**binddn** | **str** | LDAP DN for searching for the user DN (optional) | [optional] 
**bindpass** | **str** | LDAP password for searching for the user DN (optional) | [optional] 
**case_sensitive_names** | **bool** | If true, case sensitivity will be used when comparing usernames and groups for matching policies. | [optional] 
**certificate** | **str** | CA certificate to use when verifying LDAP server certificate, must be x509 PEM encoded (optional) | [optional] 
**client_tls_cert** | **str** | Client certificate to provide to the LDAP server, must be x509 PEM encoded (optional) | [optional] 
**client_tls_key** | **str** | Client certificate key to provide to the LDAP server, must be x509 PEM encoded (optional) | [optional] 
**connection_timeout** | **str** | Timeout, in seconds, when attempting to connect to the LDAP server before trying the next URL in the configuration. | [optional] [default to '30s']
**deny_null_bind** | **bool** | Denies an unauthenticated LDAP bind request if the user&#39;s password is empty; defaults to true | [optional] [default to True]
**dereference_aliases** | **str** | When aliases should be dereferenced on search operations. Accepted values are &#39;never&#39;, &#39;finding&#39;, &#39;searching&#39;, &#39;always&#39;. Defaults to &#39;never&#39;. | [optional] [default to 'never']
**discoverdn** | **bool** | Use anonymous bind to discover the bind DN of a user (optional) | [optional] 
**groupattr** | **str** | LDAP attribute to follow on objects returned by &lt;groupfilter&gt; in order to enumerate user group membership. Examples: \&quot;cn\&quot; or \&quot;memberOf\&quot;, etc. Default: cn | [optional] [default to 'cn']
**groupdn** | **str** | LDAP search base to use for group membership search (eg: ou&#x3D;Groups,dc&#x3D;example,dc&#x3D;org) | [optional] 
**groupfilter** | **str** | Go template for querying group membership of user (optional) The template can access the following context variables: UserDN, Username Example: (&amp;(objectClass&#x3D;group)(member:1.2.840.113556.1.4.1941:&#x3D;{{.UserDN}})) Default: (|(memberUid&#x3D;{{.Username}})(member&#x3D;{{.UserDN}})(uniqueMember&#x3D;{{.UserDN}})) | [optional] [default to '(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))']
**insecure_tls** | **bool** | Skip LDAP server SSL Certificate verification - VERY insecure (optional) | [optional] 
**length** | **int** | The desired length of passwords that Vault generates. | [optional] 
**max_page_size** | **int** | If set to a value greater than 0, the LDAP backend will use the LDAP server&#39;s paged search control to request pages of up to the given size. This can be used to avoid hitting the LDAP server&#39;s maximum result size limit. Otherwise, the LDAP backend will not use the paged search control. | [optional] [default to 0]
**max_ttl** | **str** | The maximum password time-to-live. | [optional] 
**password_policy** | **str** | Password policy to use to generate passwords | [optional] 
**request_timeout** | **str** | Timeout, in seconds, for the connection when making requests against the server before returning back an error. | [optional] [default to '90s']
**var_schema** | **str** | The desired LDAP schema used when modifying user account passwords. | [optional] [default to 'openldap']
**starttls** | **bool** | Issue a StartTLS command after establishing unencrypted connection (optional) | [optional] 
**tls_max_version** | **str** | Maximum TLS version to use. Accepted values are &#39;tls10&#39;, &#39;tls11&#39;, &#39;tls12&#39; or &#39;tls13&#39;. Defaults to &#39;tls12&#39; | [optional] [default to 'tls12']
**tls_min_version** | **str** | Minimum TLS version to use. Accepted values are &#39;tls10&#39;, &#39;tls11&#39;, &#39;tls12&#39; or &#39;tls13&#39;. Defaults to &#39;tls12&#39; | [optional] [default to 'tls12']
**ttl** | **str** | The default password time-to-live. | [optional] 
**upndomain** | **str** | Enables userPrincipalDomain login with [username]@UPNDomain (optional) | [optional] 
**url** | **str** | LDAP URL to connect to (default: ldap://127.0.0.1). Multiple URLs can be specified by concatenating them with commas; they will be tried in-order. | [optional] [default to 'ldap://127.0.0.1']
**use_pre111_group_cn_behavior** | **bool** | In Vault 1.1.1 a fix for handling group CN values of different cases unfortunately introduced a regression that could cause previously defined groups to not be found due to a change in the resulting name. If set true, the pre-1.1.1 behavior for matching group CNs will be used. This is only needed in some upgrade scenarios for backwards compatibility. It is enabled by default if the config is upgraded but disabled by default on new configurations. | [optional] 
**use_token_groups** | **bool** | If true, use the Active Directory tokenGroups constructed attribute of the user to find the group memberships. This will find all security groups including nested ones. | [optional] [default to False]
**userattr** | **str** | Attribute used for users (default: cn) | [optional] [default to 'cn']
**userdn** | **str** | LDAP domain to use for users (eg: ou&#x3D;People,dc&#x3D;example,dc&#x3D;org) | [optional] 
**userfilter** | **str** | Go template for LDAP user search filer (optional) The template can access the following context variables: UserAttr, Username Default: ({{.UserAttr}}&#x3D;{{.Username}}) | [optional] [default to '({{.UserAttr}}={{.Username}})']
**username_as_alias** | **bool** | If true, sets the alias name to the username | [optional] [default to False]

## Example

```python
from ahvac.models.ldap_configure_request import LdapConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapConfigureRequest from a JSON string
ldap_configure_request_instance = LdapConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(LdapConfigureRequest.to_json())

# convert the object into a dict
ldap_configure_request_dict = ldap_configure_request_instance.to_dict()
# create an instance of LdapConfigureRequest from a dict
ldap_configure_request_from_dict = LdapConfigureRequest.from_dict(ldap_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


