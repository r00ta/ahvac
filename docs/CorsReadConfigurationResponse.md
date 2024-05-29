# CorsReadConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_headers** | **List[str]** |  | [optional] 
**allowed_origins** | **List[str]** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from ahvac.models.cors_read_configuration_response import CorsReadConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorsReadConfigurationResponse from a JSON string
cors_read_configuration_response_instance = CorsReadConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(CorsReadConfigurationResponse.to_json())

# convert the object into a dict
cors_read_configuration_response_dict = cors_read_configuration_response_instance.to_dict()
# create an instance of CorsReadConfigurationResponse from a dict
cors_read_configuration_response_from_dict = CorsReadConfigurationResponse.from_dict(cors_read_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


