# AwsConfigureLeaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease** | **str** | Default lease for roles. | [optional] 
**lease_max** | **str** | Maximum time a credential is valid for. | [optional] 

## Example

```python
from ahvac.models.aws_configure_lease_request import AwsConfigureLeaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsConfigureLeaseRequest from a JSON string
aws_configure_lease_request_instance = AwsConfigureLeaseRequest.from_json(json)
# print the JSON string representation of the object
print(AwsConfigureLeaseRequest.to_json())

# convert the object into a dict
aws_configure_lease_request_dict = aws_configure_lease_request_instance.to_dict()
# create an instance of AwsConfigureLeaseRequest from a dict
aws_configure_lease_request_from_dict = AwsConfigureLeaseRequest.from_dict(aws_configure_lease_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


