# ConsulConfigureAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Consul server address | [optional] 
**ca_cert** | **str** | CA certificate to use when verifying Consul server certificate, must be x509 PEM encoded. | [optional] 
**client_cert** | **str** | Client certificate used for Consul&#39;s TLS communication, must be x509 PEM encoded and if this is set you need to also set client_key. | [optional] 
**client_key** | **str** | Client key used for Consul&#39;s TLS communication, must be x509 PEM encoded and if this is set you need to also set client_cert. | [optional] 
**scheme** | **str** | URI scheme for the Consul address | [optional] [default to 'http']
**token** | **str** | Token for API calls | [optional] 

## Example

```python
from ahvac.models.consul_configure_access_request import ConsulConfigureAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsulConfigureAccessRequest from a JSON string
consul_configure_access_request_instance = ConsulConfigureAccessRequest.from_json(json)
# print the JSON string representation of the object
print(ConsulConfigureAccessRequest.to_json())

# convert the object into a dict
consul_configure_access_request_dict = consul_configure_access_request_instance.to_dict()
# create an instance of ConsulConfigureAccessRequest from a dict
consul_configure_access_request_from_dict = ConsulConfigureAccessRequest.from_dict(consul_configure_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


