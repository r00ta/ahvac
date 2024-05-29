# PkiConfigureCaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pem_bundle** | **str** | PEM-format, concatenated unencrypted secret key and certificate. | [optional] 

## Example

```python
from ahvac.models.pki_configure_ca_request import PkiConfigureCaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureCaRequest from a JSON string
pki_configure_ca_request_instance = PkiConfigureCaRequest.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureCaRequest.to_json())

# convert the object into a dict
pki_configure_ca_request_dict = pki_configure_ca_request_instance.to_dict()
# create an instance of PkiConfigureCaRequest from a dict
pki_configure_ca_request_from_dict = PkiConfigureCaRequest.from_dict(pki_configure_ca_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


