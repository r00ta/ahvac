# CertLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the certificate role to authenticate against. | [optional] 

## Example

```python
from ahvac.models.cert_login_request import CertLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertLoginRequest from a JSON string
cert_login_request_instance = CertLoginRequest.from_json(json)
# print the JSON string representation of the object
print(CertLoginRequest.to_json())

# convert the object into a dict
cert_login_request_dict = cert_login_request_instance.to_dict()
# create an instance of CertLoginRequest from a dict
cert_login_request_from_dict = CertLoginRequest.from_dict(cert_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


