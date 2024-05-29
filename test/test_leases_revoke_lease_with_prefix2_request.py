# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.leases_revoke_lease_with_prefix2_request import LeasesRevokeLeaseWithPrefix2Request

class TestLeasesRevokeLeaseWithPrefix2Request(unittest.TestCase):
    """LeasesRevokeLeaseWithPrefix2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeasesRevokeLeaseWithPrefix2Request:
        """Test LeasesRevokeLeaseWithPrefix2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeasesRevokeLeaseWithPrefix2Request`
        """
        model = LeasesRevokeLeaseWithPrefix2Request()
        if include_optional:
            return LeasesRevokeLeaseWithPrefix2Request(
                sync = True
            )
        else:
            return LeasesRevokeLeaseWithPrefix2Request(
        )
        """

    def testLeasesRevokeLeaseWithPrefix2Request(self):
        """Test LeasesRevokeLeaseWithPrefix2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()