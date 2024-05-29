# RekeyVerificationUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** |  | [optional] 
**nounce** | **str** |  | [optional] 

## Example

```python
from ahvac.models.rekey_verification_update_response import RekeyVerificationUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyVerificationUpdateResponse from a JSON string
rekey_verification_update_response_instance = RekeyVerificationUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RekeyVerificationUpdateResponse.to_json())

# convert the object into a dict
rekey_verification_update_response_dict = rekey_verification_update_response_instance.to_dict()
# create an instance of RekeyVerificationUpdateResponse from a dict
rekey_verification_update_response_from_dict = RekeyVerificationUpdateResponse.from_dict(rekey_verification_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


