# coding: utf-8

"""
    HashiCorp Vault API

    HTTP API that gives you full access to Vault. All API routes are prefixed with `/v1/`.

    The version of the OpenAPI document: 1.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ahvac.models.collect_host_information_response import CollectHostInformationResponse

class TestCollectHostInformationResponse(unittest.TestCase):
    """CollectHostInformationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectHostInformationResponse:
        """Test CollectHostInformationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectHostInformationResponse`
        """
        model = CollectHostInformationResponse()
        if include_optional:
            return CollectHostInformationResponse(
                cpu = [
                    None
                    ],
                cpu_times = [
                    None
                    ],
                disk = [
                    None
                    ],
                host = None,
                memory = None,
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CollectHostInformationResponse(
        )
        """

    def testCollectHostInformationResponse(self):
        """Test CollectHostInformationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()