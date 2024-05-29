# CloudFoundryConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_api_addr** | **str** | CF’s API address. | [optional] 
**cf_api_mutual_tls_certificate** | **str** | The PEM-format certificates that are presented for mutual TLS with the CloudFoundry API. If not set, mutual TLS is not used | [optional] 
**cf_api_mutual_tls_key** | **str** | The PEM-format private key that are used for mutual TLS with the CloudFoundry API. If not set, mutual TLS is not used | [optional] 
**cf_api_trusted_certificates** | **List[str]** | The PEM-format CA certificates that are acceptable for the CF API to present. | [optional] 
**cf_client_id** | **str** | The client id for CF’s API. | [optional] 
**cf_client_secret** | **str** | The client secret for CF’s API. | [optional] 
**cf_password** | **str** | The password for CF’s API. | [optional] 
**cf_username** | **str** | The username for CF’s API. | [optional] 
**identity_ca_certificates** | **List[str]** | The PEM-format CA certificates that are required to have issued the instance certificates presented for logging in. | [optional] 
**login_max_seconds_not_after** | **int** | Duration in seconds for the maximum acceptable length in the future a \&quot;signing_time\&quot; can be. Useful for clock drift. Set low to reduce the opportunity for replay attacks. | [optional] [default to 60]
**login_max_seconds_not_before** | **str** | Duration in seconds for the maximum acceptable age of a \&quot;signing_time\&quot;. Useful for clock drift. Set low to reduce the opportunity for replay attacks. | [optional] [default to '300']
**pcf_api_addr** | **str** | Deprecated. Please use \&quot;cf_api_addr\&quot;. | [optional] 
**pcf_api_trusted_certificates** | **List[str]** | Deprecated. Please use \&quot;cf_api_trusted_certificates\&quot;. | [optional] 
**pcf_password** | **str** | Deprecated. Please use \&quot;cf_password\&quot;. | [optional] 
**pcf_username** | **str** | Deprecated. Please use \&quot;cf_username\&quot;. | [optional] 

## Example

```python
from ahvac.models.cloud_foundry_configure_request import CloudFoundryConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudFoundryConfigureRequest from a JSON string
cloud_foundry_configure_request_instance = CloudFoundryConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(CloudFoundryConfigureRequest.to_json())

# convert the object into a dict
cloud_foundry_configure_request_dict = cloud_foundry_configure_request_instance.to_dict()
# create an instance of CloudFoundryConfigureRequest from a dict
cloud_foundry_configure_request_from_dict = CloudFoundryConfigureRequest.from_dict(cloud_foundry_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


