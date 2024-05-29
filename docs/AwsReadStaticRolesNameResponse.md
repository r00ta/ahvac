# AwsReadStaticRolesNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this role. | [optional] 
**rotation_period** | **str** | Period by which to rotate the backing credential of the adopted user. This can be a Go duration (e.g, &#39;1m&#39;, 24h&#39;), or an integer number of seconds. | [optional] 
**username** | **str** | The IAM user to adopt as a static role. | [optional] 

## Example

```python
from ahvac.models.aws_read_static_roles_name_response import AwsReadStaticRolesNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AwsReadStaticRolesNameResponse from a JSON string
aws_read_static_roles_name_response_instance = AwsReadStaticRolesNameResponse.from_json(json)
# print the JSON string representation of the object
print(AwsReadStaticRolesNameResponse.to_json())

# convert the object into a dict
aws_read_static_roles_name_response_dict = aws_read_static_roles_name_response_instance.to_dict()
# create an instance of AwsReadStaticRolesNameResponse from a dict
aws_read_static_roles_name_response_from_dict = AwsReadStaticRolesNameResponse.from_dict(aws_read_static_roles_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


