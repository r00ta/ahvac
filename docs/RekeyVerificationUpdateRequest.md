# RekeyVerificationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies a single unseal share key from the new set of shares. | [optional] 
**nonce** | **str** | Specifies the nonce of the rekey verification operation. | [optional] 

## Example

```python
from ahvac.models.rekey_verification_update_request import RekeyVerificationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyVerificationUpdateRequest from a JSON string
rekey_verification_update_request_instance = RekeyVerificationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RekeyVerificationUpdateRequest.to_json())

# convert the object into a dict
rekey_verification_update_request_dict = rekey_verification_update_request_instance.to_dict()
# create an instance of RekeyVerificationUpdateRequest from a dict
rekey_verification_update_request_from_dict = RekeyVerificationUpdateRequest.from_dict(rekey_verification_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


