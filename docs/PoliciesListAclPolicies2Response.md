# PoliciesListAclPolicies2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** |  | [optional] 
**policies** | **List[str]** |  | [optional] 

## Example

```python
from ahvac.models.policies_list_acl_policies2_response import PoliciesListAclPolicies2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesListAclPolicies2Response from a JSON string
policies_list_acl_policies2_response_instance = PoliciesListAclPolicies2Response.from_json(json)
# print the JSON string representation of the object
print(PoliciesListAclPolicies2Response.to_json())

# convert the object into a dict
policies_list_acl_policies2_response_dict = policies_list_acl_policies2_response_instance.to_dict()
# create an instance of PoliciesListAclPolicies2Response from a dict
policies_list_acl_policies2_response_from_dict = PoliciesListAclPolicies2Response.from_dict(policies_list_acl_policies2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


