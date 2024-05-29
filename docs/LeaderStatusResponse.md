# LeaderStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_time** | **datetime** |  | [optional] 
**ha_enabled** | **bool** |  | [optional] 
**is_self** | **bool** |  | [optional] 
**last_wal** | **int** |  | [optional] 
**leader_address** | **str** |  | [optional] 
**leader_cluster_address** | **str** |  | [optional] 
**performance_standby** | **bool** |  | [optional] 
**performance_standby_last_remote_wal** | **int** |  | [optional] 
**raft_applied_index** | **int** |  | [optional] 
**raft_committed_index** | **int** |  | [optional] 

## Example

```python
from ahvac.models.leader_status_response import LeaderStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderStatusResponse from a JSON string
leader_status_response_instance = LeaderStatusResponse.from_json(json)
# print the JSON string representation of the object
print(LeaderStatusResponse.to_json())

# convert the object into a dict
leader_status_response_dict = leader_status_response_instance.to_dict()
# create an instance of LeaderStatusResponse from a dict
leader_status_response_from_dict = LeaderStatusResponse.from_dict(leader_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


