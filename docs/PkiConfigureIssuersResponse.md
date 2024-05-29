# PkiConfigureIssuersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) to the default issuer. | [optional] 
**default_follows_latest_issuer** | **bool** | Whether the default issuer should automatically follow the latest generated or imported issuer. Defaults to false. | [optional] 

## Example

```python
from ahvac.models.pki_configure_issuers_response import PkiConfigureIssuersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureIssuersResponse from a JSON string
pki_configure_issuers_response_instance = PkiConfigureIssuersResponse.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureIssuersResponse.to_json())

# convert the object into a dict
pki_configure_issuers_response_dict = pki_configure_issuers_response_instance.to_dict()
# create an instance of PkiConfigureIssuersResponse from a dict
pki_configure_issuers_response_from_dict = PkiConfigureIssuersResponse.from_dict(pki_configure_issuers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


