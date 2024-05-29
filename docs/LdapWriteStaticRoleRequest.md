# LdapWriteStaticRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** | The distinguished name of the entry to manage. | [optional] 
**rotation_period** | **str** | Period for automatic credential rotation of the given entry. | [optional] 
**username** | **str** | The username/logon name for the entry with which this role will be associated. | [optional] 

## Example

```python
from ahvac.models.ldap_write_static_role_request import LdapWriteStaticRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapWriteStaticRoleRequest from a JSON string
ldap_write_static_role_request_instance = LdapWriteStaticRoleRequest.from_json(json)
# print the JSON string representation of the object
print(LdapWriteStaticRoleRequest.to_json())

# convert the object into a dict
ldap_write_static_role_request_dict = ldap_write_static_role_request_instance.to_dict()
# create an instance of LdapWriteStaticRoleRequest from a dict
ldap_write_static_role_request_from_dict = LdapWriteStaticRoleRequest.from_dict(ldap_write_static_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


