# PkiReplaceRootRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Reference (name or identifier) to the default issuer. | [optional] [default to 'next']

## Example

```python
from ahvac.models.pki_replace_root_request import PkiReplaceRootRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiReplaceRootRequest from a JSON string
pki_replace_root_request_instance = PkiReplaceRootRequest.from_json(json)
# print the JSON string representation of the object
print(PkiReplaceRootRequest.to_json())

# convert the object into a dict
pki_replace_root_request_dict = pki_replace_root_request_instance.to_dict()
# create an instance of PkiReplaceRootRequest from a dict
pki_replace_root_request_from_dict = PkiReplaceRootRequest.from_dict(pki_replace_root_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


