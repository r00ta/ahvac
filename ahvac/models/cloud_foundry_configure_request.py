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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CloudFoundryConfigureRequest(BaseModel):
    """
    CloudFoundryConfigureRequest
    """ # noqa: E501
    cf_api_addr: Optional[StrictStr] = Field(default=None, description="CF’s API address.")
    cf_api_mutual_tls_certificate: Optional[StrictStr] = Field(default=None, description="The PEM-format certificates that are presented for mutual TLS with the CloudFoundry API. If not set, mutual TLS is not used")
    cf_api_mutual_tls_key: Optional[StrictStr] = Field(default=None, description="The PEM-format private key that are used for mutual TLS with the CloudFoundry API. If not set, mutual TLS is not used")
    cf_api_trusted_certificates: Optional[List[StrictStr]] = Field(default=None, description="The PEM-format CA certificates that are acceptable for the CF API to present.")
    cf_client_id: Optional[StrictStr] = Field(default=None, description="The client id for CF’s API.")
    cf_client_secret: Optional[StrictStr] = Field(default=None, description="The client secret for CF’s API.")
    cf_password: Optional[StrictStr] = Field(default=None, description="The password for CF’s API.")
    cf_username: Optional[StrictStr] = Field(default=None, description="The username for CF’s API.")
    identity_ca_certificates: Optional[List[StrictStr]] = Field(default=None, description="The PEM-format CA certificates that are required to have issued the instance certificates presented for logging in.")
    login_max_seconds_not_after: Optional[StrictInt] = Field(default=60, description="Duration in seconds for the maximum acceptable length in the future a \"signing_time\" can be. Useful for clock drift. Set low to reduce the opportunity for replay attacks.")
    login_max_seconds_not_before: Optional[StrictStr] = Field(default='300', description="Duration in seconds for the maximum acceptable age of a \"signing_time\". Useful for clock drift. Set low to reduce the opportunity for replay attacks.")
    pcf_api_addr: Optional[StrictStr] = Field(default=None, description="Deprecated. Please use \"cf_api_addr\".")
    pcf_api_trusted_certificates: Optional[List[StrictStr]] = Field(default=None, description="Deprecated. Please use \"cf_api_trusted_certificates\".")
    pcf_password: Optional[StrictStr] = Field(default=None, description="Deprecated. Please use \"cf_password\".")
    pcf_username: Optional[StrictStr] = Field(default=None, description="Deprecated. Please use \"cf_username\".")
    __properties: ClassVar[List[str]] = ["cf_api_addr", "cf_api_mutual_tls_certificate", "cf_api_mutual_tls_key", "cf_api_trusted_certificates", "cf_client_id", "cf_client_secret", "cf_password", "cf_username", "identity_ca_certificates", "login_max_seconds_not_after", "login_max_seconds_not_before", "pcf_api_addr", "pcf_api_trusted_certificates", "pcf_password", "pcf_username"]

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
        """Create an instance of CloudFoundryConfigureRequest from a JSON string"""
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
        """Create an instance of CloudFoundryConfigureRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cf_api_addr": obj.get("cf_api_addr"),
            "cf_api_mutual_tls_certificate": obj.get("cf_api_mutual_tls_certificate"),
            "cf_api_mutual_tls_key": obj.get("cf_api_mutual_tls_key"),
            "cf_api_trusted_certificates": obj.get("cf_api_trusted_certificates"),
            "cf_client_id": obj.get("cf_client_id"),
            "cf_client_secret": obj.get("cf_client_secret"),
            "cf_password": obj.get("cf_password"),
            "cf_username": obj.get("cf_username"),
            "identity_ca_certificates": obj.get("identity_ca_certificates"),
            "login_max_seconds_not_after": obj.get("login_max_seconds_not_after") if obj.get("login_max_seconds_not_after") is not None else 60,
            "login_max_seconds_not_before": obj.get("login_max_seconds_not_before") if obj.get("login_max_seconds_not_before") is not None else '300',
            "pcf_api_addr": obj.get("pcf_api_addr"),
            "pcf_api_trusted_certificates": obj.get("pcf_api_trusted_certificates"),
            "pcf_password": obj.get("pcf_password"),
            "pcf_username": obj.get("pcf_username")
        })
        return _obj


