# MongoDbAtlasWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_blocks** | **List[str]** | Access list entry in CIDR notation to be added for the API key. Optional for organization and project keys. | [optional] 
**ip_addresses** | **List[str]** | IP address to be added to the access list for the API key. Optional for organization and project keys. | [optional] 
**max_ttl** | **str** | The maximum allowed lifetime of credentials issued using this role. | [optional] 
**organization_id** | **str** | Organization ID required for an organization API key | [optional] 
**project_id** | **str** | Project ID the project API key belongs to. | [optional] 
**project_roles** | **List[str]** | Roles assigned when an organization API Key is assigned to a project API key | [optional] 
**roles** | **List[str]** | List of roles that the API Key should be granted. A minimum of one role must be provided. Any roles provided must be valid for the assigned Project, required for organization and project keys. | 
**ttl** | **str** | Duration in seconds after which the issued credential should expire. Defaults to 0, in which case the value will fallback to the system/mount defaults. | [optional] 

## Example

```python
from ahvac.models.mongo_db_atlas_write_role_request import MongoDbAtlasWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDbAtlasWriteRoleRequest from a JSON string
mongo_db_atlas_write_role_request_instance = MongoDbAtlasWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(MongoDbAtlasWriteRoleRequest.to_json())

# convert the object into a dict
mongo_db_atlas_write_role_request_dict = mongo_db_atlas_write_role_request_instance.to_dict()
# create an instance of MongoDbAtlasWriteRoleRequest from a dict
mongo_db_atlas_write_role_request_from_dict = MongoDbAtlasWriteRoleRequest.from_dict(mongo_db_atlas_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


