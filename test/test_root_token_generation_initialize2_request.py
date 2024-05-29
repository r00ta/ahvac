# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.root_token_generation_initialize2_request import RootTokenGenerationInitialize2Request

class TestRootTokenGenerationInitialize2Request(unittest.TestCase):
    """RootTokenGenerationInitialize2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RootTokenGenerationInitialize2Request:
        """Test RootTokenGenerationInitialize2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RootTokenGenerationInitialize2Request`
        """
        model = RootTokenGenerationInitialize2Request()
        if include_optional:
            return RootTokenGenerationInitialize2Request(
                pgp_key = ''
            )
        else:
            return RootTokenGenerationInitialize2Request(
        )
        """

    def testRootTokenGenerationInitialize2Request(self):
        """Test RootTokenGenerationInitialize2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
