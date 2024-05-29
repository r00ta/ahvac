# LeasesRevokeLeaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_id** | **str** | The lease identifier to renew. This is included with a lease. | [optional] 
**sync** | **bool** | Whether or not to perform the revocation synchronously | [optional] [default to True]

## Example

```python
from ahvac.models.leases_revoke_lease_request import LeasesRevokeLeaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesRevokeLeaseRequest from a JSON string
leases_revoke_lease_request_instance = LeasesRevokeLeaseRequest.from_json(json)
# print the JSON string representation of the object
print(LeasesRevokeLeaseRequest.to_json())

# convert the object into a dict
leases_revoke_lease_request_dict = leases_revoke_lease_request_instance.to_dict()
# create an instance of LeasesRevokeLeaseRequest from a dict
leases_revoke_lease_request_from_dict = LeasesRevokeLeaseRequest.from_dict(leases_revoke_lease_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


