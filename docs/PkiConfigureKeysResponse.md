# PkiConfigureKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) to the default issuer. | [optional] 

## Example

```python
from ahvac.models.pki_configure_keys_response import PkiConfigureKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureKeysResponse from a JSON string
pki_configure_keys_response_instance = PkiConfigureKeysResponse.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureKeysResponse.to_json())

# convert the object into a dict
pki_configure_keys_response_dict = pki_configure_keys_response_instance.to_dict()
# create an instance of PkiConfigureKeysResponse from a dict
pki_configure_keys_response_from_dict = PkiConfigureKeysResponse.from_dict(pki_configure_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


