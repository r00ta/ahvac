# PkiReplaceRootResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) to the default issuer. | [optional] 
**default_follows_latest_issuer** | **bool** | Whether the default issuer should automatically follow the latest generated or imported issuer. Defaults to false. | [optional] 

## Example

```python
from ahvac.models.pki_replace_root_response import PkiReplaceRootResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReplaceRootResponse from a JSON string
pki_replace_root_response_instance = PkiReplaceRootResponse.from_json(json)
# print the JSON string representation of the object
print(PkiReplaceRootResponse.to_json())

# convert the object into a dict
pki_replace_root_response_dict = pki_replace_root_response_instance.to_dict()
# create an instance of PkiReplaceRootResponse from a dict
pki_replace_root_response_from_dict = PkiReplaceRootResponse.from_dict(pki_replace_root_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


