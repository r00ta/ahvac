# EncryptionKeyReadRotationConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**interval** | **str** |  | [optional] 
**max_operations** | **int** |  | [optional] 

## Example

```python
from ahvac.models.encryption_key_read_rotation_configuration_response import EncryptionKeyReadRotationConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyReadRotationConfigurationResponse from a JSON string
encryption_key_read_rotation_configuration_response_instance = EncryptionKeyReadRotationConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeyReadRotationConfigurationResponse.to_json())

# convert the object into a dict
encryption_key_read_rotation_configuration_response_dict = encryption_key_read_rotation_configuration_response_instance.to_dict()
# create an instance of EncryptionKeyReadRotationConfigurationResponse from a dict
encryption_key_read_rotation_configuration_response_from_dict = EncryptionKeyReadRotationConfigurationResponse.from_dict(encryption_key_read_rotation_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


