# NomadConfigureLeaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_ttl** | **str** | Duration after which the issued token should not be allowed to be renewed | [optional] 
**ttl** | **str** | Duration before which the issued token needs renewal | [optional] 

## Example

```python
from ahvac.models.nomad_configure_lease_request import NomadConfigureLeaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomadConfigureLeaseRequest from a JSON string
nomad_configure_lease_request_instance = NomadConfigureLeaseRequest.from_json(json)
# print the JSON string representation of the object
print(NomadConfigureLeaseRequest.to_json())

# convert the object into a dict
nomad_configure_lease_request_dict = nomad_configure_lease_request_instance.to_dict()
# create an instance of NomadConfigureLeaseRequest from a dict
nomad_configure_lease_request_from_dict = NomadConfigureLeaseRequest.from_dict(nomad_configure_lease_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


