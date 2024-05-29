# PkiConfigureIssuersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) to the default issuer. | [optional] 
**default_follows_latest_issuer** | **bool** | Whether the default issuer should automatically follow the latest generated or imported issuer. Defaults to false. | [optional] [default to False]

## Example

```python
from ahvac.models.pki_configure_issuers_request import PkiConfigureIssuersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureIssuersRequest from a JSON string
pki_configure_issuers_request_instance = PkiConfigureIssuersRequest.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureIssuersRequest.to_json())

# convert the object into a dict
pki_configure_issuers_request_dict = pki_configure_issuers_request_instance.to_dict()
# create an instance of PkiConfigureIssuersRequest from a dict
pki_configure_issuers_request_from_dict = PkiConfigureIssuersRequest.from_dict(pki_configure_issuers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


