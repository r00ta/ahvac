# PkiConfigureUrlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl_distribution_points** | **List[str]** | Comma-separated list of URLs to be used for the CRL distribution points attribute. See also RFC 5280 Section 4.2.1.13. | [optional] 
**enable_templating** | **bool** | Whether or not to enabling templating of the above AIA fields. When templating is enabled the special values &#39;{{issuer_id}}&#39; and &#39;{{cluster_path}}&#39; are available, but the addresses are not checked for URI validity until issuance time. This requires /config/cluster&#39;s path to be set on all PR Secondary clusters. | [optional] [default to False]
**issuing_certificates** | **List[str]** | Comma-separated list of URLs to be used for the issuing certificate attribute. See also RFC 5280 Section 4.2.2.1. | [optional] 
**ocsp_servers** | **List[str]** | Comma-separated list of URLs to be used for the OCSP servers attribute. See also RFC 5280 Section 4.2.2.1. | [optional] 

## Example

```python
from ahvac.models.pki_configure_urls_response import PkiConfigureUrlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureUrlsResponse from a JSON string
pki_configure_urls_response_instance = PkiConfigureUrlsResponse.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureUrlsResponse.to_json())

# convert the object into a dict
pki_configure_urls_response_dict = pki_configure_urls_response_instance.to_dict()
# create an instance of PkiConfigureUrlsResponse from a dict
pki_configure_urls_response_from_dict = PkiConfigureUrlsResponse.from_dict(pki_configure_urls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


