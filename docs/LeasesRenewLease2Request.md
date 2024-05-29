# LeasesRenewLease2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**increment** | **str** | The desired increment in seconds to the lease | [optional] 
**lease_id** | **str** | The lease identifier to renew. This is included with a lease. | [optional] 

## Example

```python
from ahvac.models.leases_renew_lease2_request import LeasesRenewLease2Request

# TODO update the JSON string below
json = "{}"
# create an instance of LeasesRenewLease2Request from a JSON string
leases_renew_lease2_request_instance = LeasesRenewLease2Request.from_json(json)
# print the JSON string representation of the object
print(LeasesRenewLease2Request.to_json())

# convert the object into a dict
leases_renew_lease2_request_dict = leases_renew_lease2_request_instance.to_dict()
# create an instance of LeasesRenewLease2Request from a dict
leases_renew_lease2_request_from_dict = LeasesRenewLease2Request.from_dict(leases_renew_lease2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


