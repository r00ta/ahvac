# ahvac.SecretsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ali_cloud_configure**](SecretsApi.md#ali_cloud_configure) | **POST** /{alicloud_mount_path}/config | 
[**ali_cloud_delete_configuration**](SecretsApi.md#ali_cloud_delete_configuration) | **DELETE** /{alicloud_mount_path}/config | 
[**ali_cloud_delete_role**](SecretsApi.md#ali_cloud_delete_role) | **DELETE** /{alicloud_mount_path}/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**ali_cloud_generate_credentials**](SecretsApi.md#ali_cloud_generate_credentials) | **GET** /{alicloud_mount_path}/creds/{name} | Generate an API key or STS credential using the given role&#39;s configuration.&#39;
[**ali_cloud_list_roles**](SecretsApi.md#ali_cloud_list_roles) | **GET** /{alicloud_mount_path}/role/ | List the existing roles in this backend.
[**ali_cloud_read_configuration**](SecretsApi.md#ali_cloud_read_configuration) | **GET** /{alicloud_mount_path}/config | 
[**ali_cloud_read_role**](SecretsApi.md#ali_cloud_read_role) | **GET** /{alicloud_mount_path}/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**ali_cloud_write_role**](SecretsApi.md#ali_cloud_write_role) | **POST** /{alicloud_mount_path}/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**aws_configure_lease**](SecretsApi.md#aws_configure_lease) | **POST** /{aws_mount_path}/config/lease | 
[**aws_configure_root_iam_credentials**](SecretsApi.md#aws_configure_root_iam_credentials) | **POST** /{aws_mount_path}/config/root | 
[**aws_delete_role**](SecretsApi.md#aws_delete_role) | **DELETE** /{aws_mount_path}/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**aws_delete_static_roles_name**](SecretsApi.md#aws_delete_static_roles_name) | **DELETE** /{aws_mount_path}/static-roles/{name} | 
[**aws_generate_credentials**](SecretsApi.md#aws_generate_credentials) | **GET** /{aws_mount_path}/creds/{name} | 
[**aws_generate_credentials_with_parameters**](SecretsApi.md#aws_generate_credentials_with_parameters) | **POST** /{aws_mount_path}/creds/{name} | 
[**aws_generate_sts_credentials**](SecretsApi.md#aws_generate_sts_credentials) | **GET** /{aws_mount_path}/sts/{name} | 
[**aws_generate_sts_credentials_with_parameters**](SecretsApi.md#aws_generate_sts_credentials_with_parameters) | **POST** /{aws_mount_path}/sts/{name} | 
[**aws_list_roles**](SecretsApi.md#aws_list_roles) | **GET** /{aws_mount_path}/roles/ | List the existing roles in this backend
[**aws_read_lease_configuration**](SecretsApi.md#aws_read_lease_configuration) | **GET** /{aws_mount_path}/config/lease | 
[**aws_read_role**](SecretsApi.md#aws_read_role) | **GET** /{aws_mount_path}/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**aws_read_root_iam_credentials_configuration**](SecretsApi.md#aws_read_root_iam_credentials_configuration) | **GET** /{aws_mount_path}/config/root | 
[**aws_read_static_creds_name**](SecretsApi.md#aws_read_static_creds_name) | **GET** /{aws_mount_path}/static-creds/{name} | 
[**aws_read_static_roles_name**](SecretsApi.md#aws_read_static_roles_name) | **GET** /{aws_mount_path}/static-roles/{name} | 
[**aws_rotate_root_iam_credentials**](SecretsApi.md#aws_rotate_root_iam_credentials) | **POST** /{aws_mount_path}/config/rotate-root | 
[**aws_write_role**](SecretsApi.md#aws_write_role) | **POST** /{aws_mount_path}/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**aws_write_static_roles_name**](SecretsApi.md#aws_write_static_roles_name) | **POST** /{aws_mount_path}/static-roles/{name} | 
[**azure_configure**](SecretsApi.md#azure_configure) | **POST** /{azure_mount_path}/config | 
[**azure_delete_configuration**](SecretsApi.md#azure_delete_configuration) | **DELETE** /{azure_mount_path}/config | 
[**azure_delete_role**](SecretsApi.md#azure_delete_role) | **DELETE** /{azure_mount_path}/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**azure_list_roles**](SecretsApi.md#azure_list_roles) | **GET** /{azure_mount_path}/roles/ | List existing roles.
[**azure_read_configuration**](SecretsApi.md#azure_read_configuration) | **GET** /{azure_mount_path}/config | 
[**azure_read_role**](SecretsApi.md#azure_read_role) | **GET** /{azure_mount_path}/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**azure_request_service_principal_credentials**](SecretsApi.md#azure_request_service_principal_credentials) | **GET** /{azure_mount_path}/creds/{role} | 
[**azure_rotate_root**](SecretsApi.md#azure_rotate_root) | **POST** /{azure_mount_path}/rotate-root | 
[**azure_write_role**](SecretsApi.md#azure_write_role) | **POST** /{azure_mount_path}/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**consul_configure_access**](SecretsApi.md#consul_configure_access) | **POST** /{consul_mount_path}/config/access | 
[**consul_delete_role**](SecretsApi.md#consul_delete_role) | **DELETE** /{consul_mount_path}/roles/{name} | 
[**consul_generate_credentials**](SecretsApi.md#consul_generate_credentials) | **GET** /{consul_mount_path}/creds/{role} | 
[**consul_list_roles**](SecretsApi.md#consul_list_roles) | **GET** /{consul_mount_path}/roles/ | 
[**consul_read_access_configuration**](SecretsApi.md#consul_read_access_configuration) | **GET** /{consul_mount_path}/config/access | 
[**consul_read_role**](SecretsApi.md#consul_read_role) | **GET** /{consul_mount_path}/roles/{name} | 
[**consul_write_role**](SecretsApi.md#consul_write_role) | **POST** /{consul_mount_path}/roles/{name} | 
[**cubbyhole_delete**](SecretsApi.md#cubbyhole_delete) | **DELETE** /cubbyhole/{path} | Deletes the secret at the specified location.
[**cubbyhole_list**](SecretsApi.md#cubbyhole_list) | **GET** /cubbyhole/{path}/ | List secret entries at the specified location.
[**cubbyhole_read**](SecretsApi.md#cubbyhole_read) | **GET** /cubbyhole/{path} | Retrieve the secret at the specified location.
[**cubbyhole_write**](SecretsApi.md#cubbyhole_write) | **POST** /cubbyhole/{path} | Store a secret at the specified location.
[**database_configure_connection**](SecretsApi.md#database_configure_connection) | **POST** /{database_mount_path}/config/{name} | 
[**database_delete_connection_configuration**](SecretsApi.md#database_delete_connection_configuration) | **DELETE** /{database_mount_path}/config/{name} | 
[**database_delete_role**](SecretsApi.md#database_delete_role) | **DELETE** /{database_mount_path}/roles/{name} | Manage the roles that can be created with this backend.
[**database_delete_static_role**](SecretsApi.md#database_delete_static_role) | **DELETE** /{database_mount_path}/static-roles/{name} | Manage the static roles that can be created with this backend.
[**database_generate_credentials**](SecretsApi.md#database_generate_credentials) | **GET** /{database_mount_path}/creds/{name} | Request database credentials for a certain role.
[**database_list_connections**](SecretsApi.md#database_list_connections) | **GET** /{database_mount_path}/config/ | Configure connection details to a database plugin.
[**database_list_roles**](SecretsApi.md#database_list_roles) | **GET** /{database_mount_path}/roles/ | Manage the roles that can be created with this backend.
[**database_list_static_roles**](SecretsApi.md#database_list_static_roles) | **GET** /{database_mount_path}/static-roles/ | Manage the static roles that can be created with this backend.
[**database_read_connection_configuration**](SecretsApi.md#database_read_connection_configuration) | **GET** /{database_mount_path}/config/{name} | 
[**database_read_role**](SecretsApi.md#database_read_role) | **GET** /{database_mount_path}/roles/{name} | Manage the roles that can be created with this backend.
[**database_read_static_role**](SecretsApi.md#database_read_static_role) | **GET** /{database_mount_path}/static-roles/{name} | Manage the static roles that can be created with this backend.
[**database_read_static_role_credentials**](SecretsApi.md#database_read_static_role_credentials) | **GET** /{database_mount_path}/static-creds/{name} | Request database credentials for a certain static role. These credentials are rotated periodically.
[**database_reset_connection**](SecretsApi.md#database_reset_connection) | **POST** /{database_mount_path}/reset/{name} | Resets a database plugin.
[**database_rotate_root_credentials**](SecretsApi.md#database_rotate_root_credentials) | **POST** /{database_mount_path}/rotate-root/{name} | 
[**database_rotate_static_role_credentials**](SecretsApi.md#database_rotate_static_role_credentials) | **POST** /{database_mount_path}/rotate-role/{name} | 
[**database_write_role**](SecretsApi.md#database_write_role) | **POST** /{database_mount_path}/roles/{name} | Manage the roles that can be created with this backend.
[**database_write_static_role**](SecretsApi.md#database_write_static_role) | **POST** /{database_mount_path}/static-roles/{name} | Manage the static roles that can be created with this backend.
[**google_cloud_configure**](SecretsApi.md#google_cloud_configure) | **POST** /{gcp_mount_path}/config | 
[**google_cloud_delete_impersonated_account**](SecretsApi.md#google_cloud_delete_impersonated_account) | **DELETE** /{gcp_mount_path}/impersonated-account/{name} | 
[**google_cloud_delete_roleset**](SecretsApi.md#google_cloud_delete_roleset) | **DELETE** /{gcp_mount_path}/roleset/{name} | 
[**google_cloud_delete_static_account**](SecretsApi.md#google_cloud_delete_static_account) | **DELETE** /{gcp_mount_path}/static-account/{name} | 
[**google_cloud_generate_impersonated_account_access_token**](SecretsApi.md#google_cloud_generate_impersonated_account_access_token) | **GET** /{gcp_mount_path}/impersonated-account/{name}/token | 
[**google_cloud_generate_impersonated_account_access_token2**](SecretsApi.md#google_cloud_generate_impersonated_account_access_token2) | **POST** /{gcp_mount_path}/impersonated-account/{name}/token | 
[**google_cloud_generate_roleset_access_token**](SecretsApi.md#google_cloud_generate_roleset_access_token) | **POST** /{gcp_mount_path}/roleset/{roleset}/token | 
[**google_cloud_generate_roleset_access_token2**](SecretsApi.md#google_cloud_generate_roleset_access_token2) | **GET** /{gcp_mount_path}/roleset/{roleset}/token | 
[**google_cloud_generate_roleset_access_token3**](SecretsApi.md#google_cloud_generate_roleset_access_token3) | **POST** /{gcp_mount_path}/token/{roleset} | 
[**google_cloud_generate_roleset_access_token4**](SecretsApi.md#google_cloud_generate_roleset_access_token4) | **GET** /{gcp_mount_path}/token/{roleset} | 
[**google_cloud_generate_roleset_key**](SecretsApi.md#google_cloud_generate_roleset_key) | **POST** /{gcp_mount_path}/roleset/{roleset}/key | 
[**google_cloud_generate_roleset_key2**](SecretsApi.md#google_cloud_generate_roleset_key2) | **GET** /{gcp_mount_path}/roleset/{roleset}/key | 
[**google_cloud_generate_roleset_key3**](SecretsApi.md#google_cloud_generate_roleset_key3) | **POST** /{gcp_mount_path}/key/{roleset} | 
[**google_cloud_generate_roleset_key4**](SecretsApi.md#google_cloud_generate_roleset_key4) | **GET** /{gcp_mount_path}/key/{roleset} | 
[**google_cloud_generate_static_account_access_token**](SecretsApi.md#google_cloud_generate_static_account_access_token) | **POST** /{gcp_mount_path}/static-account/{name}/token | 
[**google_cloud_generate_static_account_access_token2**](SecretsApi.md#google_cloud_generate_static_account_access_token2) | **GET** /{gcp_mount_path}/static-account/{name}/token | 
[**google_cloud_generate_static_account_key**](SecretsApi.md#google_cloud_generate_static_account_key) | **POST** /{gcp_mount_path}/static-account/{name}/key | 
[**google_cloud_generate_static_account_key2**](SecretsApi.md#google_cloud_generate_static_account_key2) | **GET** /{gcp_mount_path}/static-account/{name}/key | 
[**google_cloud_kms_configure**](SecretsApi.md#google_cloud_kms_configure) | **POST** /{gcpkms_mount_path}/config | 
[**google_cloud_kms_configure_key**](SecretsApi.md#google_cloud_kms_configure_key) | **POST** /{gcpkms_mount_path}/keys/config/{key} | 
[**google_cloud_kms_decrypt**](SecretsApi.md#google_cloud_kms_decrypt) | **POST** /{gcpkms_mount_path}/decrypt/{key} | Decrypt a ciphertext value using a named key
[**google_cloud_kms_delete_configuration**](SecretsApi.md#google_cloud_kms_delete_configuration) | **DELETE** /{gcpkms_mount_path}/config | 
[**google_cloud_kms_delete_key**](SecretsApi.md#google_cloud_kms_delete_key) | **DELETE** /{gcpkms_mount_path}/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**google_cloud_kms_deregister_key**](SecretsApi.md#google_cloud_kms_deregister_key) | **POST** /{gcpkms_mount_path}/keys/deregister/{key} | 
[**google_cloud_kms_deregister_key2**](SecretsApi.md#google_cloud_kms_deregister_key2) | **DELETE** /{gcpkms_mount_path}/keys/deregister/{key} | 
[**google_cloud_kms_encrypt**](SecretsApi.md#google_cloud_kms_encrypt) | **POST** /{gcpkms_mount_path}/encrypt/{key} | Encrypt a plaintext value using a named key
[**google_cloud_kms_list_keys**](SecretsApi.md#google_cloud_kms_list_keys) | **GET** /{gcpkms_mount_path}/keys/ | List named keys
[**google_cloud_kms_read_configuration**](SecretsApi.md#google_cloud_kms_read_configuration) | **GET** /{gcpkms_mount_path}/config | 
[**google_cloud_kms_read_key**](SecretsApi.md#google_cloud_kms_read_key) | **GET** /{gcpkms_mount_path}/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**google_cloud_kms_read_key_configuration**](SecretsApi.md#google_cloud_kms_read_key_configuration) | **GET** /{gcpkms_mount_path}/keys/config/{key} | 
[**google_cloud_kms_reencrypt**](SecretsApi.md#google_cloud_kms_reencrypt) | **POST** /{gcpkms_mount_path}/reencrypt/{key} | Re-encrypt existing ciphertext data to a new version
[**google_cloud_kms_register_key**](SecretsApi.md#google_cloud_kms_register_key) | **POST** /{gcpkms_mount_path}/keys/register/{key} | Register an existing crypto key in Google Cloud KMS
[**google_cloud_kms_retrieve_public_key**](SecretsApi.md#google_cloud_kms_retrieve_public_key) | **GET** /{gcpkms_mount_path}/pubkey/{key} | Retrieve the public key associated with the named key
[**google_cloud_kms_rotate_key**](SecretsApi.md#google_cloud_kms_rotate_key) | **POST** /{gcpkms_mount_path}/keys/rotate/{key} | Rotate a crypto key to a new primary version
[**google_cloud_kms_sign**](SecretsApi.md#google_cloud_kms_sign) | **POST** /{gcpkms_mount_path}/sign/{key} | Signs a message or digest using a named key
[**google_cloud_kms_trim_key_versions**](SecretsApi.md#google_cloud_kms_trim_key_versions) | **POST** /{gcpkms_mount_path}/keys/trim/{key} | 
[**google_cloud_kms_trim_key_versions2**](SecretsApi.md#google_cloud_kms_trim_key_versions2) | **DELETE** /{gcpkms_mount_path}/keys/trim/{key} | 
[**google_cloud_kms_verify**](SecretsApi.md#google_cloud_kms_verify) | **POST** /{gcpkms_mount_path}/verify/{key} | Verify a signature using a named key
[**google_cloud_kms_write_key**](SecretsApi.md#google_cloud_kms_write_key) | **POST** /{gcpkms_mount_path}/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**google_cloud_list_impersonated_accounts**](SecretsApi.md#google_cloud_list_impersonated_accounts) | **GET** /{gcp_mount_path}/impersonated-account/ | 
[**google_cloud_list_impersonated_accounts2**](SecretsApi.md#google_cloud_list_impersonated_accounts2) | **GET** /{gcp_mount_path}/impersonated-accounts/ | 
[**google_cloud_list_rolesets**](SecretsApi.md#google_cloud_list_rolesets) | **GET** /{gcp_mount_path}/roleset/ | 
[**google_cloud_list_rolesets2**](SecretsApi.md#google_cloud_list_rolesets2) | **GET** /{gcp_mount_path}/rolesets/ | 
[**google_cloud_list_static_accounts**](SecretsApi.md#google_cloud_list_static_accounts) | **GET** /{gcp_mount_path}/static-account/ | 
[**google_cloud_list_static_accounts2**](SecretsApi.md#google_cloud_list_static_accounts2) | **GET** /{gcp_mount_path}/static-accounts/ | 
[**google_cloud_read_configuration**](SecretsApi.md#google_cloud_read_configuration) | **GET** /{gcp_mount_path}/config | 
[**google_cloud_read_impersonated_account**](SecretsApi.md#google_cloud_read_impersonated_account) | **GET** /{gcp_mount_path}/impersonated-account/{name} | 
[**google_cloud_read_roleset**](SecretsApi.md#google_cloud_read_roleset) | **GET** /{gcp_mount_path}/roleset/{name} | 
[**google_cloud_read_static_account**](SecretsApi.md#google_cloud_read_static_account) | **GET** /{gcp_mount_path}/static-account/{name} | 
[**google_cloud_rotate_roleset**](SecretsApi.md#google_cloud_rotate_roleset) | **POST** /{gcp_mount_path}/roleset/{name}/rotate | 
[**google_cloud_rotate_roleset_key**](SecretsApi.md#google_cloud_rotate_roleset_key) | **POST** /{gcp_mount_path}/roleset/{name}/rotate-key | 
[**google_cloud_rotate_root_credentials**](SecretsApi.md#google_cloud_rotate_root_credentials) | **POST** /{gcp_mount_path}/config/rotate-root | 
[**google_cloud_rotate_static_account_key**](SecretsApi.md#google_cloud_rotate_static_account_key) | **POST** /{gcp_mount_path}/static-account/{name}/rotate-key | 
[**google_cloud_write_impersonated_account**](SecretsApi.md#google_cloud_write_impersonated_account) | **POST** /{gcp_mount_path}/impersonated-account/{name} | 
[**google_cloud_write_roleset**](SecretsApi.md#google_cloud_write_roleset) | **POST** /{gcp_mount_path}/roleset/{name} | 
[**google_cloud_write_static_account**](SecretsApi.md#google_cloud_write_static_account) | **POST** /{gcp_mount_path}/static-account/{name} | 
[**kubernetes_check_configuration**](SecretsApi.md#kubernetes_check_configuration) | **GET** /{kubernetes_mount_path}/check | 
[**kubernetes_configure**](SecretsApi.md#kubernetes_configure) | **POST** /{kubernetes_mount_path}/config | 
[**kubernetes_delete_configuration**](SecretsApi.md#kubernetes_delete_configuration) | **DELETE** /{kubernetes_mount_path}/config | 
[**kubernetes_delete_role**](SecretsApi.md#kubernetes_delete_role) | **DELETE** /{kubernetes_mount_path}/roles/{name} | 
[**kubernetes_generate_credentials**](SecretsApi.md#kubernetes_generate_credentials) | **POST** /{kubernetes_mount_path}/creds/{name} | 
[**kubernetes_list_roles**](SecretsApi.md#kubernetes_list_roles) | **GET** /{kubernetes_mount_path}/roles/ | 
[**kubernetes_read_configuration**](SecretsApi.md#kubernetes_read_configuration) | **GET** /{kubernetes_mount_path}/config | 
[**kubernetes_read_role**](SecretsApi.md#kubernetes_read_role) | **GET** /{kubernetes_mount_path}/roles/{name} | 
[**kubernetes_write_role**](SecretsApi.md#kubernetes_write_role) | **POST** /{kubernetes_mount_path}/roles/{name} | 
[**kv_v1_delete**](SecretsApi.md#kv_v1_delete) | **DELETE** /{kv_v1_mount_path}/{path} | 
[**kv_v1_list**](SecretsApi.md#kv_v1_list) | **GET** /{kv_v1_mount_path}/{path}/ | 
[**kv_v1_read**](SecretsApi.md#kv_v1_read) | **GET** /{kv_v1_mount_path}/{path} | 
[**kv_v1_write**](SecretsApi.md#kv_v1_write) | **POST** /{kv_v1_mount_path}/{path} | 
[**kv_v2_configure**](SecretsApi.md#kv_v2_configure) | **POST** /{kv_v2_mount_path}/config | Configure backend level settings that are applied to every key in the key-value store.
[**kv_v2_delete**](SecretsApi.md#kv_v2_delete) | **DELETE** /{kv_v2_mount_path}/data/{path} | 
[**kv_v2_delete_metadata_and_all_versions**](SecretsApi.md#kv_v2_delete_metadata_and_all_versions) | **DELETE** /{kv_v2_mount_path}/metadata/{path} | 
[**kv_v2_delete_versions**](SecretsApi.md#kv_v2_delete_versions) | **POST** /{kv_v2_mount_path}/delete/{path} | 
[**kv_v2_destroy_versions**](SecretsApi.md#kv_v2_destroy_versions) | **POST** /{kv_v2_mount_path}/destroy/{path} | 
[**kv_v2_list**](SecretsApi.md#kv_v2_list) | **GET** /{kv_v2_mount_path}/metadata/{path}/ | 
[**kv_v2_read**](SecretsApi.md#kv_v2_read) | **GET** /{kv_v2_mount_path}/data/{path} | 
[**kv_v2_read_configuration**](SecretsApi.md#kv_v2_read_configuration) | **GET** /{kv_v2_mount_path}/config | Read the backend level settings.
[**kv_v2_read_metadata**](SecretsApi.md#kv_v2_read_metadata) | **GET** /{kv_v2_mount_path}/metadata/{path} | 
[**kv_v2_read_subkeys**](SecretsApi.md#kv_v2_read_subkeys) | **GET** /{kv_v2_mount_path}/subkeys/{path} | 
[**kv_v2_undelete_versions**](SecretsApi.md#kv_v2_undelete_versions) | **POST** /{kv_v2_mount_path}/undelete/{path} | 
[**kv_v2_write**](SecretsApi.md#kv_v2_write) | **POST** /{kv_v2_mount_path}/data/{path} | 
[**kv_v2_write_metadata**](SecretsApi.md#kv_v2_write_metadata) | **POST** /{kv_v2_mount_path}/metadata/{path} | 
[**ldap_configure**](SecretsApi.md#ldap_configure) | **POST** /{ldap_mount_path}/config | 
[**ldap_delete_configuration**](SecretsApi.md#ldap_delete_configuration) | **DELETE** /{ldap_mount_path}/config | 
[**ldap_delete_dynamic_role**](SecretsApi.md#ldap_delete_dynamic_role) | **DELETE** /{ldap_mount_path}/role/{name} | 
[**ldap_delete_static_role**](SecretsApi.md#ldap_delete_static_role) | **DELETE** /{ldap_mount_path}/static-role/{name} | 
[**ldap_library_check_in**](SecretsApi.md#ldap_library_check_in) | **POST** /{ldap_mount_path}/library/{name}/check-in | Check service accounts in to the library.
[**ldap_library_check_out**](SecretsApi.md#ldap_library_check_out) | **POST** /{ldap_mount_path}/library/{name}/check-out | Check a service account out from the library.
[**ldap_library_check_status**](SecretsApi.md#ldap_library_check_status) | **GET** /{ldap_mount_path}/library/{name}/status | Check the status of the service accounts in a library set.
[**ldap_library_configure**](SecretsApi.md#ldap_library_configure) | **POST** /{ldap_mount_path}/library/{name} | Update a library set.
[**ldap_library_delete**](SecretsApi.md#ldap_library_delete) | **DELETE** /{ldap_mount_path}/library/{name} | Delete a library set.
[**ldap_library_force_check_in**](SecretsApi.md#ldap_library_force_check_in) | **POST** /{ldap_mount_path}/library/manage/{name}/check-in | Check service accounts in to the library.
[**ldap_library_list**](SecretsApi.md#ldap_library_list) | **GET** /{ldap_mount_path}/library/ | 
[**ldap_library_read**](SecretsApi.md#ldap_library_read) | **GET** /{ldap_mount_path}/library/{name} | Read a library set.
[**ldap_list_dynamic_roles**](SecretsApi.md#ldap_list_dynamic_roles) | **GET** /{ldap_mount_path}/role/ | 
[**ldap_list_static_roles**](SecretsApi.md#ldap_list_static_roles) | **GET** /{ldap_mount_path}/static-role/ | 
[**ldap_read_configuration**](SecretsApi.md#ldap_read_configuration) | **GET** /{ldap_mount_path}/config | 
[**ldap_read_dynamic_role**](SecretsApi.md#ldap_read_dynamic_role) | **GET** /{ldap_mount_path}/role/{name} | 
[**ldap_read_static_role**](SecretsApi.md#ldap_read_static_role) | **GET** /{ldap_mount_path}/static-role/{name} | 
[**ldap_request_dynamic_role_credentials**](SecretsApi.md#ldap_request_dynamic_role_credentials) | **GET** /{ldap_mount_path}/creds/{name} | 
[**ldap_request_static_role_credentials**](SecretsApi.md#ldap_request_static_role_credentials) | **GET** /{ldap_mount_path}/static-cred/{name} | 
[**ldap_rotate_root_credentials**](SecretsApi.md#ldap_rotate_root_credentials) | **POST** /{ldap_mount_path}/rotate-root | 
[**ldap_rotate_static_role**](SecretsApi.md#ldap_rotate_static_role) | **POST** /{ldap_mount_path}/rotate-role/{name} | 
[**ldap_write_dynamic_role**](SecretsApi.md#ldap_write_dynamic_role) | **POST** /{ldap_mount_path}/role/{name} | 
[**ldap_write_static_role**](SecretsApi.md#ldap_write_static_role) | **POST** /{ldap_mount_path}/static-role/{name} | 
[**mongo_db_atlas_configure**](SecretsApi.md#mongo_db_atlas_configure) | **POST** /{mongodbatlas_mount_path}/config | 
[**mongo_db_atlas_delete_role**](SecretsApi.md#mongo_db_atlas_delete_role) | **DELETE** /{mongodbatlas_mount_path}/roles/{name} | Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
[**mongo_db_atlas_generate_credentials**](SecretsApi.md#mongo_db_atlas_generate_credentials) | **GET** /{mongodbatlas_mount_path}/creds/{name} | 
[**mongo_db_atlas_generate_credentials2**](SecretsApi.md#mongo_db_atlas_generate_credentials2) | **POST** /{mongodbatlas_mount_path}/creds/{name} | 
[**mongo_db_atlas_list_roles**](SecretsApi.md#mongo_db_atlas_list_roles) | **GET** /{mongodbatlas_mount_path}/roles/ | List the existing roles in this backend
[**mongo_db_atlas_read_configuration**](SecretsApi.md#mongo_db_atlas_read_configuration) | **GET** /{mongodbatlas_mount_path}/config | 
[**mongo_db_atlas_read_role**](SecretsApi.md#mongo_db_atlas_read_role) | **GET** /{mongodbatlas_mount_path}/roles/{name} | Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
[**mongo_db_atlas_write_role**](SecretsApi.md#mongo_db_atlas_write_role) | **POST** /{mongodbatlas_mount_path}/roles/{name} | Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
[**nomad_configure_access**](SecretsApi.md#nomad_configure_access) | **POST** /{nomad_mount_path}/config/access | 
[**nomad_configure_lease**](SecretsApi.md#nomad_configure_lease) | **POST** /{nomad_mount_path}/config/lease | 
[**nomad_delete_access_configuration**](SecretsApi.md#nomad_delete_access_configuration) | **DELETE** /{nomad_mount_path}/config/access | 
[**nomad_delete_lease_configuration**](SecretsApi.md#nomad_delete_lease_configuration) | **DELETE** /{nomad_mount_path}/config/lease | 
[**nomad_delete_role**](SecretsApi.md#nomad_delete_role) | **DELETE** /{nomad_mount_path}/role/{name} | 
[**nomad_generate_credentials**](SecretsApi.md#nomad_generate_credentials) | **GET** /{nomad_mount_path}/creds/{name} | 
[**nomad_list_roles**](SecretsApi.md#nomad_list_roles) | **GET** /{nomad_mount_path}/role/ | 
[**nomad_read_access_configuration**](SecretsApi.md#nomad_read_access_configuration) | **GET** /{nomad_mount_path}/config/access | 
[**nomad_read_lease_configuration**](SecretsApi.md#nomad_read_lease_configuration) | **GET** /{nomad_mount_path}/config/lease | 
[**nomad_read_role**](SecretsApi.md#nomad_read_role) | **GET** /{nomad_mount_path}/role/{name} | 
[**nomad_write_role**](SecretsApi.md#nomad_write_role) | **POST** /{nomad_mount_path}/role/{name} | 
[**pki_configure_acme**](SecretsApi.md#pki_configure_acme) | **POST** /{pki_mount_path}/config/acme | 
[**pki_configure_auto_tidy**](SecretsApi.md#pki_configure_auto_tidy) | **POST** /{pki_mount_path}/config/auto-tidy | 
[**pki_configure_ca**](SecretsApi.md#pki_configure_ca) | **POST** /{pki_mount_path}/config/ca | 
[**pki_configure_cluster**](SecretsApi.md#pki_configure_cluster) | **POST** /{pki_mount_path}/config/cluster | 
[**pki_configure_crl**](SecretsApi.md#pki_configure_crl) | **POST** /{pki_mount_path}/config/crl | 
[**pki_configure_issuers**](SecretsApi.md#pki_configure_issuers) | **POST** /{pki_mount_path}/config/issuers | 
[**pki_configure_keys**](SecretsApi.md#pki_configure_keys) | **POST** /{pki_mount_path}/config/keys | 
[**pki_configure_urls**](SecretsApi.md#pki_configure_urls) | **POST** /{pki_mount_path}/config/urls | 
[**pki_cross_sign_intermediate**](SecretsApi.md#pki_cross_sign_intermediate) | **POST** /{pki_mount_path}/intermediate/cross-sign | 
[**pki_delete_eab_key**](SecretsApi.md#pki_delete_eab_key) | **DELETE** /{pki_mount_path}/eab/{key_id} | 
[**pki_delete_issuer**](SecretsApi.md#pki_delete_issuer) | **DELETE** /{pki_mount_path}/issuer/{issuer_ref} | 
[**pki_delete_key**](SecretsApi.md#pki_delete_key) | **DELETE** /{pki_mount_path}/key/{key_ref} | 
[**pki_delete_role**](SecretsApi.md#pki_delete_role) | **DELETE** /{pki_mount_path}/roles/{name} | 
[**pki_delete_root**](SecretsApi.md#pki_delete_root) | **DELETE** /{pki_mount_path}/root | 
[**pki_generate_eab_key**](SecretsApi.md#pki_generate_eab_key) | **POST** /{pki_mount_path}/acme/new-eab | 
[**pki_generate_eab_key_for_issuer**](SecretsApi.md#pki_generate_eab_key_for_issuer) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/new-eab | 
[**pki_generate_eab_key_for_issuer_and_role**](SecretsApi.md#pki_generate_eab_key_for_issuer_and_role) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/new-eab | 
[**pki_generate_eab_key_for_role**](SecretsApi.md#pki_generate_eab_key_for_role) | **POST** /{pki_mount_path}/roles/{role}/acme/new-eab | 
[**pki_generate_exported_key**](SecretsApi.md#pki_generate_exported_key) | **POST** /{pki_mount_path}/keys/generate/exported | 
[**pki_generate_intermediate**](SecretsApi.md#pki_generate_intermediate) | **POST** /{pki_mount_path}/intermediate/generate/{exported} | 
[**pki_generate_internal_key**](SecretsApi.md#pki_generate_internal_key) | **POST** /{pki_mount_path}/keys/generate/internal | 
[**pki_generate_kms_key**](SecretsApi.md#pki_generate_kms_key) | **POST** /{pki_mount_path}/keys/generate/kms | 
[**pki_generate_root**](SecretsApi.md#pki_generate_root) | **POST** /{pki_mount_path}/root/generate/{exported} | 
[**pki_import_key**](SecretsApi.md#pki_import_key) | **POST** /{pki_mount_path}/keys/import | 
[**pki_issue_with_role**](SecretsApi.md#pki_issue_with_role) | **POST** /{pki_mount_path}/issue/{role} | 
[**pki_issuer_issue_with_role**](SecretsApi.md#pki_issuer_issue_with_role) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/issue/{role} | 
[**pki_issuer_read_crl**](SecretsApi.md#pki_issuer_read_crl) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/crl | 
[**pki_issuer_read_crl_delta**](SecretsApi.md#pki_issuer_read_crl_delta) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/crl/delta | 
[**pki_issuer_read_crl_delta_der**](SecretsApi.md#pki_issuer_read_crl_delta_der) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/crl/delta/der | 
[**pki_issuer_read_crl_delta_pem**](SecretsApi.md#pki_issuer_read_crl_delta_pem) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/crl/delta/pem | 
[**pki_issuer_read_crl_der**](SecretsApi.md#pki_issuer_read_crl_der) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/crl/der | 
[**pki_issuer_read_crl_pem**](SecretsApi.md#pki_issuer_read_crl_pem) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/crl/pem | 
[**pki_issuer_resign_crls**](SecretsApi.md#pki_issuer_resign_crls) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/resign-crls | 
[**pki_issuer_sign_intermediate**](SecretsApi.md#pki_issuer_sign_intermediate) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/sign-intermediate | 
[**pki_issuer_sign_revocation_list**](SecretsApi.md#pki_issuer_sign_revocation_list) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/sign-revocation-list | 
[**pki_issuer_sign_self_issued**](SecretsApi.md#pki_issuer_sign_self_issued) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/sign-self-issued | 
[**pki_issuer_sign_verbatim**](SecretsApi.md#pki_issuer_sign_verbatim) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/sign-verbatim | 
[**pki_issuer_sign_verbatim_with_role**](SecretsApi.md#pki_issuer_sign_verbatim_with_role) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/sign-verbatim/{role} | 
[**pki_issuer_sign_with_role**](SecretsApi.md#pki_issuer_sign_with_role) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/sign/{role} | 
[**pki_issuers_generate_intermediate**](SecretsApi.md#pki_issuers_generate_intermediate) | **POST** /{pki_mount_path}/issuers/generate/intermediate/{exported} | 
[**pki_issuers_generate_root**](SecretsApi.md#pki_issuers_generate_root) | **POST** /{pki_mount_path}/issuers/generate/root/{exported} | 
[**pki_issuers_import_bundle**](SecretsApi.md#pki_issuers_import_bundle) | **POST** /{pki_mount_path}/issuers/import/bundle | 
[**pki_issuers_import_cert**](SecretsApi.md#pki_issuers_import_cert) | **POST** /{pki_mount_path}/issuers/import/cert | 
[**pki_list_certs**](SecretsApi.md#pki_list_certs) | **GET** /{pki_mount_path}/certs/ | 
[**pki_list_eab_keys**](SecretsApi.md#pki_list_eab_keys) | **GET** /{pki_mount_path}/eab/ | 
[**pki_list_issuers**](SecretsApi.md#pki_list_issuers) | **GET** /{pki_mount_path}/issuers/ | 
[**pki_list_keys**](SecretsApi.md#pki_list_keys) | **GET** /{pki_mount_path}/keys/ | 
[**pki_list_revoked_certs**](SecretsApi.md#pki_list_revoked_certs) | **GET** /{pki_mount_path}/certs/revoked/ | 
[**pki_list_roles**](SecretsApi.md#pki_list_roles) | **GET** /{pki_mount_path}/roles/ | 
[**pki_query_ocsp**](SecretsApi.md#pki_query_ocsp) | **POST** /{pki_mount_path}/ocsp | 
[**pki_query_ocsp_with_get_req**](SecretsApi.md#pki_query_ocsp_with_get_req) | **GET** /{pki_mount_path}/ocsp/{req} | 
[**pki_read_acme_configuration**](SecretsApi.md#pki_read_acme_configuration) | **GET** /{pki_mount_path}/config/acme | 
[**pki_read_acme_directory**](SecretsApi.md#pki_read_acme_directory) | **GET** /{pki_mount_path}/acme/directory | 
[**pki_read_acme_new_nonce**](SecretsApi.md#pki_read_acme_new_nonce) | **GET** /{pki_mount_path}/acme/new-nonce | 
[**pki_read_auto_tidy_configuration**](SecretsApi.md#pki_read_auto_tidy_configuration) | **GET** /{pki_mount_path}/config/auto-tidy | 
[**pki_read_ca_chain_pem**](SecretsApi.md#pki_read_ca_chain_pem) | **GET** /{pki_mount_path}/ca_chain | 
[**pki_read_ca_der**](SecretsApi.md#pki_read_ca_der) | **GET** /{pki_mount_path}/ca | 
[**pki_read_ca_pem**](SecretsApi.md#pki_read_ca_pem) | **GET** /{pki_mount_path}/ca/pem | 
[**pki_read_cert**](SecretsApi.md#pki_read_cert) | **GET** /{pki_mount_path}/cert/{serial} | 
[**pki_read_cert_ca_chain**](SecretsApi.md#pki_read_cert_ca_chain) | **GET** /{pki_mount_path}/cert/ca_chain | 
[**pki_read_cert_crl**](SecretsApi.md#pki_read_cert_crl) | **GET** /{pki_mount_path}/cert/crl | 
[**pki_read_cert_delta_crl**](SecretsApi.md#pki_read_cert_delta_crl) | **GET** /{pki_mount_path}/cert/delta-crl | 
[**pki_read_cert_raw_der**](SecretsApi.md#pki_read_cert_raw_der) | **GET** /{pki_mount_path}/cert/{serial}/raw | 
[**pki_read_cert_raw_pem**](SecretsApi.md#pki_read_cert_raw_pem) | **GET** /{pki_mount_path}/cert/{serial}/raw/pem | 
[**pki_read_cluster_configuration**](SecretsApi.md#pki_read_cluster_configuration) | **GET** /{pki_mount_path}/config/cluster | 
[**pki_read_crl_configuration**](SecretsApi.md#pki_read_crl_configuration) | **GET** /{pki_mount_path}/config/crl | 
[**pki_read_crl_delta**](SecretsApi.md#pki_read_crl_delta) | **GET** /{pki_mount_path}/crl/delta | 
[**pki_read_crl_delta_pem**](SecretsApi.md#pki_read_crl_delta_pem) | **GET** /{pki_mount_path}/crl/delta/pem | 
[**pki_read_crl_der**](SecretsApi.md#pki_read_crl_der) | **GET** /{pki_mount_path}/crl | 
[**pki_read_crl_pem**](SecretsApi.md#pki_read_crl_pem) | **GET** /{pki_mount_path}/crl/pem | 
[**pki_read_issuer**](SecretsApi.md#pki_read_issuer) | **GET** /{pki_mount_path}/issuer/{issuer_ref} | 
[**pki_read_issuer_der**](SecretsApi.md#pki_read_issuer_der) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/der | 
[**pki_read_issuer_issuer_ref_acme_directory**](SecretsApi.md#pki_read_issuer_issuer_ref_acme_directory) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/acme/directory | 
[**pki_read_issuer_issuer_ref_acme_new_nonce**](SecretsApi.md#pki_read_issuer_issuer_ref_acme_new_nonce) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/acme/new-nonce | 
[**pki_read_issuer_issuer_ref_roles_role_acme_directory**](SecretsApi.md#pki_read_issuer_issuer_ref_roles_role_acme_directory) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/directory | 
[**pki_read_issuer_issuer_ref_roles_role_acme_new_nonce**](SecretsApi.md#pki_read_issuer_issuer_ref_roles_role_acme_new_nonce) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/new-nonce | 
[**pki_read_issuer_json**](SecretsApi.md#pki_read_issuer_json) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/json | 
[**pki_read_issuer_pem**](SecretsApi.md#pki_read_issuer_pem) | **GET** /{pki_mount_path}/issuer/{issuer_ref}/pem | 
[**pki_read_issuers_configuration**](SecretsApi.md#pki_read_issuers_configuration) | **GET** /{pki_mount_path}/config/issuers | 
[**pki_read_key**](SecretsApi.md#pki_read_key) | **GET** /{pki_mount_path}/key/{key_ref} | 
[**pki_read_keys_configuration**](SecretsApi.md#pki_read_keys_configuration) | **GET** /{pki_mount_path}/config/keys | 
[**pki_read_role**](SecretsApi.md#pki_read_role) | **GET** /{pki_mount_path}/roles/{name} | 
[**pki_read_roles_role_acme_directory**](SecretsApi.md#pki_read_roles_role_acme_directory) | **GET** /{pki_mount_path}/roles/{role}/acme/directory | 
[**pki_read_roles_role_acme_new_nonce**](SecretsApi.md#pki_read_roles_role_acme_new_nonce) | **GET** /{pki_mount_path}/roles/{role}/acme/new-nonce | 
[**pki_read_urls_configuration**](SecretsApi.md#pki_read_urls_configuration) | **GET** /{pki_mount_path}/config/urls | 
[**pki_replace_root**](SecretsApi.md#pki_replace_root) | **POST** /{pki_mount_path}/root/replace | 
[**pki_revoke**](SecretsApi.md#pki_revoke) | **POST** /{pki_mount_path}/revoke | 
[**pki_revoke_issuer**](SecretsApi.md#pki_revoke_issuer) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/revoke | 
[**pki_revoke_with_key**](SecretsApi.md#pki_revoke_with_key) | **POST** /{pki_mount_path}/revoke-with-key | 
[**pki_root_sign_intermediate**](SecretsApi.md#pki_root_sign_intermediate) | **POST** /{pki_mount_path}/root/sign-intermediate | 
[**pki_root_sign_self_issued**](SecretsApi.md#pki_root_sign_self_issued) | **POST** /{pki_mount_path}/root/sign-self-issued | 
[**pki_rotate_crl**](SecretsApi.md#pki_rotate_crl) | **GET** /{pki_mount_path}/crl/rotate | 
[**pki_rotate_delta_crl**](SecretsApi.md#pki_rotate_delta_crl) | **GET** /{pki_mount_path}/crl/rotate-delta | 
[**pki_rotate_root**](SecretsApi.md#pki_rotate_root) | **POST** /{pki_mount_path}/root/rotate/{exported} | 
[**pki_set_signed_intermediate**](SecretsApi.md#pki_set_signed_intermediate) | **POST** /{pki_mount_path}/intermediate/set-signed | 
[**pki_sign_verbatim**](SecretsApi.md#pki_sign_verbatim) | **POST** /{pki_mount_path}/sign-verbatim | 
[**pki_sign_verbatim_with_role**](SecretsApi.md#pki_sign_verbatim_with_role) | **POST** /{pki_mount_path}/sign-verbatim/{role} | 
[**pki_sign_with_role**](SecretsApi.md#pki_sign_with_role) | **POST** /{pki_mount_path}/sign/{role} | 
[**pki_tidy**](SecretsApi.md#pki_tidy) | **POST** /{pki_mount_path}/tidy | 
[**pki_tidy_cancel**](SecretsApi.md#pki_tidy_cancel) | **POST** /{pki_mount_path}/tidy-cancel | 
[**pki_tidy_status**](SecretsApi.md#pki_tidy_status) | **GET** /{pki_mount_path}/tidy-status | 
[**pki_write_acme_account_kid**](SecretsApi.md#pki_write_acme_account_kid) | **POST** /{pki_mount_path}/acme/account/{kid} | 
[**pki_write_acme_authorization_auth_id**](SecretsApi.md#pki_write_acme_authorization_auth_id) | **POST** /{pki_mount_path}/acme/authorization/{auth_id} | 
[**pki_write_acme_challenge_auth_id_challenge_type**](SecretsApi.md#pki_write_acme_challenge_auth_id_challenge_type) | **POST** /{pki_mount_path}/acme/challenge/{auth_id}/{challenge_type} | 
[**pki_write_acme_new_account**](SecretsApi.md#pki_write_acme_new_account) | **POST** /{pki_mount_path}/acme/new-account | 
[**pki_write_acme_new_order**](SecretsApi.md#pki_write_acme_new_order) | **POST** /{pki_mount_path}/acme/new-order | 
[**pki_write_acme_order_order_id**](SecretsApi.md#pki_write_acme_order_order_id) | **POST** /{pki_mount_path}/acme/order/{order_id} | 
[**pki_write_acme_order_order_id_cert**](SecretsApi.md#pki_write_acme_order_order_id_cert) | **POST** /{pki_mount_path}/acme/order/{order_id}/cert | 
[**pki_write_acme_order_order_id_finalize**](SecretsApi.md#pki_write_acme_order_order_id_finalize) | **POST** /{pki_mount_path}/acme/order/{order_id}/finalize | 
[**pki_write_acme_orders**](SecretsApi.md#pki_write_acme_orders) | **POST** /{pki_mount_path}/acme/orders | 
[**pki_write_acme_revoke_cert**](SecretsApi.md#pki_write_acme_revoke_cert) | **POST** /{pki_mount_path}/acme/revoke-cert | 
[**pki_write_issuer**](SecretsApi.md#pki_write_issuer) | **POST** /{pki_mount_path}/issuer/{issuer_ref} | 
[**pki_write_issuer_issuer_ref_acme_account_kid**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_account_kid) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/account/{kid} | 
[**pki_write_issuer_issuer_ref_acme_authorization_auth_id**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_authorization_auth_id) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/authorization/{auth_id} | 
[**pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/challenge/{auth_id}/{challenge_type} | 
[**pki_write_issuer_issuer_ref_acme_new_account**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_new_account) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/new-account | 
[**pki_write_issuer_issuer_ref_acme_new_order**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_new_order) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/new-order | 
[**pki_write_issuer_issuer_ref_acme_order_order_id**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_order_order_id) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/order/{order_id} | 
[**pki_write_issuer_issuer_ref_acme_order_order_id_cert**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_order_order_id_cert) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/order/{order_id}/cert | 
[**pki_write_issuer_issuer_ref_acme_order_order_id_finalize**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_order_order_id_finalize) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/order/{order_id}/finalize | 
[**pki_write_issuer_issuer_ref_acme_orders**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_orders) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/orders | 
[**pki_write_issuer_issuer_ref_acme_revoke_cert**](SecretsApi.md#pki_write_issuer_issuer_ref_acme_revoke_cert) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/acme/revoke-cert | 
[**pki_write_issuer_issuer_ref_roles_role_acme_account_kid**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_account_kid) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/account/{kid} | 
[**pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/authorization/{auth_id} | 
[**pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/challenge/{auth_id}/{challenge_type} | 
[**pki_write_issuer_issuer_ref_roles_role_acme_new_account**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_new_account) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/new-account | 
[**pki_write_issuer_issuer_ref_roles_role_acme_new_order**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_new_order) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/new-order | 
[**pki_write_issuer_issuer_ref_roles_role_acme_order_order_id**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_order_order_id) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/order/{order_id} | 
[**pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/order/{order_id}/cert | 
[**pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/order/{order_id}/finalize | 
[**pki_write_issuer_issuer_ref_roles_role_acme_orders**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_orders) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/orders | 
[**pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert**](SecretsApi.md#pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert) | **POST** /{pki_mount_path}/issuer/{issuer_ref}/roles/{role}/acme/revoke-cert | 
[**pki_write_key**](SecretsApi.md#pki_write_key) | **POST** /{pki_mount_path}/key/{key_ref} | 
[**pki_write_role**](SecretsApi.md#pki_write_role) | **POST** /{pki_mount_path}/roles/{name} | 
[**pki_write_roles_role_acme_account_kid**](SecretsApi.md#pki_write_roles_role_acme_account_kid) | **POST** /{pki_mount_path}/roles/{role}/acme/account/{kid} | 
[**pki_write_roles_role_acme_authorization_auth_id**](SecretsApi.md#pki_write_roles_role_acme_authorization_auth_id) | **POST** /{pki_mount_path}/roles/{role}/acme/authorization/{auth_id} | 
[**pki_write_roles_role_acme_challenge_auth_id_challenge_type**](SecretsApi.md#pki_write_roles_role_acme_challenge_auth_id_challenge_type) | **POST** /{pki_mount_path}/roles/{role}/acme/challenge/{auth_id}/{challenge_type} | 
[**pki_write_roles_role_acme_new_account**](SecretsApi.md#pki_write_roles_role_acme_new_account) | **POST** /{pki_mount_path}/roles/{role}/acme/new-account | 
[**pki_write_roles_role_acme_new_order**](SecretsApi.md#pki_write_roles_role_acme_new_order) | **POST** /{pki_mount_path}/roles/{role}/acme/new-order | 
[**pki_write_roles_role_acme_order_order_id**](SecretsApi.md#pki_write_roles_role_acme_order_order_id) | **POST** /{pki_mount_path}/roles/{role}/acme/order/{order_id} | 
[**pki_write_roles_role_acme_order_order_id_cert**](SecretsApi.md#pki_write_roles_role_acme_order_order_id_cert) | **POST** /{pki_mount_path}/roles/{role}/acme/order/{order_id}/cert | 
[**pki_write_roles_role_acme_order_order_id_finalize**](SecretsApi.md#pki_write_roles_role_acme_order_order_id_finalize) | **POST** /{pki_mount_path}/roles/{role}/acme/order/{order_id}/finalize | 
[**pki_write_roles_role_acme_orders**](SecretsApi.md#pki_write_roles_role_acme_orders) | **POST** /{pki_mount_path}/roles/{role}/acme/orders | 
[**pki_write_roles_role_acme_revoke_cert**](SecretsApi.md#pki_write_roles_role_acme_revoke_cert) | **POST** /{pki_mount_path}/roles/{role}/acme/revoke-cert | 
[**rabbit_mq_configure_connection**](SecretsApi.md#rabbit_mq_configure_connection) | **POST** /{rabbitmq_mount_path}/config/connection | Configure the connection URI, username, and password to talk to RabbitMQ management HTTP API.
[**rabbit_mq_configure_lease**](SecretsApi.md#rabbit_mq_configure_lease) | **POST** /{rabbitmq_mount_path}/config/lease | 
[**rabbit_mq_delete_role**](SecretsApi.md#rabbit_mq_delete_role) | **DELETE** /{rabbitmq_mount_path}/roles/{name} | Manage the roles that can be created with this backend.
[**rabbit_mq_list_roles**](SecretsApi.md#rabbit_mq_list_roles) | **GET** /{rabbitmq_mount_path}/roles/ | Manage the roles that can be created with this backend.
[**rabbit_mq_read_lease_configuration**](SecretsApi.md#rabbit_mq_read_lease_configuration) | **GET** /{rabbitmq_mount_path}/config/lease | 
[**rabbit_mq_read_role**](SecretsApi.md#rabbit_mq_read_role) | **GET** /{rabbitmq_mount_path}/roles/{name} | Manage the roles that can be created with this backend.
[**rabbit_mq_request_credentials**](SecretsApi.md#rabbit_mq_request_credentials) | **GET** /{rabbitmq_mount_path}/creds/{name} | Request RabbitMQ credentials for a certain role.
[**rabbit_mq_write_role**](SecretsApi.md#rabbit_mq_write_role) | **POST** /{rabbitmq_mount_path}/roles/{name} | Manage the roles that can be created with this backend.
[**ssh_configure_ca**](SecretsApi.md#ssh_configure_ca) | **POST** /{ssh_mount_path}/config/ca | 
[**ssh_configure_zero_address**](SecretsApi.md#ssh_configure_zero_address) | **POST** /{ssh_mount_path}/config/zeroaddress | 
[**ssh_delete_ca_configuration**](SecretsApi.md#ssh_delete_ca_configuration) | **DELETE** /{ssh_mount_path}/config/ca | 
[**ssh_delete_role**](SecretsApi.md#ssh_delete_role) | **DELETE** /{ssh_mount_path}/roles/{role} | Manage the &#39;roles&#39; that can be created with this backend.
[**ssh_delete_zero_address_configuration**](SecretsApi.md#ssh_delete_zero_address_configuration) | **DELETE** /{ssh_mount_path}/config/zeroaddress | 
[**ssh_generate_credentials**](SecretsApi.md#ssh_generate_credentials) | **POST** /{ssh_mount_path}/creds/{role} | Creates a credential for establishing SSH connection with the remote host.
[**ssh_issue_certificate**](SecretsApi.md#ssh_issue_certificate) | **POST** /{ssh_mount_path}/issue/{role} | 
[**ssh_list_roles**](SecretsApi.md#ssh_list_roles) | **GET** /{ssh_mount_path}/roles/ | Manage the &#39;roles&#39; that can be created with this backend.
[**ssh_list_roles_by_ip**](SecretsApi.md#ssh_list_roles_by_ip) | **POST** /{ssh_mount_path}/lookup | List all the roles associated with the given IP address.
[**ssh_read_ca_configuration**](SecretsApi.md#ssh_read_ca_configuration) | **GET** /{ssh_mount_path}/config/ca | 
[**ssh_read_public_key**](SecretsApi.md#ssh_read_public_key) | **GET** /{ssh_mount_path}/public_key | Retrieve the public key.
[**ssh_read_role**](SecretsApi.md#ssh_read_role) | **GET** /{ssh_mount_path}/roles/{role} | Manage the &#39;roles&#39; that can be created with this backend.
[**ssh_read_zero_address_configuration**](SecretsApi.md#ssh_read_zero_address_configuration) | **GET** /{ssh_mount_path}/config/zeroaddress | 
[**ssh_sign_certificate**](SecretsApi.md#ssh_sign_certificate) | **POST** /{ssh_mount_path}/sign/{role} | Request signing an SSH key using a certain role with the provided details.
[**ssh_tidy_dynamic_host_keys**](SecretsApi.md#ssh_tidy_dynamic_host_keys) | **DELETE** /{ssh_mount_path}/tidy/dynamic-keys | This endpoint removes the stored host keys used for the removed Dynamic Key feature, if present.
[**ssh_verify_otp**](SecretsApi.md#ssh_verify_otp) | **POST** /{ssh_mount_path}/verify | Validate the OTP provided by Vault SSH Agent.
[**ssh_write_role**](SecretsApi.md#ssh_write_role) | **POST** /{ssh_mount_path}/roles/{role} | Manage the &#39;roles&#39; that can be created with this backend.
[**terraform_cloud_configure**](SecretsApi.md#terraform_cloud_configure) | **POST** /{terraform_mount_path}/config | 
[**terraform_cloud_delete_configuration**](SecretsApi.md#terraform_cloud_delete_configuration) | **DELETE** /{terraform_mount_path}/config | 
[**terraform_cloud_delete_role**](SecretsApi.md#terraform_cloud_delete_role) | **DELETE** /{terraform_mount_path}/role/{name} | 
[**terraform_cloud_generate_credentials**](SecretsApi.md#terraform_cloud_generate_credentials) | **GET** /{terraform_mount_path}/creds/{name} | 
[**terraform_cloud_generate_credentials2**](SecretsApi.md#terraform_cloud_generate_credentials2) | **POST** /{terraform_mount_path}/creds/{name} | 
[**terraform_cloud_list_roles**](SecretsApi.md#terraform_cloud_list_roles) | **GET** /{terraform_mount_path}/role/ | 
[**terraform_cloud_read_configuration**](SecretsApi.md#terraform_cloud_read_configuration) | **GET** /{terraform_mount_path}/config | 
[**terraform_cloud_read_role**](SecretsApi.md#terraform_cloud_read_role) | **GET** /{terraform_mount_path}/role/{name} | 
[**terraform_cloud_rotate_role**](SecretsApi.md#terraform_cloud_rotate_role) | **POST** /{terraform_mount_path}/rotate-role/{name} | 
[**terraform_cloud_write_role**](SecretsApi.md#terraform_cloud_write_role) | **POST** /{terraform_mount_path}/role/{name} | 
[**totp_create_key**](SecretsApi.md#totp_create_key) | **POST** /{totp_mount_path}/keys/{name} | 
[**totp_delete_key**](SecretsApi.md#totp_delete_key) | **DELETE** /{totp_mount_path}/keys/{name} | 
[**totp_generate_code**](SecretsApi.md#totp_generate_code) | **GET** /{totp_mount_path}/code/{name} | 
[**totp_list_keys**](SecretsApi.md#totp_list_keys) | **GET** /{totp_mount_path}/keys/ | Manage the keys that can be created with this backend.
[**totp_read_key**](SecretsApi.md#totp_read_key) | **GET** /{totp_mount_path}/keys/{name} | 
[**totp_validate_code**](SecretsApi.md#totp_validate_code) | **POST** /{totp_mount_path}/code/{name} | 
[**transit_back_up_key**](SecretsApi.md#transit_back_up_key) | **GET** /{transit_mount_path}/backup/{name} | Backup the named key
[**transit_byok_key**](SecretsApi.md#transit_byok_key) | **GET** /{transit_mount_path}/byok-export/{destination}/{source} | Securely export named encryption or signing key
[**transit_byok_key_version**](SecretsApi.md#transit_byok_key_version) | **GET** /{transit_mount_path}/byok-export/{destination}/{source}/{version} | Securely export named encryption or signing key
[**transit_configure_cache**](SecretsApi.md#transit_configure_cache) | **POST** /{transit_mount_path}/cache-config | Configures a new cache of the specified size
[**transit_configure_key**](SecretsApi.md#transit_configure_key) | **POST** /{transit_mount_path}/keys/{name}/config | Configure a named encryption key
[**transit_configure_keys**](SecretsApi.md#transit_configure_keys) | **POST** /{transit_mount_path}/config/keys | 
[**transit_create_key**](SecretsApi.md#transit_create_key) | **POST** /{transit_mount_path}/keys/{name} | 
[**transit_decrypt**](SecretsApi.md#transit_decrypt) | **POST** /{transit_mount_path}/decrypt/{name} | Decrypt a ciphertext value using a named key
[**transit_delete_key**](SecretsApi.md#transit_delete_key) | **DELETE** /{transit_mount_path}/keys/{name} | 
[**transit_encrypt**](SecretsApi.md#transit_encrypt) | **POST** /{transit_mount_path}/encrypt/{name} | Encrypt a plaintext value or a batch of plaintext blocks using a named key
[**transit_export_key**](SecretsApi.md#transit_export_key) | **GET** /{transit_mount_path}/export/{type}/{name} | Export named encryption or signing key
[**transit_export_key_version**](SecretsApi.md#transit_export_key_version) | **GET** /{transit_mount_path}/export/{type}/{name}/{version} | Export named encryption or signing key
[**transit_generate_csr_for_key**](SecretsApi.md#transit_generate_csr_for_key) | **POST** /{transit_mount_path}/keys/{name}/csr | 
[**transit_generate_data_key**](SecretsApi.md#transit_generate_data_key) | **POST** /{transit_mount_path}/datakey/{plaintext}/{name} | Generate a data key
[**transit_generate_hmac**](SecretsApi.md#transit_generate_hmac) | **POST** /{transit_mount_path}/hmac/{name} | Generate an HMAC for input data using the named key
[**transit_generate_hmac_with_algorithm**](SecretsApi.md#transit_generate_hmac_with_algorithm) | **POST** /{transit_mount_path}/hmac/{name}/{urlalgorithm} | Generate an HMAC for input data using the named key
[**transit_generate_random**](SecretsApi.md#transit_generate_random) | **POST** /{transit_mount_path}/random | Generate random bytes
[**transit_generate_random_with_bytes**](SecretsApi.md#transit_generate_random_with_bytes) | **POST** /{transit_mount_path}/random/{urlbytes} | Generate random bytes
[**transit_generate_random_with_source**](SecretsApi.md#transit_generate_random_with_source) | **POST** /{transit_mount_path}/random/{source} | Generate random bytes
[**transit_generate_random_with_source_and_bytes**](SecretsApi.md#transit_generate_random_with_source_and_bytes) | **POST** /{transit_mount_path}/random/{source}/{urlbytes} | Generate random bytes
[**transit_hash**](SecretsApi.md#transit_hash) | **POST** /{transit_mount_path}/hash | Generate a hash sum for input data
[**transit_hash_with_algorithm**](SecretsApi.md#transit_hash_with_algorithm) | **POST** /{transit_mount_path}/hash/{urlalgorithm} | Generate a hash sum for input data
[**transit_import_key**](SecretsApi.md#transit_import_key) | **POST** /{transit_mount_path}/keys/{name}/import | Imports an externally-generated key into a new transit key
[**transit_import_key_version**](SecretsApi.md#transit_import_key_version) | **POST** /{transit_mount_path}/keys/{name}/import_version | Imports an externally-generated key into an existing imported key
[**transit_list_keys**](SecretsApi.md#transit_list_keys) | **GET** /{transit_mount_path}/keys/ | Managed named encryption keys
[**transit_read_cache_configuration**](SecretsApi.md#transit_read_cache_configuration) | **GET** /{transit_mount_path}/cache-config | Returns the size of the active cache
[**transit_read_key**](SecretsApi.md#transit_read_key) | **GET** /{transit_mount_path}/keys/{name} | 
[**transit_read_keys_configuration**](SecretsApi.md#transit_read_keys_configuration) | **GET** /{transit_mount_path}/config/keys | 
[**transit_read_wrapping_key**](SecretsApi.md#transit_read_wrapping_key) | **GET** /{transit_mount_path}/wrapping_key | Returns the public key to use for wrapping imported keys
[**transit_restore_and_rename_key**](SecretsApi.md#transit_restore_and_rename_key) | **POST** /{transit_mount_path}/restore/{name} | Restore the named key
[**transit_restore_key**](SecretsApi.md#transit_restore_key) | **POST** /{transit_mount_path}/restore | Restore the named key
[**transit_rewrap**](SecretsApi.md#transit_rewrap) | **POST** /{transit_mount_path}/rewrap/{name} | Rewrap ciphertext
[**transit_rotate_key**](SecretsApi.md#transit_rotate_key) | **POST** /{transit_mount_path}/keys/{name}/rotate | Rotate named encryption key
[**transit_set_certificate_for_key**](SecretsApi.md#transit_set_certificate_for_key) | **POST** /{transit_mount_path}/keys/{name}/set-certificate | 
[**transit_sign**](SecretsApi.md#transit_sign) | **POST** /{transit_mount_path}/sign/{name} | Generate a signature for input data using the named key
[**transit_sign_with_algorithm**](SecretsApi.md#transit_sign_with_algorithm) | **POST** /{transit_mount_path}/sign/{name}/{urlalgorithm} | Generate a signature for input data using the named key
[**transit_trim_key**](SecretsApi.md#transit_trim_key) | **POST** /{transit_mount_path}/keys/{name}/trim | Trim key versions of a named key
[**transit_verify**](SecretsApi.md#transit_verify) | **POST** /{transit_mount_path}/verify/{name} | Verify a signature or HMAC for input data created using the named key
[**transit_verify_with_algorithm**](SecretsApi.md#transit_verify_with_algorithm) | **POST** /{transit_mount_path}/verify/{name}/{urlalgorithm} | Verify a signature or HMAC for input data created using the named key


# **ali_cloud_configure**
> ali_cloud_configure(alicloud_mount_path, ali_cloud_configure_request)



### Example


```python
import ahvac
from ahvac.models.ali_cloud_configure_request import AliCloudConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')
    ali_cloud_configure_request = ahvac.AliCloudConfigureRequest() # AliCloudConfigureRequest | 

    try:
        await api_instance.ali_cloud_configure(alicloud_mount_path, ali_cloud_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]
 **ali_cloud_configure_request** | [**AliCloudConfigureRequest**](AliCloudConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ali_cloud_delete_configuration**
> ali_cloud_delete_configuration(alicloud_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')

    try:
        await api_instance.ali_cloud_delete_configuration(alicloud_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ali_cloud_delete_role**
> ali_cloud_delete_role(name, alicloud_mount_path)

Read, write and reference policies and roles that API keys or STS credentials can be made for.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of the role.
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')

    try:
        # Read, write and reference policies and roles that API keys or STS credentials can be made for.
        await api_instance.ali_cloud_delete_role(name, alicloud_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the role. | 
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ali_cloud_generate_credentials**
> ali_cloud_generate_credentials(name, alicloud_mount_path)

Generate an API key or STS credential using the given role's configuration.'

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of the role.
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')

    try:
        # Generate an API key or STS credential using the given role's configuration.'
        await api_instance.ali_cloud_generate_credentials(name, alicloud_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the role. | 
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ali_cloud_list_roles**
> StandardListResponse ali_cloud_list_roles(alicloud_mount_path, list)

List the existing roles in this backend.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')
    list = 'list_example' # str | Must be set to `true`

    try:
        # List the existing roles in this backend.
        api_response = await api_instance.ali_cloud_list_roles(alicloud_mount_path, list)
        print("The response of SecretsApi->ali_cloud_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ali_cloud_read_configuration**
> ali_cloud_read_configuration(alicloud_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')

    try:
        await api_instance.ali_cloud_read_configuration(alicloud_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ali_cloud_read_role**
> ali_cloud_read_role(name, alicloud_mount_path)

Read, write and reference policies and roles that API keys or STS credentials can be made for.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of the role.
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')

    try:
        # Read, write and reference policies and roles that API keys or STS credentials can be made for.
        await api_instance.ali_cloud_read_role(name, alicloud_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the role. | 
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ali_cloud_write_role**
> ali_cloud_write_role(name, alicloud_mount_path, ali_cloud_write_role_request)

Read, write and reference policies and roles that API keys or STS credentials can be made for.

### Example


```python
import ahvac
from ahvac.models.ali_cloud_write_role_request import AliCloudWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of the role.
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')
    ali_cloud_write_role_request = ahvac.AliCloudWriteRoleRequest() # AliCloudWriteRoleRequest | 

    try:
        # Read, write and reference policies and roles that API keys or STS credentials can be made for.
        await api_instance.ali_cloud_write_role(name, alicloud_mount_path, ali_cloud_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ali_cloud_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the role. | 
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]
 **ali_cloud_write_role_request** | [**AliCloudWriteRoleRequest**](AliCloudWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_configure_lease**
> aws_configure_lease(aws_mount_path, aws_configure_lease_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_lease_request import AwsConfigureLeaseRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_lease_request = ahvac.AwsConfigureLeaseRequest() # AwsConfigureLeaseRequest | 

    try:
        await api_instance.aws_configure_lease(aws_mount_path, aws_configure_lease_request)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_configure_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_lease_request** | [**AwsConfigureLeaseRequest**](AwsConfigureLeaseRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_configure_root_iam_credentials**
> aws_configure_root_iam_credentials(aws_mount_path, aws_configure_root_iam_credentials_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_root_iam_credentials_request import AwsConfigureRootIamCredentialsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_root_iam_credentials_request = ahvac.AwsConfigureRootIamCredentialsRequest() # AwsConfigureRootIamCredentialsRequest | 

    try:
        await api_instance.aws_configure_root_iam_credentials(aws_mount_path, aws_configure_root_iam_credentials_request)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_configure_root_iam_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_root_iam_credentials_request** | [**AwsConfigureRootIamCredentialsRequest**](AwsConfigureRootIamCredentialsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_delete_role**
> aws_delete_role(name, aws_mount_path)

Read, write and reference IAM policies that access keys can be made for.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        # Read, write and reference IAM policies that access keys can be made for.
        await api_instance.aws_delete_role(name, aws_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_delete_static_roles_name**
> aws_delete_static_roles_name(name, aws_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of this role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_static_roles_name(name, aws_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_delete_static_roles_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of this role. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_generate_credentials**
> aws_generate_credentials(name, aws_mount_path, role_arn=role_arn, role_session_name=role_session_name, ttl=ttl)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    role_arn = 'role_arn_example' # str | ARN of role to assume when credential_type is assumed_role (optional)
    role_session_name = 'role_session_name_example' # str | Session name to use when assuming role. Max chars: 64 (optional)
    ttl = '3600' # str | Lifetime of the returned credentials in seconds (optional) (default to '3600')

    try:
        await api_instance.aws_generate_credentials(name, aws_mount_path, role_arn=role_arn, role_session_name=role_session_name, ttl=ttl)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **role_arn** | **str**| ARN of role to assume when credential_type is assumed_role | [optional] 
 **role_session_name** | **str**| Session name to use when assuming role. Max chars: 64 | [optional] 
 **ttl** | **str**| Lifetime of the returned credentials in seconds | [optional] [default to &#39;3600&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_generate_credentials_with_parameters**
> aws_generate_credentials_with_parameters(name, aws_mount_path, aws_generate_credentials_with_parameters_request)



### Example


```python
import ahvac
from ahvac.models.aws_generate_credentials_with_parameters_request import AwsGenerateCredentialsWithParametersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_generate_credentials_with_parameters_request = ahvac.AwsGenerateCredentialsWithParametersRequest() # AwsGenerateCredentialsWithParametersRequest | 

    try:
        await api_instance.aws_generate_credentials_with_parameters(name, aws_mount_path, aws_generate_credentials_with_parameters_request)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_generate_credentials_with_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_generate_credentials_with_parameters_request** | [**AwsGenerateCredentialsWithParametersRequest**](AwsGenerateCredentialsWithParametersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_generate_sts_credentials**
> aws_generate_sts_credentials(name, aws_mount_path, role_arn=role_arn, role_session_name=role_session_name, ttl=ttl)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    role_arn = 'role_arn_example' # str | ARN of role to assume when credential_type is assumed_role (optional)
    role_session_name = 'role_session_name_example' # str | Session name to use when assuming role. Max chars: 64 (optional)
    ttl = '3600' # str | Lifetime of the returned credentials in seconds (optional) (default to '3600')

    try:
        await api_instance.aws_generate_sts_credentials(name, aws_mount_path, role_arn=role_arn, role_session_name=role_session_name, ttl=ttl)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_generate_sts_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **role_arn** | **str**| ARN of role to assume when credential_type is assumed_role | [optional] 
 **role_session_name** | **str**| Session name to use when assuming role. Max chars: 64 | [optional] 
 **ttl** | **str**| Lifetime of the returned credentials in seconds | [optional] [default to &#39;3600&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_generate_sts_credentials_with_parameters**
> aws_generate_sts_credentials_with_parameters(name, aws_mount_path, aws_generate_sts_credentials_with_parameters_request)



### Example


```python
import ahvac
from ahvac.models.aws_generate_sts_credentials_with_parameters_request import AwsGenerateStsCredentialsWithParametersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_generate_sts_credentials_with_parameters_request = ahvac.AwsGenerateStsCredentialsWithParametersRequest() # AwsGenerateStsCredentialsWithParametersRequest | 

    try:
        await api_instance.aws_generate_sts_credentials_with_parameters(name, aws_mount_path, aws_generate_sts_credentials_with_parameters_request)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_generate_sts_credentials_with_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_generate_sts_credentials_with_parameters_request** | [**AwsGenerateStsCredentialsWithParametersRequest**](AwsGenerateStsCredentialsWithParametersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_list_roles**
> StandardListResponse aws_list_roles(aws_mount_path, list)

List the existing roles in this backend

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        # List the existing roles in this backend
        api_response = await api_instance.aws_list_roles(aws_mount_path, list)
        print("The response of SecretsApi->aws_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_read_lease_configuration**
> aws_read_lease_configuration(aws_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_lease_configuration(aws_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_read_lease_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_read_role**
> aws_read_role(name, aws_mount_path)

Read, write and reference IAM policies that access keys can be made for.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        # Read, write and reference IAM policies that access keys can be made for.
        await api_instance.aws_read_role(name, aws_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_read_root_iam_credentials_configuration**
> aws_read_root_iam_credentials_configuration(aws_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_root_iam_credentials_configuration(aws_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_read_root_iam_credentials_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_read_static_creds_name**
> AwsReadStaticCredsNameResponse aws_read_static_creds_name(name, aws_mount_path)



### Example


```python
import ahvac
from ahvac.models.aws_read_static_creds_name_response import AwsReadStaticCredsNameResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of this role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        api_response = await api_instance.aws_read_static_creds_name(name, aws_mount_path)
        print("The response of SecretsApi->aws_read_static_creds_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_read_static_creds_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of this role. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

[**AwsReadStaticCredsNameResponse**](AwsReadStaticCredsNameResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_read_static_roles_name**
> AwsReadStaticRolesNameResponse aws_read_static_roles_name(name, aws_mount_path)



### Example


```python
import ahvac
from ahvac.models.aws_read_static_roles_name_response import AwsReadStaticRolesNameResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of this role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        api_response = await api_instance.aws_read_static_roles_name(name, aws_mount_path)
        print("The response of SecretsApi->aws_read_static_roles_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_read_static_roles_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of this role. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

[**AwsReadStaticRolesNameResponse**](AwsReadStaticRolesNameResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_rotate_root_iam_credentials**
> aws_rotate_root_iam_credentials(aws_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_rotate_root_iam_credentials(aws_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_rotate_root_iam_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_write_role**
> aws_write_role(name, aws_mount_path, aws_write_role_request)

Read, write and reference IAM policies that access keys can be made for.

### Example


```python
import ahvac
from ahvac.models.aws_write_role_request import AwsWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_write_role_request = ahvac.AwsWriteRoleRequest() # AwsWriteRoleRequest | 

    try:
        # Read, write and reference IAM policies that access keys can be made for.
        await api_instance.aws_write_role(name, aws_mount_path, aws_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_write_role_request** | [**AwsWriteRoleRequest**](AwsWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_write_static_roles_name**
> AwsWriteStaticRolesNameResponse aws_write_static_roles_name(name, aws_mount_path, aws_write_static_roles_name_request)



### Example


```python
import ahvac
from ahvac.models.aws_write_static_roles_name_request import AwsWriteStaticRolesNameRequest
from ahvac.models.aws_write_static_roles_name_response import AwsWriteStaticRolesNameResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of this role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_write_static_roles_name_request = ahvac.AwsWriteStaticRolesNameRequest() # AwsWriteStaticRolesNameRequest | 

    try:
        api_response = await api_instance.aws_write_static_roles_name(name, aws_mount_path, aws_write_static_roles_name_request)
        print("The response of SecretsApi->aws_write_static_roles_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->aws_write_static_roles_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of this role. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_write_static_roles_name_request** | [**AwsWriteStaticRolesNameRequest**](AwsWriteStaticRolesNameRequest.md)|  | 

### Return type

[**AwsWriteStaticRolesNameResponse**](AwsWriteStaticRolesNameResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_configure**
> azure_configure(azure_mount_path, azure_configure_request)



### Example


```python
import ahvac
from ahvac.models.azure_configure_request import AzureConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')
    azure_configure_request = ahvac.AzureConfigureRequest() # AzureConfigureRequest | 

    try:
        await api_instance.azure_configure(azure_mount_path, azure_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]
 **azure_configure_request** | [**AzureConfigureRequest**](AzureConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_delete_configuration**
> azure_delete_configuration(azure_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_delete_configuration(azure_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_delete_role**
> azure_delete_role(name, azure_mount_path)

Manage the Vault roles used to generate Azure credentials.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        # Manage the Vault roles used to generate Azure credentials.
        await api_instance.azure_delete_role(name, azure_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_list_roles**
> StandardListResponse azure_list_roles(azure_mount_path, list)

List existing roles.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')
    list = 'list_example' # str | Must be set to `true`

    try:
        # List existing roles.
        api_response = await api_instance.azure_list_roles(azure_mount_path, list)
        print("The response of SecretsApi->azure_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_read_configuration**
> azure_read_configuration(azure_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_read_configuration(azure_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_read_role**
> azure_read_role(name, azure_mount_path)

Manage the Vault roles used to generate Azure credentials.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        # Manage the Vault roles used to generate Azure credentials.
        await api_instance.azure_read_role(name, azure_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_request_service_principal_credentials**
> azure_request_service_principal_credentials(role, azure_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | Name of the Vault role
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_request_service_principal_credentials(role, azure_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_request_service_principal_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the Vault role | 
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_rotate_root**
> azure_rotate_root(azure_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_rotate_root(azure_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_rotate_root: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_write_role**
> azure_write_role(name, azure_mount_path, azure_write_role_request)

Manage the Vault roles used to generate Azure credentials.

### Example


```python
import ahvac
from ahvac.models.azure_write_role_request import AzureWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')
    azure_write_role_request = ahvac.AzureWriteRoleRequest() # AzureWriteRoleRequest | 

    try:
        # Manage the Vault roles used to generate Azure credentials.
        await api_instance.azure_write_role(name, azure_mount_path, azure_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->azure_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]
 **azure_write_role_request** | [**AzureWriteRoleRequest**](AzureWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consul_configure_access**
> consul_configure_access(consul_mount_path, consul_configure_access_request)



### Example


```python
import ahvac
from ahvac.models.consul_configure_access_request import ConsulConfigureAccessRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    consul_mount_path = 'consul' # str | Path that the backend was mounted at (default to 'consul')
    consul_configure_access_request = ahvac.ConsulConfigureAccessRequest() # ConsulConfigureAccessRequest | 

    try:
        await api_instance.consul_configure_access(consul_mount_path, consul_configure_access_request)
    except Exception as e:
        print("Exception when calling SecretsApi->consul_configure_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consul_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;consul&#39;]
 **consul_configure_access_request** | [**ConsulConfigureAccessRequest**](ConsulConfigureAccessRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consul_delete_role**
> consul_delete_role(name, consul_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    consul_mount_path = 'consul' # str | Path that the backend was mounted at (default to 'consul')

    try:
        await api_instance.consul_delete_role(name, consul_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->consul_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **consul_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;consul&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consul_generate_credentials**
> consul_generate_credentials(role, consul_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | Name of the role.
    consul_mount_path = 'consul' # str | Path that the backend was mounted at (default to 'consul')

    try:
        await api_instance.consul_generate_credentials(role, consul_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->consul_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
 **consul_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;consul&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consul_list_roles**
> StandardListResponse consul_list_roles(consul_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    consul_mount_path = 'consul' # str | Path that the backend was mounted at (default to 'consul')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.consul_list_roles(consul_mount_path, list)
        print("The response of SecretsApi->consul_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->consul_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consul_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;consul&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consul_read_access_configuration**
> consul_read_access_configuration(consul_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    consul_mount_path = 'consul' # str | Path that the backend was mounted at (default to 'consul')

    try:
        await api_instance.consul_read_access_configuration(consul_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->consul_read_access_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consul_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;consul&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consul_read_role**
> consul_read_role(name, consul_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    consul_mount_path = 'consul' # str | Path that the backend was mounted at (default to 'consul')

    try:
        await api_instance.consul_read_role(name, consul_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->consul_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **consul_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;consul&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consul_write_role**
> consul_write_role(name, consul_mount_path, consul_write_role_request)



### Example


```python
import ahvac
from ahvac.models.consul_write_role_request import ConsulWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    consul_mount_path = 'consul' # str | Path that the backend was mounted at (default to 'consul')
    consul_write_role_request = ahvac.ConsulWriteRoleRequest() # ConsulWriteRoleRequest | 

    try:
        await api_instance.consul_write_role(name, consul_mount_path, consul_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->consul_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **consul_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;consul&#39;]
 **consul_write_role_request** | [**ConsulWriteRoleRequest**](ConsulWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubbyhole_delete**
> cubbyhole_delete(path)

Deletes the secret at the specified location.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Specifies the path of the secret.

    try:
        # Deletes the secret at the specified location.
        await api_instance.cubbyhole_delete(path)
    except Exception as e:
        print("Exception when calling SecretsApi->cubbyhole_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Specifies the path of the secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubbyhole_list**
> StandardListResponse cubbyhole_list(path, list)

List secret entries at the specified location.

Folders are suffixed with /. The input must be a folder; list on a file will not return a value. The values themselves are not accessible via this command.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Specifies the path of the secret.
    list = 'list_example' # str | Must be set to `true`

    try:
        # List secret entries at the specified location.
        api_response = await api_instance.cubbyhole_list(path, list)
        print("The response of SecretsApi->cubbyhole_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->cubbyhole_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Specifies the path of the secret. | 
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubbyhole_read**
> cubbyhole_read(path)

Retrieve the secret at the specified location.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Specifies the path of the secret.

    try:
        # Retrieve the secret at the specified location.
        await api_instance.cubbyhole_read(path)
    except Exception as e:
        print("Exception when calling SecretsApi->cubbyhole_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Specifies the path of the secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubbyhole_write**
> cubbyhole_write(path, request_body)

Store a secret at the specified location.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Specifies the path of the secret.
    request_body = None # Dict[str, object] | 

    try:
        # Store a secret at the specified location.
        await api_instance.cubbyhole_write(path, request_body)
    except Exception as e:
        print("Exception when calling SecretsApi->cubbyhole_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Specifies the path of the secret. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_configure_connection**
> database_configure_connection(name, database_mount_path, database_configure_connection_request)



### Example


```python
import ahvac
from ahvac.models.database_configure_connection_request import DatabaseConfigureConnectionRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of this database connection
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')
    database_configure_connection_request = ahvac.DatabaseConfigureConnectionRequest() # DatabaseConfigureConnectionRequest | 

    try:
        await api_instance.database_configure_connection(name, database_mount_path, database_configure_connection_request)
    except Exception as e:
        print("Exception when calling SecretsApi->database_configure_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of this database connection | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]
 **database_configure_connection_request** | [**DatabaseConfigureConnectionRequest**](DatabaseConfigureConnectionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_delete_connection_configuration**
> database_delete_connection_configuration(name, database_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of this database connection
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        await api_instance.database_delete_connection_configuration(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_delete_connection_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of this database connection | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_delete_role**
> database_delete_role(name, database_mount_path)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        # Manage the roles that can be created with this backend.
        await api_instance.database_delete_role(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_delete_static_role**
> database_delete_static_role(name, database_mount_path)

Manage the static roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        # Manage the static roles that can be created with this backend.
        await api_instance.database_delete_static_role(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_delete_static_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_generate_credentials**
> database_generate_credentials(name, database_mount_path)

Request database credentials for a certain role.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        # Request database credentials for a certain role.
        await api_instance.database_generate_credentials(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_list_connections**
> StandardListResponse database_list_connections(database_mount_path, list)

Configure connection details to a database plugin.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Configure connection details to a database plugin.
        api_response = await api_instance.database_list_connections(database_mount_path, list)
        print("The response of SecretsApi->database_list_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->database_list_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_list_roles**
> StandardListResponse database_list_roles(database_mount_path, list)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage the roles that can be created with this backend.
        api_response = await api_instance.database_list_roles(database_mount_path, list)
        print("The response of SecretsApi->database_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->database_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_list_static_roles**
> StandardListResponse database_list_static_roles(database_mount_path, list)

Manage the static roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage the static roles that can be created with this backend.
        api_response = await api_instance.database_list_static_roles(database_mount_path, list)
        print("The response of SecretsApi->database_list_static_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->database_list_static_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_read_connection_configuration**
> database_read_connection_configuration(name, database_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of this database connection
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        await api_instance.database_read_connection_configuration(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_read_connection_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of this database connection | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_read_role**
> database_read_role(name, database_mount_path)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        # Manage the roles that can be created with this backend.
        await api_instance.database_read_role(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_read_static_role**
> database_read_static_role(name, database_mount_path)

Manage the static roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        # Manage the static roles that can be created with this backend.
        await api_instance.database_read_static_role(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_read_static_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_read_static_role_credentials**
> database_read_static_role_credentials(name, database_mount_path)

Request database credentials for a certain static role. These credentials are rotated periodically.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the static role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        # Request database credentials for a certain static role. These credentials are rotated periodically.
        await api_instance.database_read_static_role_credentials(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_read_static_role_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the static role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_reset_connection**
> database_reset_connection(name, database_mount_path)

Resets a database plugin.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of this database connection
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        # Resets a database plugin.
        await api_instance.database_reset_connection(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_reset_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of this database connection | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_rotate_root_credentials**
> database_rotate_root_credentials(name, database_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of this database connection
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        await api_instance.database_rotate_root_credentials(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_rotate_root_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of this database connection | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_rotate_static_role_credentials**
> database_rotate_static_role_credentials(name, database_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the static role
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')

    try:
        await api_instance.database_rotate_static_role_credentials(name, database_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->database_rotate_static_role_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the static role | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_write_role**
> database_write_role(name, database_mount_path, database_write_role_request)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.database_write_role_request import DatabaseWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')
    database_write_role_request = ahvac.DatabaseWriteRoleRequest() # DatabaseWriteRoleRequest | 

    try:
        # Manage the roles that can be created with this backend.
        await api_instance.database_write_role(name, database_mount_path, database_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->database_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]
 **database_write_role_request** | [**DatabaseWriteRoleRequest**](DatabaseWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_write_static_role**
> database_write_static_role(name, database_mount_path, database_write_static_role_request)

Manage the static roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.database_write_static_role_request import DatabaseWriteStaticRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    database_mount_path = 'database' # str | Path that the backend was mounted at (default to 'database')
    database_write_static_role_request = ahvac.DatabaseWriteStaticRoleRequest() # DatabaseWriteStaticRoleRequest | 

    try:
        # Manage the static roles that can be created with this backend.
        await api_instance.database_write_static_role(name, database_mount_path, database_write_static_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->database_write_static_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **database_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;database&#39;]
 **database_write_static_role_request** | [**DatabaseWriteStaticRoleRequest**](DatabaseWriteStaticRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_configure**
> google_cloud_configure(gcp_mount_path, google_cloud_configure_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_configure_request import GoogleCloudConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_configure_request = ahvac.GoogleCloudConfigureRequest() # GoogleCloudConfigureRequest | 

    try:
        await api_instance.google_cloud_configure(gcp_mount_path, google_cloud_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_configure_request** | [**GoogleCloudConfigureRequest**](GoogleCloudConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_delete_impersonated_account**
> google_cloud_delete_impersonated_account(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name to refer to this impersonated account in Vault. Cannot be updated.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_delete_impersonated_account(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_delete_impersonated_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name to refer to this impersonated account in Vault. Cannot be updated. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_delete_roleset**
> google_cloud_delete_roleset(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_delete_roleset(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_delete_roleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_delete_static_account**
> google_cloud_delete_static_account(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name to refer to this static account in Vault. Cannot be updated.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_delete_static_account(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_delete_static_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name to refer to this static account in Vault. Cannot be updated. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_impersonated_account_access_token**
> google_cloud_generate_impersonated_account_access_token(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the impersonated account.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_impersonated_account_access_token(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_impersonated_account_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the impersonated account. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_impersonated_account_access_token2**
> google_cloud_generate_impersonated_account_access_token2(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the impersonated account.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_impersonated_account_access_token2(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_impersonated_account_access_token2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the impersonated account. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_access_token**
> google_cloud_generate_roleset_access_token(roleset, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_roleset_access_token(roleset, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_access_token2**
> google_cloud_generate_roleset_access_token2(roleset, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_roleset_access_token2(roleset, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_access_token2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_access_token3**
> google_cloud_generate_roleset_access_token3(roleset, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_roleset_access_token3(roleset, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_access_token3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_access_token4**
> google_cloud_generate_roleset_access_token4(roleset, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_roleset_access_token4(roleset, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_access_token4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_key**
> google_cloud_generate_roleset_key(roleset, gcp_mount_path, google_cloud_generate_roleset_key_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_generate_roleset_key_request import GoogleCloudGenerateRolesetKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_generate_roleset_key_request = ahvac.GoogleCloudGenerateRolesetKeyRequest() # GoogleCloudGenerateRolesetKeyRequest | 

    try:
        await api_instance.google_cloud_generate_roleset_key(roleset, gcp_mount_path, google_cloud_generate_roleset_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_generate_roleset_key_request** | [**GoogleCloudGenerateRolesetKeyRequest**](GoogleCloudGenerateRolesetKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_key2**
> google_cloud_generate_roleset_key2(roleset, gcp_mount_path, key_algorithm=key_algorithm, key_type=key_type, ttl=ttl)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    key_algorithm = 'KEY_ALG_RSA_2048' # str | Private key algorithm for service account key - defaults to KEY_ALG_RSA_2048\" (optional) (default to 'KEY_ALG_RSA_2048')
    key_type = 'TYPE_GOOGLE_CREDENTIALS_FILE' # str | Private key type for service account key - defaults to TYPE_GOOGLE_CREDENTIALS_FILE\" (optional) (default to 'TYPE_GOOGLE_CREDENTIALS_FILE')
    ttl = 'ttl_example' # str | Lifetime of the service account key (optional)

    try:
        await api_instance.google_cloud_generate_roleset_key2(roleset, gcp_mount_path, key_algorithm=key_algorithm, key_type=key_type, ttl=ttl)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_key2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **key_algorithm** | **str**| Private key algorithm for service account key - defaults to KEY_ALG_RSA_2048\&quot; | [optional] [default to &#39;KEY_ALG_RSA_2048&#39;]
 **key_type** | **str**| Private key type for service account key - defaults to TYPE_GOOGLE_CREDENTIALS_FILE\&quot; | [optional] [default to &#39;TYPE_GOOGLE_CREDENTIALS_FILE&#39;]
 **ttl** | **str**| Lifetime of the service account key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_key3**
> google_cloud_generate_roleset_key3(roleset, gcp_mount_path, google_cloud_generate_roleset_key3_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_generate_roleset_key3_request import GoogleCloudGenerateRolesetKey3Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_generate_roleset_key3_request = ahvac.GoogleCloudGenerateRolesetKey3Request() # GoogleCloudGenerateRolesetKey3Request | 

    try:
        await api_instance.google_cloud_generate_roleset_key3(roleset, gcp_mount_path, google_cloud_generate_roleset_key3_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_key3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_generate_roleset_key3_request** | [**GoogleCloudGenerateRolesetKey3Request**](GoogleCloudGenerateRolesetKey3Request.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_roleset_key4**
> google_cloud_generate_roleset_key4(roleset, gcp_mount_path, key_algorithm=key_algorithm, key_type=key_type, ttl=ttl)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    roleset = 'roleset_example' # str | Required. Name of the role set.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    key_algorithm = 'KEY_ALG_RSA_2048' # str | Private key algorithm for service account key - defaults to KEY_ALG_RSA_2048\" (optional) (default to 'KEY_ALG_RSA_2048')
    key_type = 'TYPE_GOOGLE_CREDENTIALS_FILE' # str | Private key type for service account key - defaults to TYPE_GOOGLE_CREDENTIALS_FILE\" (optional) (default to 'TYPE_GOOGLE_CREDENTIALS_FILE')
    ttl = 'ttl_example' # str | Lifetime of the service account key (optional)

    try:
        await api_instance.google_cloud_generate_roleset_key4(roleset, gcp_mount_path, key_algorithm=key_algorithm, key_type=key_type, ttl=ttl)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_roleset_key4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleset** | **str**| Required. Name of the role set. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **key_algorithm** | **str**| Private key algorithm for service account key - defaults to KEY_ALG_RSA_2048\&quot; | [optional] [default to &#39;KEY_ALG_RSA_2048&#39;]
 **key_type** | **str**| Private key type for service account key - defaults to TYPE_GOOGLE_CREDENTIALS_FILE\&quot; | [optional] [default to &#39;TYPE_GOOGLE_CREDENTIALS_FILE&#39;]
 **ttl** | **str**| Lifetime of the service account key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_static_account_access_token**
> google_cloud_generate_static_account_access_token(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the static account.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_static_account_access_token(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_static_account_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the static account. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_static_account_access_token2**
> google_cloud_generate_static_account_access_token2(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the static account.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_generate_static_account_access_token2(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_static_account_access_token2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the static account. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_static_account_key**
> google_cloud_generate_static_account_key(name, gcp_mount_path, google_cloud_generate_static_account_key_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_generate_static_account_key_request import GoogleCloudGenerateStaticAccountKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the static account.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_generate_static_account_key_request = ahvac.GoogleCloudGenerateStaticAccountKeyRequest() # GoogleCloudGenerateStaticAccountKeyRequest | 

    try:
        await api_instance.google_cloud_generate_static_account_key(name, gcp_mount_path, google_cloud_generate_static_account_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_static_account_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the static account. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_generate_static_account_key_request** | [**GoogleCloudGenerateStaticAccountKeyRequest**](GoogleCloudGenerateStaticAccountKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_generate_static_account_key2**
> google_cloud_generate_static_account_key2(name, gcp_mount_path, key_algorithm=key_algorithm, key_type=key_type, ttl=ttl)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the static account.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    key_algorithm = 'KEY_ALG_RSA_2048' # str | Private key algorithm for service account key. Defaults to KEY_ALG_RSA_2048.\" (optional) (default to 'KEY_ALG_RSA_2048')
    key_type = 'TYPE_GOOGLE_CREDENTIALS_FILE' # str | Private key type for service account key. Defaults to TYPE_GOOGLE_CREDENTIALS_FILE.\" (optional) (default to 'TYPE_GOOGLE_CREDENTIALS_FILE')
    ttl = 'ttl_example' # str | Lifetime of the service account key (optional)

    try:
        await api_instance.google_cloud_generate_static_account_key2(name, gcp_mount_path, key_algorithm=key_algorithm, key_type=key_type, ttl=ttl)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_generate_static_account_key2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the static account. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **key_algorithm** | **str**| Private key algorithm for service account key. Defaults to KEY_ALG_RSA_2048.\&quot; | [optional] [default to &#39;KEY_ALG_RSA_2048&#39;]
 **key_type** | **str**| Private key type for service account key. Defaults to TYPE_GOOGLE_CREDENTIALS_FILE.\&quot; | [optional] [default to &#39;TYPE_GOOGLE_CREDENTIALS_FILE&#39;]
 **ttl** | **str**| Lifetime of the service account key | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_configure**
> google_cloud_kms_configure(gcpkms_mount_path, google_cloud_kms_configure_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_configure_request import GoogleCloudKmsConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_configure_request = ahvac.GoogleCloudKmsConfigureRequest() # GoogleCloudKmsConfigureRequest | 

    try:
        await api_instance.google_cloud_kms_configure(gcpkms_mount_path, google_cloud_kms_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_configure_request** | [**GoogleCloudKmsConfigureRequest**](GoogleCloudKmsConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_configure_key**
> google_cloud_kms_configure_key(key, gcpkms_mount_path, google_cloud_kms_configure_key_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_configure_key_request import GoogleCloudKmsConfigureKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_configure_key_request = ahvac.GoogleCloudKmsConfigureKeyRequest() # GoogleCloudKmsConfigureKeyRequest | 

    try:
        await api_instance.google_cloud_kms_configure_key(key, gcpkms_mount_path, google_cloud_kms_configure_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_configure_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_configure_key_request** | [**GoogleCloudKmsConfigureKeyRequest**](GoogleCloudKmsConfigureKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_decrypt**
> google_cloud_kms_decrypt(key, gcpkms_mount_path, google_cloud_kms_decrypt_request)

Decrypt a ciphertext value using a named key

### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_decrypt_request import GoogleCloudKmsDecryptRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault to use for decryption. This key must already exist in Vault and must map back to a Google Cloud KMS key.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_decrypt_request = ahvac.GoogleCloudKmsDecryptRequest() # GoogleCloudKmsDecryptRequest | 

    try:
        # Decrypt a ciphertext value using a named key
        await api_instance.google_cloud_kms_decrypt(key, gcpkms_mount_path, google_cloud_kms_decrypt_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_decrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault to use for decryption. This key must already exist in Vault and must map back to a Google Cloud KMS key. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_decrypt_request** | [**GoogleCloudKmsDecryptRequest**](GoogleCloudKmsDecryptRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_delete_configuration**
> google_cloud_kms_delete_configuration(gcpkms_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        await api_instance.google_cloud_kms_delete_configuration(gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_delete_key**
> google_cloud_kms_delete_key(key, gcpkms_mount_path)

Interact with crypto keys in Vault and Google Cloud KMS

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        # Interact with crypto keys in Vault and Google Cloud KMS
        await api_instance.google_cloud_kms_delete_key(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_deregister_key**
> google_cloud_kms_deregister_key(key, gcpkms_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key to deregister in Vault. If the key exists in Google Cloud KMS, it will be left untouched.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        await api_instance.google_cloud_kms_deregister_key(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_deregister_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key to deregister in Vault. If the key exists in Google Cloud KMS, it will be left untouched. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_deregister_key2**
> google_cloud_kms_deregister_key2(key, gcpkms_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key to deregister in Vault. If the key exists in Google Cloud KMS, it will be left untouched.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        await api_instance.google_cloud_kms_deregister_key2(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_deregister_key2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key to deregister in Vault. If the key exists in Google Cloud KMS, it will be left untouched. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_encrypt**
> google_cloud_kms_encrypt(key, gcpkms_mount_path, google_cloud_kms_encrypt_request)

Encrypt a plaintext value using a named key

### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_encrypt_request import GoogleCloudKmsEncryptRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault to use for encryption. This key must already exist in Vault and must map back to a Google Cloud KMS key.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_encrypt_request = ahvac.GoogleCloudKmsEncryptRequest() # GoogleCloudKmsEncryptRequest | 

    try:
        # Encrypt a plaintext value using a named key
        await api_instance.google_cloud_kms_encrypt(key, gcpkms_mount_path, google_cloud_kms_encrypt_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_encrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault to use for encryption. This key must already exist in Vault and must map back to a Google Cloud KMS key. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_encrypt_request** | [**GoogleCloudKmsEncryptRequest**](GoogleCloudKmsEncryptRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_list_keys**
> StandardListResponse google_cloud_kms_list_keys(gcpkms_mount_path, list)

List named keys

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    list = 'list_example' # str | Must be set to `true`

    try:
        # List named keys
        api_response = await api_instance.google_cloud_kms_list_keys(gcpkms_mount_path, list)
        print("The response of SecretsApi->google_cloud_kms_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_list_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_read_configuration**
> google_cloud_kms_read_configuration(gcpkms_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        await api_instance.google_cloud_kms_read_configuration(gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_read_key**
> google_cloud_kms_read_key(key, gcpkms_mount_path)

Interact with crypto keys in Vault and Google Cloud KMS

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        # Interact with crypto keys in Vault and Google Cloud KMS
        await api_instance.google_cloud_kms_read_key(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_read_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_read_key_configuration**
> google_cloud_kms_read_key_configuration(key, gcpkms_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        await api_instance.google_cloud_kms_read_key_configuration(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_read_key_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_reencrypt**
> google_cloud_kms_reencrypt(key, gcpkms_mount_path, google_cloud_kms_reencrypt_request)

Re-encrypt existing ciphertext data to a new version

### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_reencrypt_request import GoogleCloudKmsReencryptRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key to use for encryption. This key must already exist in Vault and Google Cloud KMS.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_reencrypt_request = ahvac.GoogleCloudKmsReencryptRequest() # GoogleCloudKmsReencryptRequest | 

    try:
        # Re-encrypt existing ciphertext data to a new version
        await api_instance.google_cloud_kms_reencrypt(key, gcpkms_mount_path, google_cloud_kms_reencrypt_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_reencrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key to use for encryption. This key must already exist in Vault and Google Cloud KMS. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_reencrypt_request** | [**GoogleCloudKmsReencryptRequest**](GoogleCloudKmsReencryptRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_register_key**
> google_cloud_kms_register_key(key, gcpkms_mount_path, google_cloud_kms_register_key_request)

Register an existing crypto key in Google Cloud KMS

### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_register_key_request import GoogleCloudKmsRegisterKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key to register in Vault. This will be the named used to refer to the underlying crypto key when encrypting or decrypting data.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_register_key_request = ahvac.GoogleCloudKmsRegisterKeyRequest() # GoogleCloudKmsRegisterKeyRequest | 

    try:
        # Register an existing crypto key in Google Cloud KMS
        await api_instance.google_cloud_kms_register_key(key, gcpkms_mount_path, google_cloud_kms_register_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_register_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key to register in Vault. This will be the named used to refer to the underlying crypto key when encrypting or decrypting data. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_register_key_request** | [**GoogleCloudKmsRegisterKeyRequest**](GoogleCloudKmsRegisterKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_retrieve_public_key**
> google_cloud_kms_retrieve_public_key(key, gcpkms_mount_path)

Retrieve the public key associated with the named key

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key for which to get the public key. This key must already exist in Vault and Google Cloud KMS.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        # Retrieve the public key associated with the named key
        await api_instance.google_cloud_kms_retrieve_public_key(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_retrieve_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key for which to get the public key. This key must already exist in Vault and Google Cloud KMS. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_rotate_key**
> google_cloud_kms_rotate_key(key, gcpkms_mount_path)

Rotate a crypto key to a new primary version

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key to rotate. This key must already be registered with Vault and point to a valid Google Cloud KMS crypto key.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        # Rotate a crypto key to a new primary version
        await api_instance.google_cloud_kms_rotate_key(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_rotate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key to rotate. This key must already be registered with Vault and point to a valid Google Cloud KMS crypto key. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_sign**
> google_cloud_kms_sign(key, gcpkms_mount_path, google_cloud_kms_sign_request)

Signs a message or digest using a named key

### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_sign_request import GoogleCloudKmsSignRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault to use for signing. This key must already exist in Vault and must map back to a Google Cloud KMS key.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_sign_request = ahvac.GoogleCloudKmsSignRequest() # GoogleCloudKmsSignRequest | 

    try:
        # Signs a message or digest using a named key
        await api_instance.google_cloud_kms_sign(key, gcpkms_mount_path, google_cloud_kms_sign_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_sign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault to use for signing. This key must already exist in Vault and must map back to a Google Cloud KMS key. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_sign_request** | [**GoogleCloudKmsSignRequest**](GoogleCloudKmsSignRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_trim_key_versions**
> google_cloud_kms_trim_key_versions(key, gcpkms_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        await api_instance.google_cloud_kms_trim_key_versions(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_trim_key_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_trim_key_versions2**
> google_cloud_kms_trim_key_versions2(key, gcpkms_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')

    try:
        await api_instance.google_cloud_kms_trim_key_versions2(key, gcpkms_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_trim_key_versions2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_verify**
> google_cloud_kms_verify(key, gcpkms_mount_path, google_cloud_kms_verify_request)

Verify a signature using a named key

### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_verify_request import GoogleCloudKmsVerifyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault to use for verification. This key must already exist in Vault and must map back to a Google Cloud KMS key.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_verify_request = ahvac.GoogleCloudKmsVerifyRequest() # GoogleCloudKmsVerifyRequest | 

    try:
        # Verify a signature using a named key
        await api_instance.google_cloud_kms_verify(key, gcpkms_mount_path, google_cloud_kms_verify_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault to use for verification. This key must already exist in Vault and must map back to a Google Cloud KMS key. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_verify_request** | [**GoogleCloudKmsVerifyRequest**](GoogleCloudKmsVerifyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_kms_write_key**
> google_cloud_kms_write_key(key, gcpkms_mount_path, google_cloud_kms_write_key_request)

Interact with crypto keys in Vault and Google Cloud KMS

### Example


```python
import ahvac
from ahvac.models.google_cloud_kms_write_key_request import GoogleCloudKmsWriteKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key = 'key_example' # str | Name of the key in Vault.
    gcpkms_mount_path = 'gcpkms' # str | Path that the backend was mounted at (default to 'gcpkms')
    google_cloud_kms_write_key_request = ahvac.GoogleCloudKmsWriteKeyRequest() # GoogleCloudKmsWriteKeyRequest | 

    try:
        # Interact with crypto keys in Vault and Google Cloud KMS
        await api_instance.google_cloud_kms_write_key(key, gcpkms_mount_path, google_cloud_kms_write_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_kms_write_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Name of the key in Vault. | 
 **gcpkms_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcpkms&#39;]
 **google_cloud_kms_write_key_request** | [**GoogleCloudKmsWriteKeyRequest**](GoogleCloudKmsWriteKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_list_impersonated_accounts**
> StandardListResponse google_cloud_list_impersonated_accounts(gcp_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.google_cloud_list_impersonated_accounts(gcp_mount_path, list)
        print("The response of SecretsApi->google_cloud_list_impersonated_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_list_impersonated_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_list_impersonated_accounts2**
> StandardListResponse google_cloud_list_impersonated_accounts2(gcp_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.google_cloud_list_impersonated_accounts2(gcp_mount_path, list)
        print("The response of SecretsApi->google_cloud_list_impersonated_accounts2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_list_impersonated_accounts2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_list_rolesets**
> StandardListResponse google_cloud_list_rolesets(gcp_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.google_cloud_list_rolesets(gcp_mount_path, list)
        print("The response of SecretsApi->google_cloud_list_rolesets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_list_rolesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_list_rolesets2**
> StandardListResponse google_cloud_list_rolesets2(gcp_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.google_cloud_list_rolesets2(gcp_mount_path, list)
        print("The response of SecretsApi->google_cloud_list_rolesets2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_list_rolesets2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_list_static_accounts**
> StandardListResponse google_cloud_list_static_accounts(gcp_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.google_cloud_list_static_accounts(gcp_mount_path, list)
        print("The response of SecretsApi->google_cloud_list_static_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_list_static_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_list_static_accounts2**
> StandardListResponse google_cloud_list_static_accounts2(gcp_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.google_cloud_list_static_accounts2(gcp_mount_path, list)
        print("The response of SecretsApi->google_cloud_list_static_accounts2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_list_static_accounts2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_read_configuration**
> google_cloud_read_configuration(gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_read_configuration(gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_read_impersonated_account**
> google_cloud_read_impersonated_account(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name to refer to this impersonated account in Vault. Cannot be updated.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_read_impersonated_account(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_read_impersonated_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name to refer to this impersonated account in Vault. Cannot be updated. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_read_roleset**
> google_cloud_read_roleset(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_read_roleset(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_read_roleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_read_static_account**
> google_cloud_read_static_account(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name to refer to this static account in Vault. Cannot be updated.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_read_static_account(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_read_static_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name to refer to this static account in Vault. Cannot be updated. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_rotate_roleset**
> google_cloud_rotate_roleset(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_rotate_roleset(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_rotate_roleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_rotate_roleset_key**
> google_cloud_rotate_roleset_key(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_rotate_roleset_key(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_rotate_roleset_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_rotate_root_credentials**
> google_cloud_rotate_root_credentials(gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_rotate_root_credentials(gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_rotate_root_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_rotate_static_account_key**
> google_cloud_rotate_static_account_key(name, gcp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the account.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_rotate_static_account_key(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_rotate_static_account_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the account. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_write_impersonated_account**
> google_cloud_write_impersonated_account(name, gcp_mount_path, google_cloud_write_impersonated_account_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_write_impersonated_account_request import GoogleCloudWriteImpersonatedAccountRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name to refer to this impersonated account in Vault. Cannot be updated.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_write_impersonated_account_request = ahvac.GoogleCloudWriteImpersonatedAccountRequest() # GoogleCloudWriteImpersonatedAccountRequest | 

    try:
        await api_instance.google_cloud_write_impersonated_account(name, gcp_mount_path, google_cloud_write_impersonated_account_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_write_impersonated_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name to refer to this impersonated account in Vault. Cannot be updated. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_write_impersonated_account_request** | [**GoogleCloudWriteImpersonatedAccountRequest**](GoogleCloudWriteImpersonatedAccountRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_write_roleset**
> google_cloud_write_roleset(name, gcp_mount_path, google_cloud_write_roleset_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_write_roleset_request import GoogleCloudWriteRolesetRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_write_roleset_request = ahvac.GoogleCloudWriteRolesetRequest() # GoogleCloudWriteRolesetRequest | 

    try:
        await api_instance.google_cloud_write_roleset(name, gcp_mount_path, google_cloud_write_roleset_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_write_roleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_write_roleset_request** | [**GoogleCloudWriteRolesetRequest**](GoogleCloudWriteRolesetRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_write_static_account**
> google_cloud_write_static_account(name, gcp_mount_path, google_cloud_write_static_account_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_write_static_account_request import GoogleCloudWriteStaticAccountRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Required. Name to refer to this static account in Vault. Cannot be updated.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_write_static_account_request = ahvac.GoogleCloudWriteStaticAccountRequest() # GoogleCloudWriteStaticAccountRequest | 

    try:
        await api_instance.google_cloud_write_static_account(name, gcp_mount_path, google_cloud_write_static_account_request)
    except Exception as e:
        print("Exception when calling SecretsApi->google_cloud_write_static_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name to refer to this static account in Vault. Cannot be updated. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_write_static_account_request** | [**GoogleCloudWriteStaticAccountRequest**](GoogleCloudWriteStaticAccountRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_check_configuration**
> kubernetes_check_configuration(kubernetes_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        await api_instance.kubernetes_check_configuration(kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_check_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_configure**
> kubernetes_configure(kubernetes_mount_path, kubernetes_configure_request)



### Example


```python
import ahvac
from ahvac.models.kubernetes_configure_request import KubernetesConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    kubernetes_configure_request = ahvac.KubernetesConfigureRequest() # KubernetesConfigureRequest | 

    try:
        await api_instance.kubernetes_configure(kubernetes_mount_path, kubernetes_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]
 **kubernetes_configure_request** | [**KubernetesConfigureRequest**](KubernetesConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_delete_configuration**
> kubernetes_delete_configuration(kubernetes_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        await api_instance.kubernetes_delete_configuration(kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_delete_role**
> kubernetes_delete_role(name, kubernetes_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        await api_instance.kubernetes_delete_role(name, kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_generate_credentials**
> kubernetes_generate_credentials(name, kubernetes_mount_path, kubernetes_generate_credentials_request)



### Example


```python
import ahvac
from ahvac.models.kubernetes_generate_credentials_request import KubernetesGenerateCredentialsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the Vault role
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    kubernetes_generate_credentials_request = ahvac.KubernetesGenerateCredentialsRequest() # KubernetesGenerateCredentialsRequest | 

    try:
        await api_instance.kubernetes_generate_credentials(name, kubernetes_mount_path, kubernetes_generate_credentials_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Vault role | 
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]
 **kubernetes_generate_credentials_request** | [**KubernetesGenerateCredentialsRequest**](KubernetesGenerateCredentialsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_list_roles**
> StandardListResponse kubernetes_list_roles(kubernetes_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.kubernetes_list_roles(kubernetes_mount_path, list)
        print("The response of SecretsApi->kubernetes_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_read_configuration**
> kubernetes_read_configuration(kubernetes_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        await api_instance.kubernetes_read_configuration(kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_read_role**
> kubernetes_read_role(name, kubernetes_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        await api_instance.kubernetes_read_role(name, kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_write_role**
> kubernetes_write_role(name, kubernetes_mount_path, kubernetes_write_role_request)



### Example


```python
import ahvac
from ahvac.models.kubernetes_write_role_request import KubernetesWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    kubernetes_write_role_request = ahvac.KubernetesWriteRoleRequest() # KubernetesWriteRoleRequest | 

    try:
        await api_instance.kubernetes_write_role(name, kubernetes_mount_path, kubernetes_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kubernetes_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]
 **kubernetes_write_role_request** | [**KubernetesWriteRoleRequest**](KubernetesWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v1_delete**
> kv_v1_delete(path, kv_v1_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v1_mount_path = 'kv-v1' # str | Path that the backend was mounted at (default to 'kv-v1')

    try:
        await api_instance.kv_v1_delete(path, kv_v1_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v1_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v1_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v1&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v1_list**
> StandardListResponse kv_v1_list(path, kv_v1_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v1_mount_path = 'kv-v1' # str | Path that the backend was mounted at (default to 'kv-v1')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.kv_v1_list(path, kv_v1_mount_path, list)
        print("The response of SecretsApi->kv_v1_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v1_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v1_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v1&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v1_read**
> kv_v1_read(path, kv_v1_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v1_mount_path = 'kv-v1' # str | Path that the backend was mounted at (default to 'kv-v1')

    try:
        await api_instance.kv_v1_read(path, kv_v1_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v1_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v1_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v1&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v1_write**
> kv_v1_write(path, kv_v1_mount_path, request_body)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v1_mount_path = 'kv-v1' # str | Path that the backend was mounted at (default to 'kv-v1')
    request_body = None # Dict[str, object] | 

    try:
        await api_instance.kv_v1_write(path, kv_v1_mount_path, request_body)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v1_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v1_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v1&#39;]
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_configure**
> kv_v2_configure(kv_v2_mount_path, kv_v2_configure_request)

Configure backend level settings that are applied to every key in the key-value store.

### Example


```python
import ahvac
from ahvac.models.kv_v2_configure_request import KvV2ConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')
    kv_v2_configure_request = ahvac.KvV2ConfigureRequest() # KvV2ConfigureRequest | 

    try:
        # Configure backend level settings that are applied to every key in the key-value store.
        await api_instance.kv_v2_configure(kv_v2_mount_path, kv_v2_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]
 **kv_v2_configure_request** | [**KvV2ConfigureRequest**](KvV2ConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_delete**
> kv_v2_delete(path, kv_v2_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')

    try:
        await api_instance.kv_v2_delete(path, kv_v2_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_delete_metadata_and_all_versions**
> kv_v2_delete_metadata_and_all_versions(path, kv_v2_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')

    try:
        await api_instance.kv_v2_delete_metadata_and_all_versions(path, kv_v2_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_delete_metadata_and_all_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_delete_versions**
> kv_v2_delete_versions(path, kv_v2_mount_path, kv_v2_delete_versions_request)



### Example


```python
import ahvac
from ahvac.models.kv_v2_delete_versions_request import KvV2DeleteVersionsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')
    kv_v2_delete_versions_request = ahvac.KvV2DeleteVersionsRequest() # KvV2DeleteVersionsRequest | 

    try:
        await api_instance.kv_v2_delete_versions(path, kv_v2_mount_path, kv_v2_delete_versions_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_delete_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]
 **kv_v2_delete_versions_request** | [**KvV2DeleteVersionsRequest**](KvV2DeleteVersionsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_destroy_versions**
> kv_v2_destroy_versions(path, kv_v2_mount_path, kv_v2_destroy_versions_request)



### Example


```python
import ahvac
from ahvac.models.kv_v2_destroy_versions_request import KvV2DestroyVersionsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')
    kv_v2_destroy_versions_request = ahvac.KvV2DestroyVersionsRequest() # KvV2DestroyVersionsRequest | 

    try:
        await api_instance.kv_v2_destroy_versions(path, kv_v2_mount_path, kv_v2_destroy_versions_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_destroy_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]
 **kv_v2_destroy_versions_request** | [**KvV2DestroyVersionsRequest**](KvV2DestroyVersionsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_list**
> StandardListResponse kv_v2_list(path, kv_v2_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.kv_v2_list(path, kv_v2_mount_path, list)
        print("The response of SecretsApi->kv_v2_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_read**
> KvV2ReadResponse kv_v2_read(path, kv_v2_mount_path)



### Example


```python
import ahvac
from ahvac.models.kv_v2_read_response import KvV2ReadResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')

    try:
        api_response = await api_instance.kv_v2_read(path, kv_v2_mount_path)
        print("The response of SecretsApi->kv_v2_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]

### Return type

[**KvV2ReadResponse**](KvV2ReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_read_configuration**
> KvV2ReadConfigurationResponse kv_v2_read_configuration(kv_v2_mount_path)

Read the backend level settings.

### Example


```python
import ahvac
from ahvac.models.kv_v2_read_configuration_response import KvV2ReadConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')

    try:
        # Read the backend level settings.
        api_response = await api_instance.kv_v2_read_configuration(kv_v2_mount_path)
        print("The response of SecretsApi->kv_v2_read_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]

### Return type

[**KvV2ReadConfigurationResponse**](KvV2ReadConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_read_metadata**
> KvV2ReadMetadataResponse kv_v2_read_metadata(path, kv_v2_mount_path)



### Example


```python
import ahvac
from ahvac.models.kv_v2_read_metadata_response import KvV2ReadMetadataResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')

    try:
        api_response = await api_instance.kv_v2_read_metadata(path, kv_v2_mount_path)
        print("The response of SecretsApi->kv_v2_read_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_read_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]

### Return type

[**KvV2ReadMetadataResponse**](KvV2ReadMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_read_subkeys**
> KvV2ReadSubkeysResponse kv_v2_read_subkeys(path, kv_v2_mount_path)



### Example


```python
import ahvac
from ahvac.models.kv_v2_read_subkeys_response import KvV2ReadSubkeysResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')

    try:
        api_response = await api_instance.kv_v2_read_subkeys(path, kv_v2_mount_path)
        print("The response of SecretsApi->kv_v2_read_subkeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_read_subkeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]

### Return type

[**KvV2ReadSubkeysResponse**](KvV2ReadSubkeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_undelete_versions**
> kv_v2_undelete_versions(path, kv_v2_mount_path, kv_v2_undelete_versions_request)



### Example


```python
import ahvac
from ahvac.models.kv_v2_undelete_versions_request import KvV2UndeleteVersionsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')
    kv_v2_undelete_versions_request = ahvac.KvV2UndeleteVersionsRequest() # KvV2UndeleteVersionsRequest | 

    try:
        await api_instance.kv_v2_undelete_versions(path, kv_v2_mount_path, kv_v2_undelete_versions_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_undelete_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]
 **kv_v2_undelete_versions_request** | [**KvV2UndeleteVersionsRequest**](KvV2UndeleteVersionsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_write**
> KvV2WriteResponse kv_v2_write(path, kv_v2_mount_path, kv_v2_write_request)



### Example


```python
import ahvac
from ahvac.models.kv_v2_write_request import KvV2WriteRequest
from ahvac.models.kv_v2_write_response import KvV2WriteResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')
    kv_v2_write_request = ahvac.KvV2WriteRequest() # KvV2WriteRequest | 

    try:
        api_response = await api_instance.kv_v2_write(path, kv_v2_mount_path, kv_v2_write_request)
        print("The response of SecretsApi->kv_v2_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]
 **kv_v2_write_request** | [**KvV2WriteRequest**](KvV2WriteRequest.md)|  | 

### Return type

[**KvV2WriteResponse**](KvV2WriteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_v2_write_metadata**
> kv_v2_write_metadata(path, kv_v2_mount_path, kv_v2_write_metadata_request)



### Example


```python
import ahvac
from ahvac.models.kv_v2_write_metadata_request import KvV2WriteMetadataRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    path = 'path_example' # str | Location of the secret.
    kv_v2_mount_path = 'kv-v2' # str | Path that the backend was mounted at (default to 'kv-v2')
    kv_v2_write_metadata_request = ahvac.KvV2WriteMetadataRequest() # KvV2WriteMetadataRequest | 

    try:
        await api_instance.kv_v2_write_metadata(path, kv_v2_mount_path, kv_v2_write_metadata_request)
    except Exception as e:
        print("Exception when calling SecretsApi->kv_v2_write_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **kv_v2_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kv-v2&#39;]
 **kv_v2_write_metadata_request** | [**KvV2WriteMetadataRequest**](KvV2WriteMetadataRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_configure**
> ldap_configure(ldap_mount_path, ldap_configure_request)



### Example


```python
import ahvac
from ahvac.models.ldap_configure_request import LdapConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_configure_request = ahvac.LdapConfigureRequest() # LdapConfigureRequest | 

    try:
        await api_instance.ldap_configure(ldap_mount_path, ldap_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_configure_request** | [**LdapConfigureRequest**](LdapConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_delete_configuration**
> ldap_delete_configuration(ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_delete_configuration(ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_delete_dynamic_role**
> ldap_delete_dynamic_role(name, ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role (lowercase)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_delete_dynamic_role(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_delete_dynamic_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role (lowercase) | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_delete_static_role**
> ldap_delete_static_role(name, ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_delete_static_role(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_delete_static_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_check_in**
> ldap_library_check_in(name, ldap_mount_path, ldap_library_check_in_request)

Check service accounts in to the library.

### Example


```python
import ahvac
from ahvac.models.ldap_library_check_in_request import LdapLibraryCheckInRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the set.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_library_check_in_request = ahvac.LdapLibraryCheckInRequest() # LdapLibraryCheckInRequest | 

    try:
        # Check service accounts in to the library.
        await api_instance.ldap_library_check_in(name, ldap_mount_path, ldap_library_check_in_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_check_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the set. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_library_check_in_request** | [**LdapLibraryCheckInRequest**](LdapLibraryCheckInRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_check_out**
> ldap_library_check_out(name, ldap_mount_path, ldap_library_check_out_request)

Check a service account out from the library.

### Example


```python
import ahvac
from ahvac.models.ldap_library_check_out_request import LdapLibraryCheckOutRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the set
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_library_check_out_request = ahvac.LdapLibraryCheckOutRequest() # LdapLibraryCheckOutRequest | 

    try:
        # Check a service account out from the library.
        await api_instance.ldap_library_check_out(name, ldap_mount_path, ldap_library_check_out_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_check_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the set | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_library_check_out_request** | [**LdapLibraryCheckOutRequest**](LdapLibraryCheckOutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_check_status**
> ldap_library_check_status(name, ldap_mount_path)

Check the status of the service accounts in a library set.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the set.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        # Check the status of the service accounts in a library set.
        await api_instance.ldap_library_check_status(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_check_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the set. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_configure**
> ldap_library_configure(name, ldap_mount_path, ldap_library_configure_request)

Update a library set.

### Example


```python
import ahvac
from ahvac.models.ldap_library_configure_request import LdapLibraryConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the set.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_library_configure_request = ahvac.LdapLibraryConfigureRequest() # LdapLibraryConfigureRequest | 

    try:
        # Update a library set.
        await api_instance.ldap_library_configure(name, ldap_mount_path, ldap_library_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the set. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_library_configure_request** | [**LdapLibraryConfigureRequest**](LdapLibraryConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_delete**
> ldap_library_delete(name, ldap_mount_path)

Delete a library set.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the set.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        # Delete a library set.
        await api_instance.ldap_library_delete(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the set. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_force_check_in**
> ldap_library_force_check_in(name, ldap_mount_path, ldap_library_force_check_in_request)

Check service accounts in to the library.

### Example


```python
import ahvac
from ahvac.models.ldap_library_force_check_in_request import LdapLibraryForceCheckInRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the set.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_library_force_check_in_request = ahvac.LdapLibraryForceCheckInRequest() # LdapLibraryForceCheckInRequest | 

    try:
        # Check service accounts in to the library.
        await api_instance.ldap_library_force_check_in(name, ldap_mount_path, ldap_library_force_check_in_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_force_check_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the set. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_library_force_check_in_request** | [**LdapLibraryForceCheckInRequest**](LdapLibraryForceCheckInRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_list**
> StandardListResponse ldap_library_list(ldap_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.ldap_library_list(ldap_mount_path, list)
        print("The response of SecretsApi->ldap_library_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_library_read**
> ldap_library_read(name, ldap_mount_path)

Read a library set.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the set.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        # Read a library set.
        await api_instance.ldap_library_read(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_library_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the set. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_list_dynamic_roles**
> StandardListResponse ldap_list_dynamic_roles(ldap_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.ldap_list_dynamic_roles(ldap_mount_path, list)
        print("The response of SecretsApi->ldap_list_dynamic_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_list_dynamic_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_list_static_roles**
> StandardListResponse ldap_list_static_roles(ldap_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.ldap_list_static_roles(ldap_mount_path, list)
        print("The response of SecretsApi->ldap_list_static_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_list_static_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_read_configuration**
> ldap_read_configuration(ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_read_configuration(ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_read_dynamic_role**
> ldap_read_dynamic_role(name, ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role (lowercase)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_read_dynamic_role(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_read_dynamic_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role (lowercase) | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_read_static_role**
> ldap_read_static_role(name, ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_read_static_role(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_read_static_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_request_dynamic_role_credentials**
> ldap_request_dynamic_role_credentials(name, ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the dynamic role.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_request_dynamic_role_credentials(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_request_dynamic_role_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the dynamic role. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_request_static_role_credentials**
> ldap_request_static_role_credentials(name, ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the static role.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_request_static_role_credentials(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_request_static_role_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the static role. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_rotate_root_credentials**
> ldap_rotate_root_credentials(ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_rotate_root_credentials(ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_rotate_root_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_rotate_static_role**
> ldap_rotate_static_role(name, ldap_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the static role
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_rotate_static_role(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_rotate_static_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the static role | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_write_dynamic_role**
> ldap_write_dynamic_role(name, ldap_mount_path, ldap_write_dynamic_role_request)



### Example


```python
import ahvac
from ahvac.models.ldap_write_dynamic_role_request import LdapWriteDynamicRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role (lowercase)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_write_dynamic_role_request = ahvac.LdapWriteDynamicRoleRequest() # LdapWriteDynamicRoleRequest | 

    try:
        await api_instance.ldap_write_dynamic_role(name, ldap_mount_path, ldap_write_dynamic_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_write_dynamic_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role (lowercase) | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_write_dynamic_role_request** | [**LdapWriteDynamicRoleRequest**](LdapWriteDynamicRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_write_static_role**
> ldap_write_static_role(name, ldap_mount_path, ldap_write_static_role_request)



### Example


```python
import ahvac
from ahvac.models.ldap_write_static_role_request import LdapWriteStaticRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_write_static_role_request = ahvac.LdapWriteStaticRoleRequest() # LdapWriteStaticRoleRequest | 

    try:
        await api_instance.ldap_write_static_role(name, ldap_mount_path, ldap_write_static_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ldap_write_static_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_write_static_role_request** | [**LdapWriteStaticRoleRequest**](LdapWriteStaticRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_configure**
> mongo_db_atlas_configure(mongodbatlas_mount_path, mongo_db_atlas_configure_request)



### Example


```python
import ahvac
from ahvac.models.mongo_db_atlas_configure_request import MongoDbAtlasConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')
    mongo_db_atlas_configure_request = ahvac.MongoDbAtlasConfigureRequest() # MongoDbAtlasConfigureRequest | 

    try:
        await api_instance.mongo_db_atlas_configure(mongodbatlas_mount_path, mongo_db_atlas_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]
 **mongo_db_atlas_configure_request** | [**MongoDbAtlasConfigureRequest**](MongoDbAtlasConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_delete_role**
> mongo_db_atlas_delete_role(name, mongodbatlas_mount_path)

Manage the roles used to generate MongoDB Atlas Programmatic API Keys.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the Roles
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')

    try:
        # Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
        await api_instance.mongo_db_atlas_delete_role(name, mongodbatlas_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Roles | 
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_generate_credentials**
> mongo_db_atlas_generate_credentials(name, mongodbatlas_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')

    try:
        await api_instance.mongo_db_atlas_generate_credentials(name, mongodbatlas_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_generate_credentials2**
> mongo_db_atlas_generate_credentials2(name, mongodbatlas_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')

    try:
        await api_instance.mongo_db_atlas_generate_credentials2(name, mongodbatlas_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_generate_credentials2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_list_roles**
> StandardListResponse mongo_db_atlas_list_roles(mongodbatlas_mount_path, list)

List the existing roles in this backend

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')
    list = 'list_example' # str | Must be set to `true`

    try:
        # List the existing roles in this backend
        api_response = await api_instance.mongo_db_atlas_list_roles(mongodbatlas_mount_path, list)
        print("The response of SecretsApi->mongo_db_atlas_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_read_configuration**
> mongo_db_atlas_read_configuration(mongodbatlas_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')

    try:
        await api_instance.mongo_db_atlas_read_configuration(mongodbatlas_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_read_role**
> mongo_db_atlas_read_role(name, mongodbatlas_mount_path)

Manage the roles used to generate MongoDB Atlas Programmatic API Keys.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the Roles
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')

    try:
        # Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
        await api_instance.mongo_db_atlas_read_role(name, mongodbatlas_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Roles | 
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mongo_db_atlas_write_role**
> mongo_db_atlas_write_role(name, mongodbatlas_mount_path, mongo_db_atlas_write_role_request)

Manage the roles used to generate MongoDB Atlas Programmatic API Keys.

### Example


```python
import ahvac
from ahvac.models.mongo_db_atlas_write_role_request import MongoDbAtlasWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the Roles
    mongodbatlas_mount_path = 'mongodbatlas' # str | Path that the backend was mounted at (default to 'mongodbatlas')
    mongo_db_atlas_write_role_request = ahvac.MongoDbAtlasWriteRoleRequest() # MongoDbAtlasWriteRoleRequest | 

    try:
        # Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
        await api_instance.mongo_db_atlas_write_role(name, mongodbatlas_mount_path, mongo_db_atlas_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->mongo_db_atlas_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Roles | 
 **mongodbatlas_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;mongodbatlas&#39;]
 **mongo_db_atlas_write_role_request** | [**MongoDbAtlasWriteRoleRequest**](MongoDbAtlasWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_configure_access**
> nomad_configure_access(nomad_mount_path, nomad_configure_access_request)



### Example


```python
import ahvac
from ahvac.models.nomad_configure_access_request import NomadConfigureAccessRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')
    nomad_configure_access_request = ahvac.NomadConfigureAccessRequest() # NomadConfigureAccessRequest | 

    try:
        await api_instance.nomad_configure_access(nomad_mount_path, nomad_configure_access_request)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_configure_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]
 **nomad_configure_access_request** | [**NomadConfigureAccessRequest**](NomadConfigureAccessRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_configure_lease**
> nomad_configure_lease(nomad_mount_path, nomad_configure_lease_request)



### Example


```python
import ahvac
from ahvac.models.nomad_configure_lease_request import NomadConfigureLeaseRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')
    nomad_configure_lease_request = ahvac.NomadConfigureLeaseRequest() # NomadConfigureLeaseRequest | 

    try:
        await api_instance.nomad_configure_lease(nomad_mount_path, nomad_configure_lease_request)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_configure_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]
 **nomad_configure_lease_request** | [**NomadConfigureLeaseRequest**](NomadConfigureLeaseRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_delete_access_configuration**
> nomad_delete_access_configuration(nomad_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')

    try:
        await api_instance.nomad_delete_access_configuration(nomad_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_delete_access_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_delete_lease_configuration**
> nomad_delete_lease_configuration(nomad_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')

    try:
        await api_instance.nomad_delete_lease_configuration(nomad_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_delete_lease_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_delete_role**
> nomad_delete_role(name, nomad_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')

    try:
        await api_instance.nomad_delete_role(name, nomad_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_generate_credentials**
> nomad_generate_credentials(name, nomad_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')

    try:
        await api_instance.nomad_generate_credentials(name, nomad_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_list_roles**
> StandardListResponse nomad_list_roles(nomad_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.nomad_list_roles(nomad_mount_path, list)
        print("The response of SecretsApi->nomad_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_read_access_configuration**
> nomad_read_access_configuration(nomad_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')

    try:
        await api_instance.nomad_read_access_configuration(nomad_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_read_access_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_read_lease_configuration**
> nomad_read_lease_configuration(nomad_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')

    try:
        await api_instance.nomad_read_lease_configuration(nomad_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_read_lease_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_read_role**
> nomad_read_role(name, nomad_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')

    try:
        await api_instance.nomad_read_role(name, nomad_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nomad_write_role**
> nomad_write_role(name, nomad_mount_path, nomad_write_role_request)



### Example


```python
import ahvac
from ahvac.models.nomad_write_role_request import NomadWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    nomad_mount_path = 'nomad' # str | Path that the backend was mounted at (default to 'nomad')
    nomad_write_role_request = ahvac.NomadWriteRoleRequest() # NomadWriteRoleRequest | 

    try:
        await api_instance.nomad_write_role(name, nomad_mount_path, nomad_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->nomad_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **nomad_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;nomad&#39;]
 **nomad_write_role_request** | [**NomadWriteRoleRequest**](NomadWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_acme**
> pki_configure_acme(pki_mount_path, pki_configure_acme_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_acme_request import PkiConfigureAcmeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_acme_request = ahvac.PkiConfigureAcmeRequest() # PkiConfigureAcmeRequest | 

    try:
        await api_instance.pki_configure_acme(pki_mount_path, pki_configure_acme_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_acme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_acme_request** | [**PkiConfigureAcmeRequest**](PkiConfigureAcmeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_auto_tidy**
> PkiConfigureAutoTidyResponse pki_configure_auto_tidy(pki_mount_path, pki_configure_auto_tidy_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_auto_tidy_request import PkiConfigureAutoTidyRequest
from ahvac.models.pki_configure_auto_tidy_response import PkiConfigureAutoTidyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_auto_tidy_request = ahvac.PkiConfigureAutoTidyRequest() # PkiConfigureAutoTidyRequest | 

    try:
        api_response = await api_instance.pki_configure_auto_tidy(pki_mount_path, pki_configure_auto_tidy_request)
        print("The response of SecretsApi->pki_configure_auto_tidy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_auto_tidy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_auto_tidy_request** | [**PkiConfigureAutoTidyRequest**](PkiConfigureAutoTidyRequest.md)|  | 

### Return type

[**PkiConfigureAutoTidyResponse**](PkiConfigureAutoTidyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_ca**
> PkiConfigureCaResponse pki_configure_ca(pki_mount_path, pki_configure_ca_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_ca_request import PkiConfigureCaRequest
from ahvac.models.pki_configure_ca_response import PkiConfigureCaResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_ca_request = ahvac.PkiConfigureCaRequest() # PkiConfigureCaRequest | 

    try:
        api_response = await api_instance.pki_configure_ca(pki_mount_path, pki_configure_ca_request)
        print("The response of SecretsApi->pki_configure_ca:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_ca: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_ca_request** | [**PkiConfigureCaRequest**](PkiConfigureCaRequest.md)|  | 

### Return type

[**PkiConfigureCaResponse**](PkiConfigureCaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_cluster**
> PkiConfigureClusterResponse pki_configure_cluster(pki_mount_path, pki_configure_cluster_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_cluster_request import PkiConfigureClusterRequest
from ahvac.models.pki_configure_cluster_response import PkiConfigureClusterResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_cluster_request = ahvac.PkiConfigureClusterRequest() # PkiConfigureClusterRequest | 

    try:
        api_response = await api_instance.pki_configure_cluster(pki_mount_path, pki_configure_cluster_request)
        print("The response of SecretsApi->pki_configure_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_cluster_request** | [**PkiConfigureClusterRequest**](PkiConfigureClusterRequest.md)|  | 

### Return type

[**PkiConfigureClusterResponse**](PkiConfigureClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_crl**
> PkiConfigureCrlResponse pki_configure_crl(pki_mount_path, pki_configure_crl_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_crl_request import PkiConfigureCrlRequest
from ahvac.models.pki_configure_crl_response import PkiConfigureCrlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_crl_request = ahvac.PkiConfigureCrlRequest() # PkiConfigureCrlRequest | 

    try:
        api_response = await api_instance.pki_configure_crl(pki_mount_path, pki_configure_crl_request)
        print("The response of SecretsApi->pki_configure_crl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_crl_request** | [**PkiConfigureCrlRequest**](PkiConfigureCrlRequest.md)|  | 

### Return type

[**PkiConfigureCrlResponse**](PkiConfigureCrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_issuers**
> PkiConfigureIssuersResponse pki_configure_issuers(pki_mount_path, pki_configure_issuers_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_issuers_request import PkiConfigureIssuersRequest
from ahvac.models.pki_configure_issuers_response import PkiConfigureIssuersResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_issuers_request = ahvac.PkiConfigureIssuersRequest() # PkiConfigureIssuersRequest | 

    try:
        api_response = await api_instance.pki_configure_issuers(pki_mount_path, pki_configure_issuers_request)
        print("The response of SecretsApi->pki_configure_issuers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_issuers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_issuers_request** | [**PkiConfigureIssuersRequest**](PkiConfigureIssuersRequest.md)|  | 

### Return type

[**PkiConfigureIssuersResponse**](PkiConfigureIssuersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_keys**
> PkiConfigureKeysResponse pki_configure_keys(pki_mount_path, pki_configure_keys_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_keys_request import PkiConfigureKeysRequest
from ahvac.models.pki_configure_keys_response import PkiConfigureKeysResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_keys_request = ahvac.PkiConfigureKeysRequest() # PkiConfigureKeysRequest | 

    try:
        api_response = await api_instance.pki_configure_keys(pki_mount_path, pki_configure_keys_request)
        print("The response of SecretsApi->pki_configure_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_keys_request** | [**PkiConfigureKeysRequest**](PkiConfigureKeysRequest.md)|  | 

### Return type

[**PkiConfigureKeysResponse**](PkiConfigureKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_configure_urls**
> PkiConfigureUrlsResponse pki_configure_urls(pki_mount_path, pki_configure_urls_request)



### Example


```python
import ahvac
from ahvac.models.pki_configure_urls_request import PkiConfigureUrlsRequest
from ahvac.models.pki_configure_urls_response import PkiConfigureUrlsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_configure_urls_request = ahvac.PkiConfigureUrlsRequest() # PkiConfigureUrlsRequest | 

    try:
        api_response = await api_instance.pki_configure_urls(pki_mount_path, pki_configure_urls_request)
        print("The response of SecretsApi->pki_configure_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_configure_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_configure_urls_request** | [**PkiConfigureUrlsRequest**](PkiConfigureUrlsRequest.md)|  | 

### Return type

[**PkiConfigureUrlsResponse**](PkiConfigureUrlsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_cross_sign_intermediate**
> PkiCrossSignIntermediateResponse pki_cross_sign_intermediate(pki_mount_path, pki_cross_sign_intermediate_request)



### Example


```python
import ahvac
from ahvac.models.pki_cross_sign_intermediate_request import PkiCrossSignIntermediateRequest
from ahvac.models.pki_cross_sign_intermediate_response import PkiCrossSignIntermediateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_cross_sign_intermediate_request = ahvac.PkiCrossSignIntermediateRequest() # PkiCrossSignIntermediateRequest | 

    try:
        api_response = await api_instance.pki_cross_sign_intermediate(pki_mount_path, pki_cross_sign_intermediate_request)
        print("The response of SecretsApi->pki_cross_sign_intermediate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_cross_sign_intermediate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_cross_sign_intermediate_request** | [**PkiCrossSignIntermediateRequest**](PkiCrossSignIntermediateRequest.md)|  | 

### Return type

[**PkiCrossSignIntermediateResponse**](PkiCrossSignIntermediateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_delete_eab_key**
> pki_delete_eab_key(key_id, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key_id = 'key_id_example' # str | EAB key identifier
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_delete_eab_key(key_id, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_delete_eab_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| EAB key identifier | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_delete_issuer**
> pki_delete_issuer(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_delete_issuer(issuer_ref, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_delete_issuer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_delete_key**
> pki_delete_key(key_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key_ref = 'default' # str | Reference to key; either \"default\" for the configured default key, an identifier of a key, or the name assigned to the key. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_delete_key(key_ref, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_ref** | **str**| Reference to key; either \&quot;default\&quot; for the configured default key, an identifier of a key, or the name assigned to the key. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_delete_role**
> pki_delete_role(name, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_delete_role(name, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_delete_root**
> pki_delete_root(pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_delete_root(pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_delete_root: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_eab_key**
> PkiGenerateEabKeyResponse pki_generate_eab_key(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_generate_eab_key_response import PkiGenerateEabKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_generate_eab_key(pki_mount_path)
        print("The response of SecretsApi->pki_generate_eab_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_eab_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiGenerateEabKeyResponse**](PkiGenerateEabKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_eab_key_for_issuer**
> PkiGenerateEabKeyForIssuerResponse pki_generate_eab_key_for_issuer(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_generate_eab_key_for_issuer_response import PkiGenerateEabKeyForIssuerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_generate_eab_key_for_issuer(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_generate_eab_key_for_issuer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_eab_key_for_issuer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiGenerateEabKeyForIssuerResponse**](PkiGenerateEabKeyForIssuerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_eab_key_for_issuer_and_role**
> PkiGenerateEabKeyForIssuerAndRoleResponse pki_generate_eab_key_for_issuer_and_role(issuer_ref, role, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_generate_eab_key_for_issuer_and_role_response import PkiGenerateEabKeyForIssuerAndRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_generate_eab_key_for_issuer_and_role(issuer_ref, role, pki_mount_path)
        print("The response of SecretsApi->pki_generate_eab_key_for_issuer_and_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_eab_key_for_issuer_and_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiGenerateEabKeyForIssuerAndRoleResponse**](PkiGenerateEabKeyForIssuerAndRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_eab_key_for_role**
> PkiGenerateEabKeyForRoleResponse pki_generate_eab_key_for_role(role, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_generate_eab_key_for_role_response import PkiGenerateEabKeyForRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_generate_eab_key_for_role(role, pki_mount_path)
        print("The response of SecretsApi->pki_generate_eab_key_for_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_eab_key_for_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiGenerateEabKeyForRoleResponse**](PkiGenerateEabKeyForRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_exported_key**
> PkiGenerateExportedKeyResponse pki_generate_exported_key(pki_mount_path, pki_generate_exported_key_request)



### Example


```python
import ahvac
from ahvac.models.pki_generate_exported_key_request import PkiGenerateExportedKeyRequest
from ahvac.models.pki_generate_exported_key_response import PkiGenerateExportedKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_generate_exported_key_request = ahvac.PkiGenerateExportedKeyRequest() # PkiGenerateExportedKeyRequest | 

    try:
        api_response = await api_instance.pki_generate_exported_key(pki_mount_path, pki_generate_exported_key_request)
        print("The response of SecretsApi->pki_generate_exported_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_exported_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_generate_exported_key_request** | [**PkiGenerateExportedKeyRequest**](PkiGenerateExportedKeyRequest.md)|  | 

### Return type

[**PkiGenerateExportedKeyResponse**](PkiGenerateExportedKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_intermediate**
> PkiGenerateIntermediateResponse pki_generate_intermediate(exported, pki_mount_path, pki_generate_intermediate_request)



### Example


```python
import ahvac
from ahvac.models.pki_generate_intermediate_request import PkiGenerateIntermediateRequest
from ahvac.models.pki_generate_intermediate_response import PkiGenerateIntermediateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    exported = 'exported_example' # str | Must be \"internal\", \"exported\" or \"kms\". If set to \"exported\", the generated private key will be returned. This is your *only* chance to retrieve the private key!
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_generate_intermediate_request = ahvac.PkiGenerateIntermediateRequest() # PkiGenerateIntermediateRequest | 

    try:
        api_response = await api_instance.pki_generate_intermediate(exported, pki_mount_path, pki_generate_intermediate_request)
        print("The response of SecretsApi->pki_generate_intermediate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_intermediate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exported** | **str**| Must be \&quot;internal\&quot;, \&quot;exported\&quot; or \&quot;kms\&quot;. If set to \&quot;exported\&quot;, the generated private key will be returned. This is your *only* chance to retrieve the private key! | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_generate_intermediate_request** | [**PkiGenerateIntermediateRequest**](PkiGenerateIntermediateRequest.md)|  | 

### Return type

[**PkiGenerateIntermediateResponse**](PkiGenerateIntermediateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_internal_key**
> PkiGenerateInternalKeyResponse pki_generate_internal_key(pki_mount_path, pki_generate_internal_key_request)



### Example


```python
import ahvac
from ahvac.models.pki_generate_internal_key_request import PkiGenerateInternalKeyRequest
from ahvac.models.pki_generate_internal_key_response import PkiGenerateInternalKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_generate_internal_key_request = ahvac.PkiGenerateInternalKeyRequest() # PkiGenerateInternalKeyRequest | 

    try:
        api_response = await api_instance.pki_generate_internal_key(pki_mount_path, pki_generate_internal_key_request)
        print("The response of SecretsApi->pki_generate_internal_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_internal_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_generate_internal_key_request** | [**PkiGenerateInternalKeyRequest**](PkiGenerateInternalKeyRequest.md)|  | 

### Return type

[**PkiGenerateInternalKeyResponse**](PkiGenerateInternalKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_kms_key**
> PkiGenerateKmsKeyResponse pki_generate_kms_key(pki_mount_path, pki_generate_kms_key_request)



### Example


```python
import ahvac
from ahvac.models.pki_generate_kms_key_request import PkiGenerateKmsKeyRequest
from ahvac.models.pki_generate_kms_key_response import PkiGenerateKmsKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_generate_kms_key_request = ahvac.PkiGenerateKmsKeyRequest() # PkiGenerateKmsKeyRequest | 

    try:
        api_response = await api_instance.pki_generate_kms_key(pki_mount_path, pki_generate_kms_key_request)
        print("The response of SecretsApi->pki_generate_kms_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_kms_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_generate_kms_key_request** | [**PkiGenerateKmsKeyRequest**](PkiGenerateKmsKeyRequest.md)|  | 

### Return type

[**PkiGenerateKmsKeyResponse**](PkiGenerateKmsKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_generate_root**
> PkiGenerateRootResponse pki_generate_root(exported, pki_mount_path, pki_generate_root_request)



### Example


```python
import ahvac
from ahvac.models.pki_generate_root_request import PkiGenerateRootRequest
from ahvac.models.pki_generate_root_response import PkiGenerateRootResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    exported = 'exported_example' # str | Must be \"internal\", \"exported\" or \"kms\". If set to \"exported\", the generated private key will be returned. This is your *only* chance to retrieve the private key!
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_generate_root_request = ahvac.PkiGenerateRootRequest() # PkiGenerateRootRequest | 

    try:
        api_response = await api_instance.pki_generate_root(exported, pki_mount_path, pki_generate_root_request)
        print("The response of SecretsApi->pki_generate_root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_generate_root: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exported** | **str**| Must be \&quot;internal\&quot;, \&quot;exported\&quot; or \&quot;kms\&quot;. If set to \&quot;exported\&quot;, the generated private key will be returned. This is your *only* chance to retrieve the private key! | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_generate_root_request** | [**PkiGenerateRootRequest**](PkiGenerateRootRequest.md)|  | 

### Return type

[**PkiGenerateRootResponse**](PkiGenerateRootResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_import_key**
> PkiImportKeyResponse pki_import_key(pki_mount_path, pki_import_key_request)



### Example


```python
import ahvac
from ahvac.models.pki_import_key_request import PkiImportKeyRequest
from ahvac.models.pki_import_key_response import PkiImportKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_import_key_request = ahvac.PkiImportKeyRequest() # PkiImportKeyRequest | 

    try:
        api_response = await api_instance.pki_import_key(pki_mount_path, pki_import_key_request)
        print("The response of SecretsApi->pki_import_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_import_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_import_key_request** | [**PkiImportKeyRequest**](PkiImportKeyRequest.md)|  | 

### Return type

[**PkiImportKeyResponse**](PkiImportKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issue_with_role**
> PkiIssueWithRoleResponse pki_issue_with_role(role, pki_mount_path, pki_issue_with_role_request)



### Example


```python
import ahvac
from ahvac.models.pki_issue_with_role_request import PkiIssueWithRoleRequest
from ahvac.models.pki_issue_with_role_response import PkiIssueWithRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role with configuration for this request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issue_with_role_request = ahvac.PkiIssueWithRoleRequest() # PkiIssueWithRoleRequest | 

    try:
        api_response = await api_instance.pki_issue_with_role(role, pki_mount_path, pki_issue_with_role_request)
        print("The response of SecretsApi->pki_issue_with_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issue_with_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role with configuration for this request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issue_with_role_request** | [**PkiIssueWithRoleRequest**](PkiIssueWithRoleRequest.md)|  | 

### Return type

[**PkiIssueWithRoleResponse**](PkiIssueWithRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_issue_with_role**
> PkiIssuerIssueWithRoleResponse pki_issuer_issue_with_role(issuer_ref, role, pki_mount_path, pki_issuer_issue_with_role_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_issue_with_role_request import PkiIssuerIssueWithRoleRequest
from ahvac.models.pki_issuer_issue_with_role_response import PkiIssuerIssueWithRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    role = 'role_example' # str | The desired role with configuration for this request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_issue_with_role_request = ahvac.PkiIssuerIssueWithRoleRequest() # PkiIssuerIssueWithRoleRequest | 

    try:
        api_response = await api_instance.pki_issuer_issue_with_role(issuer_ref, role, pki_mount_path, pki_issuer_issue_with_role_request)
        print("The response of SecretsApi->pki_issuer_issue_with_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_issue_with_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **role** | **str**| The desired role with configuration for this request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_issue_with_role_request** | [**PkiIssuerIssueWithRoleRequest**](PkiIssuerIssueWithRoleRequest.md)|  | 

### Return type

[**PkiIssuerIssueWithRoleResponse**](PkiIssuerIssueWithRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_read_crl**
> PkiIssuerReadCrlResponse pki_issuer_read_crl(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_read_crl_response import PkiIssuerReadCrlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_issuer_read_crl(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_issuer_read_crl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_read_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiIssuerReadCrlResponse**](PkiIssuerReadCrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_read_crl_delta**
> PkiIssuerReadCrlDeltaResponse pki_issuer_read_crl_delta(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_read_crl_delta_response import PkiIssuerReadCrlDeltaResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_issuer_read_crl_delta(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_issuer_read_crl_delta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_read_crl_delta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiIssuerReadCrlDeltaResponse**](PkiIssuerReadCrlDeltaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_read_crl_delta_der**
> PkiIssuerReadCrlDeltaDerResponse pki_issuer_read_crl_delta_der(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_read_crl_delta_der_response import PkiIssuerReadCrlDeltaDerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_issuer_read_crl_delta_der(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_issuer_read_crl_delta_der:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_read_crl_delta_der: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiIssuerReadCrlDeltaDerResponse**](PkiIssuerReadCrlDeltaDerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_read_crl_delta_pem**
> PkiIssuerReadCrlDeltaPemResponse pki_issuer_read_crl_delta_pem(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_read_crl_delta_pem_response import PkiIssuerReadCrlDeltaPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_issuer_read_crl_delta_pem(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_issuer_read_crl_delta_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_read_crl_delta_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiIssuerReadCrlDeltaPemResponse**](PkiIssuerReadCrlDeltaPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_read_crl_der**
> PkiIssuerReadCrlDerResponse pki_issuer_read_crl_der(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_read_crl_der_response import PkiIssuerReadCrlDerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_issuer_read_crl_der(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_issuer_read_crl_der:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_read_crl_der: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiIssuerReadCrlDerResponse**](PkiIssuerReadCrlDerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_read_crl_pem**
> PkiIssuerReadCrlPemResponse pki_issuer_read_crl_pem(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_read_crl_pem_response import PkiIssuerReadCrlPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_issuer_read_crl_pem(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_issuer_read_crl_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_read_crl_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiIssuerReadCrlPemResponse**](PkiIssuerReadCrlPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_resign_crls**
> PkiIssuerResignCrlsResponse pki_issuer_resign_crls(issuer_ref, pki_mount_path, pki_issuer_resign_crls_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_resign_crls_request import PkiIssuerResignCrlsRequest
from ahvac.models.pki_issuer_resign_crls_response import PkiIssuerResignCrlsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_resign_crls_request = ahvac.PkiIssuerResignCrlsRequest() # PkiIssuerResignCrlsRequest | 

    try:
        api_response = await api_instance.pki_issuer_resign_crls(issuer_ref, pki_mount_path, pki_issuer_resign_crls_request)
        print("The response of SecretsApi->pki_issuer_resign_crls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_resign_crls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_resign_crls_request** | [**PkiIssuerResignCrlsRequest**](PkiIssuerResignCrlsRequest.md)|  | 

### Return type

[**PkiIssuerResignCrlsResponse**](PkiIssuerResignCrlsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_sign_intermediate**
> PkiIssuerSignIntermediateResponse pki_issuer_sign_intermediate(issuer_ref, pki_mount_path, pki_issuer_sign_intermediate_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_sign_intermediate_request import PkiIssuerSignIntermediateRequest
from ahvac.models.pki_issuer_sign_intermediate_response import PkiIssuerSignIntermediateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_sign_intermediate_request = ahvac.PkiIssuerSignIntermediateRequest() # PkiIssuerSignIntermediateRequest | 

    try:
        api_response = await api_instance.pki_issuer_sign_intermediate(issuer_ref, pki_mount_path, pki_issuer_sign_intermediate_request)
        print("The response of SecretsApi->pki_issuer_sign_intermediate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_sign_intermediate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_sign_intermediate_request** | [**PkiIssuerSignIntermediateRequest**](PkiIssuerSignIntermediateRequest.md)|  | 

### Return type

[**PkiIssuerSignIntermediateResponse**](PkiIssuerSignIntermediateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_sign_revocation_list**
> PkiIssuerSignRevocationListResponse pki_issuer_sign_revocation_list(issuer_ref, pki_mount_path, pki_issuer_sign_revocation_list_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_sign_revocation_list_request import PkiIssuerSignRevocationListRequest
from ahvac.models.pki_issuer_sign_revocation_list_response import PkiIssuerSignRevocationListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_sign_revocation_list_request = ahvac.PkiIssuerSignRevocationListRequest() # PkiIssuerSignRevocationListRequest | 

    try:
        api_response = await api_instance.pki_issuer_sign_revocation_list(issuer_ref, pki_mount_path, pki_issuer_sign_revocation_list_request)
        print("The response of SecretsApi->pki_issuer_sign_revocation_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_sign_revocation_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_sign_revocation_list_request** | [**PkiIssuerSignRevocationListRequest**](PkiIssuerSignRevocationListRequest.md)|  | 

### Return type

[**PkiIssuerSignRevocationListResponse**](PkiIssuerSignRevocationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_sign_self_issued**
> PkiIssuerSignSelfIssuedResponse pki_issuer_sign_self_issued(issuer_ref, pki_mount_path, pki_issuer_sign_self_issued_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_sign_self_issued_request import PkiIssuerSignSelfIssuedRequest
from ahvac.models.pki_issuer_sign_self_issued_response import PkiIssuerSignSelfIssuedResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_sign_self_issued_request = ahvac.PkiIssuerSignSelfIssuedRequest() # PkiIssuerSignSelfIssuedRequest | 

    try:
        api_response = await api_instance.pki_issuer_sign_self_issued(issuer_ref, pki_mount_path, pki_issuer_sign_self_issued_request)
        print("The response of SecretsApi->pki_issuer_sign_self_issued:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_sign_self_issued: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_sign_self_issued_request** | [**PkiIssuerSignSelfIssuedRequest**](PkiIssuerSignSelfIssuedRequest.md)|  | 

### Return type

[**PkiIssuerSignSelfIssuedResponse**](PkiIssuerSignSelfIssuedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_sign_verbatim**
> PkiIssuerSignVerbatimResponse pki_issuer_sign_verbatim(issuer_ref, pki_mount_path, pki_issuer_sign_verbatim_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_sign_verbatim_request import PkiIssuerSignVerbatimRequest
from ahvac.models.pki_issuer_sign_verbatim_response import PkiIssuerSignVerbatimResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_sign_verbatim_request = ahvac.PkiIssuerSignVerbatimRequest() # PkiIssuerSignVerbatimRequest | 

    try:
        api_response = await api_instance.pki_issuer_sign_verbatim(issuer_ref, pki_mount_path, pki_issuer_sign_verbatim_request)
        print("The response of SecretsApi->pki_issuer_sign_verbatim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_sign_verbatim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_sign_verbatim_request** | [**PkiIssuerSignVerbatimRequest**](PkiIssuerSignVerbatimRequest.md)|  | 

### Return type

[**PkiIssuerSignVerbatimResponse**](PkiIssuerSignVerbatimResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_sign_verbatim_with_role**
> PkiIssuerSignVerbatimWithRoleResponse pki_issuer_sign_verbatim_with_role(issuer_ref, role, pki_mount_path, pki_issuer_sign_verbatim_with_role_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_sign_verbatim_with_role_request import PkiIssuerSignVerbatimWithRoleRequest
from ahvac.models.pki_issuer_sign_verbatim_with_role_response import PkiIssuerSignVerbatimWithRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    role = 'role_example' # str | The desired role with configuration for this request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_sign_verbatim_with_role_request = ahvac.PkiIssuerSignVerbatimWithRoleRequest() # PkiIssuerSignVerbatimWithRoleRequest | 

    try:
        api_response = await api_instance.pki_issuer_sign_verbatim_with_role(issuer_ref, role, pki_mount_path, pki_issuer_sign_verbatim_with_role_request)
        print("The response of SecretsApi->pki_issuer_sign_verbatim_with_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_sign_verbatim_with_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **role** | **str**| The desired role with configuration for this request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_sign_verbatim_with_role_request** | [**PkiIssuerSignVerbatimWithRoleRequest**](PkiIssuerSignVerbatimWithRoleRequest.md)|  | 

### Return type

[**PkiIssuerSignVerbatimWithRoleResponse**](PkiIssuerSignVerbatimWithRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuer_sign_with_role**
> PkiIssuerSignWithRoleResponse pki_issuer_sign_with_role(issuer_ref, role, pki_mount_path, pki_issuer_sign_with_role_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuer_sign_with_role_request import PkiIssuerSignWithRoleRequest
from ahvac.models.pki_issuer_sign_with_role_response import PkiIssuerSignWithRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    role = 'role_example' # str | The desired role with configuration for this request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuer_sign_with_role_request = ahvac.PkiIssuerSignWithRoleRequest() # PkiIssuerSignWithRoleRequest | 

    try:
        api_response = await api_instance.pki_issuer_sign_with_role(issuer_ref, role, pki_mount_path, pki_issuer_sign_with_role_request)
        print("The response of SecretsApi->pki_issuer_sign_with_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuer_sign_with_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **role** | **str**| The desired role with configuration for this request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuer_sign_with_role_request** | [**PkiIssuerSignWithRoleRequest**](PkiIssuerSignWithRoleRequest.md)|  | 

### Return type

[**PkiIssuerSignWithRoleResponse**](PkiIssuerSignWithRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuers_generate_intermediate**
> PkiIssuersGenerateIntermediateResponse pki_issuers_generate_intermediate(exported, pki_mount_path, pki_issuers_generate_intermediate_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuers_generate_intermediate_request import PkiIssuersGenerateIntermediateRequest
from ahvac.models.pki_issuers_generate_intermediate_response import PkiIssuersGenerateIntermediateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    exported = 'exported_example' # str | Must be \"internal\", \"exported\" or \"kms\". If set to \"exported\", the generated private key will be returned. This is your *only* chance to retrieve the private key!
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuers_generate_intermediate_request = ahvac.PkiIssuersGenerateIntermediateRequest() # PkiIssuersGenerateIntermediateRequest | 

    try:
        api_response = await api_instance.pki_issuers_generate_intermediate(exported, pki_mount_path, pki_issuers_generate_intermediate_request)
        print("The response of SecretsApi->pki_issuers_generate_intermediate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuers_generate_intermediate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exported** | **str**| Must be \&quot;internal\&quot;, \&quot;exported\&quot; or \&quot;kms\&quot;. If set to \&quot;exported\&quot;, the generated private key will be returned. This is your *only* chance to retrieve the private key! | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuers_generate_intermediate_request** | [**PkiIssuersGenerateIntermediateRequest**](PkiIssuersGenerateIntermediateRequest.md)|  | 

### Return type

[**PkiIssuersGenerateIntermediateResponse**](PkiIssuersGenerateIntermediateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuers_generate_root**
> PkiIssuersGenerateRootResponse pki_issuers_generate_root(exported, pki_mount_path, pki_issuers_generate_root_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuers_generate_root_request import PkiIssuersGenerateRootRequest
from ahvac.models.pki_issuers_generate_root_response import PkiIssuersGenerateRootResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    exported = 'exported_example' # str | Must be \"internal\", \"exported\" or \"kms\". If set to \"exported\", the generated private key will be returned. This is your *only* chance to retrieve the private key!
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuers_generate_root_request = ahvac.PkiIssuersGenerateRootRequest() # PkiIssuersGenerateRootRequest | 

    try:
        api_response = await api_instance.pki_issuers_generate_root(exported, pki_mount_path, pki_issuers_generate_root_request)
        print("The response of SecretsApi->pki_issuers_generate_root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuers_generate_root: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exported** | **str**| Must be \&quot;internal\&quot;, \&quot;exported\&quot; or \&quot;kms\&quot;. If set to \&quot;exported\&quot;, the generated private key will be returned. This is your *only* chance to retrieve the private key! | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuers_generate_root_request** | [**PkiIssuersGenerateRootRequest**](PkiIssuersGenerateRootRequest.md)|  | 

### Return type

[**PkiIssuersGenerateRootResponse**](PkiIssuersGenerateRootResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuers_import_bundle**
> PkiIssuersImportBundleResponse pki_issuers_import_bundle(pki_mount_path, pki_issuers_import_bundle_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuers_import_bundle_request import PkiIssuersImportBundleRequest
from ahvac.models.pki_issuers_import_bundle_response import PkiIssuersImportBundleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuers_import_bundle_request = ahvac.PkiIssuersImportBundleRequest() # PkiIssuersImportBundleRequest | 

    try:
        api_response = await api_instance.pki_issuers_import_bundle(pki_mount_path, pki_issuers_import_bundle_request)
        print("The response of SecretsApi->pki_issuers_import_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuers_import_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuers_import_bundle_request** | [**PkiIssuersImportBundleRequest**](PkiIssuersImportBundleRequest.md)|  | 

### Return type

[**PkiIssuersImportBundleResponse**](PkiIssuersImportBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_issuers_import_cert**
> PkiIssuersImportCertResponse pki_issuers_import_cert(pki_mount_path, pki_issuers_import_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_issuers_import_cert_request import PkiIssuersImportCertRequest
from ahvac.models.pki_issuers_import_cert_response import PkiIssuersImportCertResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_issuers_import_cert_request = ahvac.PkiIssuersImportCertRequest() # PkiIssuersImportCertRequest | 

    try:
        api_response = await api_instance.pki_issuers_import_cert(pki_mount_path, pki_issuers_import_cert_request)
        print("The response of SecretsApi->pki_issuers_import_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_issuers_import_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_issuers_import_cert_request** | [**PkiIssuersImportCertRequest**](PkiIssuersImportCertRequest.md)|  | 

### Return type

[**PkiIssuersImportCertResponse**](PkiIssuersImportCertResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_list_certs**
> StandardListResponse pki_list_certs(pki_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.pki_list_certs(pki_mount_path, list)
        print("The response of SecretsApi->pki_list_certs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_list_certs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_list_eab_keys**
> PkiListEabKeysResponse pki_list_eab_keys(pki_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.pki_list_eab_keys_response import PkiListEabKeysResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.pki_list_eab_keys(pki_mount_path, list)
        print("The response of SecretsApi->pki_list_eab_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_list_eab_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**PkiListEabKeysResponse**](PkiListEabKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_list_issuers**
> PkiListIssuersResponse pki_list_issuers(pki_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.pki_list_issuers_response import PkiListIssuersResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.pki_list_issuers(pki_mount_path, list)
        print("The response of SecretsApi->pki_list_issuers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_list_issuers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**PkiListIssuersResponse**](PkiListIssuersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_list_keys**
> PkiListKeysResponse pki_list_keys(pki_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.pki_list_keys_response import PkiListKeysResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.pki_list_keys(pki_mount_path, list)
        print("The response of SecretsApi->pki_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_list_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**PkiListKeysResponse**](PkiListKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_list_revoked_certs**
> StandardListResponse pki_list_revoked_certs(pki_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.pki_list_revoked_certs(pki_mount_path, list)
        print("The response of SecretsApi->pki_list_revoked_certs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_list_revoked_certs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_list_roles**
> StandardListResponse pki_list_roles(pki_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.pki_list_roles(pki_mount_path, list)
        print("The response of SecretsApi->pki_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_query_ocsp**
> pki_query_ocsp(pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_query_ocsp(pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_query_ocsp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_query_ocsp_with_get_req**
> pki_query_ocsp_with_get_req(req, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    req = 'req_example' # str | base-64 encoded ocsp request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_query_ocsp_with_get_req(req, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_query_ocsp_with_get_req: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req** | **str**| base-64 encoded ocsp request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_acme_configuration**
> pki_read_acme_configuration(pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_acme_configuration(pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_acme_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_acme_directory**
> pki_read_acme_directory(pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_acme_directory(pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_acme_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_acme_new_nonce**
> pki_read_acme_new_nonce(pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_acme_new_nonce(pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_acme_new_nonce: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_auto_tidy_configuration**
> PkiReadAutoTidyConfigurationResponse pki_read_auto_tidy_configuration(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_auto_tidy_configuration_response import PkiReadAutoTidyConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_auto_tidy_configuration(pki_mount_path)
        print("The response of SecretsApi->pki_read_auto_tidy_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_auto_tidy_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadAutoTidyConfigurationResponse**](PkiReadAutoTidyConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_ca_chain_pem**
> PkiReadCaChainPemResponse pki_read_ca_chain_pem(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_ca_chain_pem_response import PkiReadCaChainPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_ca_chain_pem(pki_mount_path)
        print("The response of SecretsApi->pki_read_ca_chain_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_ca_chain_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCaChainPemResponse**](PkiReadCaChainPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_ca_der**
> PkiReadCaDerResponse pki_read_ca_der(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_ca_der_response import PkiReadCaDerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_ca_der(pki_mount_path)
        print("The response of SecretsApi->pki_read_ca_der:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_ca_der: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCaDerResponse**](PkiReadCaDerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_ca_pem**
> PkiReadCaPemResponse pki_read_ca_pem(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_ca_pem_response import PkiReadCaPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_ca_pem(pki_mount_path)
        print("The response of SecretsApi->pki_read_ca_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_ca_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCaPemResponse**](PkiReadCaPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_cert**
> PkiReadCertResponse pki_read_cert(serial, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_cert_response import PkiReadCertResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    serial = 'serial_example' # str | Certificate serial number, in colon- or hyphen-separated octal
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_cert(serial, pki_mount_path)
        print("The response of SecretsApi->pki_read_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Certificate serial number, in colon- or hyphen-separated octal | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCertResponse**](PkiReadCertResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_cert_ca_chain**
> PkiReadCertCaChainResponse pki_read_cert_ca_chain(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_cert_ca_chain_response import PkiReadCertCaChainResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_cert_ca_chain(pki_mount_path)
        print("The response of SecretsApi->pki_read_cert_ca_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_cert_ca_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCertCaChainResponse**](PkiReadCertCaChainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_cert_crl**
> PkiReadCertCrlResponse pki_read_cert_crl(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_cert_crl_response import PkiReadCertCrlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_cert_crl(pki_mount_path)
        print("The response of SecretsApi->pki_read_cert_crl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_cert_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCertCrlResponse**](PkiReadCertCrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_cert_delta_crl**
> PkiReadCertDeltaCrlResponse pki_read_cert_delta_crl(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_cert_delta_crl_response import PkiReadCertDeltaCrlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_cert_delta_crl(pki_mount_path)
        print("The response of SecretsApi->pki_read_cert_delta_crl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_cert_delta_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCertDeltaCrlResponse**](PkiReadCertDeltaCrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_cert_raw_der**
> PkiReadCertRawDerResponse pki_read_cert_raw_der(serial, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_cert_raw_der_response import PkiReadCertRawDerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    serial = 'serial_example' # str | Certificate serial number, in colon- or hyphen-separated octal
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_cert_raw_der(serial, pki_mount_path)
        print("The response of SecretsApi->pki_read_cert_raw_der:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_cert_raw_der: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Certificate serial number, in colon- or hyphen-separated octal | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCertRawDerResponse**](PkiReadCertRawDerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_cert_raw_pem**
> PkiReadCertRawPemResponse pki_read_cert_raw_pem(serial, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_cert_raw_pem_response import PkiReadCertRawPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    serial = 'serial_example' # str | Certificate serial number, in colon- or hyphen-separated octal
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_cert_raw_pem(serial, pki_mount_path)
        print("The response of SecretsApi->pki_read_cert_raw_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_cert_raw_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Certificate serial number, in colon- or hyphen-separated octal | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCertRawPemResponse**](PkiReadCertRawPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_cluster_configuration**
> PkiReadClusterConfigurationResponse pki_read_cluster_configuration(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_cluster_configuration_response import PkiReadClusterConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_cluster_configuration(pki_mount_path)
        print("The response of SecretsApi->pki_read_cluster_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_cluster_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadClusterConfigurationResponse**](PkiReadClusterConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_crl_configuration**
> PkiReadCrlConfigurationResponse pki_read_crl_configuration(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_crl_configuration_response import PkiReadCrlConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_crl_configuration(pki_mount_path)
        print("The response of SecretsApi->pki_read_crl_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_crl_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCrlConfigurationResponse**](PkiReadCrlConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_crl_delta**
> PkiReadCrlDeltaResponse pki_read_crl_delta(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_crl_delta_response import PkiReadCrlDeltaResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_crl_delta(pki_mount_path)
        print("The response of SecretsApi->pki_read_crl_delta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_crl_delta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCrlDeltaResponse**](PkiReadCrlDeltaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_crl_delta_pem**
> PkiReadCrlDeltaPemResponse pki_read_crl_delta_pem(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_crl_delta_pem_response import PkiReadCrlDeltaPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_crl_delta_pem(pki_mount_path)
        print("The response of SecretsApi->pki_read_crl_delta_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_crl_delta_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCrlDeltaPemResponse**](PkiReadCrlDeltaPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_crl_der**
> PkiReadCrlDerResponse pki_read_crl_der(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_crl_der_response import PkiReadCrlDerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_crl_der(pki_mount_path)
        print("The response of SecretsApi->pki_read_crl_der:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_crl_der: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCrlDerResponse**](PkiReadCrlDerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_crl_pem**
> PkiReadCrlPemResponse pki_read_crl_pem(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_crl_pem_response import PkiReadCrlPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_crl_pem(pki_mount_path)
        print("The response of SecretsApi->pki_read_crl_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_crl_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadCrlPemResponse**](PkiReadCrlPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer**
> PkiReadIssuerResponse pki_read_issuer(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_issuer_response import PkiReadIssuerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_issuer(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_read_issuer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadIssuerResponse**](PkiReadIssuerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer_der**
> PkiReadIssuerDerResponse pki_read_issuer_der(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_issuer_der_response import PkiReadIssuerDerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_issuer_der(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_read_issuer_der:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer_der: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadIssuerDerResponse**](PkiReadIssuerDerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer_issuer_ref_acme_directory**
> pki_read_issuer_issuer_ref_acme_directory(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_issuer_issuer_ref_acme_directory(issuer_ref, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer_issuer_ref_acme_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer_issuer_ref_acme_new_nonce**
> pki_read_issuer_issuer_ref_acme_new_nonce(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_issuer_issuer_ref_acme_new_nonce(issuer_ref, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer_issuer_ref_acme_new_nonce: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer_issuer_ref_roles_role_acme_directory**
> pki_read_issuer_issuer_ref_roles_role_acme_directory(issuer_ref, role, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_issuer_issuer_ref_roles_role_acme_directory(issuer_ref, role, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer_issuer_ref_roles_role_acme_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer_issuer_ref_roles_role_acme_new_nonce**
> pki_read_issuer_issuer_ref_roles_role_acme_new_nonce(issuer_ref, role, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_issuer_issuer_ref_roles_role_acme_new_nonce(issuer_ref, role, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer_issuer_ref_roles_role_acme_new_nonce: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer_json**
> PkiReadIssuerJsonResponse pki_read_issuer_json(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_issuer_json_response import PkiReadIssuerJsonResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_issuer_json(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_read_issuer_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadIssuerJsonResponse**](PkiReadIssuerJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuer_pem**
> PkiReadIssuerPemResponse pki_read_issuer_pem(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_issuer_pem_response import PkiReadIssuerPemResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_issuer_pem(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_read_issuer_pem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuer_pem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadIssuerPemResponse**](PkiReadIssuerPemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_issuers_configuration**
> PkiReadIssuersConfigurationResponse pki_read_issuers_configuration(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_issuers_configuration_response import PkiReadIssuersConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_issuers_configuration(pki_mount_path)
        print("The response of SecretsApi->pki_read_issuers_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_issuers_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadIssuersConfigurationResponse**](PkiReadIssuersConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_key**
> PkiReadKeyResponse pki_read_key(key_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_key_response import PkiReadKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key_ref = 'default' # str | Reference to key; either \"default\" for the configured default key, an identifier of a key, or the name assigned to the key. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_key(key_ref, pki_mount_path)
        print("The response of SecretsApi->pki_read_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_ref** | **str**| Reference to key; either \&quot;default\&quot; for the configured default key, an identifier of a key, or the name assigned to the key. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadKeyResponse**](PkiReadKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_keys_configuration**
> PkiReadKeysConfigurationResponse pki_read_keys_configuration(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_keys_configuration_response import PkiReadKeysConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_keys_configuration(pki_mount_path)
        print("The response of SecretsApi->pki_read_keys_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_keys_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadKeysConfigurationResponse**](PkiReadKeysConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_role**
> PkiReadRoleResponse pki_read_role(name, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_role_response import PkiReadRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_role(name, pki_mount_path)
        print("The response of SecretsApi->pki_read_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadRoleResponse**](PkiReadRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_roles_role_acme_directory**
> pki_read_roles_role_acme_directory(role, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_roles_role_acme_directory(role, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_roles_role_acme_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_roles_role_acme_new_nonce**
> pki_read_roles_role_acme_new_nonce(role, pki_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        await api_instance.pki_read_roles_role_acme_new_nonce(role, pki_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_roles_role_acme_new_nonce: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_read_urls_configuration**
> PkiReadUrlsConfigurationResponse pki_read_urls_configuration(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_read_urls_configuration_response import PkiReadUrlsConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_read_urls_configuration(pki_mount_path)
        print("The response of SecretsApi->pki_read_urls_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_read_urls_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiReadUrlsConfigurationResponse**](PkiReadUrlsConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_replace_root**
> PkiReplaceRootResponse pki_replace_root(pki_mount_path, pki_replace_root_request)



### Example


```python
import ahvac
from ahvac.models.pki_replace_root_request import PkiReplaceRootRequest
from ahvac.models.pki_replace_root_response import PkiReplaceRootResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_replace_root_request = ahvac.PkiReplaceRootRequest() # PkiReplaceRootRequest | 

    try:
        api_response = await api_instance.pki_replace_root(pki_mount_path, pki_replace_root_request)
        print("The response of SecretsApi->pki_replace_root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_replace_root: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_replace_root_request** | [**PkiReplaceRootRequest**](PkiReplaceRootRequest.md)|  | 

### Return type

[**PkiReplaceRootResponse**](PkiReplaceRootResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_revoke**
> PkiRevokeResponse pki_revoke(pki_mount_path, pki_revoke_request)



### Example


```python
import ahvac
from ahvac.models.pki_revoke_request import PkiRevokeRequest
from ahvac.models.pki_revoke_response import PkiRevokeResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_revoke_request = ahvac.PkiRevokeRequest() # PkiRevokeRequest | 

    try:
        api_response = await api_instance.pki_revoke(pki_mount_path, pki_revoke_request)
        print("The response of SecretsApi->pki_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_revoke_request** | [**PkiRevokeRequest**](PkiRevokeRequest.md)|  | 

### Return type

[**PkiRevokeResponse**](PkiRevokeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_revoke_issuer**
> PkiRevokeIssuerResponse pki_revoke_issuer(issuer_ref, pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_revoke_issuer_response import PkiRevokeIssuerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_revoke_issuer(issuer_ref, pki_mount_path)
        print("The response of SecretsApi->pki_revoke_issuer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_revoke_issuer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiRevokeIssuerResponse**](PkiRevokeIssuerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_revoke_with_key**
> PkiRevokeWithKeyResponse pki_revoke_with_key(pki_mount_path, pki_revoke_with_key_request)



### Example


```python
import ahvac
from ahvac.models.pki_revoke_with_key_request import PkiRevokeWithKeyRequest
from ahvac.models.pki_revoke_with_key_response import PkiRevokeWithKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_revoke_with_key_request = ahvac.PkiRevokeWithKeyRequest() # PkiRevokeWithKeyRequest | 

    try:
        api_response = await api_instance.pki_revoke_with_key(pki_mount_path, pki_revoke_with_key_request)
        print("The response of SecretsApi->pki_revoke_with_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_revoke_with_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_revoke_with_key_request** | [**PkiRevokeWithKeyRequest**](PkiRevokeWithKeyRequest.md)|  | 

### Return type

[**PkiRevokeWithKeyResponse**](PkiRevokeWithKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_root_sign_intermediate**
> PkiRootSignIntermediateResponse pki_root_sign_intermediate(pki_mount_path, pki_root_sign_intermediate_request)



### Example


```python
import ahvac
from ahvac.models.pki_root_sign_intermediate_request import PkiRootSignIntermediateRequest
from ahvac.models.pki_root_sign_intermediate_response import PkiRootSignIntermediateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_root_sign_intermediate_request = ahvac.PkiRootSignIntermediateRequest() # PkiRootSignIntermediateRequest | 

    try:
        api_response = await api_instance.pki_root_sign_intermediate(pki_mount_path, pki_root_sign_intermediate_request)
        print("The response of SecretsApi->pki_root_sign_intermediate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_root_sign_intermediate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_root_sign_intermediate_request** | [**PkiRootSignIntermediateRequest**](PkiRootSignIntermediateRequest.md)|  | 

### Return type

[**PkiRootSignIntermediateResponse**](PkiRootSignIntermediateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_root_sign_self_issued**
> PkiRootSignSelfIssuedResponse pki_root_sign_self_issued(pki_mount_path, pki_root_sign_self_issued_request)



### Example


```python
import ahvac
from ahvac.models.pki_root_sign_self_issued_request import PkiRootSignSelfIssuedRequest
from ahvac.models.pki_root_sign_self_issued_response import PkiRootSignSelfIssuedResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_root_sign_self_issued_request = ahvac.PkiRootSignSelfIssuedRequest() # PkiRootSignSelfIssuedRequest | 

    try:
        api_response = await api_instance.pki_root_sign_self_issued(pki_mount_path, pki_root_sign_self_issued_request)
        print("The response of SecretsApi->pki_root_sign_self_issued:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_root_sign_self_issued: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_root_sign_self_issued_request** | [**PkiRootSignSelfIssuedRequest**](PkiRootSignSelfIssuedRequest.md)|  | 

### Return type

[**PkiRootSignSelfIssuedResponse**](PkiRootSignSelfIssuedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_rotate_crl**
> PkiRotateCrlResponse pki_rotate_crl(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_rotate_crl_response import PkiRotateCrlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_rotate_crl(pki_mount_path)
        print("The response of SecretsApi->pki_rotate_crl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_rotate_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiRotateCrlResponse**](PkiRotateCrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_rotate_delta_crl**
> PkiRotateDeltaCrlResponse pki_rotate_delta_crl(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_rotate_delta_crl_response import PkiRotateDeltaCrlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_rotate_delta_crl(pki_mount_path)
        print("The response of SecretsApi->pki_rotate_delta_crl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_rotate_delta_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiRotateDeltaCrlResponse**](PkiRotateDeltaCrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_rotate_root**
> PkiRotateRootResponse pki_rotate_root(exported, pki_mount_path, pki_rotate_root_request)



### Example


```python
import ahvac
from ahvac.models.pki_rotate_root_request import PkiRotateRootRequest
from ahvac.models.pki_rotate_root_response import PkiRotateRootResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    exported = 'exported_example' # str | Must be \"internal\", \"exported\" or \"kms\". If set to \"exported\", the generated private key will be returned. This is your *only* chance to retrieve the private key!
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_rotate_root_request = ahvac.PkiRotateRootRequest() # PkiRotateRootRequest | 

    try:
        api_response = await api_instance.pki_rotate_root(exported, pki_mount_path, pki_rotate_root_request)
        print("The response of SecretsApi->pki_rotate_root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_rotate_root: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exported** | **str**| Must be \&quot;internal\&quot;, \&quot;exported\&quot; or \&quot;kms\&quot;. If set to \&quot;exported\&quot;, the generated private key will be returned. This is your *only* chance to retrieve the private key! | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_rotate_root_request** | [**PkiRotateRootRequest**](PkiRotateRootRequest.md)|  | 

### Return type

[**PkiRotateRootResponse**](PkiRotateRootResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_set_signed_intermediate**
> PkiSetSignedIntermediateResponse pki_set_signed_intermediate(pki_mount_path, pki_set_signed_intermediate_request)



### Example


```python
import ahvac
from ahvac.models.pki_set_signed_intermediate_request import PkiSetSignedIntermediateRequest
from ahvac.models.pki_set_signed_intermediate_response import PkiSetSignedIntermediateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_set_signed_intermediate_request = ahvac.PkiSetSignedIntermediateRequest() # PkiSetSignedIntermediateRequest | 

    try:
        api_response = await api_instance.pki_set_signed_intermediate(pki_mount_path, pki_set_signed_intermediate_request)
        print("The response of SecretsApi->pki_set_signed_intermediate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_set_signed_intermediate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_set_signed_intermediate_request** | [**PkiSetSignedIntermediateRequest**](PkiSetSignedIntermediateRequest.md)|  | 

### Return type

[**PkiSetSignedIntermediateResponse**](PkiSetSignedIntermediateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_sign_verbatim**
> PkiSignVerbatimResponse pki_sign_verbatim(pki_mount_path, pki_sign_verbatim_request)



### Example


```python
import ahvac
from ahvac.models.pki_sign_verbatim_request import PkiSignVerbatimRequest
from ahvac.models.pki_sign_verbatim_response import PkiSignVerbatimResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_sign_verbatim_request = ahvac.PkiSignVerbatimRequest() # PkiSignVerbatimRequest | 

    try:
        api_response = await api_instance.pki_sign_verbatim(pki_mount_path, pki_sign_verbatim_request)
        print("The response of SecretsApi->pki_sign_verbatim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_sign_verbatim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_sign_verbatim_request** | [**PkiSignVerbatimRequest**](PkiSignVerbatimRequest.md)|  | 

### Return type

[**PkiSignVerbatimResponse**](PkiSignVerbatimResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_sign_verbatim_with_role**
> PkiSignVerbatimWithRoleResponse pki_sign_verbatim_with_role(role, pki_mount_path, pki_sign_verbatim_with_role_request)



### Example


```python
import ahvac
from ahvac.models.pki_sign_verbatim_with_role_request import PkiSignVerbatimWithRoleRequest
from ahvac.models.pki_sign_verbatim_with_role_response import PkiSignVerbatimWithRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role with configuration for this request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_sign_verbatim_with_role_request = ahvac.PkiSignVerbatimWithRoleRequest() # PkiSignVerbatimWithRoleRequest | 

    try:
        api_response = await api_instance.pki_sign_verbatim_with_role(role, pki_mount_path, pki_sign_verbatim_with_role_request)
        print("The response of SecretsApi->pki_sign_verbatim_with_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_sign_verbatim_with_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role with configuration for this request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_sign_verbatim_with_role_request** | [**PkiSignVerbatimWithRoleRequest**](PkiSignVerbatimWithRoleRequest.md)|  | 

### Return type

[**PkiSignVerbatimWithRoleResponse**](PkiSignVerbatimWithRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_sign_with_role**
> PkiSignWithRoleResponse pki_sign_with_role(role, pki_mount_path, pki_sign_with_role_request)



### Example


```python
import ahvac
from ahvac.models.pki_sign_with_role_request import PkiSignWithRoleRequest
from ahvac.models.pki_sign_with_role_response import PkiSignWithRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role with configuration for this request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_sign_with_role_request = ahvac.PkiSignWithRoleRequest() # PkiSignWithRoleRequest | 

    try:
        api_response = await api_instance.pki_sign_with_role(role, pki_mount_path, pki_sign_with_role_request)
        print("The response of SecretsApi->pki_sign_with_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_sign_with_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role with configuration for this request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_sign_with_role_request** | [**PkiSignWithRoleRequest**](PkiSignWithRoleRequest.md)|  | 

### Return type

[**PkiSignWithRoleResponse**](PkiSignWithRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_tidy**
> pki_tidy(pki_mount_path, pki_tidy_request)



### Example


```python
import ahvac
from ahvac.models.pki_tidy_request import PkiTidyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_tidy_request = ahvac.PkiTidyRequest() # PkiTidyRequest | 

    try:
        await api_instance.pki_tidy(pki_mount_path, pki_tidy_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_tidy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_tidy_request** | [**PkiTidyRequest**](PkiTidyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_tidy_cancel**
> PkiTidyCancelResponse pki_tidy_cancel(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_tidy_cancel_response import PkiTidyCancelResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_tidy_cancel(pki_mount_path)
        print("The response of SecretsApi->pki_tidy_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_tidy_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiTidyCancelResponse**](PkiTidyCancelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_tidy_status**
> PkiTidyStatusResponse pki_tidy_status(pki_mount_path)



### Example


```python
import ahvac
from ahvac.models.pki_tidy_status_response import PkiTidyStatusResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')

    try:
        api_response = await api_instance.pki_tidy_status(pki_mount_path)
        print("The response of SecretsApi->pki_tidy_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_tidy_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]

### Return type

[**PkiTidyStatusResponse**](PkiTidyStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_account_kid**
> pki_write_acme_account_kid(kid, pki_mount_path, pki_write_acme_account_kid_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_account_kid_request import PkiWriteAcmeAccountKidRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kid = 'kid_example' # str | The key identifier provided by the CA
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_account_kid_request = ahvac.PkiWriteAcmeAccountKidRequest() # PkiWriteAcmeAccountKidRequest | 

    try:
        await api_instance.pki_write_acme_account_kid(kid, pki_mount_path, pki_write_acme_account_kid_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_account_kid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| The key identifier provided by the CA | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_account_kid_request** | [**PkiWriteAcmeAccountKidRequest**](PkiWriteAcmeAccountKidRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_authorization_auth_id**
> pki_write_acme_authorization_auth_id(auth_id, pki_mount_path, pki_write_acme_authorization_auth_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_authorization_auth_id_request import PkiWriteAcmeAuthorizationAuthIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_authorization_auth_id_request = ahvac.PkiWriteAcmeAuthorizationAuthIdRequest() # PkiWriteAcmeAuthorizationAuthIdRequest | 

    try:
        await api_instance.pki_write_acme_authorization_auth_id(auth_id, pki_mount_path, pki_write_acme_authorization_auth_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_authorization_auth_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_authorization_auth_id_request** | [**PkiWriteAcmeAuthorizationAuthIdRequest**](PkiWriteAcmeAuthorizationAuthIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_challenge_auth_id_challenge_type**
> pki_write_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, pki_mount_path, pki_write_acme_challenge_auth_id_challenge_type_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_challenge_auth_id_challenge_type_request import PkiWriteAcmeChallengeAuthIdChallengeTypeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    challenge_type = 'challenge_type_example' # str | ACME challenge type
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_challenge_auth_id_challenge_type_request = ahvac.PkiWriteAcmeChallengeAuthIdChallengeTypeRequest() # PkiWriteAcmeChallengeAuthIdChallengeTypeRequest | 

    try:
        await api_instance.pki_write_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, pki_mount_path, pki_write_acme_challenge_auth_id_challenge_type_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_challenge_auth_id_challenge_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **challenge_type** | **str**| ACME challenge type | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_challenge_auth_id_challenge_type_request** | [**PkiWriteAcmeChallengeAuthIdChallengeTypeRequest**](PkiWriteAcmeChallengeAuthIdChallengeTypeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_new_account**
> pki_write_acme_new_account(pki_mount_path, pki_write_acme_new_account_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_new_account_request import PkiWriteAcmeNewAccountRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_new_account_request = ahvac.PkiWriteAcmeNewAccountRequest() # PkiWriteAcmeNewAccountRequest | 

    try:
        await api_instance.pki_write_acme_new_account(pki_mount_path, pki_write_acme_new_account_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_new_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_new_account_request** | [**PkiWriteAcmeNewAccountRequest**](PkiWriteAcmeNewAccountRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_new_order**
> pki_write_acme_new_order(pki_mount_path, pki_write_acme_new_order_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_new_order_request import PkiWriteAcmeNewOrderRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_new_order_request = ahvac.PkiWriteAcmeNewOrderRequest() # PkiWriteAcmeNewOrderRequest | 

    try:
        await api_instance.pki_write_acme_new_order(pki_mount_path, pki_write_acme_new_order_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_new_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_new_order_request** | [**PkiWriteAcmeNewOrderRequest**](PkiWriteAcmeNewOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_order_order_id**
> pki_write_acme_order_order_id(order_id, pki_mount_path, pki_write_acme_order_order_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_order_order_id_request import PkiWriteAcmeOrderOrderIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_order_order_id_request = ahvac.PkiWriteAcmeOrderOrderIdRequest() # PkiWriteAcmeOrderOrderIdRequest | 

    try:
        await api_instance.pki_write_acme_order_order_id(order_id, pki_mount_path, pki_write_acme_order_order_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_order_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ACME order identifier to fetch | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_order_order_id_request** | [**PkiWriteAcmeOrderOrderIdRequest**](PkiWriteAcmeOrderOrderIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_order_order_id_cert**
> pki_write_acme_order_order_id_cert(order_id, pki_mount_path, pki_write_acme_order_order_id_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_order_order_id_cert_request import PkiWriteAcmeOrderOrderIdCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_order_order_id_cert_request = ahvac.PkiWriteAcmeOrderOrderIdCertRequest() # PkiWriteAcmeOrderOrderIdCertRequest | 

    try:
        await api_instance.pki_write_acme_order_order_id_cert(order_id, pki_mount_path, pki_write_acme_order_order_id_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_order_order_id_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ACME order identifier to fetch | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_order_order_id_cert_request** | [**PkiWriteAcmeOrderOrderIdCertRequest**](PkiWriteAcmeOrderOrderIdCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_order_order_id_finalize**
> pki_write_acme_order_order_id_finalize(order_id, pki_mount_path, pki_write_acme_order_order_id_finalize_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_order_order_id_finalize_request import PkiWriteAcmeOrderOrderIdFinalizeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_order_order_id_finalize_request = ahvac.PkiWriteAcmeOrderOrderIdFinalizeRequest() # PkiWriteAcmeOrderOrderIdFinalizeRequest | 

    try:
        await api_instance.pki_write_acme_order_order_id_finalize(order_id, pki_mount_path, pki_write_acme_order_order_id_finalize_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_order_order_id_finalize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ACME order identifier to fetch | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_order_order_id_finalize_request** | [**PkiWriteAcmeOrderOrderIdFinalizeRequest**](PkiWriteAcmeOrderOrderIdFinalizeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_orders**
> pki_write_acme_orders(pki_mount_path, pki_write_acme_orders_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_orders_request import PkiWriteAcmeOrdersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_orders_request = ahvac.PkiWriteAcmeOrdersRequest() # PkiWriteAcmeOrdersRequest | 

    try:
        await api_instance.pki_write_acme_orders(pki_mount_path, pki_write_acme_orders_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_orders_request** | [**PkiWriteAcmeOrdersRequest**](PkiWriteAcmeOrdersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_acme_revoke_cert**
> pki_write_acme_revoke_cert(pki_mount_path, pki_write_acme_revoke_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_acme_revoke_cert_request import PkiWriteAcmeRevokeCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_acme_revoke_cert_request = ahvac.PkiWriteAcmeRevokeCertRequest() # PkiWriteAcmeRevokeCertRequest | 

    try:
        await api_instance.pki_write_acme_revoke_cert(pki_mount_path, pki_write_acme_revoke_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_acme_revoke_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_acme_revoke_cert_request** | [**PkiWriteAcmeRevokeCertRequest**](PkiWriteAcmeRevokeCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer**
> PkiWriteIssuerResponse pki_write_issuer(issuer_ref, pki_mount_path, pki_write_issuer_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_request import PkiWriteIssuerRequest
from ahvac.models.pki_write_issuer_response import PkiWriteIssuerResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'default' # str | Reference to a existing issuer; either \"default\" for the configured default issuer, an identifier or the name assigned to the issuer. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_request = ahvac.PkiWriteIssuerRequest() # PkiWriteIssuerRequest | 

    try:
        api_response = await api_instance.pki_write_issuer(issuer_ref, pki_mount_path, pki_write_issuer_request)
        print("The response of SecretsApi->pki_write_issuer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to a existing issuer; either \&quot;default\&quot; for the configured default issuer, an identifier or the name assigned to the issuer. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_request** | [**PkiWriteIssuerRequest**](PkiWriteIssuerRequest.md)|  | 

### Return type

[**PkiWriteIssuerResponse**](PkiWriteIssuerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_account_kid**
> pki_write_issuer_issuer_ref_acme_account_kid(issuer_ref, kid, pki_mount_path, pki_write_issuer_issuer_ref_acme_account_kid_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_account_kid_request import PkiWriteIssuerIssuerRefAcmeAccountKidRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    kid = 'kid_example' # str | The key identifier provided by the CA
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_account_kid_request = ahvac.PkiWriteIssuerIssuerRefAcmeAccountKidRequest() # PkiWriteIssuerIssuerRefAcmeAccountKidRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_account_kid(issuer_ref, kid, pki_mount_path, pki_write_issuer_issuer_ref_acme_account_kid_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_account_kid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **kid** | **str**| The key identifier provided by the CA | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_account_kid_request** | [**PkiWriteIssuerIssuerRefAcmeAccountKidRequest**](PkiWriteIssuerIssuerRefAcmeAccountKidRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_authorization_auth_id**
> pki_write_issuer_issuer_ref_acme_authorization_auth_id(auth_id, issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_authorization_auth_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_authorization_auth_id_request import PkiWriteIssuerIssuerRefAcmeAuthorizationAuthIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_authorization_auth_id_request = ahvac.PkiWriteIssuerIssuerRefAcmeAuthorizationAuthIdRequest() # PkiWriteIssuerIssuerRefAcmeAuthorizationAuthIdRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_authorization_auth_id(auth_id, issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_authorization_auth_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_authorization_auth_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_authorization_auth_id_request** | [**PkiWriteIssuerIssuerRefAcmeAuthorizationAuthIdRequest**](PkiWriteIssuerIssuerRefAcmeAuthorizationAuthIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type**
> pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type_request import PkiWriteIssuerIssuerRefAcmeChallengeAuthIdChallengeTypeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    challenge_type = 'challenge_type_example' # str | ACME challenge type
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type_request = ahvac.PkiWriteIssuerIssuerRefAcmeChallengeAuthIdChallengeTypeRequest() # PkiWriteIssuerIssuerRefAcmeChallengeAuthIdChallengeTypeRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **challenge_type** | **str**| ACME challenge type | 
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_challenge_auth_id_challenge_type_request** | [**PkiWriteIssuerIssuerRefAcmeChallengeAuthIdChallengeTypeRequest**](PkiWriteIssuerIssuerRefAcmeChallengeAuthIdChallengeTypeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_new_account**
> pki_write_issuer_issuer_ref_acme_new_account(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_new_account_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_new_account_request import PkiWriteIssuerIssuerRefAcmeNewAccountRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_new_account_request = ahvac.PkiWriteIssuerIssuerRefAcmeNewAccountRequest() # PkiWriteIssuerIssuerRefAcmeNewAccountRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_new_account(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_new_account_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_new_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_new_account_request** | [**PkiWriteIssuerIssuerRefAcmeNewAccountRequest**](PkiWriteIssuerIssuerRefAcmeNewAccountRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_new_order**
> pki_write_issuer_issuer_ref_acme_new_order(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_new_order_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_new_order_request import PkiWriteIssuerIssuerRefAcmeNewOrderRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_new_order_request = ahvac.PkiWriteIssuerIssuerRefAcmeNewOrderRequest() # PkiWriteIssuerIssuerRefAcmeNewOrderRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_new_order(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_new_order_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_new_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_new_order_request** | [**PkiWriteIssuerIssuerRefAcmeNewOrderRequest**](PkiWriteIssuerIssuerRefAcmeNewOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_order_order_id**
> pki_write_issuer_issuer_ref_acme_order_order_id(issuer_ref, order_id, pki_mount_path, pki_write_issuer_issuer_ref_acme_order_order_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_order_order_id_request import PkiWriteIssuerIssuerRefAcmeOrderOrderIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_order_order_id_request = ahvac.PkiWriteIssuerIssuerRefAcmeOrderOrderIdRequest() # PkiWriteIssuerIssuerRefAcmeOrderOrderIdRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_order_order_id(issuer_ref, order_id, pki_mount_path, pki_write_issuer_issuer_ref_acme_order_order_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_order_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **order_id** | **str**| The ACME order identifier to fetch | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_order_order_id_request** | [**PkiWriteIssuerIssuerRefAcmeOrderOrderIdRequest**](PkiWriteIssuerIssuerRefAcmeOrderOrderIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_order_order_id_cert**
> pki_write_issuer_issuer_ref_acme_order_order_id_cert(issuer_ref, order_id, pki_mount_path, pki_write_issuer_issuer_ref_acme_order_order_id_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_order_order_id_cert_request import PkiWriteIssuerIssuerRefAcmeOrderOrderIdCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_order_order_id_cert_request = ahvac.PkiWriteIssuerIssuerRefAcmeOrderOrderIdCertRequest() # PkiWriteIssuerIssuerRefAcmeOrderOrderIdCertRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_order_order_id_cert(issuer_ref, order_id, pki_mount_path, pki_write_issuer_issuer_ref_acme_order_order_id_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_order_order_id_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **order_id** | **str**| The ACME order identifier to fetch | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_order_order_id_cert_request** | [**PkiWriteIssuerIssuerRefAcmeOrderOrderIdCertRequest**](PkiWriteIssuerIssuerRefAcmeOrderOrderIdCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_order_order_id_finalize**
> pki_write_issuer_issuer_ref_acme_order_order_id_finalize(issuer_ref, order_id, pki_mount_path, pki_write_issuer_issuer_ref_acme_order_order_id_finalize_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_order_order_id_finalize_request import PkiWriteIssuerIssuerRefAcmeOrderOrderIdFinalizeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_order_order_id_finalize_request = ahvac.PkiWriteIssuerIssuerRefAcmeOrderOrderIdFinalizeRequest() # PkiWriteIssuerIssuerRefAcmeOrderOrderIdFinalizeRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_order_order_id_finalize(issuer_ref, order_id, pki_mount_path, pki_write_issuer_issuer_ref_acme_order_order_id_finalize_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_order_order_id_finalize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **order_id** | **str**| The ACME order identifier to fetch | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_order_order_id_finalize_request** | [**PkiWriteIssuerIssuerRefAcmeOrderOrderIdFinalizeRequest**](PkiWriteIssuerIssuerRefAcmeOrderOrderIdFinalizeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_orders**
> pki_write_issuer_issuer_ref_acme_orders(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_orders_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_orders_request import PkiWriteIssuerIssuerRefAcmeOrdersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_orders_request = ahvac.PkiWriteIssuerIssuerRefAcmeOrdersRequest() # PkiWriteIssuerIssuerRefAcmeOrdersRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_orders(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_orders_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_orders_request** | [**PkiWriteIssuerIssuerRefAcmeOrdersRequest**](PkiWriteIssuerIssuerRefAcmeOrdersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_acme_revoke_cert**
> pki_write_issuer_issuer_ref_acme_revoke_cert(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_revoke_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_acme_revoke_cert_request import PkiWriteIssuerIssuerRefAcmeRevokeCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_acme_revoke_cert_request = ahvac.PkiWriteIssuerIssuerRefAcmeRevokeCertRequest() # PkiWriteIssuerIssuerRefAcmeRevokeCertRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_acme_revoke_cert(issuer_ref, pki_mount_path, pki_write_issuer_issuer_ref_acme_revoke_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_acme_revoke_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_acme_revoke_cert_request** | [**PkiWriteIssuerIssuerRefAcmeRevokeCertRequest**](PkiWriteIssuerIssuerRefAcmeRevokeCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_account_kid**
> pki_write_issuer_issuer_ref_roles_role_acme_account_kid(issuer_ref, kid, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_account_kid_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_account_kid_request import PkiWriteIssuerIssuerRefRolesRoleAcmeAccountKidRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    kid = 'kid_example' # str | The key identifier provided by the CA
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_account_kid_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeAccountKidRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeAccountKidRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_account_kid(issuer_ref, kid, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_account_kid_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_account_kid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **kid** | **str**| The key identifier provided by the CA | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_account_kid_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeAccountKidRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeAccountKidRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id**
> pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id(auth_id, issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id_request import PkiWriteIssuerIssuerRefRolesRoleAcmeAuthorizationAuthIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeAuthorizationAuthIdRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeAuthorizationAuthIdRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id(auth_id, issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_authorization_auth_id_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeAuthorizationAuthIdRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeAuthorizationAuthIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type**
> pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type_request import PkiWriteIssuerIssuerRefRolesRoleAcmeChallengeAuthIdChallengeTypeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    challenge_type = 'challenge_type_example' # str | ACME challenge type
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeChallengeAuthIdChallengeTypeRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeChallengeAuthIdChallengeTypeRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **challenge_type** | **str**| ACME challenge type | 
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_challenge_auth_id_challenge_type_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeChallengeAuthIdChallengeTypeRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeChallengeAuthIdChallengeTypeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_new_account**
> pki_write_issuer_issuer_ref_roles_role_acme_new_account(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_new_account_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_new_account_request import PkiWriteIssuerIssuerRefRolesRoleAcmeNewAccountRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_new_account_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeNewAccountRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeNewAccountRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_new_account(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_new_account_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_new_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_new_account_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeNewAccountRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeNewAccountRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_new_order**
> pki_write_issuer_issuer_ref_roles_role_acme_new_order(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_new_order_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_new_order_request import PkiWriteIssuerIssuerRefRolesRoleAcmeNewOrderRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_new_order_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeNewOrderRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeNewOrderRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_new_order(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_new_order_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_new_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_new_order_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeNewOrderRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeNewOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_order_order_id**
> pki_write_issuer_issuer_ref_roles_role_acme_order_order_id(issuer_ref, order_id, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_request import PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_order_order_id(issuer_ref, order_id, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_order_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **order_id** | **str**| The ACME order identifier to fetch | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert**
> pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert(issuer_ref, order_id, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert_request import PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdCertRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdCertRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert(issuer_ref, order_id, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **order_id** | **str**| The ACME order identifier to fetch | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_cert_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdCertRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize**
> pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize(issuer_ref, order_id, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize_request import PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize(issuer_ref, order_id, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **order_id** | **str**| The ACME order identifier to fetch | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_order_order_id_finalize_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeOrderOrderIdFinalizeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_orders**
> pki_write_issuer_issuer_ref_roles_role_acme_orders(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_orders_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_orders_request import PkiWriteIssuerIssuerRefRolesRoleAcmeOrdersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_orders_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeOrdersRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeOrdersRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_orders(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_orders_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_orders_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeOrdersRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeOrdersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert**
> pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert_request import PkiWriteIssuerIssuerRefRolesRoleAcmeRevokeCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    issuer_ref = 'issuer_ref_example' # str | Reference to an existing issuer name or issuer id
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert_request = ahvac.PkiWriteIssuerIssuerRefRolesRoleAcmeRevokeCertRequest() # PkiWriteIssuerIssuerRefRolesRoleAcmeRevokeCertRequest | 

    try:
        await api_instance.pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert(issuer_ref, role, pki_mount_path, pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issuer_ref** | **str**| Reference to an existing issuer name or issuer id | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_issuer_issuer_ref_roles_role_acme_revoke_cert_request** | [**PkiWriteIssuerIssuerRefRolesRoleAcmeRevokeCertRequest**](PkiWriteIssuerIssuerRefRolesRoleAcmeRevokeCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_key**
> PkiWriteKeyResponse pki_write_key(key_ref, pki_mount_path, pki_write_key_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_key_request import PkiWriteKeyRequest
from ahvac.models.pki_write_key_response import PkiWriteKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    key_ref = 'default' # str | Reference to key; either \"default\" for the configured default key, an identifier of a key, or the name assigned to the key. (default to 'default')
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_key_request = ahvac.PkiWriteKeyRequest() # PkiWriteKeyRequest | 

    try:
        api_response = await api_instance.pki_write_key(key_ref, pki_mount_path, pki_write_key_request)
        print("The response of SecretsApi->pki_write_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_ref** | **str**| Reference to key; either \&quot;default\&quot; for the configured default key, an identifier of a key, or the name assigned to the key. | [default to &#39;default&#39;]
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_key_request** | [**PkiWriteKeyRequest**](PkiWriteKeyRequest.md)|  | 

### Return type

[**PkiWriteKeyResponse**](PkiWriteKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_role**
> PkiWriteRoleResponse pki_write_role(name, pki_mount_path, pki_write_role_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_role_request import PkiWriteRoleRequest
from ahvac.models.pki_write_role_response import PkiWriteRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_role_request = ahvac.PkiWriteRoleRequest() # PkiWriteRoleRequest | 

    try:
        api_response = await api_instance.pki_write_role(name, pki_mount_path, pki_write_role_request)
        print("The response of SecretsApi->pki_write_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_role_request** | [**PkiWriteRoleRequest**](PkiWriteRoleRequest.md)|  | 

### Return type

[**PkiWriteRoleResponse**](PkiWriteRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_account_kid**
> pki_write_roles_role_acme_account_kid(kid, role, pki_mount_path, pki_write_roles_role_acme_account_kid_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_account_kid_request import PkiWriteRolesRoleAcmeAccountKidRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    kid = 'kid_example' # str | The key identifier provided by the CA
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_account_kid_request = ahvac.PkiWriteRolesRoleAcmeAccountKidRequest() # PkiWriteRolesRoleAcmeAccountKidRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_account_kid(kid, role, pki_mount_path, pki_write_roles_role_acme_account_kid_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_account_kid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| The key identifier provided by the CA | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_account_kid_request** | [**PkiWriteRolesRoleAcmeAccountKidRequest**](PkiWriteRolesRoleAcmeAccountKidRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_authorization_auth_id**
> pki_write_roles_role_acme_authorization_auth_id(auth_id, role, pki_mount_path, pki_write_roles_role_acme_authorization_auth_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_authorization_auth_id_request import PkiWriteRolesRoleAcmeAuthorizationAuthIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_authorization_auth_id_request = ahvac.PkiWriteRolesRoleAcmeAuthorizationAuthIdRequest() # PkiWriteRolesRoleAcmeAuthorizationAuthIdRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_authorization_auth_id(auth_id, role, pki_mount_path, pki_write_roles_role_acme_authorization_auth_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_authorization_auth_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_authorization_auth_id_request** | [**PkiWriteRolesRoleAcmeAuthorizationAuthIdRequest**](PkiWriteRolesRoleAcmeAuthorizationAuthIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_challenge_auth_id_challenge_type**
> pki_write_roles_role_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, role, pki_mount_path, pki_write_roles_role_acme_challenge_auth_id_challenge_type_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_challenge_auth_id_challenge_type_request import PkiWriteRolesRoleAcmeChallengeAuthIdChallengeTypeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    auth_id = 'auth_id_example' # str | ACME authorization identifier value
    challenge_type = 'challenge_type_example' # str | ACME challenge type
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_challenge_auth_id_challenge_type_request = ahvac.PkiWriteRolesRoleAcmeChallengeAuthIdChallengeTypeRequest() # PkiWriteRolesRoleAcmeChallengeAuthIdChallengeTypeRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_challenge_auth_id_challenge_type(auth_id, challenge_type, role, pki_mount_path, pki_write_roles_role_acme_challenge_auth_id_challenge_type_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_challenge_auth_id_challenge_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_id** | **str**| ACME authorization identifier value | 
 **challenge_type** | **str**| ACME challenge type | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_challenge_auth_id_challenge_type_request** | [**PkiWriteRolesRoleAcmeChallengeAuthIdChallengeTypeRequest**](PkiWriteRolesRoleAcmeChallengeAuthIdChallengeTypeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_new_account**
> pki_write_roles_role_acme_new_account(role, pki_mount_path, pki_write_roles_role_acme_new_account_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_new_account_request import PkiWriteRolesRoleAcmeNewAccountRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_new_account_request = ahvac.PkiWriteRolesRoleAcmeNewAccountRequest() # PkiWriteRolesRoleAcmeNewAccountRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_new_account(role, pki_mount_path, pki_write_roles_role_acme_new_account_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_new_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_new_account_request** | [**PkiWriteRolesRoleAcmeNewAccountRequest**](PkiWriteRolesRoleAcmeNewAccountRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_new_order**
> pki_write_roles_role_acme_new_order(role, pki_mount_path, pki_write_roles_role_acme_new_order_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_new_order_request import PkiWriteRolesRoleAcmeNewOrderRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_new_order_request = ahvac.PkiWriteRolesRoleAcmeNewOrderRequest() # PkiWriteRolesRoleAcmeNewOrderRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_new_order(role, pki_mount_path, pki_write_roles_role_acme_new_order_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_new_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_new_order_request** | [**PkiWriteRolesRoleAcmeNewOrderRequest**](PkiWriteRolesRoleAcmeNewOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_order_order_id**
> pki_write_roles_role_acme_order_order_id(order_id, role, pki_mount_path, pki_write_roles_role_acme_order_order_id_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_order_order_id_request import PkiWriteRolesRoleAcmeOrderOrderIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_order_order_id_request = ahvac.PkiWriteRolesRoleAcmeOrderOrderIdRequest() # PkiWriteRolesRoleAcmeOrderOrderIdRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_order_order_id(order_id, role, pki_mount_path, pki_write_roles_role_acme_order_order_id_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_order_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ACME order identifier to fetch | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_order_order_id_request** | [**PkiWriteRolesRoleAcmeOrderOrderIdRequest**](PkiWriteRolesRoleAcmeOrderOrderIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_order_order_id_cert**
> pki_write_roles_role_acme_order_order_id_cert(order_id, role, pki_mount_path, pki_write_roles_role_acme_order_order_id_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_order_order_id_cert_request import PkiWriteRolesRoleAcmeOrderOrderIdCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_order_order_id_cert_request = ahvac.PkiWriteRolesRoleAcmeOrderOrderIdCertRequest() # PkiWriteRolesRoleAcmeOrderOrderIdCertRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_order_order_id_cert(order_id, role, pki_mount_path, pki_write_roles_role_acme_order_order_id_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_order_order_id_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ACME order identifier to fetch | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_order_order_id_cert_request** | [**PkiWriteRolesRoleAcmeOrderOrderIdCertRequest**](PkiWriteRolesRoleAcmeOrderOrderIdCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_order_order_id_finalize**
> pki_write_roles_role_acme_order_order_id_finalize(order_id, role, pki_mount_path, pki_write_roles_role_acme_order_order_id_finalize_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_order_order_id_finalize_request import PkiWriteRolesRoleAcmeOrderOrderIdFinalizeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    order_id = 'order_id_example' # str | The ACME order identifier to fetch
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_order_order_id_finalize_request = ahvac.PkiWriteRolesRoleAcmeOrderOrderIdFinalizeRequest() # PkiWriteRolesRoleAcmeOrderOrderIdFinalizeRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_order_order_id_finalize(order_id, role, pki_mount_path, pki_write_roles_role_acme_order_order_id_finalize_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_order_order_id_finalize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ACME order identifier to fetch | 
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_order_order_id_finalize_request** | [**PkiWriteRolesRoleAcmeOrderOrderIdFinalizeRequest**](PkiWriteRolesRoleAcmeOrderOrderIdFinalizeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_orders**
> pki_write_roles_role_acme_orders(role, pki_mount_path, pki_write_roles_role_acme_orders_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_orders_request import PkiWriteRolesRoleAcmeOrdersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_orders_request = ahvac.PkiWriteRolesRoleAcmeOrdersRequest() # PkiWriteRolesRoleAcmeOrdersRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_orders(role, pki_mount_path, pki_write_roles_role_acme_orders_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_orders_request** | [**PkiWriteRolesRoleAcmeOrdersRequest**](PkiWriteRolesRoleAcmeOrdersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pki_write_roles_role_acme_revoke_cert**
> pki_write_roles_role_acme_revoke_cert(role, pki_mount_path, pki_write_roles_role_acme_revoke_cert_request)



### Example


```python
import ahvac
from ahvac.models.pki_write_roles_role_acme_revoke_cert_request import PkiWriteRolesRoleAcmeRevokeCertRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role for the acme request
    pki_mount_path = 'pki' # str | Path that the backend was mounted at (default to 'pki')
    pki_write_roles_role_acme_revoke_cert_request = ahvac.PkiWriteRolesRoleAcmeRevokeCertRequest() # PkiWriteRolesRoleAcmeRevokeCertRequest | 

    try:
        await api_instance.pki_write_roles_role_acme_revoke_cert(role, pki_mount_path, pki_write_roles_role_acme_revoke_cert_request)
    except Exception as e:
        print("Exception when calling SecretsApi->pki_write_roles_role_acme_revoke_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role for the acme request | 
 **pki_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;pki&#39;]
 **pki_write_roles_role_acme_revoke_cert_request** | [**PkiWriteRolesRoleAcmeRevokeCertRequest**](PkiWriteRolesRoleAcmeRevokeCertRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_configure_connection**
> rabbit_mq_configure_connection(rabbitmq_mount_path, rabbit_mq_configure_connection_request)

Configure the connection URI, username, and password to talk to RabbitMQ management HTTP API.

### Example


```python
import ahvac
from ahvac.models.rabbit_mq_configure_connection_request import RabbitMqConfigureConnectionRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')
    rabbit_mq_configure_connection_request = ahvac.RabbitMqConfigureConnectionRequest() # RabbitMqConfigureConnectionRequest | 

    try:
        # Configure the connection URI, username, and password to talk to RabbitMQ management HTTP API.
        await api_instance.rabbit_mq_configure_connection(rabbitmq_mount_path, rabbit_mq_configure_connection_request)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_configure_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]
 **rabbit_mq_configure_connection_request** | [**RabbitMqConfigureConnectionRequest**](RabbitMqConfigureConnectionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_configure_lease**
> rabbit_mq_configure_lease(rabbitmq_mount_path, rabbit_mq_configure_lease_request)



### Example


```python
import ahvac
from ahvac.models.rabbit_mq_configure_lease_request import RabbitMqConfigureLeaseRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')
    rabbit_mq_configure_lease_request = ahvac.RabbitMqConfigureLeaseRequest() # RabbitMqConfigureLeaseRequest | 

    try:
        await api_instance.rabbit_mq_configure_lease(rabbitmq_mount_path, rabbit_mq_configure_lease_request)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_configure_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]
 **rabbit_mq_configure_lease_request** | [**RabbitMqConfigureLeaseRequest**](RabbitMqConfigureLeaseRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_delete_role**
> rabbit_mq_delete_role(name, rabbitmq_mount_path)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')

    try:
        # Manage the roles that can be created with this backend.
        await api_instance.rabbit_mq_delete_role(name, rabbitmq_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_list_roles**
> StandardListResponse rabbit_mq_list_roles(rabbitmq_mount_path, list)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage the roles that can be created with this backend.
        api_response = await api_instance.rabbit_mq_list_roles(rabbitmq_mount_path, list)
        print("The response of SecretsApi->rabbit_mq_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_read_lease_configuration**
> rabbit_mq_read_lease_configuration(rabbitmq_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')

    try:
        await api_instance.rabbit_mq_read_lease_configuration(rabbitmq_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_read_lease_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_read_role**
> rabbit_mq_read_role(name, rabbitmq_mount_path)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')

    try:
        # Manage the roles that can be created with this backend.
        await api_instance.rabbit_mq_read_role(name, rabbitmq_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_request_credentials**
> rabbit_mq_request_credentials(name, rabbitmq_mount_path)

Request RabbitMQ credentials for a certain role.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')

    try:
        # Request RabbitMQ credentials for a certain role.
        await api_instance.rabbit_mq_request_credentials(name, rabbitmq_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_request_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rabbit_mq_write_role**
> rabbit_mq_write_role(name, rabbitmq_mount_path, rabbit_mq_write_role_request)

Manage the roles that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.rabbit_mq_write_role_request import RabbitMqWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role.
    rabbitmq_mount_path = 'rabbitmq' # str | Path that the backend was mounted at (default to 'rabbitmq')
    rabbit_mq_write_role_request = ahvac.RabbitMqWriteRoleRequest() # RabbitMqWriteRoleRequest | 

    try:
        # Manage the roles that can be created with this backend.
        await api_instance.rabbit_mq_write_role(name, rabbitmq_mount_path, rabbit_mq_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->rabbit_mq_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **rabbitmq_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;rabbitmq&#39;]
 **rabbit_mq_write_role_request** | [**RabbitMqWriteRoleRequest**](RabbitMqWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_configure_ca**
> ssh_configure_ca(ssh_mount_path, ssh_configure_ca_request)



### Example


```python
import ahvac
from ahvac.models.ssh_configure_ca_request import SshConfigureCaRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_configure_ca_request = ahvac.SshConfigureCaRequest() # SshConfigureCaRequest | 

    try:
        await api_instance.ssh_configure_ca(ssh_mount_path, ssh_configure_ca_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_configure_ca: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_configure_ca_request** | [**SshConfigureCaRequest**](SshConfigureCaRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_configure_zero_address**
> ssh_configure_zero_address(ssh_mount_path, ssh_configure_zero_address_request)



### Example


```python
import ahvac
from ahvac.models.ssh_configure_zero_address_request import SshConfigureZeroAddressRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_configure_zero_address_request = ahvac.SshConfigureZeroAddressRequest() # SshConfigureZeroAddressRequest | 

    try:
        await api_instance.ssh_configure_zero_address(ssh_mount_path, ssh_configure_zero_address_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_configure_zero_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_configure_zero_address_request** | [**SshConfigureZeroAddressRequest**](SshConfigureZeroAddressRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_delete_ca_configuration**
> ssh_delete_ca_configuration(ssh_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        await api_instance.ssh_delete_ca_configuration(ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_delete_ca_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_delete_role**
> ssh_delete_role(role, ssh_mount_path)

Manage the 'roles' that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | [Required for all types] Name of the role being created.
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        # Manage the 'roles' that can be created with this backend.
        await api_instance.ssh_delete_role(role, ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| [Required for all types] Name of the role being created. | 
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_delete_zero_address_configuration**
> ssh_delete_zero_address_configuration(ssh_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        await api_instance.ssh_delete_zero_address_configuration(ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_delete_zero_address_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_generate_credentials**
> ssh_generate_credentials(role, ssh_mount_path, ssh_generate_credentials_request)

Creates a credential for establishing SSH connection with the remote host.

### Example


```python
import ahvac
from ahvac.models.ssh_generate_credentials_request import SshGenerateCredentialsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | [Required] Name of the role
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_generate_credentials_request = ahvac.SshGenerateCredentialsRequest() # SshGenerateCredentialsRequest | 

    try:
        # Creates a credential for establishing SSH connection with the remote host.
        await api_instance.ssh_generate_credentials(role, ssh_mount_path, ssh_generate_credentials_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| [Required] Name of the role | 
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_generate_credentials_request** | [**SshGenerateCredentialsRequest**](SshGenerateCredentialsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_issue_certificate**
> ssh_issue_certificate(role, ssh_mount_path, ssh_issue_certificate_request)



### Example


```python
import ahvac
from ahvac.models.ssh_issue_certificate_request import SshIssueCertificateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role with configuration for this request.
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_issue_certificate_request = ahvac.SshIssueCertificateRequest() # SshIssueCertificateRequest | 

    try:
        await api_instance.ssh_issue_certificate(role, ssh_mount_path, ssh_issue_certificate_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_issue_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role with configuration for this request. | 
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_issue_certificate_request** | [**SshIssueCertificateRequest**](SshIssueCertificateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_list_roles**
> StandardListResponse ssh_list_roles(ssh_mount_path, list)

Manage the 'roles' that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage the 'roles' that can be created with this backend.
        api_response = await api_instance.ssh_list_roles(ssh_mount_path, list)
        print("The response of SecretsApi->ssh_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_list_roles_by_ip**
> ssh_list_roles_by_ip(ssh_mount_path, ssh_list_roles_by_ip_request)

List all the roles associated with the given IP address.

### Example


```python
import ahvac
from ahvac.models.ssh_list_roles_by_ip_request import SshListRolesByIpRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_list_roles_by_ip_request = ahvac.SshListRolesByIpRequest() # SshListRolesByIpRequest | 

    try:
        # List all the roles associated with the given IP address.
        await api_instance.ssh_list_roles_by_ip(ssh_mount_path, ssh_list_roles_by_ip_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_list_roles_by_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_list_roles_by_ip_request** | [**SshListRolesByIpRequest**](SshListRolesByIpRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_read_ca_configuration**
> ssh_read_ca_configuration(ssh_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        await api_instance.ssh_read_ca_configuration(ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_read_ca_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_read_public_key**
> ssh_read_public_key(ssh_mount_path)

Retrieve the public key.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        # Retrieve the public key.
        await api_instance.ssh_read_public_key(ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_read_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_read_role**
> ssh_read_role(role, ssh_mount_path)

Manage the 'roles' that can be created with this backend.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | [Required for all types] Name of the role being created.
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        # Manage the 'roles' that can be created with this backend.
        await api_instance.ssh_read_role(role, ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| [Required for all types] Name of the role being created. | 
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_read_zero_address_configuration**
> ssh_read_zero_address_configuration(ssh_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        await api_instance.ssh_read_zero_address_configuration(ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_read_zero_address_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_sign_certificate**
> ssh_sign_certificate(role, ssh_mount_path, ssh_sign_certificate_request)

Request signing an SSH key using a certain role with the provided details.

### Example


```python
import ahvac
from ahvac.models.ssh_sign_certificate_request import SshSignCertificateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | The desired role with configuration for this request.
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_sign_certificate_request = ahvac.SshSignCertificateRequest() # SshSignCertificateRequest | 

    try:
        # Request signing an SSH key using a certain role with the provided details.
        await api_instance.ssh_sign_certificate(role, ssh_mount_path, ssh_sign_certificate_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_sign_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The desired role with configuration for this request. | 
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_sign_certificate_request** | [**SshSignCertificateRequest**](SshSignCertificateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_tidy_dynamic_host_keys**
> ssh_tidy_dynamic_host_keys(ssh_mount_path)

This endpoint removes the stored host keys used for the removed Dynamic Key feature, if present.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')

    try:
        # This endpoint removes the stored host keys used for the removed Dynamic Key feature, if present.
        await api_instance.ssh_tidy_dynamic_host_keys(ssh_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_tidy_dynamic_host_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_verify_otp**
> ssh_verify_otp(ssh_mount_path, ssh_verify_otp_request)

Validate the OTP provided by Vault SSH Agent.

### Example


```python
import ahvac
from ahvac.models.ssh_verify_otp_request import SshVerifyOtpRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_verify_otp_request = ahvac.SshVerifyOtpRequest() # SshVerifyOtpRequest | 

    try:
        # Validate the OTP provided by Vault SSH Agent.
        await api_instance.ssh_verify_otp(ssh_mount_path, ssh_verify_otp_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_verify_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_verify_otp_request** | [**SshVerifyOtpRequest**](SshVerifyOtpRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_write_role**
> ssh_write_role(role, ssh_mount_path, ssh_write_role_request)

Manage the 'roles' that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.ssh_write_role_request import SshWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    role = 'role_example' # str | [Required for all types] Name of the role being created.
    ssh_mount_path = 'ssh' # str | Path that the backend was mounted at (default to 'ssh')
    ssh_write_role_request = ahvac.SshWriteRoleRequest() # SshWriteRoleRequest | 

    try:
        # Manage the 'roles' that can be created with this backend.
        await api_instance.ssh_write_role(role, ssh_mount_path, ssh_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->ssh_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| [Required for all types] Name of the role being created. | 
 **ssh_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ssh&#39;]
 **ssh_write_role_request** | [**SshWriteRoleRequest**](SshWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_configure**
> terraform_cloud_configure(terraform_mount_path, terraform_cloud_configure_request)



### Example


```python
import ahvac
from ahvac.models.terraform_cloud_configure_request import TerraformCloudConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')
    terraform_cloud_configure_request = ahvac.TerraformCloudConfigureRequest() # TerraformCloudConfigureRequest | 

    try:
        await api_instance.terraform_cloud_configure(terraform_mount_path, terraform_cloud_configure_request)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]
 **terraform_cloud_configure_request** | [**TerraformCloudConfigureRequest**](TerraformCloudConfigureRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_delete_configuration**
> terraform_cloud_delete_configuration(terraform_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')

    try:
        await api_instance.terraform_cloud_delete_configuration(terraform_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_delete_role**
> terraform_cloud_delete_role(name, terraform_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')

    try:
        await api_instance.terraform_cloud_delete_role(name, terraform_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_generate_credentials**
> terraform_cloud_generate_credentials(name, terraform_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')

    try:
        await api_instance.terraform_cloud_generate_credentials(name, terraform_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_generate_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_generate_credentials2**
> terraform_cloud_generate_credentials2(name, terraform_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')

    try:
        await api_instance.terraform_cloud_generate_credentials2(name, terraform_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_generate_credentials2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_list_roles**
> StandardListResponse terraform_cloud_list_roles(terraform_mount_path, list)



### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.terraform_cloud_list_roles(terraform_mount_path, list)
        print("The response of SecretsApi->terraform_cloud_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_read_configuration**
> terraform_cloud_read_configuration(terraform_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')

    try:
        await api_instance.terraform_cloud_read_configuration(terraform_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_read_role**
> terraform_cloud_read_role(name, terraform_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')

    try:
        await api_instance.terraform_cloud_read_role(name, terraform_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_rotate_role**
> terraform_cloud_rotate_role(name, terraform_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the team or organization role
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')

    try:
        await api_instance.terraform_cloud_rotate_role(name, terraform_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_rotate_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the team or organization role | 
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terraform_cloud_write_role**
> terraform_cloud_write_role(name, terraform_mount_path, terraform_cloud_write_role_request)



### Example


```python
import ahvac
from ahvac.models.terraform_cloud_write_role_request import TerraformCloudWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the role
    terraform_mount_path = 'terraform' # str | Path that the backend was mounted at (default to 'terraform')
    terraform_cloud_write_role_request = ahvac.TerraformCloudWriteRoleRequest() # TerraformCloudWriteRoleRequest | 

    try:
        await api_instance.terraform_cloud_write_role(name, terraform_mount_path, terraform_cloud_write_role_request)
    except Exception as e:
        print("Exception when calling SecretsApi->terraform_cloud_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **terraform_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;terraform&#39;]
 **terraform_cloud_write_role_request** | [**TerraformCloudWriteRoleRequest**](TerraformCloudWriteRoleRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totp_create_key**
> totp_create_key(name, totp_mount_path, totp_create_key_request)



### Example


```python
import ahvac
from ahvac.models.totp_create_key_request import TotpCreateKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key.
    totp_mount_path = 'totp' # str | Path that the backend was mounted at (default to 'totp')
    totp_create_key_request = ahvac.TotpCreateKeyRequest() # TotpCreateKeyRequest | 

    try:
        await api_instance.totp_create_key(name, totp_mount_path, totp_create_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->totp_create_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key. | 
 **totp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;totp&#39;]
 **totp_create_key_request** | [**TotpCreateKeyRequest**](TotpCreateKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totp_delete_key**
> totp_delete_key(name, totp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key.
    totp_mount_path = 'totp' # str | Path that the backend was mounted at (default to 'totp')

    try:
        await api_instance.totp_delete_key(name, totp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->totp_delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key. | 
 **totp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;totp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totp_generate_code**
> totp_generate_code(name, totp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key.
    totp_mount_path = 'totp' # str | Path that the backend was mounted at (default to 'totp')

    try:
        await api_instance.totp_generate_code(name, totp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->totp_generate_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key. | 
 **totp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;totp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totp_list_keys**
> StandardListResponse totp_list_keys(totp_mount_path, list)

Manage the keys that can be created with this backend.

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    totp_mount_path = 'totp' # str | Path that the backend was mounted at (default to 'totp')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage the keys that can be created with this backend.
        api_response = await api_instance.totp_list_keys(totp_mount_path, list)
        print("The response of SecretsApi->totp_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->totp_list_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **totp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;totp&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totp_read_key**
> totp_read_key(name, totp_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key.
    totp_mount_path = 'totp' # str | Path that the backend was mounted at (default to 'totp')

    try:
        await api_instance.totp_read_key(name, totp_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->totp_read_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key. | 
 **totp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;totp&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totp_validate_code**
> totp_validate_code(name, totp_mount_path, totp_validate_code_request)



### Example


```python
import ahvac
from ahvac.models.totp_validate_code_request import TotpValidateCodeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key.
    totp_mount_path = 'totp' # str | Path that the backend was mounted at (default to 'totp')
    totp_validate_code_request = ahvac.TotpValidateCodeRequest() # TotpValidateCodeRequest | 

    try:
        await api_instance.totp_validate_code(name, totp_mount_path, totp_validate_code_request)
    except Exception as e:
        print("Exception when calling SecretsApi->totp_validate_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key. | 
 **totp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;totp&#39;]
 **totp_validate_code_request** | [**TotpValidateCodeRequest**](TotpValidateCodeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_back_up_key**
> transit_back_up_key(name, transit_mount_path)

Backup the named key

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        # Backup the named key
        await api_instance.transit_back_up_key(name, transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_back_up_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_byok_key**
> transit_byok_key(destination, source, transit_mount_path)

Securely export named encryption or signing key

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    destination = 'destination_example' # str | Destination key to export to; usually the public wrapping key of another Transit instance.
    source = 'source_example' # str | Source key to export; could be any present key within Transit.
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        # Securely export named encryption or signing key
        await api_instance.transit_byok_key(destination, source, transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_byok_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **str**| Destination key to export to; usually the public wrapping key of another Transit instance. | 
 **source** | **str**| Source key to export; could be any present key within Transit. | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_byok_key_version**
> transit_byok_key_version(destination, source, version, transit_mount_path)

Securely export named encryption or signing key

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    destination = 'destination_example' # str | Destination key to export to; usually the public wrapping key of another Transit instance.
    source = 'source_example' # str | Source key to export; could be any present key within Transit.
    version = 'version_example' # str | Optional version of the key to export, else all key versions are exported.
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        # Securely export named encryption or signing key
        await api_instance.transit_byok_key_version(destination, source, version, transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_byok_key_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **str**| Destination key to export to; usually the public wrapping key of another Transit instance. | 
 **source** | **str**| Source key to export; could be any present key within Transit. | 
 **version** | **str**| Optional version of the key to export, else all key versions are exported. | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_configure_cache**
> transit_configure_cache(transit_mount_path, transit_configure_cache_request)

Configures a new cache of the specified size

### Example


```python
import ahvac
from ahvac.models.transit_configure_cache_request import TransitConfigureCacheRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_configure_cache_request = ahvac.TransitConfigureCacheRequest() # TransitConfigureCacheRequest | 

    try:
        # Configures a new cache of the specified size
        await api_instance.transit_configure_cache(transit_mount_path, transit_configure_cache_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_configure_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_configure_cache_request** | [**TransitConfigureCacheRequest**](TransitConfigureCacheRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_configure_key**
> transit_configure_key(name, transit_mount_path, transit_configure_key_request)

Configure a named encryption key

### Example


```python
import ahvac
from ahvac.models.transit_configure_key_request import TransitConfigureKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_configure_key_request = ahvac.TransitConfigureKeyRequest() # TransitConfigureKeyRequest | 

    try:
        # Configure a named encryption key
        await api_instance.transit_configure_key(name, transit_mount_path, transit_configure_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_configure_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_configure_key_request** | [**TransitConfigureKeyRequest**](TransitConfigureKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_configure_keys**
> transit_configure_keys(transit_mount_path, transit_configure_keys_request)



### Example


```python
import ahvac
from ahvac.models.transit_configure_keys_request import TransitConfigureKeysRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_configure_keys_request = ahvac.TransitConfigureKeysRequest() # TransitConfigureKeysRequest | 

    try:
        await api_instance.transit_configure_keys(transit_mount_path, transit_configure_keys_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_configure_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_configure_keys_request** | [**TransitConfigureKeysRequest**](TransitConfigureKeysRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_create_key**
> transit_create_key(name, transit_mount_path, transit_create_key_request)



### Example


```python
import ahvac
from ahvac.models.transit_create_key_request import TransitCreateKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_create_key_request = ahvac.TransitCreateKeyRequest() # TransitCreateKeyRequest | 

    try:
        await api_instance.transit_create_key(name, transit_mount_path, transit_create_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_create_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_create_key_request** | [**TransitCreateKeyRequest**](TransitCreateKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_decrypt**
> transit_decrypt(name, transit_mount_path, transit_decrypt_request)

Decrypt a ciphertext value using a named key

### Example


```python
import ahvac
from ahvac.models.transit_decrypt_request import TransitDecryptRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_decrypt_request = ahvac.TransitDecryptRequest() # TransitDecryptRequest | 

    try:
        # Decrypt a ciphertext value using a named key
        await api_instance.transit_decrypt(name, transit_mount_path, transit_decrypt_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_decrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_decrypt_request** | [**TransitDecryptRequest**](TransitDecryptRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_delete_key**
> transit_delete_key(name, transit_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        await api_instance.transit_delete_key(name, transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_encrypt**
> transit_encrypt(name, transit_mount_path, transit_encrypt_request)

Encrypt a plaintext value or a batch of plaintext blocks using a named key

### Example


```python
import ahvac
from ahvac.models.transit_encrypt_request import TransitEncryptRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_encrypt_request = ahvac.TransitEncryptRequest() # TransitEncryptRequest | 

    try:
        # Encrypt a plaintext value or a batch of plaintext blocks using a named key
        await api_instance.transit_encrypt(name, transit_mount_path, transit_encrypt_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_encrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_encrypt_request** | [**TransitEncryptRequest**](TransitEncryptRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_export_key**
> transit_export_key(name, type, transit_mount_path)

Export named encryption or signing key

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    type = 'type_example' # str | Type of key to export (encryption-key, signing-key, hmac-key, public-key)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        # Export named encryption or signing key
        await api_instance.transit_export_key(name, type, transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_export_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **type** | **str**| Type of key to export (encryption-key, signing-key, hmac-key, public-key) | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_export_key_version**
> transit_export_key_version(name, type, version, transit_mount_path)

Export named encryption or signing key

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    type = 'type_example' # str | Type of key to export (encryption-key, signing-key, hmac-key, public-key)
    version = 'version_example' # str | Version of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        # Export named encryption or signing key
        await api_instance.transit_export_key_version(name, type, version, transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_export_key_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **type** | **str**| Type of key to export (encryption-key, signing-key, hmac-key, public-key) | 
 **version** | **str**| Version of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_csr_for_key**
> transit_generate_csr_for_key(name, transit_mount_path, transit_generate_csr_for_key_request)



### Example


```python
import ahvac
from ahvac.models.transit_generate_csr_for_key_request import TransitGenerateCsrForKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_csr_for_key_request = ahvac.TransitGenerateCsrForKeyRequest() # TransitGenerateCsrForKeyRequest | 

    try:
        await api_instance.transit_generate_csr_for_key(name, transit_mount_path, transit_generate_csr_for_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_csr_for_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_csr_for_key_request** | [**TransitGenerateCsrForKeyRequest**](TransitGenerateCsrForKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_data_key**
> transit_generate_data_key(name, plaintext, transit_mount_path, transit_generate_data_key_request)

Generate a data key

### Example


```python
import ahvac
from ahvac.models.transit_generate_data_key_request import TransitGenerateDataKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The backend key used for encrypting the data key
    plaintext = 'plaintext_example' # str | \"plaintext\" will return the key in both plaintext and ciphertext; \"wrapped\" will return the ciphertext only.
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_data_key_request = ahvac.TransitGenerateDataKeyRequest() # TransitGenerateDataKeyRequest | 

    try:
        # Generate a data key
        await api_instance.transit_generate_data_key(name, plaintext, transit_mount_path, transit_generate_data_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_data_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The backend key used for encrypting the data key | 
 **plaintext** | **str**| \&quot;plaintext\&quot; will return the key in both plaintext and ciphertext; \&quot;wrapped\&quot; will return the ciphertext only. | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_data_key_request** | [**TransitGenerateDataKeyRequest**](TransitGenerateDataKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_hmac**
> transit_generate_hmac(name, transit_mount_path, transit_generate_hmac_request)

Generate an HMAC for input data using the named key

### Example


```python
import ahvac
from ahvac.models.transit_generate_hmac_request import TransitGenerateHmacRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The key to use for the HMAC function
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_hmac_request = ahvac.TransitGenerateHmacRequest() # TransitGenerateHmacRequest | 

    try:
        # Generate an HMAC for input data using the named key
        await api_instance.transit_generate_hmac(name, transit_mount_path, transit_generate_hmac_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_hmac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The key to use for the HMAC function | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_hmac_request** | [**TransitGenerateHmacRequest**](TransitGenerateHmacRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_hmac_with_algorithm**
> transit_generate_hmac_with_algorithm(name, urlalgorithm, transit_mount_path, transit_generate_hmac_with_algorithm_request)

Generate an HMAC for input data using the named key

### Example


```python
import ahvac
from ahvac.models.transit_generate_hmac_with_algorithm_request import TransitGenerateHmacWithAlgorithmRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The key to use for the HMAC function
    urlalgorithm = 'urlalgorithm_example' # str | Algorithm to use (POST URL parameter)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_hmac_with_algorithm_request = ahvac.TransitGenerateHmacWithAlgorithmRequest() # TransitGenerateHmacWithAlgorithmRequest | 

    try:
        # Generate an HMAC for input data using the named key
        await api_instance.transit_generate_hmac_with_algorithm(name, urlalgorithm, transit_mount_path, transit_generate_hmac_with_algorithm_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_hmac_with_algorithm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The key to use for the HMAC function | 
 **urlalgorithm** | **str**| Algorithm to use (POST URL parameter) | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_hmac_with_algorithm_request** | [**TransitGenerateHmacWithAlgorithmRequest**](TransitGenerateHmacWithAlgorithmRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_random**
> transit_generate_random(transit_mount_path, transit_generate_random_request)

Generate random bytes

### Example


```python
import ahvac
from ahvac.models.transit_generate_random_request import TransitGenerateRandomRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_random_request = ahvac.TransitGenerateRandomRequest() # TransitGenerateRandomRequest | 

    try:
        # Generate random bytes
        await api_instance.transit_generate_random(transit_mount_path, transit_generate_random_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_random: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_random_request** | [**TransitGenerateRandomRequest**](TransitGenerateRandomRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_random_with_bytes**
> transit_generate_random_with_bytes(urlbytes, transit_mount_path, transit_generate_random_with_bytes_request)

Generate random bytes

### Example


```python
import ahvac
from ahvac.models.transit_generate_random_with_bytes_request import TransitGenerateRandomWithBytesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    urlbytes = 'urlbytes_example' # str | The number of bytes to generate (POST URL parameter)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_random_with_bytes_request = ahvac.TransitGenerateRandomWithBytesRequest() # TransitGenerateRandomWithBytesRequest | 

    try:
        # Generate random bytes
        await api_instance.transit_generate_random_with_bytes(urlbytes, transit_mount_path, transit_generate_random_with_bytes_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_random_with_bytes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urlbytes** | **str**| The number of bytes to generate (POST URL parameter) | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_random_with_bytes_request** | [**TransitGenerateRandomWithBytesRequest**](TransitGenerateRandomWithBytesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_random_with_source**
> transit_generate_random_with_source(source, transit_mount_path, transit_generate_random_with_source_request)

Generate random bytes

### Example


```python
import ahvac
from ahvac.models.transit_generate_random_with_source_request import TransitGenerateRandomWithSourceRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    source = 'platform' # str | Which system to source random data from, ether \"platform\", \"seal\", or \"all\". (default to 'platform')
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_random_with_source_request = ahvac.TransitGenerateRandomWithSourceRequest() # TransitGenerateRandomWithSourceRequest | 

    try:
        # Generate random bytes
        await api_instance.transit_generate_random_with_source(source, transit_mount_path, transit_generate_random_with_source_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_random_with_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Which system to source random data from, ether \&quot;platform\&quot;, \&quot;seal\&quot;, or \&quot;all\&quot;. | [default to &#39;platform&#39;]
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_random_with_source_request** | [**TransitGenerateRandomWithSourceRequest**](TransitGenerateRandomWithSourceRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_generate_random_with_source_and_bytes**
> transit_generate_random_with_source_and_bytes(source, urlbytes, transit_mount_path, transit_generate_random_with_source_and_bytes_request)

Generate random bytes

### Example


```python
import ahvac
from ahvac.models.transit_generate_random_with_source_and_bytes_request import TransitGenerateRandomWithSourceAndBytesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    source = 'platform' # str | Which system to source random data from, ether \"platform\", \"seal\", or \"all\". (default to 'platform')
    urlbytes = 'urlbytes_example' # str | The number of bytes to generate (POST URL parameter)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_generate_random_with_source_and_bytes_request = ahvac.TransitGenerateRandomWithSourceAndBytesRequest() # TransitGenerateRandomWithSourceAndBytesRequest | 

    try:
        # Generate random bytes
        await api_instance.transit_generate_random_with_source_and_bytes(source, urlbytes, transit_mount_path, transit_generate_random_with_source_and_bytes_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_generate_random_with_source_and_bytes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Which system to source random data from, ether \&quot;platform\&quot;, \&quot;seal\&quot;, or \&quot;all\&quot;. | [default to &#39;platform&#39;]
 **urlbytes** | **str**| The number of bytes to generate (POST URL parameter) | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_generate_random_with_source_and_bytes_request** | [**TransitGenerateRandomWithSourceAndBytesRequest**](TransitGenerateRandomWithSourceAndBytesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_hash**
> transit_hash(transit_mount_path, transit_hash_request)

Generate a hash sum for input data

### Example


```python
import ahvac
from ahvac.models.transit_hash_request import TransitHashRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_hash_request = ahvac.TransitHashRequest() # TransitHashRequest | 

    try:
        # Generate a hash sum for input data
        await api_instance.transit_hash(transit_mount_path, transit_hash_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_hash_request** | [**TransitHashRequest**](TransitHashRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_hash_with_algorithm**
> transit_hash_with_algorithm(urlalgorithm, transit_mount_path, transit_hash_with_algorithm_request)

Generate a hash sum for input data

### Example


```python
import ahvac
from ahvac.models.transit_hash_with_algorithm_request import TransitHashWithAlgorithmRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    urlalgorithm = 'urlalgorithm_example' # str | Algorithm to use (POST URL parameter)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_hash_with_algorithm_request = ahvac.TransitHashWithAlgorithmRequest() # TransitHashWithAlgorithmRequest | 

    try:
        # Generate a hash sum for input data
        await api_instance.transit_hash_with_algorithm(urlalgorithm, transit_mount_path, transit_hash_with_algorithm_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_hash_with_algorithm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urlalgorithm** | **str**| Algorithm to use (POST URL parameter) | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_hash_with_algorithm_request** | [**TransitHashWithAlgorithmRequest**](TransitHashWithAlgorithmRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_import_key**
> transit_import_key(name, transit_mount_path, transit_import_key_request)

Imports an externally-generated key into a new transit key

### Example


```python
import ahvac
from ahvac.models.transit_import_key_request import TransitImportKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_import_key_request = ahvac.TransitImportKeyRequest() # TransitImportKeyRequest | 

    try:
        # Imports an externally-generated key into a new transit key
        await api_instance.transit_import_key(name, transit_mount_path, transit_import_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_import_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_import_key_request** | [**TransitImportKeyRequest**](TransitImportKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_import_key_version**
> transit_import_key_version(name, transit_mount_path, transit_import_key_version_request)

Imports an externally-generated key into an existing imported key

### Example


```python
import ahvac
from ahvac.models.transit_import_key_version_request import TransitImportKeyVersionRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_import_key_version_request = ahvac.TransitImportKeyVersionRequest() # TransitImportKeyVersionRequest | 

    try:
        # Imports an externally-generated key into an existing imported key
        await api_instance.transit_import_key_version(name, transit_mount_path, transit_import_key_version_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_import_key_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_import_key_version_request** | [**TransitImportKeyVersionRequest**](TransitImportKeyVersionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_list_keys**
> StandardListResponse transit_list_keys(transit_mount_path, list)

Managed named encryption keys

### Example


```python
import ahvac
from ahvac.models.standard_list_response import StandardListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Managed named encryption keys
        api_response = await api_instance.transit_list_keys(transit_mount_path, list)
        print("The response of SecretsApi->transit_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_list_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**StandardListResponse**](StandardListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_read_cache_configuration**
> transit_read_cache_configuration(transit_mount_path)

Returns the size of the active cache

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        # Returns the size of the active cache
        await api_instance.transit_read_cache_configuration(transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_read_cache_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_read_key**
> transit_read_key(name, transit_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        await api_instance.transit_read_key(name, transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_read_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_read_keys_configuration**
> transit_read_keys_configuration(transit_mount_path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        await api_instance.transit_read_keys_configuration(transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_read_keys_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_read_wrapping_key**
> transit_read_wrapping_key(transit_mount_path)

Returns the public key to use for wrapping imported keys

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')

    try:
        # Returns the public key to use for wrapping imported keys
        await api_instance.transit_read_wrapping_key(transit_mount_path)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_read_wrapping_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_restore_and_rename_key**
> transit_restore_and_rename_key(name, transit_mount_path, transit_restore_and_rename_key_request)

Restore the named key

### Example


```python
import ahvac
from ahvac.models.transit_restore_and_rename_key_request import TransitRestoreAndRenameKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | If set, this will be the name of the restored key.
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_restore_and_rename_key_request = ahvac.TransitRestoreAndRenameKeyRequest() # TransitRestoreAndRenameKeyRequest | 

    try:
        # Restore the named key
        await api_instance.transit_restore_and_rename_key(name, transit_mount_path, transit_restore_and_rename_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_restore_and_rename_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| If set, this will be the name of the restored key. | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_restore_and_rename_key_request** | [**TransitRestoreAndRenameKeyRequest**](TransitRestoreAndRenameKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_restore_key**
> transit_restore_key(transit_mount_path, transit_restore_key_request)

Restore the named key

### Example


```python
import ahvac
from ahvac.models.transit_restore_key_request import TransitRestoreKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_restore_key_request = ahvac.TransitRestoreKeyRequest() # TransitRestoreKeyRequest | 

    try:
        # Restore the named key
        await api_instance.transit_restore_key(transit_mount_path, transit_restore_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_restore_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_restore_key_request** | [**TransitRestoreKeyRequest**](TransitRestoreKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_rewrap**
> transit_rewrap(name, transit_mount_path, transit_rewrap_request)

Rewrap ciphertext

### Example


```python
import ahvac
from ahvac.models.transit_rewrap_request import TransitRewrapRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_rewrap_request = ahvac.TransitRewrapRequest() # TransitRewrapRequest | 

    try:
        # Rewrap ciphertext
        await api_instance.transit_rewrap(name, transit_mount_path, transit_rewrap_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_rewrap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_rewrap_request** | [**TransitRewrapRequest**](TransitRewrapRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_rotate_key**
> transit_rotate_key(name, transit_mount_path, transit_rotate_key_request)

Rotate named encryption key

### Example


```python
import ahvac
from ahvac.models.transit_rotate_key_request import TransitRotateKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_rotate_key_request = ahvac.TransitRotateKeyRequest() # TransitRotateKeyRequest | 

    try:
        # Rotate named encryption key
        await api_instance.transit_rotate_key(name, transit_mount_path, transit_rotate_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_rotate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_rotate_key_request** | [**TransitRotateKeyRequest**](TransitRotateKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_set_certificate_for_key**
> transit_set_certificate_for_key(name, transit_mount_path, transit_set_certificate_for_key_request)



### Example


```python
import ahvac
from ahvac.models.transit_set_certificate_for_key_request import TransitSetCertificateForKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_set_certificate_for_key_request = ahvac.TransitSetCertificateForKeyRequest() # TransitSetCertificateForKeyRequest | 

    try:
        await api_instance.transit_set_certificate_for_key(name, transit_mount_path, transit_set_certificate_for_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_set_certificate_for_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_set_certificate_for_key_request** | [**TransitSetCertificateForKeyRequest**](TransitSetCertificateForKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_sign**
> transit_sign(name, transit_mount_path, transit_sign_request)

Generate a signature for input data using the named key

### Example


```python
import ahvac
from ahvac.models.transit_sign_request import TransitSignRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The key to use
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_sign_request = ahvac.TransitSignRequest() # TransitSignRequest | 

    try:
        # Generate a signature for input data using the named key
        await api_instance.transit_sign(name, transit_mount_path, transit_sign_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_sign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The key to use | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_sign_request** | [**TransitSignRequest**](TransitSignRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_sign_with_algorithm**
> transit_sign_with_algorithm(name, urlalgorithm, transit_mount_path, transit_sign_with_algorithm_request)

Generate a signature for input data using the named key

### Example


```python
import ahvac
from ahvac.models.transit_sign_with_algorithm_request import TransitSignWithAlgorithmRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The key to use
    urlalgorithm = 'urlalgorithm_example' # str | Hash algorithm to use (POST URL parameter)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_sign_with_algorithm_request = ahvac.TransitSignWithAlgorithmRequest() # TransitSignWithAlgorithmRequest | 

    try:
        # Generate a signature for input data using the named key
        await api_instance.transit_sign_with_algorithm(name, urlalgorithm, transit_mount_path, transit_sign_with_algorithm_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_sign_with_algorithm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The key to use | 
 **urlalgorithm** | **str**| Hash algorithm to use (POST URL parameter) | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_sign_with_algorithm_request** | [**TransitSignWithAlgorithmRequest**](TransitSignWithAlgorithmRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_trim_key**
> transit_trim_key(name, transit_mount_path, transit_trim_key_request)

Trim key versions of a named key

### Example


```python
import ahvac
from ahvac.models.transit_trim_key_request import TransitTrimKeyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | Name of the key
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_trim_key_request = ahvac.TransitTrimKeyRequest() # TransitTrimKeyRequest | 

    try:
        # Trim key versions of a named key
        await api_instance.transit_trim_key(name, transit_mount_path, transit_trim_key_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_trim_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_trim_key_request** | [**TransitTrimKeyRequest**](TransitTrimKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_verify**
> transit_verify(name, transit_mount_path, transit_verify_request)

Verify a signature or HMAC for input data created using the named key

### Example


```python
import ahvac
from ahvac.models.transit_verify_request import TransitVerifyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The key to use
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_verify_request = ahvac.TransitVerifyRequest() # TransitVerifyRequest | 

    try:
        # Verify a signature or HMAC for input data created using the named key
        await api_instance.transit_verify(name, transit_mount_path, transit_verify_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The key to use | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_verify_request** | [**TransitVerifyRequest**](TransitVerifyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transit_verify_with_algorithm**
> transit_verify_with_algorithm(name, urlalgorithm, transit_mount_path, transit_verify_with_algorithm_request)

Verify a signature or HMAC for input data created using the named key

### Example


```python
import ahvac
from ahvac.models.transit_verify_with_algorithm_request import TransitVerifyWithAlgorithmRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SecretsApi(api_client)
    name = 'name_example' # str | The key to use
    urlalgorithm = 'urlalgorithm_example' # str | Hash algorithm to use (POST URL parameter)
    transit_mount_path = 'transit' # str | Path that the backend was mounted at (default to 'transit')
    transit_verify_with_algorithm_request = ahvac.TransitVerifyWithAlgorithmRequest() # TransitVerifyWithAlgorithmRequest | 

    try:
        # Verify a signature or HMAC for input data created using the named key
        await api_instance.transit_verify_with_algorithm(name, urlalgorithm, transit_mount_path, transit_verify_with_algorithm_request)
    except Exception as e:
        print("Exception when calling SecretsApi->transit_verify_with_algorithm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The key to use | 
 **urlalgorithm** | **str**| Hash algorithm to use (POST URL parameter) | 
 **transit_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;transit&#39;]
 **transit_verify_with_algorithm_request** | [**TransitVerifyWithAlgorithmRequest**](TransitVerifyWithAlgorithmRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

