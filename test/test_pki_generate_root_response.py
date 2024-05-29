# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.pki_generate_root_response import PkiGenerateRootResponse

class TestPkiGenerateRootResponse(unittest.TestCase):
    """PkiGenerateRootResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PkiGenerateRootResponse:
        """Test PkiGenerateRootResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkiGenerateRootResponse`
        """
        model = PkiGenerateRootResponse()
        if include_optional:
            return PkiGenerateRootResponse(
                certificate = '',
                expiration = 56,
                issuer_id = '',
                issuer_name = '',
                issuing_ca = '',
                key_id = '',
                key_name = '',
                private_key = '',
                serial_number = ''
            )
        else:
            return PkiGenerateRootResponse(
        )
        """

    def testPkiGenerateRootResponse(self):
        """Test PkiGenerateRootResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
