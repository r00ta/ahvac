# GenerateRandomWithSourceAndBytesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **int** | The number of bytes to generate (POST body parameter). Defaults to 32 (256 bits). | [optional] [default to 32]
**format** | **str** | Encoding format to use. Can be \&quot;hex\&quot; or \&quot;base64\&quot;. Defaults to \&quot;base64\&quot;. | [optional] [default to 'base64']

## Example

```python
from ahvac.models.generate_random_with_source_and_bytes_request import GenerateRandomWithSourceAndBytesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateRandomWithSourceAndBytesRequest from a JSON string
generate_random_with_source_and_bytes_request_instance = GenerateRandomWithSourceAndBytesRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateRandomWithSourceAndBytesRequest.to_json())

# convert the object into a dict
generate_random_with_source_and_bytes_request_dict = generate_random_with_source_and_bytes_request_instance.to_dict()
# create an instance of GenerateRandomWithSourceAndBytesRequest from a dict
generate_random_with_source_and_bytes_request_from_dict = GenerateRandomWithSourceAndBytesRequest.from_dict(generate_random_with_source_and_bytes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


