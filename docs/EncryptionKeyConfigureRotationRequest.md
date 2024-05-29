# EncryptionKeyConfigureRotationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether automatic rotation is enabled. | [optional] 
**interval** | **str** | How long after installation of an active key term that the key will be automatically rotated. | [optional] 
**max_operations** | **int** | The number of encryption operations performed before the barrier key is automatically rotated. | [optional] 

## Example

```python
from ahvac.models.encryption_key_configure_rotation_request import EncryptionKeyConfigureRotationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyConfigureRotationRequest from a JSON string
encryption_key_configure_rotation_request_instance = EncryptionKeyConfigureRotationRequest.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeyConfigureRotationRequest.to_json())

# convert the object into a dict
encryption_key_configure_rotation_request_dict = encryption_key_configure_rotation_request_instance.to_dict()
# create an instance of EncryptionKeyConfigureRotationRequest from a dict
encryption_key_configure_rotation_request_from_dict = EncryptionKeyConfigureRotationRequest.from_dict(encryption_key_configure_rotation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


