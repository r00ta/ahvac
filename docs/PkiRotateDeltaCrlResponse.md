# PkiRotateDeltaCrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether rotation was successful | [optional] 

## Example

```python
from ahvac.models.pki_rotate_delta_crl_response import PkiRotateDeltaCrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiRotateDeltaCrlResponse from a JSON string
pki_rotate_delta_crl_response_instance = PkiRotateDeltaCrlResponse.from_json(json)
# print the JSON string representation of the object
print(PkiRotateDeltaCrlResponse.to_json())

# convert the object into a dict
pki_rotate_delta_crl_response_dict = pki_rotate_delta_crl_response_instance.to_dict()
# create an instance of PkiRotateDeltaCrlResponse from a dict
pki_rotate_delta_crl_response_from_dict = PkiRotateDeltaCrlResponse.from_dict(pki_rotate_delta_crl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


