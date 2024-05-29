# LdapLibraryCheckInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_names** | **List[str]** | The username/logon name for the service accounts to check in. | [optional] 

## Example

```python
from ahvac.models.ldap_library_check_in_request import LdapLibraryCheckInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapLibraryCheckInRequest from a JSON string
ldap_library_check_in_request_instance = LdapLibraryCheckInRequest.from_json(json)
# print the JSON string representation of the object
print(LdapLibraryCheckInRequest.to_json())

# convert the object into a dict
ldap_library_check_in_request_dict = ldap_library_check_in_request_instance.to_dict()
# create an instance of LdapLibraryCheckInRequest from a dict
ldap_library_check_in_request_from_dict = LdapLibraryCheckInRequest.from_dict(ldap_library_check_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


