# TransitSetCertificateForKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_chain** | **str** | PEM encoded certificate chain. It should be composed by one or more concatenated PEM blocks and ordered starting from the end-entity certificate. | 
**version** | **int** | Optional version of key, &#39;latest&#39; if not set | [optional] 

## Example

```python
from ahvac.models.transit_set_certificate_for_key_request import TransitSetCertificateForKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitSetCertificateForKeyRequest from a JSON string
transit_set_certificate_for_key_request_instance = TransitSetCertificateForKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitSetCertificateForKeyRequest.to_json())

# convert the object into a dict
transit_set_certificate_for_key_request_dict = transit_set_certificate_for_key_request_instance.to_dict()
# create an instance of TransitSetCertificateForKeyRequest from a dict
transit_set_certificate_for_key_request_from_dict = TransitSetCertificateForKeyRequest.from_dict(transit_set_certificate_for_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


