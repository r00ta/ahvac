# AwsWriteStaticRolesNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rotation_period** | **str** | Period by which to rotate the backing credential of the adopted user. This can be a Go duration (e.g, &#39;1m&#39;, 24h&#39;), or an integer number of seconds. | [optional] 
**username** | **str** | The IAM user to adopt as a static role. | [optional] 

## Example

```python
from ahvac.models.aws_write_static_roles_name_request import AwsWriteStaticRolesNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsWriteStaticRolesNameRequest from a JSON string
aws_write_static_roles_name_request_instance = AwsWriteStaticRolesNameRequest.from_json(json)
# print the JSON string representation of the object
print(AwsWriteStaticRolesNameRequest.to_json())

# convert the object into a dict
aws_write_static_roles_name_request_dict = aws_write_static_roles_name_request_instance.to_dict()
# create an instance of AwsWriteStaticRolesNameRequest from a dict
aws_write_static_roles_name_request_from_dict = AwsWriteStaticRolesNameRequest.from_dict(aws_write_static_roles_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


