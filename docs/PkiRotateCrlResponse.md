# PkiRotateCrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether rotation was successful | [optional] 

## Example

```python
from ahvac.models.pki_rotate_crl_response import PkiRotateCrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRotateCrlResponse from a JSON string
pki_rotate_crl_response_instance = PkiRotateCrlResponse.from_json(json)
# print the JSON string representation of the object
print(PkiRotateCrlResponse.to_json())

# convert the object into a dict
pki_rotate_crl_response_dict = pki_rotate_crl_response_instance.to_dict()
# create an instance of PkiRotateCrlResponse from a dict
pki_rotate_crl_response_from_dict = PkiRotateCrlResponse.from_dict(pki_rotate_crl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


