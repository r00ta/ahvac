# SshGenerateCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | [Required] IP of the remote host | [optional] 
**username** | **str** | [Optional] Username in remote host | [optional] 

## Example

```python
from ahvac.models.ssh_generate_credentials_request import SshGenerateCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SshGenerateCredentialsRequest from a JSON string
ssh_generate_credentials_request_instance = SshGenerateCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(SshGenerateCredentialsRequest.to_json())

# convert the object into a dict
ssh_generate_credentials_request_dict = ssh_generate_credentials_request_instance.to_dict()
# create an instance of SshGenerateCredentialsRequest from a dict
ssh_generate_credentials_request_from_dict = SshGenerateCredentialsRequest.from_dict(ssh_generate_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


