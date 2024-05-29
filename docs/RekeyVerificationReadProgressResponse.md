# RekeyVerificationReadProgressResponse


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
from ahvac.models.rekey_verification_read_progress_response import RekeyVerificationReadProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyVerificationReadProgressResponse from a JSON string
rekey_verification_read_progress_response_instance = RekeyVerificationReadProgressResponse.from_json(json)
# print the JSON string representation of the object
print(RekeyVerificationReadProgressResponse.to_json())

# convert the object into a dict
rekey_verification_read_progress_response_dict = rekey_verification_read_progress_response_instance.to_dict()
# create an instance of RekeyVerificationReadProgressResponse from a dict
rekey_verification_read_progress_response_from_dict = RekeyVerificationReadProgressResponse.from_dict(rekey_verification_read_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

