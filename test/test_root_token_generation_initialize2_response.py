# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.root_token_generation_initialize2_response import RootTokenGenerationInitialize2Response

class TestRootTokenGenerationInitialize2Response(unittest.TestCase):
    """RootTokenGenerationInitialize2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RootTokenGenerationInitialize2Response:
        """Test RootTokenGenerationInitialize2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RootTokenGenerationInitialize2Response`
        """
        model = RootTokenGenerationInitialize2Response()
        if include_optional:
            return RootTokenGenerationInitialize2Response(
                complete = True,
                encoded_root_token = '',
                encoded_token = '',
                nonce = '',
                otp = '',
                otp_length = 56,
                pgp_fingerprint = '',
                progress = 56,
                required = 56,
                started = True
            )
        else:
            return RootTokenGenerationInitialize2Response(
        )
        """

    def testRootTokenGenerationInitialize2Response(self):
        """Test RootTokenGenerationInitialize2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
