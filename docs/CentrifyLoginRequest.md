# CentrifyLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Auth mode (&#39;ro&#39; for resource owner, &#39;cc&#39; for credential client). | [optional] [default to 'ro']
**password** | **str** | Password for this user. | [optional] 
**username** | **str** | Username of the user. | [optional] 

## Example

```python
from ahvac.models.centrify_login_request import CentrifyLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CentrifyLoginRequest from a JSON string
centrify_login_request_instance = CentrifyLoginRequest.from_json(json)
# print the JSON string representation of the object
print(CentrifyLoginRequest.to_json())

# convert the object into a dict
centrify_login_request_dict = centrify_login_request_instance.to_dict()
# create an instance of CentrifyLoginRequest from a dict
centrify_login_request_from_dict = CentrifyLoginRequest.from_dict(centrify_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


