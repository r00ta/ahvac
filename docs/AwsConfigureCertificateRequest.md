# AwsConfigureCertificateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_public_cert** | **str** | Base64 encoded AWS Public cert required to verify PKCS7 signature of the EC2 instance metadata. | [optional] 
**type** | **str** | Takes the value of either \&quot;pkcs7\&quot; or \&quot;identity\&quot;, indicating the type of document which can be verified using the given certificate. The reason is that the PKCS#7 document will have a DSA digest and the identity signature will have an RSA signature, and accordingly the public certificates to verify those also vary. Defaults to \&quot;pkcs7\&quot;. | [optional] [default to 'pkcs7']

## Example

```python
from ahvac.models.aws_configure_certificate_request import AwsConfigureCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsConfigureCertificateRequest from a JSON string
aws_configure_certificate_request_instance = AwsConfigureCertificateRequest.from_json(json)
# print the JSON string representation of the object
print(AwsConfigureCertificateRequest.to_json())

# convert the object into a dict
aws_configure_certificate_request_dict = aws_configure_certificate_request_instance.to_dict()
# create an instance of AwsConfigureCertificateRequest from a dict
aws_configure_certificate_request_from_dict = AwsConfigureCertificateRequest.from_dict(aws_configure_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


