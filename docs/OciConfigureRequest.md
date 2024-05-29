# OciConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_tenancy_id** | **str** | The tenancy id of the account. | [optional] 

## Example

```python
from ahvac.models.oci_configure_request import OciConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OciConfigureRequest from a JSON string
oci_configure_request_instance = OciConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(OciConfigureRequest.to_json())

# convert the object into a dict
oci_configure_request_dict = oci_configure_request_instance.to_dict()
# create an instance of OciConfigureRequest from a dict
oci_configure_request_from_dict = OciConfigureRequest.from_dict(oci_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


