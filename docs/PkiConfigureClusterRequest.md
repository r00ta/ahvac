# PkiConfigureClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aia_path** | **str** | Optional URI to this mount&#39;s AIA distribution point; may refer to an external non-Vault responder. This is for resolving AIA URLs and providing the {{cluster_aia_path}} template parameter and will not be used for other purposes. As such, unlike path above, this could safely be an insecure transit mechanism (like HTTP without TLS). For example: http://cdn.example.com/pr1/pki | [optional] 
**path** | **str** | Canonical URI to this mount on this performance replication cluster&#39;s external address. This is for resolving AIA URLs and providing the {{cluster_path}} template parameter but might be used for other purposes in the future. This should only point back to this particular PR replica and should not ever point to another PR cluster. It may point to any node in the PR replica, including standby nodes, and need not always point to the active node. For example: https://pr1.vault.example.com:8200/v1/pki | [optional] 

## Example

```python
from ahvac.models.pki_configure_cluster_request import PkiConfigureClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureClusterRequest from a JSON string
pki_configure_cluster_request_instance = PkiConfigureClusterRequest.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureClusterRequest.to_json())

# convert the object into a dict
pki_configure_cluster_request_dict = pki_configure_cluster_request_instance.to_dict()
# create an instance of PkiConfigureClusterRequest from a dict
pki_configure_cluster_request_from_dict = PkiConfigureClusterRequest.from_dict(pki_configure_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


