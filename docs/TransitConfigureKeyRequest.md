# TransitConfigureKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_plaintext_backup** | **bool** | Enables taking a backup of the named key in plaintext format. Once set, this cannot be disabled. | [optional] 
**auto_rotate_period** | **str** | Amount of time the key should live before being automatically rotated. A value of 0 disables automatic rotation for the key. | [optional] 
**deletion_allowed** | **bool** | Whether to allow deletion of the key | [optional] 
**exportable** | **bool** | Enables export of the key. Once set, this cannot be disabled. | [optional] 
**min_decryption_version** | **int** | If set, the minimum version of the key allowed to be decrypted. For signing keys, the minimum version allowed to be used for verification. | [optional] 
**min_encryption_version** | **int** | If set, the minimum version of the key allowed to be used for encryption; or for signing keys, to be used for signing. If set to zero, only the latest version of the key is allowed. | [optional] 

## Example

```python
from ahvac.models.transit_configure_key_request import TransitConfigureKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitConfigureKeyRequest from a JSON string
transit_configure_key_request_instance = TransitConfigureKeyRequest.from_json(json)
# print the JSON string representation of the object
print(TransitConfigureKeyRequest.to_json())

# convert the object into a dict
transit_configure_key_request_dict = transit_configure_key_request_instance.to_dict()
# create an instance of TransitConfigureKeyRequest from a dict
transit_configure_key_request_from_dict = TransitConfigureKeyRequest.from_dict(transit_configure_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


