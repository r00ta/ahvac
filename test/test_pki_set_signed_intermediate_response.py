# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.pki_set_signed_intermediate_response import PkiSetSignedIntermediateResponse

class TestPkiSetSignedIntermediateResponse(unittest.TestCase):
    """PkiSetSignedIntermediateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PkiSetSignedIntermediateResponse:
        """Test PkiSetSignedIntermediateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkiSetSignedIntermediateResponse`
        """
        model = PkiSetSignedIntermediateResponse()
        if include_optional:
            return PkiSetSignedIntermediateResponse(
                existing_issuers = [
                    ''
                    ],
                existing_keys = [
                    ''
                    ],
                imported_issuers = [
                    ''
                    ],
                imported_keys = [
                    ''
                    ],
                mapping = None
            )
        else:
            return PkiSetSignedIntermediateResponse(
        )
        """

    def testPkiSetSignedIntermediateResponse(self):
        """Test PkiSetSignedIntermediateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
