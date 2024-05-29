# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.transit_sign_with_algorithm_request import TransitSignWithAlgorithmRequest

class TestTransitSignWithAlgorithmRequest(unittest.TestCase):
    """TransitSignWithAlgorithmRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransitSignWithAlgorithmRequest:
        """Test TransitSignWithAlgorithmRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransitSignWithAlgorithmRequest`
        """
        model = TransitSignWithAlgorithmRequest()
        if include_optional:
            return TransitSignWithAlgorithmRequest(
                algorithm = 'sha2-256',
                batch_input = [
                    None
                    ],
                context = '',
                hash_algorithm = 'sha2-256',
                input = '',
                key_version = 56,
                marshaling_algorithm = 'asn1',
                prehashed = True,
                salt_length = 'auto',
                signature_algorithm = ''
            )
        else:
            return TransitSignWithAlgorithmRequest(
        )
        """

    def testTransitSignWithAlgorithmRequest(self):
        """Test TransitSignWithAlgorithmRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
