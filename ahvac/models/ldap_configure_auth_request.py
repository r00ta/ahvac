# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LdapConfigureAuthRequest(BaseModel):
    """
    LdapConfigureAuthRequest
    """ # noqa: E501
    anonymous_group_search: Optional[StrictBool] = Field(default=False, description="Use anonymous binds when performing LDAP group searches (if true the initial credentials will still be used for the initial connection test).")
    binddn: Optional[StrictStr] = Field(default=None, description="LDAP DN for searching for the user DN (optional)")
    bindpass: Optional[StrictStr] = Field(default=None, description="LDAP password for searching for the user DN (optional)")
    case_sensitive_names: Optional[StrictBool] = Field(default=None, description="If true, case sensitivity will be used when comparing usernames and groups for matching policies.")
    certificate: Optional[StrictStr] = Field(default=None, description="CA certificate to use when verifying LDAP server certificate, must be x509 PEM encoded (optional)")
    client_tls_cert: Optional[StrictStr] = Field(default=None, description="Client certificate to provide to the LDAP server, must be x509 PEM encoded (optional)")
    client_tls_key: Optional[StrictStr] = Field(default=None, description="Client certificate key to provide to the LDAP server, must be x509 PEM encoded (optional)")
    connection_timeout: Optional[StrictStr] = Field(default='30s', description="Timeout, in seconds, when attempting to connect to the LDAP server before trying the next URL in the configuration.")
    deny_null_bind: Optional[StrictBool] = Field(default=True, description="Denies an unauthenticated LDAP bind request if the user's password is empty; defaults to true")
    dereference_aliases: Optional[StrictStr] = Field(default='never', description="When aliases should be dereferenced on search operations. Accepted values are 'never', 'finding', 'searching', 'always'. Defaults to 'never'.")
    discoverdn: Optional[StrictBool] = Field(default=None, description="Use anonymous bind to discover the bind DN of a user (optional)")
    groupattr: Optional[StrictStr] = Field(default='cn', description="LDAP attribute to follow on objects returned by <groupfilter> in order to enumerate user group membership. Examples: \"cn\" or \"memberOf\", etc. Default: cn")
    groupdn: Optional[StrictStr] = Field(default=None, description="LDAP search base to use for group membership search (eg: ou=Groups,dc=example,dc=org)")
    groupfilter: Optional[StrictStr] = Field(default='(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))', description="Go template for querying group membership of user (optional) The template can access the following context variables: UserDN, Username Example: (&(objectClass=group)(member:1.2.840.113556.1.4.1941:={{.UserDN}})) Default: (|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))")
    insecure_tls: Optional[StrictBool] = Field(default=None, description="Skip LDAP server SSL Certificate verification - VERY insecure (optional)")
    max_page_size: Optional[StrictInt] = Field(default=0, description="If set to a value greater than 0, the LDAP backend will use the LDAP server's paged search control to request pages of up to the given size. This can be used to avoid hitting the LDAP server's maximum result size limit. Otherwise, the LDAP backend will not use the paged search control.")
    request_timeout: Optional[StrictStr] = Field(default='90s', description="Timeout, in seconds, for the connection when making requests against the server before returning back an error.")
    starttls: Optional[StrictBool] = Field(default=None, description="Issue a StartTLS command after establishing unencrypted connection (optional)")
    tls_max_version: Optional[StrictStr] = Field(default='tls12', description="Maximum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'")
    tls_min_version: Optional[StrictStr] = Field(default='tls12', description="Minimum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12'")
    token_bound_cidrs: Optional[List[StrictStr]] = Field(default=None, description="Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token.")
    token_explicit_max_ttl: Optional[StrictStr] = Field(default=None, description="If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed.")
    token_max_ttl: Optional[StrictStr] = Field(default=None, description="The maximum lifetime of the generated token")
    token_no_default_policy: Optional[StrictBool] = Field(default=None, description="If true, the 'default' policy will not automatically be added to generated tokens")
    token_num_uses: Optional[StrictInt] = Field(default=None, description="The maximum number of times a token may be used, a value of zero means unlimited")
    token_period: Optional[StrictStr] = Field(default=None, description="If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \"24h\").")
    token_policies: Optional[List[StrictStr]] = Field(default=None, description="Comma-separated list of policies. This will apply to all tokens generated by this auth method, in addition to any configured for specific users/groups.")
    token_ttl: Optional[StrictStr] = Field(default=None, description="The initial ttl of the token to generate")
    token_type: Optional[StrictStr] = Field(default='default-service', description="The type of token to generate, service or batch")
    upndomain: Optional[StrictStr] = Field(default=None, description="Enables userPrincipalDomain login with [username]@UPNDomain (optional)")
    url: Optional[StrictStr] = Field(default='ldap://127.0.0.1', description="LDAP URL to connect to (default: ldap://127.0.0.1). Multiple URLs can be specified by concatenating them with commas; they will be tried in-order.")
    use_pre111_group_cn_behavior: Optional[StrictBool] = Field(default=None, description="In Vault 1.1.1 a fix for handling group CN values of different cases unfortunately introduced a regression that could cause previously defined groups to not be found due to a change in the resulting name. If set true, the pre-1.1.1 behavior for matching group CNs will be used. This is only needed in some upgrade scenarios for backwards compatibility. It is enabled by default if the config is upgraded but disabled by default on new configurations.")
    use_token_groups: Optional[StrictBool] = Field(default=False, description="If true, use the Active Directory tokenGroups constructed attribute of the user to find the group memberships. This will find all security groups including nested ones.")
    userattr: Optional[StrictStr] = Field(default='cn', description="Attribute used for users (default: cn)")
    userdn: Optional[StrictStr] = Field(default=None, description="LDAP domain to use for users (eg: ou=People,dc=example,dc=org)")
    userfilter: Optional[StrictStr] = Field(default='({{.UserAttr}}={{.Username}})', description="Go template for LDAP user search filer (optional) The template can access the following context variables: UserAttr, Username Default: ({{.UserAttr}}={{.Username}})")
    username_as_alias: Optional[StrictBool] = Field(default=False, description="If true, sets the alias name to the username")
    __properties: ClassVar[List[str]] = ["anonymous_group_search", "binddn", "bindpass", "case_sensitive_names", "certificate", "client_tls_cert", "client_tls_key", "connection_timeout", "deny_null_bind", "dereference_aliases", "discoverdn", "groupattr", "groupdn", "groupfilter", "insecure_tls", "max_page_size", "request_timeout", "starttls", "tls_max_version", "tls_min_version", "token_bound_cidrs", "token_explicit_max_ttl", "token_max_ttl", "token_no_default_policy", "token_num_uses", "token_period", "token_policies", "token_ttl", "token_type", "upndomain", "url", "use_pre111_group_cn_behavior", "use_token_groups", "userattr", "userdn", "userfilter", "username_as_alias"]

    @field_validator('dereference_aliases')
    def dereference_aliases_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['never', 'finding', 'searching', 'always']):
            raise ValueError("must be one of enum values ('never', 'finding', 'searching', 'always')")
        return value

    @field_validator('tls_max_version')
    def tls_max_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['tls10', 'tls11', 'tls12', 'tls13']):
            raise ValueError("must be one of enum values ('tls10', 'tls11', 'tls12', 'tls13')")
        return value

    @field_validator('tls_min_version')
    def tls_min_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['tls10', 'tls11', 'tls12', 'tls13']):
            raise ValueError("must be one of enum values ('tls10', 'tls11', 'tls12', 'tls13')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LdapConfigureAuthRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LdapConfigureAuthRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "anonymous_group_search": obj.get("anonymous_group_search") if obj.get("anonymous_group_search") is not None else False,
            "binddn": obj.get("binddn"),
            "bindpass": obj.get("bindpass"),
            "case_sensitive_names": obj.get("case_sensitive_names"),
            "certificate": obj.get("certificate"),
            "client_tls_cert": obj.get("client_tls_cert"),
            "client_tls_key": obj.get("client_tls_key"),
            "connection_timeout": obj.get("connection_timeout") if obj.get("connection_timeout") is not None else '30s',
            "deny_null_bind": obj.get("deny_null_bind") if obj.get("deny_null_bind") is not None else True,
            "dereference_aliases": obj.get("dereference_aliases") if obj.get("dereference_aliases") is not None else 'never',
            "discoverdn": obj.get("discoverdn"),
            "groupattr": obj.get("groupattr") if obj.get("groupattr") is not None else 'cn',
            "groupdn": obj.get("groupdn"),
            "groupfilter": obj.get("groupfilter") if obj.get("groupfilter") is not None else '(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))',
            "insecure_tls": obj.get("insecure_tls"),
            "max_page_size": obj.get("max_page_size") if obj.get("max_page_size") is not None else 0,
            "request_timeout": obj.get("request_timeout") if obj.get("request_timeout") is not None else '90s',
            "starttls": obj.get("starttls"),
            "tls_max_version": obj.get("tls_max_version") if obj.get("tls_max_version") is not None else 'tls12',
            "tls_min_version": obj.get("tls_min_version") if obj.get("tls_min_version") is not None else 'tls12',
            "token_bound_cidrs": obj.get("token_bound_cidrs"),
            "token_explicit_max_ttl": obj.get("token_explicit_max_ttl"),
            "token_max_ttl": obj.get("token_max_ttl"),
            "token_no_default_policy": obj.get("token_no_default_policy"),
            "token_num_uses": obj.get("token_num_uses"),
            "token_period": obj.get("token_period"),
            "token_policies": obj.get("token_policies"),
            "token_ttl": obj.get("token_ttl"),
            "token_type": obj.get("token_type") if obj.get("token_type") is not None else 'default-service',
            "upndomain": obj.get("upndomain"),
            "url": obj.get("url") if obj.get("url") is not None else 'ldap://127.0.0.1',
            "use_pre111_group_cn_behavior": obj.get("use_pre111_group_cn_behavior"),
            "use_token_groups": obj.get("use_token_groups") if obj.get("use_token_groups") is not None else False,
            "userattr": obj.get("userattr") if obj.get("userattr") is not None else 'cn',
            "userdn": obj.get("userdn"),
            "userfilter": obj.get("userfilter") if obj.get("userfilter") is not None else '({{.UserAttr}}={{.Username}})',
            "username_as_alias": obj.get("username_as_alias") if obj.get("username_as_alias") is not None else False
        })
        return _obj


