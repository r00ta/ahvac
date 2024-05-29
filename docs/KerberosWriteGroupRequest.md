# KerberosWriteGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | **List[str]** | Comma-separated list of policies associated to the group. | [optional] 

## Example

```python
from ahvac.models.kerberos_write_group_request import KerberosWriteGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosWriteGroupRequest from a JSON string
kerberos_write_group_request_instance = KerberosWriteGroupRequest.from_json(json)
# print the JSON string representation of the object
print(KerberosWriteGroupRequest.to_json())

# convert the object into a dict
kerberos_write_group_request_dict = kerberos_write_group_request_instance.to_dict()
# create an instance of KerberosWriteGroupRequest from a dict
kerberos_write_group_request_from_dict = KerberosWriteGroupRequest.from_dict(kerberos_write_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


