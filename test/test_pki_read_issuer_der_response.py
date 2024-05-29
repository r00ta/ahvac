# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.pki_read_issuer_der_response import PkiReadIssuerDerResponse

class TestPkiReadIssuerDerResponse(unittest.TestCase):
    """PkiReadIssuerDerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PkiReadIssuerDerResponse:
        """Test PkiReadIssuerDerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkiReadIssuerDerResponse`
        """
        model = PkiReadIssuerDerResponse()
        if include_optional:
            return PkiReadIssuerDerResponse(
                ca_chain = [
                    ''
                    ],
                certificate = '',
                issuer_id = '',
                issuer_name = ''
            )
        else:
            return PkiReadIssuerDerResponse(
        )
        """

    def testPkiReadIssuerDerResponse(self):
        """Test PkiReadIssuerDerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
