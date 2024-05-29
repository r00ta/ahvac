# LdapLibraryForceCheckInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_names** | **List[str]** | The username/logon name for the service accounts to check in. | [optional] 

## Example

```python
from ahvac.models.ldap_library_force_check_in_request import LdapLibraryForceCheckInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapLibraryForceCheckInRequest from a JSON string
ldap_library_force_check_in_request_instance = LdapLibraryForceCheckInRequest.from_json(json)
# print the JSON string representation of the object
print(LdapLibraryForceCheckInRequest.to_json())

# convert the object into a dict
ldap_library_force_check_in_request_dict = ldap_library_force_check_in_request_instance.to_dict()
# create an instance of LdapLibraryForceCheckInRequest from a dict
ldap_library_force_check_in_request_from_dict = LdapLibraryForceCheckInRequest.from_dict(ldap_library_force_check_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


