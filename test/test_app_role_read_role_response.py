# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.app_role_read_role_response import AppRoleReadRoleResponse

class TestAppRoleReadRoleResponse(unittest.TestCase):
    """AppRoleReadRoleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppRoleReadRoleResponse:
        """Test AppRoleReadRoleResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppRoleReadRoleResponse`
        """
        model = AppRoleReadRoleResponse()
        if include_optional:
            return AppRoleReadRoleResponse(
                bind_secret_id = True,
                local_secret_ids = True,
                period = '',
                policies = [
                    ''
                    ],
                secret_id_bound_cidrs = [
                    ''
                    ],
                secret_id_num_uses = 56,
                secret_id_ttl = '',
                token_bound_cidrs = [
                    ''
                    ],
                token_explicit_max_ttl = '',
                token_max_ttl = '',
                token_no_default_policy = True,
                token_num_uses = 56,
                token_period = '',
                token_policies = [
                    ''
                    ],
                token_ttl = '',
                token_type = 'default-service'
            )
        else:
            return AppRoleReadRoleResponse(
        )
        """

    def testAppRoleReadRoleResponse(self):
        """Test AppRoleReadRoleResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
