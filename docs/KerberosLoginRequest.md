# KerberosLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **str** | SPNEGO Authorization header. Required. | [optional] 

## Example

```python
from ahvac.models.kerberos_login_request import KerberosLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosLoginRequest from a JSON string
kerberos_login_request_instance = KerberosLoginRequest.from_json(json)
# print the JSON string representation of the object
print(KerberosLoginRequest.to_json())

# convert the object into a dict
kerberos_login_request_dict = kerberos_login_request_instance.to_dict()
# create an instance of KerberosLoginRequest from a dict
kerberos_login_request_from_dict = KerberosLoginRequest.from_dict(kerberos_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


