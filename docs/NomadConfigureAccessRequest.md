# NomadConfigureAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Nomad server address | [optional] 
**ca_cert** | **str** | CA certificate to use when verifying Nomad server certificate, must be x509 PEM encoded. | [optional] 
**client_cert** | **str** | Client certificate used for Nomad&#39;s TLS communication, must be x509 PEM encoded and if this is set you need to also set client_key. | [optional] 
**client_key** | **str** | Client key used for Nomad&#39;s TLS communication, must be x509 PEM encoded and if this is set you need to also set client_cert. | [optional] 
**max_token_name_length** | **int** | Max length for name of generated Nomad tokens | [optional] 
**token** | **str** | Token for API calls | [optional] 

## Example

```python
from ahvac.models.nomad_configure_access_request import NomadConfigureAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomadConfigureAccessRequest from a JSON string
nomad_configure_access_request_instance = NomadConfigureAccessRequest.from_json(json)
# print the JSON string representation of the object
print(NomadConfigureAccessRequest.to_json())

# convert the object into a dict
nomad_configure_access_request_dict = nomad_configure_access_request_instance.to_dict()
# create an instance of NomadConfigureAccessRequest from a dict
nomad_configure_access_request_from_dict = NomadConfigureAccessRequest.from_dict(nomad_configure_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


