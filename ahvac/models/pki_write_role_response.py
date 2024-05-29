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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PkiWriteRoleResponse(BaseModel):
    """
    PkiWriteRoleResponse
    """ # noqa: E501
    allow_any_name: Optional[StrictBool] = Field(default=None, description="If set, clients can request certificates for any domain, regardless of allowed_domains restrictions. See the documentation for more information.")
    allow_bare_domains: Optional[StrictBool] = Field(default=None, description="If set, clients can request certificates for the base domains themselves, e.g. \"example.com\" of domains listed in allowed_domains. This is a separate option as in some cases this can be considered a security threat. See the documentation for more information.")
    allow_glob_domains: Optional[StrictBool] = Field(default=None, description="If set, domains specified in allowed_domains can include shell-style glob patterns, e.g. \"ftp*.example.com\". See the documentation for more information.")
    allow_ip_sans: Optional[StrictBool] = Field(default=None, description="If set, IP Subject Alternative Names are allowed. Any valid IP is accepted and No authorization checking is performed.")
    allow_localhost: Optional[StrictBool] = Field(default=None, description="Whether to allow \"localhost\" and \"localdomain\" as a valid common name in a request, independent of allowed_domains value.")
    allow_subdomains: Optional[StrictBool] = Field(default=None, description="If set, clients can request certificates for subdomains of domains listed in allowed_domains, including wildcard subdomains. See the documentation for more information.")
    allow_token_displayname: Optional[StrictBool] = Field(default=None, description="Whether to allow \"localhost\" and \"localdomain\" as a valid common name in a request, independent of allowed_domains value.")
    allow_wildcard_certificates: Optional[StrictBool] = Field(default=None, description="If set, allows certificates with wildcards in the common name to be issued, conforming to RFC 6125's Section 6.4.3; e.g., \"*.example.net\" or \"b*z.example.net\". See the documentation for more information.")
    allowed_domains: Optional[List[StrictStr]] = Field(default=None, description="Specifies the domains this role is allowed to issue certificates for. This is used with the allow_bare_domains, allow_subdomains, and allow_glob_domains to determine matches for the common name, DNS-typed SAN entries, and Email-typed SAN entries of certificates. See the documentation for more information. This parameter accepts a comma-separated string or list of domains.")
    allowed_domains_template: Optional[StrictBool] = Field(default=None, description="If set, Allowed domains can be specified using identity template policies. Non-templated domains are also permitted.")
    allowed_other_sans: Optional[List[StrictStr]] = Field(default=None, description="If set, an array of allowed other names to put in SANs. These values support globbing and must be in the format <oid>;<type>:<value>. Currently only \"utf8\" is a valid type. All values, including globbing values, must use this syntax, with the exception being a single \"*\" which allows any OID and any value (but type must still be utf8).")
    allowed_serial_numbers: Optional[List[StrictStr]] = Field(default=None, description="If set, an array of allowed serial numbers to put in Subject. These values support globbing.")
    allowed_uri_sans: Optional[List[StrictStr]] = Field(default=None, description="If set, an array of allowed URIs for URI Subject Alternative Names. Any valid URI is accepted, these values support globbing.")
    allowed_uri_sans_template: Optional[StrictBool] = Field(default=None, description="If set, Allowed URI SANs can be specified using identity template policies. Non-templated URI SANs are also permitted.")
    allowed_user_ids: Optional[List[StrictStr]] = Field(default=None, description="If set, an array of allowed user-ids to put in user system login name specified here: https://www.rfc-editor.org/rfc/rfc1274#section-9.3.1")
    basic_constraints_valid_for_non_ca: Optional[StrictBool] = Field(default=None, description="Mark Basic Constraints valid when issuing non-CA certificates.")
    client_flag: Optional[StrictBool] = Field(default=None, description="If set, certificates are flagged for client auth use. Defaults to true. See also RFC 5280 Section 4.2.1.12.")
    cn_validations: Optional[List[StrictStr]] = Field(default=None, description="List of allowed validations to run against the Common Name field. Values can include 'email' to validate the CN is a email address, 'hostname' to validate the CN is a valid hostname (potentially including wildcards). When multiple validations are specified, these take OR semantics (either email OR hostname are allowed). The special value 'disabled' allows disabling all CN name validations, allowing for arbitrary non-Hostname, non-Email address CNs.")
    code_signing_flag: Optional[StrictBool] = Field(default=None, description="If set, certificates are flagged for code signing use. Defaults to false. See also RFC 5280 Section 4.2.1.12.")
    country: Optional[List[StrictStr]] = Field(default=None, description="If set, Country will be set to this value in certificates issued by this role.")
    email_protection_flag: Optional[StrictBool] = Field(default=None, description="If set, certificates are flagged for email protection use. Defaults to false. See also RFC 5280 Section 4.2.1.12.")
    enforce_hostnames: Optional[StrictBool] = Field(default=None, description="If set, only valid host names are allowed for CN and DNS SANs, and the host part of email addresses. Defaults to true.")
    ext_key_usage: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated string or list of extended key usages. Valid values can be found at https://golang.org/pkg/crypto/x509/#ExtKeyUsage -- simply drop the \"ExtKeyUsage\" part of the name. To remove all key usages from being set, set this value to an empty list. See also RFC 5280 Section 4.2.1.12.")
    ext_key_usage_oids: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated string or list of extended key usage oids.")
    generate_lease: Optional[StrictBool] = Field(default=None, description="If set, certificates issued/signed against this role will have Vault leases attached to them. Defaults to \"false\". Certificates can be added to the CRL by \"vault revoke <lease_id>\" when certificates are associated with leases. It can also be done using the \"pki/revoke\" endpoint. However, when lease generation is disabled, invoking \"pki/revoke\" would be the only way to add the certificates to the CRL. When large number of certificates are generated with long lifetimes, it is recommended that lease generation be disabled, as large amount of leases adversely affect the startup time of Vault.")
    issuer_ref: Optional[StrictStr] = Field(default=None, description="Reference to the issuer used to sign requests serviced by this role.")
    key_bits: Optional[StrictInt] = Field(default=None, description="The number of bits to use. Allowed values are 0 (universal default); with rsa key_type: 2048 (default), 3072, or 4096; with ec key_type: 224, 256 (default), 384, or 521; ignored with ed25519.")
    key_type: Optional[StrictStr] = Field(default=None, description="The type of key to use; defaults to RSA. \"rsa\" \"ec\", \"ed25519\" and \"any\" are the only valid values.")
    key_usage: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated string or list of key usages (not extended key usages). Valid values can be found at https://golang.org/pkg/crypto/x509/#KeyUsage -- simply drop the \"KeyUsage\" part of the name. To remove all key usages from being set, set this value to an empty list. See also RFC 5280 Section 4.2.1.3.")
    locality: Optional[List[StrictStr]] = Field(default=None, description="If set, Locality will be set to this value in certificates issued by this role.")
    max_ttl: Optional[StrictInt] = Field(default=None, description="The maximum allowed lease duration. If not set, defaults to the system maximum lease TTL.")
    no_store: Optional[StrictBool] = Field(default=None, description="If set, certificates issued/signed against this role will not be stored in the storage backend. This can improve performance when issuing large numbers of certificates. However, certificates issued in this way cannot be enumerated or revoked, so this option is recommended only for certificates that are non-sensitive, or extremely short-lived. This option implies a value of \"false\" for \"generate_lease\".")
    not_after: Optional[StrictStr] = Field(default=None, description="Set the not after field of the certificate with specified date value. The value format should be given in UTC format YYYY-MM-ddTHH:MM:SSZ.")
    not_before_duration: Optional[StrictInt] = Field(default=None, description="The duration in seconds before now which the certificate needs to be backdated by.")
    organization: Optional[List[StrictStr]] = Field(default=None, description="If set, O (Organization) will be set to this value in certificates issued by this role.")
    ou: Optional[List[StrictStr]] = Field(default=None, description="If set, OU (OrganizationalUnit) will be set to this value in certificates issued by this role.")
    policy_identifiers: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated string or list of policy OIDs, or a JSON list of qualified policy information, which must include an oid, and may include a notice and/or cps url, using the form [{\"oid\"=\"1.3.6.1.4.1.7.8\",\"notice\"=\"I am a user Notice\"}, {\"oid\"=\"1.3.6.1.4.1.44947.1.2.4 \",\"cps\"=\"https://example.com\"}].")
    postal_code: Optional[List[StrictStr]] = Field(default=None, description="If set, Postal Code will be set to this value in certificates issued by this role.")
    province: Optional[List[StrictStr]] = Field(default=None, description="If set, Province will be set to this value in certificates issued by this role.")
    require_cn: Optional[StrictBool] = Field(default=None, description="If set to false, makes the 'common_name' field optional while generating a certificate.")
    server_flag: Optional[StrictBool] = Field(default=True, description="If set, certificates are flagged for server auth use. Defaults to true. See also RFC 5280 Section 4.2.1.12.")
    signature_bits: Optional[StrictInt] = Field(default=None, description="The number of bits to use in the signature algorithm; accepts 256 for SHA-2-256, 384 for SHA-2-384, and 512 for SHA-2-512. Defaults to 0 to automatically detect based on key length (SHA-2-256 for RSA keys, and matching the curve size for NIST P-Curves).")
    street_address: Optional[List[StrictStr]] = Field(default=None, description="If set, Street Address will be set to this value in certificates issued by this role.")
    ttl: Optional[StrictInt] = Field(default=None, description="The lease duration (validity period of the certificate) if no specific lease duration is requested. The lease duration controls the expiration of certificates issued by this backend. Defaults to the system default value or the value of max_ttl, whichever is shorter.")
    use_csr_common_name: Optional[StrictBool] = Field(default=None, description="If set, when used with a signing profile, the common name in the CSR will be used. This does *not* include any requested Subject Alternative Names; use use_csr_sans for that. Defaults to true.")
    use_csr_sans: Optional[StrictBool] = Field(default=None, description="If set, when used with a signing profile, the SANs in the CSR will be used. This does *not* include the Common Name (cn); use use_csr_common_name for that. Defaults to true.")
    use_pss: Optional[StrictBool] = Field(default=None, description="Whether or not to use PSS signatures when using a RSA key-type issuer. Defaults to false.")
    __properties: ClassVar[List[str]] = ["allow_any_name", "allow_bare_domains", "allow_glob_domains", "allow_ip_sans", "allow_localhost", "allow_subdomains", "allow_token_displayname", "allow_wildcard_certificates", "allowed_domains", "allowed_domains_template", "allowed_other_sans", "allowed_serial_numbers", "allowed_uri_sans", "allowed_uri_sans_template", "allowed_user_ids", "basic_constraints_valid_for_non_ca", "client_flag", "cn_validations", "code_signing_flag", "country", "email_protection_flag", "enforce_hostnames", "ext_key_usage", "ext_key_usage_oids", "generate_lease", "issuer_ref", "key_bits", "key_type", "key_usage", "locality", "max_ttl", "no_store", "not_after", "not_before_duration", "organization", "ou", "policy_identifiers", "postal_code", "province", "require_cn", "server_flag", "signature_bits", "street_address", "ttl", "use_csr_common_name", "use_csr_sans", "use_pss"]

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
        """Create an instance of PkiWriteRoleResponse from a JSON string"""
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
        """Create an instance of PkiWriteRoleResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allow_any_name": obj.get("allow_any_name"),
            "allow_bare_domains": obj.get("allow_bare_domains"),
            "allow_glob_domains": obj.get("allow_glob_domains"),
            "allow_ip_sans": obj.get("allow_ip_sans"),
            "allow_localhost": obj.get("allow_localhost"),
            "allow_subdomains": obj.get("allow_subdomains"),
            "allow_token_displayname": obj.get("allow_token_displayname"),
            "allow_wildcard_certificates": obj.get("allow_wildcard_certificates"),
            "allowed_domains": obj.get("allowed_domains"),
            "allowed_domains_template": obj.get("allowed_domains_template"),
            "allowed_other_sans": obj.get("allowed_other_sans"),
            "allowed_serial_numbers": obj.get("allowed_serial_numbers"),
            "allowed_uri_sans": obj.get("allowed_uri_sans"),
            "allowed_uri_sans_template": obj.get("allowed_uri_sans_template"),
            "allowed_user_ids": obj.get("allowed_user_ids"),
            "basic_constraints_valid_for_non_ca": obj.get("basic_constraints_valid_for_non_ca"),
            "client_flag": obj.get("client_flag"),
            "cn_validations": obj.get("cn_validations"),
            "code_signing_flag": obj.get("code_signing_flag"),
            "country": obj.get("country"),
            "email_protection_flag": obj.get("email_protection_flag"),
            "enforce_hostnames": obj.get("enforce_hostnames"),
            "ext_key_usage": obj.get("ext_key_usage"),
            "ext_key_usage_oids": obj.get("ext_key_usage_oids"),
            "generate_lease": obj.get("generate_lease"),
            "issuer_ref": obj.get("issuer_ref"),
            "key_bits": obj.get("key_bits"),
            "key_type": obj.get("key_type"),
            "key_usage": obj.get("key_usage"),
            "locality": obj.get("locality"),
            "max_ttl": obj.get("max_ttl"),
            "no_store": obj.get("no_store"),
            "not_after": obj.get("not_after"),
            "not_before_duration": obj.get("not_before_duration"),
            "organization": obj.get("organization"),
            "ou": obj.get("ou"),
            "policy_identifiers": obj.get("policy_identifiers"),
            "postal_code": obj.get("postal_code"),
            "province": obj.get("province"),
            "require_cn": obj.get("require_cn"),
            "server_flag": obj.get("server_flag") if obj.get("server_flag") is not None else True,
            "signature_bits": obj.get("signature_bits"),
            "street_address": obj.get("street_address"),
            "ttl": obj.get("ttl"),
            "use_csr_common_name": obj.get("use_csr_common_name"),
            "use_csr_sans": obj.get("use_csr_sans"),
            "use_pss": obj.get("use_pss")
        })
        return _obj


