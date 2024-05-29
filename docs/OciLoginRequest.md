# OciLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_headers** | **str** | The signed headers of the client | [optional] 

## Example

```python
from ahvac.models.oci_login_request import OciLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OciLoginRequest from a JSON string
oci_login_request_instance = OciLoginRequest.from_json(json)
# print the JSON string representation of the object
print(OciLoginRequest.to_json())

# convert the object into a dict
oci_login_request_dict = oci_login_request_instance.to_dict()
# create an instance of OciLoginRequest from a dict
oci_login_request_from_dict = OciLoginRequest.from_dict(oci_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


