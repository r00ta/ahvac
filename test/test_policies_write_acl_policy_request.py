# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.policies_write_acl_policy_request import PoliciesWriteAclPolicyRequest

class TestPoliciesWriteAclPolicyRequest(unittest.TestCase):
    """PoliciesWriteAclPolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoliciesWriteAclPolicyRequest:
        """Test PoliciesWriteAclPolicyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoliciesWriteAclPolicyRequest`
        """
        model = PoliciesWriteAclPolicyRequest()
        if include_optional:
            return PoliciesWriteAclPolicyRequest(
                policy = ''
            )
        else:
            return PoliciesWriteAclPolicyRequest(
        )
        """

    def testPoliciesWriteAclPolicyRequest(self):
        """Test PoliciesWriteAclPolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
