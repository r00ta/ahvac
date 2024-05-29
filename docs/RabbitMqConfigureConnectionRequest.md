# RabbitMqConfigureConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_uri** | **str** | RabbitMQ Management URI | [optional] 
**password** | **str** | Password of the provided RabbitMQ management user | [optional] 
**password_policy** | **str** | Name of the password policy to use to generate passwords for dynamic credentials. | [optional] 
**username** | **str** | Username of a RabbitMQ management administrator | [optional] 
**username_template** | **str** | Template describing how dynamic usernames are generated. | [optional] 
**verify_connection** | **bool** | If set, connection_uri is verified by actually connecting to the RabbitMQ management API | [optional] [default to True]

## Example

```python
from ahvac.models.rabbit_mq_configure_connection_request import RabbitMqConfigureConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RabbitMqConfigureConnectionRequest from a JSON string
rabbit_mq_configure_connection_request_instance = RabbitMqConfigureConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(RabbitMqConfigureConnectionRequest.to_json())

# convert the object into a dict
rabbit_mq_configure_connection_request_dict = rabbit_mq_configure_connection_request_instance.to_dict()
# create an instance of RabbitMqConfigureConnectionRequest from a dict
rabbit_mq_configure_connection_request_from_dict = RabbitMqConfigureConnectionRequest.from_dict(rabbit_mq_configure_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


