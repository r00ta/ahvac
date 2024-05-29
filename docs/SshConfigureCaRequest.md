# SshConfigureCaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generate_signing_key** | **bool** | Generate SSH key pair internally rather than use the private_key and public_key fields. | [optional] [default to True]
**key_bits** | **int** | Specifies the desired key bits when generating variable-length keys (such as when key_type&#x3D;\&quot;ssh-rsa\&quot;) or which NIST P-curve to use when key_type&#x3D;\&quot;ec\&quot; (256, 384, or 521). | [optional] [default to 0]
**key_type** | **str** | Specifies the desired key type when generating; could be a OpenSSH key type identifier (ssh-rsa, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521, or ssh-ed25519) or an algorithm (rsa, ec, ed25519). | [optional] [default to 'ssh-rsa']
**private_key** | **str** | Private half of the SSH key that will be used to sign certificates. | [optional] 
**public_key** | **str** | Public half of the SSH key that will be used to sign certificates. | [optional] 

## Example

```python
from ahvac.models.ssh_configure_ca_request import SshConfigureCaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SshConfigureCaRequest from a JSON string
ssh_configure_ca_request_instance = SshConfigureCaRequest.from_json(json)
# print the JSON string representation of the object
print(SshConfigureCaRequest.to_json())

# convert the object into a dict
ssh_configure_ca_request_dict = ssh_configure_ca_request_instance.to_dict()
# create an instance of SshConfigureCaRequest from a dict
ssh_configure_ca_request_from_dict = SshConfigureCaRequest.from_dict(ssh_configure_ca_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


