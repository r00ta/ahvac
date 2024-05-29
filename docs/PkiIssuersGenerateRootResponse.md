# PkiIssuersGenerateRootResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The generated self-signed CA certificate. | [optional] 
**expiration** | **int** | The expiration of the given issuer. | [optional] 
**issuer_id** | **str** | The ID of the issuer | [optional] 
**issuer_name** | **str** | The name of the issuer. | [optional] 
**issuing_ca** | **str** | The issuing certificate authority. | [optional] 
**key_id** | **str** | The ID of the key. | [optional] 
**key_name** | **str** | The key name if given. | [optional] 
**private_key** | **str** | The private key if exported was specified. | [optional] 
**serial_number** | **str** | The requested Subject&#39;s named serial number. | [optional] 

## Example

```python
from ahvac.models.pki_issuers_generate_root_response import PkiIssuersGenerateRootResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuersGenerateRootResponse from a JSON string
pki_issuers_generate_root_response_instance = PkiIssuersGenerateRootResponse.from_json(json)
# print the JSON string representation of the object
print(PkiIssuersGenerateRootResponse.to_json())

# convert the object into a dict
pki_issuers_generate_root_response_dict = pki_issuers_generate_root_response_instance.to_dict()
# create an instance of PkiIssuersGenerateRootResponse from a dict
pki_issuers_generate_root_response_from_dict = PkiIssuersGenerateRootResponse.from_dict(pki_issuers_generate_root_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


