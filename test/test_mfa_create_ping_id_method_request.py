# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.mfa_create_ping_id_method_request import MfaCreatePingIdMethodRequest

class TestMfaCreatePingIdMethodRequest(unittest.TestCase):
    """MfaCreatePingIdMethodRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MfaCreatePingIdMethodRequest:
        """Test MfaCreatePingIdMethodRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MfaCreatePingIdMethodRequest`
        """
        model = MfaCreatePingIdMethodRequest()
        if include_optional:
            return MfaCreatePingIdMethodRequest(
                method_name = '',
                settings_file_base64 = '',
                username_format = ''
            )
        else:
            return MfaCreatePingIdMethodRequest(
        )
        """

    def testMfaCreatePingIdMethodRequest(self):
        """Test MfaCreatePingIdMethodRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
