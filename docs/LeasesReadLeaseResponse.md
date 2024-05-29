# LeasesReadLeaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_time** | **datetime** | Optional lease expiry time | [optional] 
**id** | **str** | Lease id | [optional] 
**issue_time** | **datetime** | Timestamp for the lease&#39;s issue time | [optional] 
**last_renewal** | **datetime** | Optional Timestamp of the last time the lease was renewed | [optional] 
**renewable** | **bool** | True if the lease is able to be renewed | [optional] 
**ttl** | **int** | Time to Live set for the lease, returns 0 if unset | [optional] 

## Example

```python
from ahvac.models.leases_read_lease_response import LeasesReadLeaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesReadLeaseResponse from a JSON string
leases_read_lease_response_instance = LeasesReadLeaseResponse.from_json(json)
# print the JSON string representation of the object
print(LeasesReadLeaseResponse.to_json())

# convert the object into a dict
leases_read_lease_response_dict = leases_read_lease_response_instance.to_dict()
# create an instance of LeasesReadLeaseResponse from a dict
leases_read_lease_response_from_dict = LeasesReadLeaseResponse.from_dict(leases_read_lease_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


