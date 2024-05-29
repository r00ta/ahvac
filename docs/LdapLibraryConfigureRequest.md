# LdapLibraryConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_check_in_enforcement** | **bool** | Disable the default behavior of requiring that check-ins are performed by the entity that checked them out. | [optional] [default to False]
**max_ttl** | **str** | In seconds, the max amount of time a check-out&#39;s renewals should last. Defaults to 24 hours. | [optional] [default to '86400']
**service_account_names** | **List[str]** | The username/logon name for the service accounts with which this set will be associated. | [optional] 
**ttl** | **str** | In seconds, the amount of time a check-out should last. Defaults to 24 hours. | [optional] [default to '86400']

## Example

```python
from ahvac.models.ldap_library_configure_request import LdapLibraryConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapLibraryConfigureRequest from a JSON string
ldap_library_configure_request_instance = LdapLibraryConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(LdapLibraryConfigureRequest.to_json())

# convert the object into a dict
ldap_library_configure_request_dict = ldap_library_configure_request_instance.to_dict()
# create an instance of LdapLibraryConfigureRequest from a dict
ldap_library_configure_request_from_dict = LdapLibraryConfigureRequest.from_dict(ldap_library_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


