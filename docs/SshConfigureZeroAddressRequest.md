# SshConfigureZeroAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** | [Required] Comma separated list of role names which allows credentials to be requested for any IP address. CIDR blocks previously registered under these roles will be ignored. | [optional] 

## Example

```python
from ahvac.models.ssh_configure_zero_address_request import SshConfigureZeroAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SshConfigureZeroAddressRequest from a JSON string
ssh_configure_zero_address_request_instance = SshConfigureZeroAddressRequest.from_json(json)
# print the JSON string representation of the object
print(SshConfigureZeroAddressRequest.to_json())

# convert the object into a dict
ssh_configure_zero_address_request_dict = ssh_configure_zero_address_request_instance.to_dict()
# create an instance of SshConfigureZeroAddressRequest from a dict
ssh_configure_zero_address_request_from_dict = SshConfigureZeroAddressRequest.from_dict(ssh_configure_zero_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


