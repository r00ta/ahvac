# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize_request import PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest

class TestPkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest(unittest.TestCase):
    """PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest:
        """Test PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest`
        """
        model = PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest()
        if include_optional:
            return PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest(
                payload = '',
                protected = '',
                signature = ''
            )
        else:
            return PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest(
        )
        """

    def testPkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest(self):
        """Test PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()