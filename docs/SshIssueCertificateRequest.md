# SshIssueCertificateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_type** | **str** | Type of certificate to be created; either \&quot;user\&quot; or \&quot;host\&quot;. | [optional] [default to 'user']
**critical_options** | **object** | Critical options that the certificate should be signed for. | [optional] 
**extensions** | **object** | Extensions that the certificate should be signed for. | [optional] 
**key_bits** | **int** | Specifies the number of bits to use for the generated keys. | [optional] [default to 0]
**key_id** | **str** | Key id that the created certificate should have. If not specified, the display name of the token will be used. | [optional] 
**key_type** | **str** | Specifies the desired key type; must be &#x60;rsa&#x60;, &#x60;ed25519&#x60; or &#x60;ec&#x60; | [optional] [default to 'rsa']
**ttl** | **str** | The requested Time To Live for the SSH certificate; sets the expiration date. If not specified the role default, backend default, or system default TTL is used, in that order. Cannot be later than the role max TTL. | [optional] 
**valid_principals** | **str** | Valid principals, either usernames or hostnames, that the certificate should be signed for. | [optional] 

## Example

```python
from ahvac.models.ssh_issue_certificate_request import SshIssueCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SshIssueCertificateRequest from a JSON string
ssh_issue_certificate_request_instance = SshIssueCertificateRequest.from_json(json)
# print the JSON string representation of the object
print(SshIssueCertificateRequest.to_json())

# convert the object into a dict
ssh_issue_certificate_request_dict = ssh_issue_certificate_request_instance.to_dict()
# create an instance of SshIssueCertificateRequest from a dict
ssh_issue_certificate_request_from_dict = SshIssueCertificateRequest.from_dict(ssh_issue_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


