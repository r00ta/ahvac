# PoliciesListAclPoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** |  | [optional] 
**policies** | **List[str]** |  | [optional] 

## Example

```python
from ahvac.models.policies_list_acl_policies_response import PoliciesListAclPoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesListAclPoliciesResponse from a JSON string
policies_list_acl_policies_response_instance = PoliciesListAclPoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(PoliciesListAclPoliciesResponse.to_json())

# convert the object into a dict
policies_list_acl_policies_response_dict = policies_list_acl_policies_response_instance.to_dict()
# create an instance of PoliciesListAclPoliciesResponse from a dict
policies_list_acl_policies_response_from_dict = PoliciesListAclPoliciesResponse.from_dict(policies_list_acl_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


