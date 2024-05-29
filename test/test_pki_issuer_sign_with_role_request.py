# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.pki_issuer_sign_with_role_request import PkiIssuerSignWithRoleRequest

class TestPkiIssuerSignWithRoleRequest(unittest.TestCase):
    """PkiIssuerSignWithRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PkiIssuerSignWithRoleRequest:
        """Test PkiIssuerSignWithRoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkiIssuerSignWithRoleRequest`
        """
        model = PkiIssuerSignWithRoleRequest()
        if include_optional:
            return PkiIssuerSignWithRoleRequest(
                alt_names = '',
                common_name = '',
                csr = '',
                exclude_cn_from_sans = True,
                format = 'pem',
                ip_sans = [
                    ''
                    ],
                not_after = '',
                other_sans = [
                    ''
                    ],
                private_key_format = 'der',
                remove_roots_from_chain = True,
                serial_number = '',
                ttl = '',
                uri_sans = [
                    ''
                    ],
                user_ids = [
                    ''
                    ]
            )
        else:
            return PkiIssuerSignWithRoleRequest(
        )
        """

    def testPkiIssuerSignWithRoleRequest(self):
        """Test PkiIssuerSignWithRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
