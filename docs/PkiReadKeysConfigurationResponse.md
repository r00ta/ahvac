# PkiReadKeysConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) to the default issuer. | [optional] 

## Example

```python
from ahvac.models.pki_read_keys_configuration_response import PkiReadKeysConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadKeysConfigurationResponse from a JSON string
pki_read_keys_configuration_response_instance = PkiReadKeysConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadKeysConfigurationResponse.to_json())

# convert the object into a dict
pki_read_keys_configuration_response_dict = pki_read_keys_configuration_response_instance.to_dict()
# create an instance of PkiReadKeysConfigurationResponse from a dict
pki_read_keys_configuration_response_from_dict = PkiReadKeysConfigurationResponse.from_dict(pki_read_keys_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


