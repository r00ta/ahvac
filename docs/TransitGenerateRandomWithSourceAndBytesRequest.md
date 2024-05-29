# TransitGenerateRandomWithSourceAndBytesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **int** | The number of bytes to generate (POST body parameter). Defaults to 32 (256 bits). | [optional] [default to 32]
**format** | **str** | Encoding format to use. Can be \&quot;hex\&quot; or \&quot;base64\&quot;. Defaults to \&quot;base64\&quot;. | [optional] [default to 'base64']

## Example

```python
from ahvac.models.transit_generate_random_with_source_and_bytes_request import TransitGenerateRandomWithSourceAndBytesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransitGenerateRandomWithSourceAndBytesRequest from a JSON string
transit_generate_random_with_source_and_bytes_request_instance = TransitGenerateRandomWithSourceAndBytesRequest.from_json(json)
# print the JSON string representation of the object
print(TransitGenerateRandomWithSourceAndBytesRequest.to_json())

# convert the object into a dict
transit_generate_random_with_source_and_bytes_request_dict = transit_generate_random_with_source_and_bytes_request_instance.to_dict()
# create an instance of TransitGenerateRandomWithSourceAndBytesRequest from a dict
transit_generate_random_with_source_and_bytes_request_from_dict = TransitGenerateRandomWithSourceAndBytesRequest.from_dict(transit_generate_random_with_source_and_bytes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


