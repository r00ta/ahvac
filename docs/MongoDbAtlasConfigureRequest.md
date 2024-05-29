# MongoDbAtlasConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** | MongoDB Atlas Programmatic Private Key | 
**public_key** | **str** | MongoDB Atlas Programmatic Public Key | 

## Example

```python
from ahvac.models.mongo_db_atlas_configure_request import MongoDbAtlasConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDbAtlasConfigureRequest from a JSON string
mongo_db_atlas_configure_request_instance = MongoDbAtlasConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(MongoDbAtlasConfigureRequest.to_json())

# convert the object into a dict
mongo_db_atlas_configure_request_dict = mongo_db_atlas_configure_request_instance.to_dict()
# create an instance of MongoDbAtlasConfigureRequest from a dict
mongo_db_atlas_configure_request_from_dict = MongoDbAtlasConfigureRequest.from_dict(mongo_db_atlas_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


