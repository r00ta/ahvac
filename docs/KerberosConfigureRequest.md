# KerberosConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_group_aliases** | **bool** | If set to true, returns any groups found in LDAP as a group alias. | [optional] 
**keytab** | **str** | Base64 encoded keytab | [optional] 
**remove_instance_name** | **bool** | Remove instance/FQDN from keytab principal names. | [optional] 
**service_account** | **str** | Service Account | [optional] 

## Example

```python
from ahvac.models.kerberos_configure_request import KerberosConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosConfigureRequest from a JSON string
kerberos_configure_request_instance = KerberosConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(KerberosConfigureRequest.to_json())

# convert the object into a dict
kerberos_configure_request_dict = kerberos_configure_request_instance.to_dict()
# create an instance of KerberosConfigureRequest from a dict
kerberos_configure_request_from_dict = KerberosConfigureRequest.from_dict(kerberos_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


