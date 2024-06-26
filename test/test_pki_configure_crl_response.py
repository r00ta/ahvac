# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.pki_configure_crl_response import PkiConfigureCrlResponse

class TestPkiConfigureCrlResponse(unittest.TestCase):
    """PkiConfigureCrlResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PkiConfigureCrlResponse:
        """Test PkiConfigureCrlResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkiConfigureCrlResponse`
        """
        model = PkiConfigureCrlResponse()
        if include_optional:
            return PkiConfigureCrlResponse(
                auto_rebuild = True,
                auto_rebuild_grace_period = '12h',
                cross_cluster_revocation = True,
                delta_rebuild_interval = '15m',
                disable = True,
                enable_delta = True,
                expiry = '72h',
                ocsp_disable = True,
                ocsp_expiry = '1h',
                unified_crl = True,
                unified_crl_on_existing_paths = True
            )
        else:
            return PkiConfigureCrlResponse(
        )
        """

    def testPkiConfigureCrlResponse(self):
        """Test PkiConfigureCrlResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
