# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.consul_write_role_request import ConsulWriteRoleRequest

class TestConsulWriteRoleRequest(unittest.TestCase):
    """ConsulWriteRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsulWriteRoleRequest:
        """Test ConsulWriteRoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConsulWriteRoleRequest`
        """
        model = ConsulWriteRoleRequest()
        if include_optional:
            return ConsulWriteRoleRequest(
                consul_namespace = '',
                consul_policies = [
                    ''
                    ],
                consul_roles = [
                    ''
                    ],
                lease = '',
                local = True,
                max_ttl = '',
                node_identities = [
                    ''
                    ],
                partition = '',
                policies = [
                    ''
                    ],
                policy = '',
                service_identities = [
                    ''
                    ],
                token_type = 'client',
                ttl = ''
            )
        else:
            return ConsulWriteRoleRequest(
        )
        """

    def testConsulWriteRoleRequest(self):
        """Test ConsulWriteRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
