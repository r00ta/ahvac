# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.aws_write_sts_role_request import AwsWriteStsRoleRequest

class TestAwsWriteStsRoleRequest(unittest.TestCase):
    """AwsWriteStsRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsWriteStsRoleRequest:
        """Test AwsWriteStsRoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsWriteStsRoleRequest`
        """
        model = AwsWriteStsRoleRequest()
        if include_optional:
            return AwsWriteStsRoleRequest(
                sts_role = ''
            )
        else:
            return AwsWriteStsRoleRequest(
        )
        """

    def testAwsWriteStsRoleRequest(self):
        """Test AwsWriteStsRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
