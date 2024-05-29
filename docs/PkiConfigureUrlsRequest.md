# PkiConfigureUrlsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl_distribution_points** | **List[str]** | Comma-separated list of URLs to be used for the CRL distribution points attribute. See also RFC 5280 Section 4.2.1.13. | [optional] 
**enable_templating** | **bool** | Whether or not to enabling templating of the above AIA fields. When templating is enabled the special values &#39;{{issuer_id}}&#39;, &#39;{{cluster_path}}&#39;, and &#39;{{cluster_aia_path}}&#39; are available, but the addresses are not checked for URI validity until issuance time. Using &#39;{{cluster_path}}&#39; requires /config/cluster&#39;s &#39;path&#39; member to be set on all PR Secondary clusters and using &#39;{{cluster_aia_path}}&#39; requires /config/cluster&#39;s &#39;aia_path&#39; member to be set on all PR secondary clusters. | [optional] [default to False]
**issuing_certificates** | **List[str]** | Comma-separated list of URLs to be used for the issuing certificate attribute. See also RFC 5280 Section 4.2.2.1. | [optional] 
**ocsp_servers** | **List[str]** | Comma-separated list of URLs to be used for the OCSP servers attribute. See also RFC 5280 Section 4.2.2.1. | [optional] 

## Example

```python
from ahvac.models.pki_configure_urls_request import PkiConfigureUrlsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkiConfigureUrlsRequest from a JSON string
pki_configure_urls_request_instance = PkiConfigureUrlsRequest.from_json(json)
# print the JSON string representation of the object
print(PkiConfigureUrlsRequest.to_json())

# convert the object into a dict
pki_configure_urls_request_dict = pki_configure_urls_request_instance.to_dict()
# create an instance of PkiConfigureUrlsRequest from a dict
pki_configure_urls_request_from_dict = PkiConfigureUrlsRequest.from_dict(pki_configure_urls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


