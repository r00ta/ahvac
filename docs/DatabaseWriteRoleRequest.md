# DatabaseWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_statements** | **List[str]** | Specifies the database statements executed to create and configure a user. See the plugin&#39;s API page for more information on support and formatting for this parameter. | [optional] 
**credential_config** | **object** | The configuration for the given credential_type. | [optional] 
**credential_type** | **str** | The type of credential to manage. Options include: &#39;password&#39;, &#39;rsa_private_key&#39;. Defaults to &#39;password&#39;. | [optional] [default to 'password']
**db_name** | **str** | Name of the database this role acts on. | [optional] 
**default_ttl** | **str** | Default ttl for role. | [optional] 
**max_ttl** | **str** | Maximum time a credential is valid for | [optional] 
**renew_statements** | **List[str]** | Specifies the database statements to be executed to renew a user. Not every plugin type will support this functionality. See the plugin&#39;s API page for more information on support and formatting for this parameter. | [optional] 
**revocation_statements** | **List[str]** | Specifies the database statements to be executed to revoke a user. See the plugin&#39;s API page for more information on support and formatting for this parameter. | [optional] 
**rollback_statements** | **List[str]** | Specifies the database statements to be executed rollback a create operation in the event of an error. Not every plugin type will support this functionality. See the plugin&#39;s API page for more information on support and formatting for this parameter. | [optional] 

## Example

```python
from ahvac.models.database_write_role_request import DatabaseWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseWriteRoleRequest from a JSON string
database_write_role_request_instance = DatabaseWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(DatabaseWriteRoleRequest.to_json())

# convert the object into a dict
database_write_role_request_dict = database_write_role_request_instance.to_dict()
# create an instance of DatabaseWriteRoleRequest from a dict
database_write_role_request_from_dict = DatabaseWriteRoleRequest.from_dict(database_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


