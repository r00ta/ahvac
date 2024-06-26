# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.nomad_configure_access_request import NomadConfigureAccessRequest

class TestNomadConfigureAccessRequest(unittest.TestCase):
    """NomadConfigureAccessRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NomadConfigureAccessRequest:
        """Test NomadConfigureAccessRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NomadConfigureAccessRequest`
        """
        model = NomadConfigureAccessRequest()
        if include_optional:
            return NomadConfigureAccessRequest(
                address = '',
                ca_cert = '',
                client_cert = '',
                client_key = '',
                max_token_name_length = 56,
                token = ''
            )
        else:
            return NomadConfigureAccessRequest(
        )
        """

    def testNomadConfigureAccessRequest(self):
        """Test NomadConfigureAccessRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
