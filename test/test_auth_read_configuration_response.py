# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.auth_read_configuration_response import AuthReadConfigurationResponse

class TestAuthReadConfigurationResponse(unittest.TestCase):
    """AuthReadConfigurationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthReadConfigurationResponse:
        """Test AuthReadConfigurationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthReadConfigurationResponse`
        """
        model = AuthReadConfigurationResponse()
        if include_optional:
            return AuthReadConfigurationResponse(
                accessor = '',
                config = None,
                deprecation_status = '',
                description = '',
                external_entropy_access = True,
                local = True,
                options = None,
                plugin_version = '',
                running_plugin_version = '',
                running_sha256 = '',
                seal_wrap = True,
                type = '',
                uuid = ''
            )
        else:
            return AuthReadConfigurationResponse(
        )
        """

    def testAuthReadConfigurationResponse(self):
        """Test AuthReadConfigurationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
