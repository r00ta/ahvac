# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.github_configure_request import GithubConfigureRequest

class TestGithubConfigureRequest(unittest.TestCase):
    """GithubConfigureRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GithubConfigureRequest:
        """Test GithubConfigureRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GithubConfigureRequest`
        """
        model = GithubConfigureRequest()
        if include_optional:
            return GithubConfigureRequest(
                base_url = '',
                max_ttl = '',
                organization = '',
                organization_id = 56,
                token_bound_cidrs = [
                    ''
                    ],
                token_explicit_max_ttl = '',
                token_max_ttl = '',
                token_no_default_policy = True,
                token_num_uses = 56,
                token_period = '',
                token_policies = [
                    ''
                    ],
                token_ttl = '',
                token_type = 'default-service',
                ttl = ''
            )
        else:
            return GithubConfigureRequest(
                organization = '',
        )
        """

    def testGithubConfigureRequest(self):
        """Test GithubConfigureRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
