# DatabaseWriteStaticRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_config** | **object** | The configuration for the given credential_type. | [optional] 
**credential_type** | **str** | The type of credential to manage. Options include: &#39;password&#39;, &#39;rsa_private_key&#39;. Defaults to &#39;password&#39;. | [optional] [default to 'password']
**db_name** | **str** | Name of the database this role acts on. | [optional] 
**rotation_period** | **str** | Period for automatic credential rotation of the given username. Not valid unless used with \&quot;username\&quot;. Mutually exclusive with \&quot;rotation_schedule.\&quot; | [optional] 
**rotation_schedule** | **str** | Schedule for automatic credential rotation of the given username. Mutually exclusive with \&quot;rotation_period.\&quot; | [optional] 
**rotation_statements** | **List[str]** | Specifies the database statements to be executed to rotate the accounts credentials. Not every plugin type will support this functionality. See the plugin&#39;s API page for more information on support and formatting for this parameter. | [optional] 
**rotation_window** | **str** | The window of time in which rotations are allowed to occur starting from a given \&quot;rotation_schedule\&quot;. Requires \&quot;rotation_schedule\&quot; to be specified | [optional] 
**username** | **str** | Name of the static user account for Vault to manage. Requires \&quot;rotation_period\&quot; to be specified | [optional] 

## Example

```python
from ahvac.models.database_write_static_role_request import DatabaseWriteStaticRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseWriteStaticRoleRequest from a JSON string
database_write_static_role_request_instance = DatabaseWriteStaticRoleRequest.from_json(json)
# print the JSON string representation of the object
print(DatabaseWriteStaticRoleRequest.to_json())

# convert the object into a dict
database_write_static_role_request_dict = database_write_static_role_request_instance.to_dict()
# create an instance of DatabaseWriteStaticRoleRequest from a dict
database_write_static_role_request_from_dict = DatabaseWriteStaticRoleRequest.from_dict(database_write_static_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


