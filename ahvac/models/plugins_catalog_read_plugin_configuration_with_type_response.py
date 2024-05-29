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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PluginsCatalogReadPluginConfigurationWithTypeResponse(BaseModel):
    """
    PluginsCatalogReadPluginConfigurationWithTypeResponse
    """ # noqa: E501
    args: Optional[List[StrictStr]] = Field(default=None, description="The args passed to plugin command.")
    builtin: Optional[StrictBool] = None
    command: Optional[StrictStr] = Field(default=None, description="The command used to start the plugin. The executable defined in this command must exist in vault's plugin directory.")
    deprecation_status: Optional[StrictStr] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the plugin")
    oci_image: Optional[StrictStr] = Field(default=None, description="The name of the OCI image to be run, without the tag or SHA256. Must already be present on the machine.")
    sha256: Optional[StrictStr] = Field(default=None, description="The SHA256 sum of the executable or container to be run. This should be HEX encoded.")
    version: Optional[StrictStr] = Field(default=None, description="The semantic version of the plugin to use, or image tag if oci_image is provided.")
    __properties: ClassVar[List[str]] = ["args", "builtin", "command", "deprecation_status", "name", "oci_image", "sha256", "version"]

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
        """Create an instance of PluginsCatalogReadPluginConfigurationWithTypeResponse from a JSON string"""
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
        """Create an instance of PluginsCatalogReadPluginConfigurationWithTypeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "args": obj.get("args"),
            "builtin": obj.get("builtin"),
            "command": obj.get("command"),
            "deprecation_status": obj.get("deprecation_status"),
            "name": obj.get("name"),
            "oci_image": obj.get("oci_image"),
            "sha256": obj.get("sha256"),
            "version": obj.get("version")
        })
        return _obj

