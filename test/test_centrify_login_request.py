# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.centrify_login_request import CentrifyLoginRequest

class TestCentrifyLoginRequest(unittest.TestCase):
    """CentrifyLoginRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CentrifyLoginRequest:
        """Test CentrifyLoginRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CentrifyLoginRequest`
        """
        model = CentrifyLoginRequest()
        if include_optional:
            return CentrifyLoginRequest(
                mode = 'ro',
                password = '',
                username = ''
            )
        else:
            return CentrifyLoginRequest(
        )
        """

    def testCentrifyLoginRequest(self):
        """Test CentrifyLoginRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
