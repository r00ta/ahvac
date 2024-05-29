# LeasesReadLeaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_id** | **str** | The lease identifier to renew. This is included with a lease. | [optional] 

## Example

```python
from ahvac.models.leases_read_lease_request import LeasesReadLeaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesReadLeaseRequest from a JSON string
leases_read_lease_request_instance = LeasesReadLeaseRequest.from_json(json)
# print the JSON string representation of the object
print(LeasesReadLeaseRequest.to_json())

# convert the object into a dict
leases_read_lease_request_dict = leases_read_lease_request_instance.to_dict()
# create an instance of LeasesReadLeaseRequest from a dict
leases_read_lease_request_from_dict = LeasesReadLeaseRequest.from_dict(leases_read_lease_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


