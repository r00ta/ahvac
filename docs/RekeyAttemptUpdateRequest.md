# RekeyAttemptUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies a single unseal key share. | [optional] 
**nonce** | **str** | Specifies the nonce of the rekey attempt. | [optional] 

## Example

```python
from ahvac.models.rekey_attempt_update_request import RekeyAttemptUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyAttemptUpdateRequest from a JSON string
rekey_attempt_update_request_instance = RekeyAttemptUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RekeyAttemptUpdateRequest.to_json())

# convert the object into a dict
rekey_attempt_update_request_dict = rekey_attempt_update_request_instance.to_dict()
# create an instance of RekeyAttemptUpdateRequest from a dict
rekey_attempt_update_request_from_dict = RekeyAttemptUpdateRequest.from_dict(rekey_attempt_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


