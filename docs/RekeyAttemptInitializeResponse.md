# RekeyAttemptInitializeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **bool** |  | [optional] 
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
from ahvac.models.rekey_attempt_initialize_response import RekeyAttemptInitializeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyAttemptInitializeResponse from a JSON string
rekey_attempt_initialize_response_instance = RekeyAttemptInitializeResponse.from_json(json)
# print the JSON string representation of the object
print(RekeyAttemptInitializeResponse.to_json())

# convert the object into a dict
rekey_attempt_initialize_response_dict = rekey_attempt_initialize_response_instance.to_dict()
# create an instance of RekeyAttemptInitializeResponse from a dict
rekey_attempt_initialize_response_from_dict = RekeyAttemptInitializeResponse.from_dict(rekey_attempt_initialize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


