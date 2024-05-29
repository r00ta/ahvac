# PkiReadIssuersConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) to the default issuer. | [optional] 
**default_follows_latest_issuer** | **bool** | Whether the default issuer should automatically follow the latest generated or imported issuer. Defaults to false. | [optional] 

## Example

```python
from ahvac.models.pki_read_issuers_configuration_response import PkiReadIssuersConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReadIssuersConfigurationResponse from a JSON string
pki_read_issuers_configuration_response_instance = PkiReadIssuersConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReadIssuersConfigurationResponse.to_json())

# convert the object into a dict
pki_read_issuers_configuration_response_dict = pki_read_issuers_configuration_response_instance.to_dict()
# create an instance of PkiReadIssuersConfigurationResponse from a dict
pki_read_issuers_configuration_response_from_dict = PkiReadIssuersConfigurationResponse.from_dict(pki_read_issuers_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


