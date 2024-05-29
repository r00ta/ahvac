# SshVerifyOtpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** | [Required] One-Time-Key that needs to be validated | [optional] 

## Example

```python
from ahvac.models.ssh_verify_otp_request import SshVerifyOtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SshVerifyOtpRequest from a JSON string
ssh_verify_otp_request_instance = SshVerifyOtpRequest.from_json(json)
# print the JSON string representation of the object
print(SshVerifyOtpRequest.to_json())

# convert the object into a dict
ssh_verify_otp_request_dict = ssh_verify_otp_request_instance.to_dict()
# create an instance of SshVerifyOtpRequest from a dict
ssh_verify_otp_request_from_dict = SshVerifyOtpRequest.from_dict(ssh_verify_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


