# LdapWriteGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | **List[str]** | Comma-separated list of policies associated to the group. | [optional] 

## Example

```python
from ahvac.models.ldap_write_group_request import LdapWriteGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapWriteGroupRequest from a JSON string
ldap_write_group_request_instance = LdapWriteGroupRequest.from_json(json)
# print the JSON string representation of the object
print(LdapWriteGroupRequest.to_json())

# convert the object into a dict
ldap_write_group_request_dict = ldap_write_group_request_instance.to_dict()
# create an instance of LdapWriteGroupRequest from a dict
ldap_write_group_request_from_dict = LdapWriteGroupRequest.from_dict(ldap_write_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


