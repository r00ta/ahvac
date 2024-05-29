# LdapLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for this user. | [optional] 

## Example

```python
from ahvac.models.ldap_login_request import LdapLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LdapLoginRequest from a JSON string
ldap_login_request_instance = LdapLoginRequest.from_json(json)
# print the JSON string representation of the object
print(LdapLoginRequest.to_json())

# convert the object into a dict
ldap_login_request_dict = ldap_login_request_instance.to_dict()
# create an instance of LdapLoginRequest from a dict
ldap_login_request_from_dict = LdapLoginRequest.from_dict(ldap_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


