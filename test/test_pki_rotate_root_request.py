# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.pki_rotate_root_request import PkiRotateRootRequest

class TestPkiRotateRootRequest(unittest.TestCase):
    """PkiRotateRootRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PkiRotateRootRequest:
        """Test PkiRotateRootRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkiRotateRootRequest`
        """
        model = PkiRotateRootRequest()
        if include_optional:
            return PkiRotateRootRequest(
                alt_names = '',
                common_name = '',
                country = [
                    ''
                    ],
                exclude_cn_from_sans = True,
                format = 'pem',
                ip_sans = [
                    ''
                    ],
                issuer_name = '',
                key_bits = 56,
                key_name = '',
                key_ref = 'default',
                key_type = 'rsa',
                locality = [
                    ''
                    ],
                managed_key_id = '',
                managed_key_name = '',
                max_path_length = 56,
                not_after = '',
                not_before_duration = '30',
                organization = [
                    ''
                    ],
                other_sans = [
                    ''
                    ],
                ou = [
                    ''
                    ],
                permitted_dns_domains = [
                    ''
                    ],
                postal_code = [
                    ''
                    ],
                private_key_format = 'der',
                province = [
                    ''
                    ],
                serial_number = '',
                signature_bits = 56,
                street_address = [
                    ''
                    ],
                ttl = '',
                uri_sans = [
                    ''
                    ],
                use_pss = True
            )
        else:
            return PkiRotateRootRequest(
        )
        """

    def testPkiRotateRootRequest(self):
        """Test PkiRotateRootRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
