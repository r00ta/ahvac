# DatabaseConfigureConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_roles** | **List[str]** | Comma separated string or array of the role names allowed to get creds from this database connection. If empty no roles are allowed. If \&quot;*\&quot; all roles are allowed. | [optional] 
**password_policy** | **str** | Password policy to use when generating passwords. | [optional] 
**plugin_name** | **str** | The name of a builtin or previously registered plugin known to vault. This endpoint will create an instance of that plugin type. | [optional] 
**plugin_version** | **str** | The version of the plugin to use. | [optional] 
**root_rotation_statements** | **List[str]** | Specifies the database statements to be executed to rotate the root user&#39;s credentials. See the plugin&#39;s API page for more information on support and formatting for this parameter. | [optional] 
**verify_connection** | **bool** | If true, the connection details are verified by actually connecting to the database. Defaults to true. | [optional] [default to True]

## Example

```python
from ahvac.models.database_configure_connection_request import DatabaseConfigureConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConfigureConnectionRequest from a JSON string
database_configure_connection_request_instance = DatabaseConfigureConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(DatabaseConfigureConnectionRequest.to_json())

# convert the object into a dict
database_configure_connection_request_dict = database_configure_connection_request_instance.to_dict()
# create an instance of DatabaseConfigureConnectionRequest from a dict
database_configure_connection_request_from_dict = DatabaseConfigureConnectionRequest.from_dict(database_configure_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


