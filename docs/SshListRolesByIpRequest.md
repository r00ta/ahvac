# SshListRolesByIpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | [Required] IP address of remote host | [optional] 

## Example

```python
from ahvac.models.ssh_list_roles_by_ip_request import SshListRolesByIpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SshListRolesByIpRequest from a JSON string
ssh_list_roles_by_ip_request_instance = SshListRolesByIpRequest.from_json(json)
# print the JSON string representation of the object
print(SshListRolesByIpRequest.to_json())

# convert the object into a dict
ssh_list_roles_by_ip_request_dict = ssh_list_roles_by_ip_request_instance.to_dict()
# create an instance of SshListRolesByIpRequest from a dict
ssh_list_roles_by_ip_request_from_dict = SshListRolesByIpRequest.from_dict(ssh_list_roles_by_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


