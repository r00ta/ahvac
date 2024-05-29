# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.token_write_role_request import TokenWriteRoleRequest

class TestTokenWriteRoleRequest(unittest.TestCase):
    """TokenWriteRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenWriteRoleRequest:
        """Test TokenWriteRoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenWriteRoleRequest`
        """
        model = TokenWriteRoleRequest()
        if include_optional:
            return TokenWriteRoleRequest(
                allowed_entity_aliases = [
                    ''
                    ],
                allowed_policies = [
                    ''
                    ],
                allowed_policies_glob = [
                    ''
                    ],
                bound_cidrs = [
                    ''
                    ],
                disallowed_policies = [
                    ''
                    ],
                disallowed_policies_glob = [
                    ''
                    ],
                explicit_max_ttl = '',
                orphan = True,
                path_suffix = '',
                period = '',
                renewable = True,
                token_bound_cidrs = [
                    ''
                    ],
                token_explicit_max_ttl = '',
                token_no_default_policy = True,
                token_num_uses = 56,
                token_period = '',
                token_type = 'default-service'
            )
        else:
            return TokenWriteRoleRequest(
        )
        """

    def testTokenWriteRoleRequest(self):
        """Test TokenWriteRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()