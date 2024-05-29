# PoliciesWriteAclPolicy2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | The rules of the policy. | [optional] 
**rules** | **str** | The rules of the policy. | [optional] 

## Example

```python
from ahvac.models.policies_write_acl_policy2_request import PoliciesWriteAclPolicy2Request

# TODO update the JSON string below
json = "{}"
# create an instance of PoliciesWriteAclPolicy2Request from a JSON string
policies_write_acl_policy2_request_instance = PoliciesWriteAclPolicy2Request.from_json(json)
# print the JSON string representation of the object
print(PoliciesWriteAclPolicy2Request.to_json())

# convert the object into a dict
policies_write_acl_policy2_request_dict = policies_write_acl_policy2_request_instance.to_dict()
# create an instance of PoliciesWriteAclPolicy2Request from a dict
policies_write_acl_policy2_request_from_dict = PoliciesWriteAclPolicy2Request.from_dict(policies_write_acl_policy2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


