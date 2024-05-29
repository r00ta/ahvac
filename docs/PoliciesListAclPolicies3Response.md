# PoliciesListAclPolicies3Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** |  | [optional] 
**policies** | **List[str]** |  | [optional] 

## Example

```python
from ahvac.models.policies_list_acl_policies3_response import PoliciesListAclPolicies3Response

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesListAclPolicies3Response from a JSON string
policies_list_acl_policies3_response_instance = PoliciesListAclPolicies3Response.from_json(json)
# print the JSON string representation of the object
print(PoliciesListAclPolicies3Response.to_json())

# convert the object into a dict
policies_list_acl_policies3_response_dict = policies_list_acl_policies3_response_instance.to_dict()
# create an instance of PoliciesListAclPolicies3Response from a dict
policies_list_acl_policies3_response_from_dict = PoliciesListAclPolicies3Response.from_dict(policies_list_acl_policies3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

