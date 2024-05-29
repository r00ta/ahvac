# TransitImportKeyVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | The base64-encoded ciphertext of the keys. The AES key should be encrypted using OAEP with the wrapping key and then concatenated with the import key, wrapped by the AES key. | [optional] 
**hash_function** | **str** | The hash function used as a random oracle in the OAEP wrapping of the user-generated, ephemeral AES key. Can be one of \&quot;SHA1\&quot;, \&quot;SHA224\&quot;, \&quot;SHA256\&quot; (default), \&quot;SHA384\&quot;, or \&quot;SHA512\&quot; | [optional] [default to 'SHA256']
**public_key** | **str** | The plaintext public key to be imported. If \&quot;ciphertext\&quot; is set, this field is ignored. | [optional] 
**version** | **int** | Key version to be updated, if left empty, a new version will be created unless a private key is specified and the &#39;Latest&#39; key is missing a private key. | [optional] 

## Example

```python
from ahvac.models.transit_import_key_version_request import TransitImportKeyVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitImportKeyVersionRequest from a JSON string
transit_import_key_version_request_instance = TransitImportKeyVersionRequest.from_json(json)
# print the JSON string representation of the object
print(TransitImportKeyVersionRequest.to_json())

# convert the object into a dict
transit_import_key_version_request_dict = transit_import_key_version_request_instance.to_dict()
# create an instance of TransitImportKeyVersionRequest from a dict
transit_import_key_version_request_from_dict = TransitImportKeyVersionRequest.from_dict(transit_import_key_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


