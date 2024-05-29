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

class AwsConfigureClientRequest(BaseModel):
    """
    AwsConfigureClientRequest
    """ # noqa: E501
    access_key: Optional[StrictStr] = Field(default='', description="AWS Access Key ID for the account used to make AWS API requests.")
    allowed_sts_header_values: Optional[List[StrictStr]] = Field(default=None, description="List of additional headers that are allowed to be in AWS STS request headers")
    endpoint: Optional[StrictStr] = Field(default='', description="URL to override the default generated endpoint for making AWS EC2 API calls.")
    iam_endpoint: Optional[StrictStr] = Field(default='', description="URL to override the default generated endpoint for making AWS IAM API calls.")
    iam_server_id_header_value: Optional[StrictStr] = Field(default='', description="Value to require in the X-Vault-AWS-IAM-Server-ID request header")
    max_retries: Optional[StrictInt] = Field(default=-1, description="Maximum number of retries for recoverable exceptions of AWS APIs")
    secret_key: Optional[StrictStr] = Field(default='', description="AWS Secret Access Key for the account used to make AWS API requests.")
    sts_endpoint: Optional[StrictStr] = Field(default='', description="URL to override the default generated endpoint for making AWS STS API calls.")
    sts_region: Optional[StrictStr] = Field(default='', description="The region ID for the sts_endpoint, if set.")
    use_sts_region_from_client: Optional[StrictBool] = Field(default=False, description="Uses the STS region from client requests for making AWS STS API calls.")
    __properties: ClassVar[List[str]] = ["access_key", "allowed_sts_header_values", "endpoint", "iam_endpoint", "iam_server_id_header_value", "max_retries", "secret_key", "sts_endpoint", "sts_region", "use_sts_region_from_client"]

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
        """Create an instance of AwsConfigureClientRequest from a JSON string"""
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
        """Create an instance of AwsConfigureClientRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_key": obj.get("access_key") if obj.get("access_key") is not None else '',
            "allowed_sts_header_values": obj.get("allowed_sts_header_values"),
            "endpoint": obj.get("endpoint") if obj.get("endpoint") is not None else '',
            "iam_endpoint": obj.get("iam_endpoint") if obj.get("iam_endpoint") is not None else '',
            "iam_server_id_header_value": obj.get("iam_server_id_header_value") if obj.get("iam_server_id_header_value") is not None else '',
            "max_retries": obj.get("max_retries") if obj.get("max_retries") is not None else -1,
            "secret_key": obj.get("secret_key") if obj.get("secret_key") is not None else '',
            "sts_endpoint": obj.get("sts_endpoint") if obj.get("sts_endpoint") is not None else '',
            "sts_region": obj.get("sts_region") if obj.get("sts_region") is not None else '',
            "use_sts_region_from_client": obj.get("use_sts_region_from_client") if obj.get("use_sts_region_from_client") is not None else False
        })
        return _obj

