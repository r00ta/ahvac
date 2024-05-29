# LdapWriteDynamicRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_ldif** | **str** | LDIF string used to create new entities within the LDAP system. This LDIF can be templated. | 
**default_ttl** | **str** | Default TTL for dynamic credentials | [optional] 
**deletion_ldif** | **str** | LDIF string used to delete entities created within the LDAP system. This LDIF can be templated. | 
**max_ttl** | **str** | Max TTL a dynamic credential can be extended to | [optional] 
**rollback_ldif** | **str** | LDIF string used to rollback changes in the event of a failure to create credentials. This LDIF can be templated. | [optional] 
**username_template** | **str** | The template used to create a username | [optional] 

## Example

```python
from ahvac.models.ldap_write_dynamic_role_request import LdapWriteDynamicRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapWriteDynamicRoleRequest from a JSON string
ldap_write_dynamic_role_request_instance = LdapWriteDynamicRoleRequest.from_json(json)
# print the JSON string representation of the object
print(LdapWriteDynamicRoleRequest.to_json())

# convert the object into a dict
ldap_write_dynamic_role_request_dict = ldap_write_dynamic_role_request_instance.to_dict()
# create an instance of LdapWriteDynamicRoleRequest from a dict
ldap_write_dynamic_role_request_from_dict = LdapWriteDynamicRoleRequest.from_dict(ldap_write_dynamic_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


