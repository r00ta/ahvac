# RekeyReadBackupRecoveryKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **object** |  | [optional] 
**keys_base64** | **object** |  | [optional] 
**nonce** | **str** |  | [optional] 

## Example

```python
from ahvac.models.rekey_read_backup_recovery_key_response import RekeyReadBackupRecoveryKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RekeyReadBackupRecoveryKeyResponse from a JSON string
rekey_read_backup_recovery_key_response_instance = RekeyReadBackupRecoveryKeyResponse.from_json(json)
# print the JSON string representation of the object
print(RekeyReadBackupRecoveryKeyResponse.to_json())

# convert the object into a dict
rekey_read_backup_recovery_key_response_dict = rekey_read_backup_recovery_key_response_instance.to_dict()
# create an instance of RekeyReadBackupRecoveryKeyResponse from a dict
rekey_read_backup_recovery_key_response_from_dict = RekeyReadBackupRecoveryKeyResponse.from_dict(rekey_read_backup_recovery_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


