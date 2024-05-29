# RabbitMqConfigureLeaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_ttl** | **str** | Duration after which the issued credentials should not be allowed to be renewed | [optional] [default to '0']
**ttl** | **str** | Duration before which the issued credentials needs renewal | [optional] [default to '0']

## Example

```python
from ahvac.models.rabbit_mq_configure_lease_request import RabbitMqConfigureLeaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RabbitMqConfigureLeaseRequest from a JSON string
rabbit_mq_configure_lease_request_instance = RabbitMqConfigureLeaseRequest.from_json(json)
# print the JSON string representation of the object
print(RabbitMqConfigureLeaseRequest.to_json())

# convert the object into a dict
rabbit_mq_configure_lease_request_dict = rabbit_mq_configure_lease_request_instance.to_dict()
# create an instance of RabbitMqConfigureLeaseRequest from a dict
rabbit_mq_configure_lease_request_from_dict = RabbitMqConfigureLeaseRequest.from_dict(rabbit_mq_configure_lease_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


