# TokenCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Name to associate with this token | [optional] 
**entity_alias** | **str** | Name of the entity alias to associate with this token | [optional] 
**explicit_max_ttl** | **str** | Explicit Max TTL of this token | [optional] 
**id** | **str** | Value for the token | [optional] 
**lease** | **str** | Use &#39;ttl&#39; instead | [optional] 
**meta** | **object** | Arbitrary key&#x3D;value metadata to associate with the token | [optional] 
**no_default_policy** | **bool** | Do not include default policy for this token | [optional] 
**no_parent** | **bool** | Create the token with no parent | [optional] 
**num_uses** | **int** | Max number of uses for this token | [optional] 
**period** | **str** | Renew period | [optional] 
**policies** | **List[str]** | List of policies for the token | [optional] 
**renewable** | **bool** | Allow token to be renewed past its initial TTL up to system/mount maximum TTL | [optional] [default to True]
**ttl** | **str** | Time to live for this token | [optional] 
**type** | **str** | Token type | [optional] 

## Example

```python
from ahvac.models.token_create_request import TokenCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCreateRequest from a JSON string
token_create_request_instance = TokenCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TokenCreateRequest.to_json())

# convert the object into a dict
token_create_request_dict = token_create_request_instance.to_dict()
# create an instance of TokenCreateRequest from a dict
token_create_request_from_dict = TokenCreateRequest.from_dict(token_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


