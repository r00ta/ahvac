# LdapLibraryCheckOutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **str** | The length of time before the check-out will expire, in seconds. | [optional] 

## Example

```python
from ahvac.models.ldap_library_check_out_request import LdapLibraryCheckOutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapLibraryCheckOutRequest from a JSON string
ldap_library_check_out_request_instance = LdapLibraryCheckOutRequest.from_json(json)
# print the JSON string representation of the object
print(LdapLibraryCheckOutRequest.to_json())

# convert the object into a dict
ldap_library_check_out_request_dict = ldap_library_check_out_request_instance.to_dict()
# create an instance of LdapLibraryCheckOutRequest from a dict
ldap_library_check_out_request_from_dict = LdapLibraryCheckOutRequest.from_dict(ldap_library_check_out_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


