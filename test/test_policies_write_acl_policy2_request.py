# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.policies_write_acl_policy2_request import PoliciesWriteAclPolicy2Request

class TestPoliciesWriteAclPolicy2Request(unittest.TestCase):
    """PoliciesWriteAclPolicy2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoliciesWriteAclPolicy2Request:
        """Test PoliciesWriteAclPolicy2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoliciesWriteAclPolicy2Request`
        """
        model = PoliciesWriteAclPolicy2Request()
        if include_optional:
            return PoliciesWriteAclPolicy2Request(
                policy = '',
                rules = ''
            )
        else:
            return PoliciesWriteAclPolicy2Request(
        )
        """

    def testPoliciesWriteAclPolicy2Request(self):
        """Test PoliciesWriteAclPolicy2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()