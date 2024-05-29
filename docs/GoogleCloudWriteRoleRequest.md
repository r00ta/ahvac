# GoogleCloudWriteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_group_aliases** | **bool** | If true, will add group aliases to auth tokens generated under this role. This will add the full list of ancestors (projects, folders, organizations) for the given entity&#39;s project. Requires IAM permission &#x60;resourcemanager.projects.get&#x60; on this project. | [optional] [default to False]
**allow_gce_inference** | **bool** | &#39;iam&#39; roles only. If false, Vault will not not allow GCE instances to login in against this role | [optional] [default to True]
**bound_instance_group** | **str** | Deprecated: use \&quot;bound_instance_groups\&quot; instead. | [optional] 
**bound_instance_groups** | **List[str]** | Comma-separated list of permitted instance groups to which the GCE instance must belong. This option only applies to \&quot;gce\&quot; roles. | [optional] 
**bound_labels** | **List[str]** | Comma-separated list of GCP labels formatted as\&quot;key:value\&quot; strings that must be present on the GCE instance in order to authenticate. This option only applies to \&quot;gce\&quot; roles. | [optional] 
**bound_projects** | **List[str]** | GCP Projects that authenticating entities must belong to. | [optional] 
**bound_region** | **str** | Deprecated: use \&quot;bound_regions\&quot; instead. | [optional] 
**bound_regions** | **List[str]** | Comma-separated list of permitted regions to which the GCE instance must belong. If a group is provided, it is assumed to be a regional group. If \&quot;zone\&quot; is provided, this option is ignored. This can be a self-link or region name. This option only applies to \&quot;gce\&quot; roles. | [optional] 
**bound_service_accounts** | **List[str]** | Can be set for both &#39;iam&#39; and &#39;gce&#39; roles (required for &#39;iam&#39;). A comma-seperated list of authorized service accounts. If the single value \&quot;*\&quot; is given, this is assumed to be all service accounts under the role&#39;s project. If this is set on a GCE role, the inferred service account from the instance metadata token will be used. | [optional] 
**bound_zone** | **str** | Deprecated: use \&quot;bound_zones\&quot; instead. | [optional] 
**bound_zones** | **List[str]** | Comma-separated list of permitted zones to which the GCE instance must belong. If a group is provided, it is assumed to be a zonal group. This can be a self-link or zone name. This option only applies to \&quot;gce\&quot; roles. | [optional] 
**max_jwt_exp** | **str** | Currently enabled for &#39;iam&#39; only. Duration in seconds from time of validation that a JWT must expire within. | [optional] [default to '900']
**max_ttl** | **str** | Use \&quot;token_max_ttl\&quot; instead. If this and \&quot;token_max_ttl\&quot; are both specified, only \&quot;token_max_ttl\&quot; will be used. | [optional] 
**period** | **str** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**policies** | **List[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**project_id** | **str** | Deprecated: use \&quot;bound_projects\&quot; instead | [optional] 
**service_accounts** | **List[str]** | Deprecated: use \&quot;bound_service_accounts\&quot; instead. | [optional] 
**token_bound_cidrs** | **List[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **str** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_max_ttl** | **str** | The maximum lifetime of the generated token | [optional] 
**token_no_default_policy** | **bool** | If true, the &#39;default&#39; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **str** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 
**token_policies** | **List[str]** | Comma-separated list of policies | [optional] 
**token_ttl** | **str** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']
**ttl** | **str** | Use \&quot;token_ttl\&quot; instead. If this and \&quot;token_ttl\&quot; are both specified, only \&quot;token_ttl\&quot; will be used. | [optional] 
**type** | **str** | Type of the role. Currently supported: iam, gce | [optional] 

## Example

```python
from ahvac.models.google_cloud_write_role_request import GoogleCloudWriteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudWriteRoleRequest from a JSON string
google_cloud_write_role_request_instance = GoogleCloudWriteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudWriteRoleRequest.to_json())

# convert the object into a dict
google_cloud_write_role_request_dict = google_cloud_write_role_request_instance.to_dict()
# create an instance of GoogleCloudWriteRoleRequest from a dict
google_cloud_write_role_request_from_dict = GoogleCloudWriteRoleRequest.from_dict(google_cloud_write_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


