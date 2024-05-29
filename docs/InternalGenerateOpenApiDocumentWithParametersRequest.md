# InternalGenerateOpenApiDocumentWithParametersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Context string appended to every operationId | [optional] 
**generic_mount_paths** | **bool** | Use generic mount paths | [optional] [default to False]

## Example

```python
from ahvac.models.internal_generate_open_api_document_with_parameters_request import InternalGenerateOpenApiDocumentWithParametersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalGenerateOpenApiDocumentWithParametersRequest from a JSON string
internal_generate_open_api_document_with_parameters_request_instance = InternalGenerateOpenApiDocumentWithParametersRequest.from_json(json)
# print the JSON string representation of the object
print(InternalGenerateOpenApiDocumentWithParametersRequest.to_json())

# convert the object into a dict
internal_generate_open_api_document_with_parameters_request_dict = internal_generate_open_api_document_with_parameters_request_instance.to_dict()
# create an instance of InternalGenerateOpenApiDocumentWithParametersRequest from a dict
internal_generate_open_api_document_with_parameters_request_from_dict = InternalGenerateOpenApiDocumentWithParametersRequest.from_dict(internal_generate_open_api_document_with_parameters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


