# RekeyVerificationCancelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n** | **int** |  | [optional] 
**nounce** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**started** | **str** |  | [optional] 
**t** | **int** |  | [optional] 

## Example

```python
from ahvac.models.rekey_verification_cancel_response import RekeyVerificationCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyVerificationCancelResponse from a JSON string
rekey_verification_cancel_response_instance = RekeyVerificationCancelResponse.from_json(json)
# print the JSON string representation of the object
print(RekeyVerificationCancelResponse.to_json())

# convert the object into a dict
rekey_verification_cancel_response_dict = rekey_verification_cancel_response_instance.to_dict()
# create an instance of RekeyVerificationCancelResponse from a dict
rekey_verification_cancel_response_from_dict = RekeyVerificationCancelResponse.from_dict(rekey_verification_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


