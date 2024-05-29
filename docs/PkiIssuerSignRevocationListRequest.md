# PkiIssuerSignRevocationListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl_number** | **int** | The sequence number to be written within the CRL Number extension. | [optional] 
**delta_crl_base_number** | **int** | Using a zero or greater value specifies the base CRL revision number to encode within a Delta CRL indicator extension, otherwise the extension will not be added. | [optional] [default to -1]
**extensions** | **List[object]** | A list of maps containing extensions with keys id (string), critical (bool), value (string) | [optional] 
**format** | **str** | The format of the combined CRL, can be \&quot;pem\&quot; or \&quot;der\&quot;. If \&quot;der\&quot;, the value will be base64 encoded. Defaults to \&quot;pem\&quot;. | [optional] [default to 'pem']
**next_update** | **str** | The amount of time the generated CRL should be valid; defaults to 72 hours. | [optional] [default to '72h']
**revoked_certs** | **List[object]** | A list of maps containing the keys serial_number (string), revocation_time (string), and extensions (map with keys id (string), critical (bool), value (string)) | [optional] 

## Example

```python
from ahvac.models.pki_issuer_sign_revocation_list_request import PkiIssuerSignRevocationListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiIssuerSignRevocationListRequest from a JSON string
pki_issuer_sign_revocation_list_request_instance = PkiIssuerSignRevocationListRequest.from_json(json)
# print the JSON string representation of the object
print(PkiIssuerSignRevocationListRequest.to_json())

# convert the object into a dict
pki_issuer_sign_revocation_list_request_dict = pki_issuer_sign_revocation_list_request_instance.to_dict()
# create an instance of PkiIssuerSignRevocationListRequest from a dict
pki_issuer_sign_revocation_list_request_from_dict = PkiIssuerSignRevocationListRequest.from_dict(pki_issuer_sign_revocation_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


