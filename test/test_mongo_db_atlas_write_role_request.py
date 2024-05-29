# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.mongo_db_atlas_write_role_request import MongoDbAtlasWriteRoleRequest

class TestMongoDbAtlasWriteRoleRequest(unittest.TestCase):
    """MongoDbAtlasWriteRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MongoDbAtlasWriteRoleRequest:
        """Test MongoDbAtlasWriteRoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MongoDbAtlasWriteRoleRequest`
        """
        model = MongoDbAtlasWriteRoleRequest()
        if include_optional:
            return MongoDbAtlasWriteRoleRequest(
                cidr_blocks = [
                    ''
                    ],
                ip_addresses = [
                    ''
                    ],
                max_ttl = '',
                organization_id = '',
                project_id = '',
                project_roles = [
                    ''
                    ],
                roles = [
                    ''
                    ],
                ttl = ''
            )
        else:
            return MongoDbAtlasWriteRoleRequest(
                roles = [
                    ''
                    ],
        )
        """

    def testMongoDbAtlasWriteRoleRequest(self):
        """Test MongoDbAtlasWriteRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
