# PkiConfigureKeysRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) of the default key. | [optional] 

## Example

```python
from ahvac.models.pki_configure_keys_request import PkiConfigureKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureKeysRequest from a JSON string
pki_configure_keys_request_instance = PkiConfigureKeysRequest.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureKeysRequest.to_json())

# convert the object into a dict
pki_configure_keys_request_dict = pki_configure_keys_request_instance.to_dict()
# create an instance of PkiConfigureKeysRequest from a dict
pki_configure_keys_request_from_dict = PkiConfigureKeysRequest.from_dict(pki_configure_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


