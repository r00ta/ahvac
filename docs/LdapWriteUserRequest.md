# LdapWriteUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Comma-separated list of additional groups associated with the user. | [optional] 
**policies** | **List[str]** | Comma-separated list of policies associated with the user. | [optional] 

## Example

```python
from ahvac.models.ldap_write_user_request import LdapWriteUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapWriteUserRequest from a JSON string
ldap_write_user_request_instance = LdapWriteUserRequest.from_json(json)
# print the JSON string representation of the object
print(LdapWriteUserRequest.to_json())

# convert the object into a dict
ldap_write_user_request_dict = ldap_write_user_request_instance.to_dict()
# create an instance of LdapWriteUserRequest from a dict
ldap_write_user_request_from_dict = LdapWriteUserRequest.from_dict(ldap_write_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


