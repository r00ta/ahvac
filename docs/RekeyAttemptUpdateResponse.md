# RekeyAttemptUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **bool** |  | [optional] 
**complete** | **bool** |  | [optional] 
**keys** | **List[str]** |  | [optional] 
**keys_base64** | **List[str]** |  | [optional] 
**n** | **int** |  | [optional] 
**nounce** | **str** |  | [optional] 
**pgp_fingerprints** | **List[str]** |  | [optional] 
**progress** | **int** |  | [optional] 
**required** | **int** |  | [optional] 
**started** | **str** |  | [optional] 
**t** | **int** |  | [optional] 
**verification_nonce** | **str** |  | [optional] 
**verification_required** | **bool** |  | [optional] 

## Example

```python
from ahvac.models.rekey_attempt_update_response import RekeyAttemptUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyAttemptUpdateResponse from a JSON string
rekey_attempt_update_response_instance = RekeyAttemptUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RekeyAttemptUpdateResponse.to_json())

# convert the object into a dict
rekey_attempt_update_response_dict = rekey_attempt_update_response_instance.to_dict()
# create an instance of RekeyAttemptUpdateResponse from a dict
rekey_attempt_update_response_from_dict = RekeyAttemptUpdateResponse.from_dict(rekey_attempt_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


