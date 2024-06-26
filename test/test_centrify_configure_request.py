# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.centrify_configure_request import CentrifyConfigureRequest

class TestCentrifyConfigureRequest(unittest.TestCase):
    """CentrifyConfigureRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CentrifyConfigureRequest:
        """Test CentrifyConfigureRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CentrifyConfigureRequest`
        """
        model = CentrifyConfigureRequest()
        if include_optional:
            return CentrifyConfigureRequest(
                app_id = 'vault_io_integration',
                client_id = '',
                client_secret = '',
                policies = [
                    ''
                    ],
                scope = 'vault_io_integration',
                service_url = '',
                token_bound_cidrs = [
                    ''
                    ],
                token_no_default_policy = True,
                token_num_uses = 56,
                token_policies = [
                    ''
                    ],
                token_ttl = '',
                token_type = 'default-service'
            )
        else:
            return CentrifyConfigureRequest(
        )
        """

    def testCentrifyConfigureRequest(self):
        """Test CentrifyConfigureRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
