# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.ssh_issue_certificate_request import SshIssueCertificateRequest

class TestSshIssueCertificateRequest(unittest.TestCase):
    """SshIssueCertificateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SshIssueCertificateRequest:
        """Test SshIssueCertificateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SshIssueCertificateRequest`
        """
        model = SshIssueCertificateRequest()
        if include_optional:
            return SshIssueCertificateRequest(
                cert_type = 'user',
                critical_options = None,
                extensions = None,
                key_bits = 56,
                key_id = '',
                key_type = 'rsa',
                ttl = '',
                valid_principals = ''
            )
        else:
            return SshIssueCertificateRequest(
        )
        """

    def testSshIssueCertificateRequest(self):
        """Test SshIssueCertificateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()