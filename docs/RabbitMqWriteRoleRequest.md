# RabbitMqWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **str** | Comma-separated list of tags for this role. | [optional] 
**vhost_topics** | **str** | A nested map of virtual hosts and exchanges to topic permissions. | [optional] 
**vhosts** | **str** | A map of virtual hosts to permissions. | [optional] 

## Example

```python
from ahvac.models.rabbit_mq_write_role_request import RabbitMqWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RabbitMqWriteRoleRequest from a JSON string
rabbit_mq_write_role_request_instance = RabbitMqWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(RabbitMqWriteRoleRequest.to_json())

# convert the object into a dict
rabbit_mq_write_role_request_dict = rabbit_mq_write_role_request_instance.to_dict()
# create an instance of RabbitMqWriteRoleRequest from a dict
rabbit_mq_write_role_request_from_dict = RabbitMqWriteRoleRequest.from_dict(rabbit_mq_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


