# ahvac.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ali_cloud_delete_auth_role**](AuthApi.md#ali_cloud_delete_auth_role) | **DELETE** /auth/{alicloud_mount_path}/role/{role} | Create a role and associate policies to it.
[**ali_cloud_list_auth_roles**](AuthApi.md#ali_cloud_list_auth_roles) | **GET** /auth/{alicloud_mount_path}/role/ | Lists all the roles that are registered with Vault.
[**ali_cloud_list_auth_roles2**](AuthApi.md#ali_cloud_list_auth_roles2) | **GET** /auth/{alicloud_mount_path}/roles/ | Lists all the roles that are registered with Vault.
[**ali_cloud_login**](AuthApi.md#ali_cloud_login) | **POST** /auth/{alicloud_mount_path}/login | Authenticates an RAM entity with Vault.
[**ali_cloud_read_auth_role**](AuthApi.md#ali_cloud_read_auth_role) | **GET** /auth/{alicloud_mount_path}/role/{role} | Create a role and associate policies to it.
[**ali_cloud_write_auth_role**](AuthApi.md#ali_cloud_write_auth_role) | **POST** /auth/{alicloud_mount_path}/role/{role} | Create a role and associate policies to it.
[**app_role_delete_bind_secret_id**](AuthApi.md#app_role_delete_bind_secret_id) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/bind-secret-id | 
[**app_role_delete_bound_cidr_list**](AuthApi.md#app_role_delete_bound_cidr_list) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/bound-cidr-list | 
[**app_role_delete_period**](AuthApi.md#app_role_delete_period) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/period | 
[**app_role_delete_policies**](AuthApi.md#app_role_delete_policies) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/policies | 
[**app_role_delete_role**](AuthApi.md#app_role_delete_role) | **DELETE** /auth/{approle_mount_path}/role/{role_name} | 
[**app_role_delete_secret_id_bound_cidrs**](AuthApi.md#app_role_delete_secret_id_bound_cidrs) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/secret-id-bound-cidrs | 
[**app_role_delete_secret_id_num_uses**](AuthApi.md#app_role_delete_secret_id_num_uses) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/secret-id-num-uses | 
[**app_role_delete_secret_id_ttl**](AuthApi.md#app_role_delete_secret_id_ttl) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/secret-id-ttl | 
[**app_role_delete_token_bound_cidrs**](AuthApi.md#app_role_delete_token_bound_cidrs) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/token-bound-cidrs | 
[**app_role_delete_token_max_ttl**](AuthApi.md#app_role_delete_token_max_ttl) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/token-max-ttl | 
[**app_role_delete_token_num_uses**](AuthApi.md#app_role_delete_token_num_uses) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/token-num-uses | 
[**app_role_delete_token_ttl**](AuthApi.md#app_role_delete_token_ttl) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/token-ttl | 
[**app_role_destroy_secret_id**](AuthApi.md#app_role_destroy_secret_id) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id/destroy | 
[**app_role_destroy_secret_id2**](AuthApi.md#app_role_destroy_secret_id2) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/secret-id/destroy | 
[**app_role_destroy_secret_id_by_accessor**](AuthApi.md#app_role_destroy_secret_id_by_accessor) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id-accessor/destroy | 
[**app_role_destroy_secret_id_by_accessor2**](AuthApi.md#app_role_destroy_secret_id_by_accessor2) | **DELETE** /auth/{approle_mount_path}/role/{role_name}/secret-id-accessor/destroy | 
[**app_role_list_roles**](AuthApi.md#app_role_list_roles) | **GET** /auth/{approle_mount_path}/role/ | 
[**app_role_list_secret_ids**](AuthApi.md#app_role_list_secret_ids) | **GET** /auth/{approle_mount_path}/role/{role_name}/secret-id/ | 
[**app_role_login**](AuthApi.md#app_role_login) | **POST** /auth/{approle_mount_path}/login | 
[**app_role_look_up_secret_id**](AuthApi.md#app_role_look_up_secret_id) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id/lookup | 
[**app_role_look_up_secret_id_by_accessor**](AuthApi.md#app_role_look_up_secret_id_by_accessor) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id-accessor/lookup | 
[**app_role_read_bind_secret_id**](AuthApi.md#app_role_read_bind_secret_id) | **GET** /auth/{approle_mount_path}/role/{role_name}/bind-secret-id | 
[**app_role_read_bound_cidr_list**](AuthApi.md#app_role_read_bound_cidr_list) | **GET** /auth/{approle_mount_path}/role/{role_name}/bound-cidr-list | 
[**app_role_read_local_secret_ids**](AuthApi.md#app_role_read_local_secret_ids) | **GET** /auth/{approle_mount_path}/role/{role_name}/local-secret-ids | 
[**app_role_read_period**](AuthApi.md#app_role_read_period) | **GET** /auth/{approle_mount_path}/role/{role_name}/period | 
[**app_role_read_policies**](AuthApi.md#app_role_read_policies) | **GET** /auth/{approle_mount_path}/role/{role_name}/policies | 
[**app_role_read_role**](AuthApi.md#app_role_read_role) | **GET** /auth/{approle_mount_path}/role/{role_name} | 
[**app_role_read_role_id**](AuthApi.md#app_role_read_role_id) | **GET** /auth/{approle_mount_path}/role/{role_name}/role-id | 
[**app_role_read_secret_id_bound_cidrs**](AuthApi.md#app_role_read_secret_id_bound_cidrs) | **GET** /auth/{approle_mount_path}/role/{role_name}/secret-id-bound-cidrs | 
[**app_role_read_secret_id_num_uses**](AuthApi.md#app_role_read_secret_id_num_uses) | **GET** /auth/{approle_mount_path}/role/{role_name}/secret-id-num-uses | 
[**app_role_read_secret_id_ttl**](AuthApi.md#app_role_read_secret_id_ttl) | **GET** /auth/{approle_mount_path}/role/{role_name}/secret-id-ttl | 
[**app_role_read_token_bound_cidrs**](AuthApi.md#app_role_read_token_bound_cidrs) | **GET** /auth/{approle_mount_path}/role/{role_name}/token-bound-cidrs | 
[**app_role_read_token_max_ttl**](AuthApi.md#app_role_read_token_max_ttl) | **GET** /auth/{approle_mount_path}/role/{role_name}/token-max-ttl | 
[**app_role_read_token_num_uses**](AuthApi.md#app_role_read_token_num_uses) | **GET** /auth/{approle_mount_path}/role/{role_name}/token-num-uses | 
[**app_role_read_token_ttl**](AuthApi.md#app_role_read_token_ttl) | **GET** /auth/{approle_mount_path}/role/{role_name}/token-ttl | 
[**app_role_tidy_secret_id**](AuthApi.md#app_role_tidy_secret_id) | **POST** /auth/{approle_mount_path}/tidy/secret-id | 
[**app_role_write_bind_secret_id**](AuthApi.md#app_role_write_bind_secret_id) | **POST** /auth/{approle_mount_path}/role/{role_name}/bind-secret-id | 
[**app_role_write_bound_cidr_list**](AuthApi.md#app_role_write_bound_cidr_list) | **POST** /auth/{approle_mount_path}/role/{role_name}/bound-cidr-list | 
[**app_role_write_custom_secret_id**](AuthApi.md#app_role_write_custom_secret_id) | **POST** /auth/{approle_mount_path}/role/{role_name}/custom-secret-id | 
[**app_role_write_period**](AuthApi.md#app_role_write_period) | **POST** /auth/{approle_mount_path}/role/{role_name}/period | 
[**app_role_write_policies**](AuthApi.md#app_role_write_policies) | **POST** /auth/{approle_mount_path}/role/{role_name}/policies | 
[**app_role_write_role**](AuthApi.md#app_role_write_role) | **POST** /auth/{approle_mount_path}/role/{role_name} | 
[**app_role_write_role_id**](AuthApi.md#app_role_write_role_id) | **POST** /auth/{approle_mount_path}/role/{role_name}/role-id | 
[**app_role_write_secret_id**](AuthApi.md#app_role_write_secret_id) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id | 
[**app_role_write_secret_id_bound_cidrs**](AuthApi.md#app_role_write_secret_id_bound_cidrs) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id-bound-cidrs | 
[**app_role_write_secret_id_num_uses**](AuthApi.md#app_role_write_secret_id_num_uses) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id-num-uses | 
[**app_role_write_secret_id_ttl**](AuthApi.md#app_role_write_secret_id_ttl) | **POST** /auth/{approle_mount_path}/role/{role_name}/secret-id-ttl | 
[**app_role_write_token_bound_cidrs**](AuthApi.md#app_role_write_token_bound_cidrs) | **POST** /auth/{approle_mount_path}/role/{role_name}/token-bound-cidrs | 
[**app_role_write_token_max_ttl**](AuthApi.md#app_role_write_token_max_ttl) | **POST** /auth/{approle_mount_path}/role/{role_name}/token-max-ttl | 
[**app_role_write_token_num_uses**](AuthApi.md#app_role_write_token_num_uses) | **POST** /auth/{approle_mount_path}/role/{role_name}/token-num-uses | 
[**app_role_write_token_ttl**](AuthApi.md#app_role_write_token_ttl) | **POST** /auth/{approle_mount_path}/role/{role_name}/token-ttl | 
[**aws_configure_certificate**](AuthApi.md#aws_configure_certificate) | **POST** /auth/{aws_mount_path}/config/certificate/{cert_name} | 
[**aws_configure_client**](AuthApi.md#aws_configure_client) | **POST** /auth/{aws_mount_path}/config/client | 
[**aws_configure_identity_access_list_tidy_operation**](AuthApi.md#aws_configure_identity_access_list_tidy_operation) | **POST** /auth/{aws_mount_path}/config/tidy/identity-accesslist | 
[**aws_configure_identity_integration**](AuthApi.md#aws_configure_identity_integration) | **POST** /auth/{aws_mount_path}/config/identity | 
[**aws_configure_identity_whitelist_tidy_operation**](AuthApi.md#aws_configure_identity_whitelist_tidy_operation) | **POST** /auth/{aws_mount_path}/config/tidy/identity-whitelist | 
[**aws_configure_role_tag_blacklist_tidy_operation**](AuthApi.md#aws_configure_role_tag_blacklist_tidy_operation) | **POST** /auth/{aws_mount_path}/config/tidy/roletag-blacklist | 
[**aws_configure_role_tag_deny_list_tidy_operation**](AuthApi.md#aws_configure_role_tag_deny_list_tidy_operation) | **POST** /auth/{aws_mount_path}/config/tidy/roletag-denylist | 
[**aws_delete_auth_role**](AuthApi.md#aws_delete_auth_role) | **DELETE** /auth/{aws_mount_path}/role/{role} | 
[**aws_delete_certificate_configuration**](AuthApi.md#aws_delete_certificate_configuration) | **DELETE** /auth/{aws_mount_path}/config/certificate/{cert_name} | 
[**aws_delete_client_configuration**](AuthApi.md#aws_delete_client_configuration) | **DELETE** /auth/{aws_mount_path}/config/client | 
[**aws_delete_identity_access_list**](AuthApi.md#aws_delete_identity_access_list) | **DELETE** /auth/{aws_mount_path}/identity-accesslist/{instance_id} | 
[**aws_delete_identity_access_list_tidy_settings**](AuthApi.md#aws_delete_identity_access_list_tidy_settings) | **DELETE** /auth/{aws_mount_path}/config/tidy/identity-accesslist | 
[**aws_delete_identity_whitelist**](AuthApi.md#aws_delete_identity_whitelist) | **DELETE** /auth/{aws_mount_path}/identity-whitelist/{instance_id} | 
[**aws_delete_identity_whitelist_tidy_settings**](AuthApi.md#aws_delete_identity_whitelist_tidy_settings) | **DELETE** /auth/{aws_mount_path}/config/tidy/identity-whitelist | 
[**aws_delete_role_tag_blacklist**](AuthApi.md#aws_delete_role_tag_blacklist) | **DELETE** /auth/{aws_mount_path}/roletag-blacklist/{role_tag} | 
[**aws_delete_role_tag_blacklist_tidy_settings**](AuthApi.md#aws_delete_role_tag_blacklist_tidy_settings) | **DELETE** /auth/{aws_mount_path}/config/tidy/roletag-blacklist | 
[**aws_delete_role_tag_deny_list**](AuthApi.md#aws_delete_role_tag_deny_list) | **DELETE** /auth/{aws_mount_path}/roletag-denylist/{role_tag} | 
[**aws_delete_role_tag_deny_list_tidy_settings**](AuthApi.md#aws_delete_role_tag_deny_list_tidy_settings) | **DELETE** /auth/{aws_mount_path}/config/tidy/roletag-denylist | 
[**aws_delete_sts_role**](AuthApi.md#aws_delete_sts_role) | **DELETE** /auth/{aws_mount_path}/config/sts/{account_id} | 
[**aws_list_auth_roles**](AuthApi.md#aws_list_auth_roles) | **GET** /auth/{aws_mount_path}/role/ | 
[**aws_list_auth_roles2**](AuthApi.md#aws_list_auth_roles2) | **GET** /auth/{aws_mount_path}/roles/ | 
[**aws_list_certificate_configurations**](AuthApi.md#aws_list_certificate_configurations) | **GET** /auth/{aws_mount_path}/config/certificates/ | 
[**aws_list_identity_access_list**](AuthApi.md#aws_list_identity_access_list) | **GET** /auth/{aws_mount_path}/identity-accesslist/ | 
[**aws_list_identity_whitelist**](AuthApi.md#aws_list_identity_whitelist) | **GET** /auth/{aws_mount_path}/identity-whitelist/ | 
[**aws_list_role_tag_blacklists**](AuthApi.md#aws_list_role_tag_blacklists) | **GET** /auth/{aws_mount_path}/roletag-blacklist/ | 
[**aws_list_role_tag_deny_lists**](AuthApi.md#aws_list_role_tag_deny_lists) | **GET** /auth/{aws_mount_path}/roletag-denylist/ | 
[**aws_list_sts_role_relationships**](AuthApi.md#aws_list_sts_role_relationships) | **GET** /auth/{aws_mount_path}/config/sts/ | 
[**aws_login**](AuthApi.md#aws_login) | **POST** /auth/{aws_mount_path}/login | 
[**aws_read_auth_role**](AuthApi.md#aws_read_auth_role) | **GET** /auth/{aws_mount_path}/role/{role} | 
[**aws_read_certificate_configuration**](AuthApi.md#aws_read_certificate_configuration) | **GET** /auth/{aws_mount_path}/config/certificate/{cert_name} | 
[**aws_read_client_configuration**](AuthApi.md#aws_read_client_configuration) | **GET** /auth/{aws_mount_path}/config/client | 
[**aws_read_identity_access_list**](AuthApi.md#aws_read_identity_access_list) | **GET** /auth/{aws_mount_path}/identity-accesslist/{instance_id} | 
[**aws_read_identity_access_list_tidy_settings**](AuthApi.md#aws_read_identity_access_list_tidy_settings) | **GET** /auth/{aws_mount_path}/config/tidy/identity-accesslist | 
[**aws_read_identity_integration_configuration**](AuthApi.md#aws_read_identity_integration_configuration) | **GET** /auth/{aws_mount_path}/config/identity | 
[**aws_read_identity_whitelist**](AuthApi.md#aws_read_identity_whitelist) | **GET** /auth/{aws_mount_path}/identity-whitelist/{instance_id} | 
[**aws_read_identity_whitelist_tidy_settings**](AuthApi.md#aws_read_identity_whitelist_tidy_settings) | **GET** /auth/{aws_mount_path}/config/tidy/identity-whitelist | 
[**aws_read_role_tag_blacklist**](AuthApi.md#aws_read_role_tag_blacklist) | **GET** /auth/{aws_mount_path}/roletag-blacklist/{role_tag} | 
[**aws_read_role_tag_blacklist_tidy_settings**](AuthApi.md#aws_read_role_tag_blacklist_tidy_settings) | **GET** /auth/{aws_mount_path}/config/tidy/roletag-blacklist | 
[**aws_read_role_tag_deny_list**](AuthApi.md#aws_read_role_tag_deny_list) | **GET** /auth/{aws_mount_path}/roletag-denylist/{role_tag} | 
[**aws_read_role_tag_deny_list_tidy_settings**](AuthApi.md#aws_read_role_tag_deny_list_tidy_settings) | **GET** /auth/{aws_mount_path}/config/tidy/roletag-denylist | 
[**aws_read_sts_role**](AuthApi.md#aws_read_sts_role) | **GET** /auth/{aws_mount_path}/config/sts/{account_id} | 
[**aws_rotate_root_credentials**](AuthApi.md#aws_rotate_root_credentials) | **POST** /auth/{aws_mount_path}/config/rotate-root | 
[**aws_tidy_identity_access_list**](AuthApi.md#aws_tidy_identity_access_list) | **POST** /auth/{aws_mount_path}/tidy/identity-accesslist | 
[**aws_tidy_identity_whitelist**](AuthApi.md#aws_tidy_identity_whitelist) | **POST** /auth/{aws_mount_path}/tidy/identity-whitelist | 
[**aws_tidy_role_tag_blacklist**](AuthApi.md#aws_tidy_role_tag_blacklist) | **POST** /auth/{aws_mount_path}/tidy/roletag-blacklist | 
[**aws_tidy_role_tag_deny_list**](AuthApi.md#aws_tidy_role_tag_deny_list) | **POST** /auth/{aws_mount_path}/tidy/roletag-denylist | 
[**aws_write_auth_role**](AuthApi.md#aws_write_auth_role) | **POST** /auth/{aws_mount_path}/role/{role} | 
[**aws_write_role_tag**](AuthApi.md#aws_write_role_tag) | **POST** /auth/{aws_mount_path}/role/{role}/tag | 
[**aws_write_role_tag_blacklist**](AuthApi.md#aws_write_role_tag_blacklist) | **POST** /auth/{aws_mount_path}/roletag-blacklist/{role_tag} | 
[**aws_write_role_tag_deny_list**](AuthApi.md#aws_write_role_tag_deny_list) | **POST** /auth/{aws_mount_path}/roletag-denylist/{role_tag} | 
[**aws_write_sts_role**](AuthApi.md#aws_write_sts_role) | **POST** /auth/{aws_mount_path}/config/sts/{account_id} | 
[**azure_configure_auth**](AuthApi.md#azure_configure_auth) | **POST** /auth/{azure_mount_path}/config | 
[**azure_delete_auth_configuration**](AuthApi.md#azure_delete_auth_configuration) | **DELETE** /auth/{azure_mount_path}/config | 
[**azure_delete_auth_role**](AuthApi.md#azure_delete_auth_role) | **DELETE** /auth/{azure_mount_path}/role/{name} | 
[**azure_list_auth_roles**](AuthApi.md#azure_list_auth_roles) | **GET** /auth/{azure_mount_path}/role/ | 
[**azure_login**](AuthApi.md#azure_login) | **POST** /auth/{azure_mount_path}/login | 
[**azure_read_auth_configuration**](AuthApi.md#azure_read_auth_configuration) | **GET** /auth/{azure_mount_path}/config | 
[**azure_read_auth_role**](AuthApi.md#azure_read_auth_role) | **GET** /auth/{azure_mount_path}/role/{name} | 
[**azure_rotate_root_credentials**](AuthApi.md#azure_rotate_root_credentials) | **POST** /auth/{azure_mount_path}/rotate-root | 
[**azure_write_auth_role**](AuthApi.md#azure_write_auth_role) | **POST** /auth/{azure_mount_path}/role/{name} | 
[**centrify_configure**](AuthApi.md#centrify_configure) | **POST** /auth/{centrify_mount_path}/config | 
[**centrify_login**](AuthApi.md#centrify_login) | **POST** /auth/{centrify_mount_path}/login | Log in with a username and password.
[**centrify_read_configuration**](AuthApi.md#centrify_read_configuration) | **GET** /auth/{centrify_mount_path}/config | 
[**cert_configure**](AuthApi.md#cert_configure) | **POST** /auth/{cert_mount_path}/config | 
[**cert_delete_certificate**](AuthApi.md#cert_delete_certificate) | **DELETE** /auth/{cert_mount_path}/certs/{name} | Manage trusted certificates used for authentication.
[**cert_delete_crl**](AuthApi.md#cert_delete_crl) | **DELETE** /auth/{cert_mount_path}/crls/{name} | Manage Certificate Revocation Lists checked during authentication.
[**cert_list_certificates**](AuthApi.md#cert_list_certificates) | **GET** /auth/{cert_mount_path}/certs/ | Manage trusted certificates used for authentication.
[**cert_list_crls**](AuthApi.md#cert_list_crls) | **GET** /auth/{cert_mount_path}/crls/ | 
[**cert_login**](AuthApi.md#cert_login) | **POST** /auth/{cert_mount_path}/login | 
[**cert_read_certificate**](AuthApi.md#cert_read_certificate) | **GET** /auth/{cert_mount_path}/certs/{name} | Manage trusted certificates used for authentication.
[**cert_read_configuration**](AuthApi.md#cert_read_configuration) | **GET** /auth/{cert_mount_path}/config | 
[**cert_read_crl**](AuthApi.md#cert_read_crl) | **GET** /auth/{cert_mount_path}/crls/{name} | Manage Certificate Revocation Lists checked during authentication.
[**cert_write_certificate**](AuthApi.md#cert_write_certificate) | **POST** /auth/{cert_mount_path}/certs/{name} | Manage trusted certificates used for authentication.
[**cert_write_crl**](AuthApi.md#cert_write_crl) | **POST** /auth/{cert_mount_path}/crls/{name} | Manage Certificate Revocation Lists checked during authentication.
[**cloud_foundry_configure**](AuthApi.md#cloud_foundry_configure) | **POST** /auth/{cf_mount_path}/config | 
[**cloud_foundry_delete_configuration**](AuthApi.md#cloud_foundry_delete_configuration) | **DELETE** /auth/{cf_mount_path}/config | 
[**cloud_foundry_delete_role**](AuthApi.md#cloud_foundry_delete_role) | **DELETE** /auth/{cf_mount_path}/roles/{role} | 
[**cloud_foundry_list_roles**](AuthApi.md#cloud_foundry_list_roles) | **GET** /auth/{cf_mount_path}/roles/ | 
[**cloud_foundry_login**](AuthApi.md#cloud_foundry_login) | **POST** /auth/{cf_mount_path}/login | 
[**cloud_foundry_read_configuration**](AuthApi.md#cloud_foundry_read_configuration) | **GET** /auth/{cf_mount_path}/config | 
[**cloud_foundry_read_role**](AuthApi.md#cloud_foundry_read_role) | **GET** /auth/{cf_mount_path}/roles/{role} | 
[**cloud_foundry_write_role**](AuthApi.md#cloud_foundry_write_role) | **POST** /auth/{cf_mount_path}/roles/{role} | 
[**github_configure**](AuthApi.md#github_configure) | **POST** /auth/{github_mount_path}/config | 
[**github_delete_team_mapping**](AuthApi.md#github_delete_team_mapping) | **DELETE** /auth/{github_mount_path}/map/teams/{key} | Read/write/delete a single teams mapping
[**github_delete_user_mapping**](AuthApi.md#github_delete_user_mapping) | **DELETE** /auth/{github_mount_path}/map/users/{key} | Read/write/delete a single users mapping
[**github_list_teams**](AuthApi.md#github_list_teams) | **GET** /auth/{github_mount_path}/map/teams/ | Read mappings for teams
[**github_list_teams2**](AuthApi.md#github_list_teams2) | **GET** /auth/{github_mount_path}/map/teams | Read mappings for teams
[**github_list_users**](AuthApi.md#github_list_users) | **GET** /auth/{github_mount_path}/map/users/ | Read mappings for users
[**github_list_users2**](AuthApi.md#github_list_users2) | **GET** /auth/{github_mount_path}/map/users | Read mappings for users
[**github_login**](AuthApi.md#github_login) | **POST** /auth/{github_mount_path}/login | 
[**github_read_configuration**](AuthApi.md#github_read_configuration) | **GET** /auth/{github_mount_path}/config | 
[**github_read_team_mapping**](AuthApi.md#github_read_team_mapping) | **GET** /auth/{github_mount_path}/map/teams/{key} | Read/write/delete a single teams mapping
[**github_read_user_mapping**](AuthApi.md#github_read_user_mapping) | **GET** /auth/{github_mount_path}/map/users/{key} | Read/write/delete a single users mapping
[**github_write_team_mapping**](AuthApi.md#github_write_team_mapping) | **POST** /auth/{github_mount_path}/map/teams/{key} | Read/write/delete a single teams mapping
[**github_write_user_mapping**](AuthApi.md#github_write_user_mapping) | **POST** /auth/{github_mount_path}/map/users/{key} | Read/write/delete a single users mapping
[**google_cloud_configure_auth**](AuthApi.md#google_cloud_configure_auth) | **POST** /auth/{gcp_mount_path}/config | 
[**google_cloud_delete_role**](AuthApi.md#google_cloud_delete_role) | **DELETE** /auth/{gcp_mount_path}/role/{name} | Create a GCP role with associated policies and required attributes.
[**google_cloud_edit_labels_for_role**](AuthApi.md#google_cloud_edit_labels_for_role) | **POST** /auth/{gcp_mount_path}/role/{name}/labels | Add or remove labels for an existing &#39;gce&#39; role
[**google_cloud_edit_service_accounts_for_role**](AuthApi.md#google_cloud_edit_service_accounts_for_role) | **POST** /auth/{gcp_mount_path}/role/{name}/service-accounts | Add or remove service accounts for an existing &#x60;iam&#x60; role
[**google_cloud_list_roles**](AuthApi.md#google_cloud_list_roles) | **GET** /auth/{gcp_mount_path}/role/ | Lists all the roles that are registered with Vault.
[**google_cloud_list_roles2**](AuthApi.md#google_cloud_list_roles2) | **GET** /auth/{gcp_mount_path}/roles/ | Lists all the roles that are registered with Vault.
[**google_cloud_login**](AuthApi.md#google_cloud_login) | **POST** /auth/{gcp_mount_path}/login | 
[**google_cloud_read_auth_configuration**](AuthApi.md#google_cloud_read_auth_configuration) | **GET** /auth/{gcp_mount_path}/config | 
[**google_cloud_read_role**](AuthApi.md#google_cloud_read_role) | **GET** /auth/{gcp_mount_path}/role/{name} | Create a GCP role with associated policies and required attributes.
[**google_cloud_write_role**](AuthApi.md#google_cloud_write_role) | **POST** /auth/{gcp_mount_path}/role/{name} | Create a GCP role with associated policies and required attributes.
[**jwt_configure**](AuthApi.md#jwt_configure) | **POST** /auth/{jwt_mount_path}/config | Configure the JWT authentication backend.
[**jwt_delete_role**](AuthApi.md#jwt_delete_role) | **DELETE** /auth/{jwt_mount_path}/role/{name} | Delete an existing role.
[**jwt_list_roles**](AuthApi.md#jwt_list_roles) | **GET** /auth/{jwt_mount_path}/role/ | Lists all the roles registered with the backend.
[**jwt_login**](AuthApi.md#jwt_login) | **POST** /auth/{jwt_mount_path}/login | Authenticates to Vault using a JWT (or OIDC) token.
[**jwt_oidc_callback**](AuthApi.md#jwt_oidc_callback) | **GET** /auth/{jwt_mount_path}/oidc/callback | Callback endpoint to complete an OIDC login.
[**jwt_oidc_callback_form_post**](AuthApi.md#jwt_oidc_callback_form_post) | **POST** /auth/{jwt_mount_path}/oidc/callback | Callback endpoint to handle form_posts.
[**jwt_oidc_request_authorization_url**](AuthApi.md#jwt_oidc_request_authorization_url) | **POST** /auth/{jwt_mount_path}/oidc/auth_url | Request an authorization URL to start an OIDC login flow.
[**jwt_read_configuration**](AuthApi.md#jwt_read_configuration) | **GET** /auth/{jwt_mount_path}/config | Read the current JWT authentication backend configuration.
[**jwt_read_role**](AuthApi.md#jwt_read_role) | **GET** /auth/{jwt_mount_path}/role/{name} | Read an existing role.
[**jwt_write_role**](AuthApi.md#jwt_write_role) | **POST** /auth/{jwt_mount_path}/role/{name} | Register an role with the backend.
[**kerberos_configure**](AuthApi.md#kerberos_configure) | **POST** /auth/{kerberos_mount_path}/config | 
[**kerberos_configure_ldap**](AuthApi.md#kerberos_configure_ldap) | **POST** /auth/{kerberos_mount_path}/config/ldap | 
[**kerberos_delete_group**](AuthApi.md#kerberos_delete_group) | **DELETE** /auth/{kerberos_mount_path}/groups/{name} | 
[**kerberos_list_groups**](AuthApi.md#kerberos_list_groups) | **GET** /auth/{kerberos_mount_path}/groups/ | 
[**kerberos_login**](AuthApi.md#kerberos_login) | **POST** /auth/{kerberos_mount_path}/login | 
[**kerberos_login2**](AuthApi.md#kerberos_login2) | **GET** /auth/{kerberos_mount_path}/login | 
[**kerberos_read_configuration**](AuthApi.md#kerberos_read_configuration) | **GET** /auth/{kerberos_mount_path}/config | 
[**kerberos_read_group**](AuthApi.md#kerberos_read_group) | **GET** /auth/{kerberos_mount_path}/groups/{name} | 
[**kerberos_read_ldap_configuration**](AuthApi.md#kerberos_read_ldap_configuration) | **GET** /auth/{kerberos_mount_path}/config/ldap | 
[**kerberos_write_group**](AuthApi.md#kerberos_write_group) | **POST** /auth/{kerberos_mount_path}/groups/{name} | 
[**kubernetes_configure_auth**](AuthApi.md#kubernetes_configure_auth) | **POST** /auth/{kubernetes_mount_path}/config | 
[**kubernetes_delete_auth_role**](AuthApi.md#kubernetes_delete_auth_role) | **DELETE** /auth/{kubernetes_mount_path}/role/{name} | Register an role with the backend.
[**kubernetes_list_auth_roles**](AuthApi.md#kubernetes_list_auth_roles) | **GET** /auth/{kubernetes_mount_path}/role/ | Lists all the roles registered with the backend.
[**kubernetes_login**](AuthApi.md#kubernetes_login) | **POST** /auth/{kubernetes_mount_path}/login | Authenticates Kubernetes service accounts with Vault.
[**kubernetes_read_auth_configuration**](AuthApi.md#kubernetes_read_auth_configuration) | **GET** /auth/{kubernetes_mount_path}/config | 
[**kubernetes_read_auth_role**](AuthApi.md#kubernetes_read_auth_role) | **GET** /auth/{kubernetes_mount_path}/role/{name} | Register an role with the backend.
[**kubernetes_write_auth_role**](AuthApi.md#kubernetes_write_auth_role) | **POST** /auth/{kubernetes_mount_path}/role/{name} | Register an role with the backend.
[**ldap_configure_auth**](AuthApi.md#ldap_configure_auth) | **POST** /auth/{ldap_mount_path}/config | 
[**ldap_delete_group**](AuthApi.md#ldap_delete_group) | **DELETE** /auth/{ldap_mount_path}/groups/{name} | Manage additional groups for users allowed to authenticate.
[**ldap_delete_user**](AuthApi.md#ldap_delete_user) | **DELETE** /auth/{ldap_mount_path}/users/{name} | Manage users allowed to authenticate.
[**ldap_list_groups**](AuthApi.md#ldap_list_groups) | **GET** /auth/{ldap_mount_path}/groups/ | Manage additional groups for users allowed to authenticate.
[**ldap_list_users**](AuthApi.md#ldap_list_users) | **GET** /auth/{ldap_mount_path}/users/ | Manage users allowed to authenticate.
[**ldap_login**](AuthApi.md#ldap_login) | **POST** /auth/{ldap_mount_path}/login/{username} | Log in with a username and password.
[**ldap_read_auth_configuration**](AuthApi.md#ldap_read_auth_configuration) | **GET** /auth/{ldap_mount_path}/config | 
[**ldap_read_group**](AuthApi.md#ldap_read_group) | **GET** /auth/{ldap_mount_path}/groups/{name} | Manage additional groups for users allowed to authenticate.
[**ldap_read_user**](AuthApi.md#ldap_read_user) | **GET** /auth/{ldap_mount_path}/users/{name} | Manage users allowed to authenticate.
[**ldap_write_group**](AuthApi.md#ldap_write_group) | **POST** /auth/{ldap_mount_path}/groups/{name} | Manage additional groups for users allowed to authenticate.
[**ldap_write_user**](AuthApi.md#ldap_write_user) | **POST** /auth/{ldap_mount_path}/users/{name} | Manage users allowed to authenticate.
[**oci_configure**](AuthApi.md#oci_configure) | **POST** /auth/{oci_mount_path}/config | 
[**oci_delete_configuration**](AuthApi.md#oci_delete_configuration) | **DELETE** /auth/{oci_mount_path}/config | 
[**oci_delete_role**](AuthApi.md#oci_delete_role) | **DELETE** /auth/{oci_mount_path}/role/{role} | Create a role and associate policies to it.
[**oci_list_roles**](AuthApi.md#oci_list_roles) | **GET** /auth/{oci_mount_path}/role/ | Lists all the roles that are registered with Vault.
[**oci_login**](AuthApi.md#oci_login) | **POST** /auth/{oci_mount_path}/login/{role} | Authenticates to Vault using OCI credentials
[**oci_read_configuration**](AuthApi.md#oci_read_configuration) | **GET** /auth/{oci_mount_path}/config | 
[**oci_read_role**](AuthApi.md#oci_read_role) | **GET** /auth/{oci_mount_path}/role/{role} | Create a role and associate policies to it.
[**oci_write_role**](AuthApi.md#oci_write_role) | **POST** /auth/{oci_mount_path}/role/{role} | Create a role and associate policies to it.
[**okta_configure**](AuthApi.md#okta_configure) | **POST** /auth/{okta_mount_path}/config | 
[**okta_delete_group**](AuthApi.md#okta_delete_group) | **DELETE** /auth/{okta_mount_path}/groups/{name} | Manage users allowed to authenticate.
[**okta_delete_user**](AuthApi.md#okta_delete_user) | **DELETE** /auth/{okta_mount_path}/users/{name} | Manage additional groups for users allowed to authenticate.
[**okta_list_groups**](AuthApi.md#okta_list_groups) | **GET** /auth/{okta_mount_path}/groups/ | Manage users allowed to authenticate.
[**okta_list_users**](AuthApi.md#okta_list_users) | **GET** /auth/{okta_mount_path}/users/ | Manage additional groups for users allowed to authenticate.
[**okta_login**](AuthApi.md#okta_login) | **POST** /auth/{okta_mount_path}/login/{username} | Log in with a username and password.
[**okta_read_configuration**](AuthApi.md#okta_read_configuration) | **GET** /auth/{okta_mount_path}/config | 
[**okta_read_group**](AuthApi.md#okta_read_group) | **GET** /auth/{okta_mount_path}/groups/{name} | Manage users allowed to authenticate.
[**okta_read_user**](AuthApi.md#okta_read_user) | **GET** /auth/{okta_mount_path}/users/{name} | Manage additional groups for users allowed to authenticate.
[**okta_verify**](AuthApi.md#okta_verify) | **GET** /auth/{okta_mount_path}/verify/{nonce} | 
[**okta_write_group**](AuthApi.md#okta_write_group) | **POST** /auth/{okta_mount_path}/groups/{name} | Manage users allowed to authenticate.
[**okta_write_user**](AuthApi.md#okta_write_user) | **POST** /auth/{okta_mount_path}/users/{name} | Manage additional groups for users allowed to authenticate.
[**radius_configure**](AuthApi.md#radius_configure) | **POST** /auth/{radius_mount_path}/config | 
[**radius_delete_user**](AuthApi.md#radius_delete_user) | **DELETE** /auth/{radius_mount_path}/users/{name} | Manage users allowed to authenticate.
[**radius_list_users**](AuthApi.md#radius_list_users) | **GET** /auth/{radius_mount_path}/users/ | Manage users allowed to authenticate.
[**radius_login**](AuthApi.md#radius_login) | **POST** /auth/{radius_mount_path}/login | Log in with a username and password.
[**radius_login_with_username**](AuthApi.md#radius_login_with_username) | **POST** /auth/{radius_mount_path}/login/{urlusername} | Log in with a username and password.
[**radius_read_configuration**](AuthApi.md#radius_read_configuration) | **GET** /auth/{radius_mount_path}/config | 
[**radius_read_user**](AuthApi.md#radius_read_user) | **GET** /auth/{radius_mount_path}/users/{name} | Manage users allowed to authenticate.
[**radius_write_user**](AuthApi.md#radius_write_user) | **POST** /auth/{radius_mount_path}/users/{name} | Manage users allowed to authenticate.
[**token_create**](AuthApi.md#token_create) | **POST** /auth/token/create | The token create path is used to create new tokens.
[**token_create_against_role**](AuthApi.md#token_create_against_role) | **POST** /auth/token/create/{role_name} | This token create path is used to create new tokens adhering to the given role.
[**token_create_orphan**](AuthApi.md#token_create_orphan) | **POST** /auth/token/create-orphan | The token create path is used to create new orphan tokens.
[**token_delete_role**](AuthApi.md#token_delete_role) | **DELETE** /auth/token/roles/{role_name} | 
[**token_list_accessors**](AuthApi.md#token_list_accessors) | **GET** /auth/token/accessors/ | List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires &#39;sudo&#39; capability in addition to &#39;list&#39;.
[**token_list_roles**](AuthApi.md#token_list_roles) | **GET** /auth/token/roles/ | This endpoint lists configured roles.
[**token_look_up**](AuthApi.md#token_look_up) | **POST** /auth/token/lookup | 
[**token_look_up2**](AuthApi.md#token_look_up2) | **GET** /auth/token/lookup | 
[**token_look_up_accessor**](AuthApi.md#token_look_up_accessor) | **POST** /auth/token/lookup-accessor | This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.
[**token_look_up_self**](AuthApi.md#token_look_up_self) | **GET** /auth/token/lookup-self | 
[**token_look_up_self2**](AuthApi.md#token_look_up_self2) | **POST** /auth/token/lookup-self | 
[**token_read_role**](AuthApi.md#token_read_role) | **GET** /auth/token/roles/{role_name} | 
[**token_renew**](AuthApi.md#token_renew) | **POST** /auth/token/renew | This endpoint will renew the given token and prevent expiration.
[**token_renew_accessor**](AuthApi.md#token_renew_accessor) | **POST** /auth/token/renew-accessor | This endpoint will renew a token associated with the given accessor and its properties. Response will not contain the token ID.
[**token_renew_self**](AuthApi.md#token_renew_self) | **POST** /auth/token/renew-self | This endpoint will renew the token used to call it and prevent expiration.
[**token_revoke**](AuthApi.md#token_revoke) | **POST** /auth/token/revoke | This endpoint will delete the given token and all of its child tokens.
[**token_revoke_accessor**](AuthApi.md#token_revoke_accessor) | **POST** /auth/token/revoke-accessor | This endpoint will delete the token associated with the accessor and all of its child tokens.
[**token_revoke_orphan**](AuthApi.md#token_revoke_orphan) | **POST** /auth/token/revoke-orphan | This endpoint will delete the token and orphan its child tokens.
[**token_revoke_self**](AuthApi.md#token_revoke_self) | **POST** /auth/token/revoke-self | This endpoint will delete the token used to call it and all of its child tokens.
[**token_tidy**](AuthApi.md#token_tidy) | **POST** /auth/token/tidy | This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.
[**token_write_role**](AuthApi.md#token_write_role) | **POST** /auth/token/roles/{role_name} | 
[**userpass_delete_user**](AuthApi.md#userpass_delete_user) | **DELETE** /auth/{userpass_mount_path}/users/{username} | Manage users allowed to authenticate.
[**userpass_list_users**](AuthApi.md#userpass_list_users) | **GET** /auth/{userpass_mount_path}/users/ | Manage users allowed to authenticate.
[**userpass_login**](AuthApi.md#userpass_login) | **POST** /auth/{userpass_mount_path}/login/{username} | Log in with a username and password.
[**userpass_read_user**](AuthApi.md#userpass_read_user) | **GET** /auth/{userpass_mount_path}/users/{username} | Manage users allowed to authenticate.
[**userpass_reset_password**](AuthApi.md#userpass_reset_password) | **POST** /auth/{userpass_mount_path}/users/{username}/password | Reset user&#39;s password.
[**userpass_update_policies**](AuthApi.md#userpass_update_policies) | **POST** /auth/{userpass_mount_path}/users/{username}/policies | Update the policies associated with the username.
[**userpass_write_user**](AuthApi.md#userpass_write_user) | **POST** /auth/{userpass_mount_path}/users/{username} | Manage users allowed to authenticate.


# **ali_cloud_delete_auth_role**
> ali_cloud_delete_auth_role(role, alicloud_mount_path)

Create a role and associate policies to it.

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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | The name of the role as it should appear in Vault.
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')

    try:
        # Create a role and associate policies to it.
        await api_instance.ali_cloud_delete_auth_role(role, alicloud_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->ali_cloud_delete_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of the role as it should appear in Vault. | 
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

# **ali_cloud_list_auth_roles**
> StandardListResponse ali_cloud_list_auth_roles(alicloud_mount_path, list)

Lists all the roles that are registered with Vault.

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
    api_instance = ahvac.AuthApi(api_client)
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Lists all the roles that are registered with Vault.
        api_response = await api_instance.ali_cloud_list_auth_roles(alicloud_mount_path, list)
        print("The response of AuthApi->ali_cloud_list_auth_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->ali_cloud_list_auth_roles: %s\n" % e)
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

# **ali_cloud_list_auth_roles2**
> StandardListResponse ali_cloud_list_auth_roles2(alicloud_mount_path, list)

Lists all the roles that are registered with Vault.

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
    api_instance = ahvac.AuthApi(api_client)
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Lists all the roles that are registered with Vault.
        api_response = await api_instance.ali_cloud_list_auth_roles2(alicloud_mount_path, list)
        print("The response of AuthApi->ali_cloud_list_auth_roles2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->ali_cloud_list_auth_roles2: %s\n" % e)
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

# **ali_cloud_login**
> ali_cloud_login(alicloud_mount_path, ali_cloud_login_request)

Authenticates an RAM entity with Vault.

### Example


```python
import ahvac
from ahvac.models.ali_cloud_login_request import AliCloudLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')
    ali_cloud_login_request = ahvac.AliCloudLoginRequest() # AliCloudLoginRequest | 

    try:
        # Authenticates an RAM entity with Vault.
        await api_instance.ali_cloud_login(alicloud_mount_path, ali_cloud_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->ali_cloud_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]
 **ali_cloud_login_request** | [**AliCloudLoginRequest**](AliCloudLoginRequest.md)|  | 

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

# **ali_cloud_read_auth_role**
> ali_cloud_read_auth_role(role, alicloud_mount_path)

Create a role and associate policies to it.

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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | The name of the role as it should appear in Vault.
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')

    try:
        # Create a role and associate policies to it.
        await api_instance.ali_cloud_read_auth_role(role, alicloud_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->ali_cloud_read_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of the role as it should appear in Vault. | 
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

# **ali_cloud_write_auth_role**
> ali_cloud_write_auth_role(role, alicloud_mount_path, ali_cloud_write_auth_role_request)

Create a role and associate policies to it.

### Example


```python
import ahvac
from ahvac.models.ali_cloud_write_auth_role_request import AliCloudWriteAuthRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | The name of the role as it should appear in Vault.
    alicloud_mount_path = 'alicloud' # str | Path that the backend was mounted at (default to 'alicloud')
    ali_cloud_write_auth_role_request = ahvac.AliCloudWriteAuthRoleRequest() # AliCloudWriteAuthRoleRequest | 

    try:
        # Create a role and associate policies to it.
        await api_instance.ali_cloud_write_auth_role(role, alicloud_mount_path, ali_cloud_write_auth_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->ali_cloud_write_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of the role as it should appear in Vault. | 
 **alicloud_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;alicloud&#39;]
 **ali_cloud_write_auth_role_request** | [**AliCloudWriteAuthRoleRequest**](AliCloudWriteAuthRoleRequest.md)|  | 

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

# **app_role_delete_bind_secret_id**
> app_role_delete_bind_secret_id(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_bind_secret_id(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_bind_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_bound_cidr_list**
> app_role_delete_bound_cidr_list(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_bound_cidr_list(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_bound_cidr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_period**
> app_role_delete_period(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_period(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_policies**
> app_role_delete_policies(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_policies(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_role**
> app_role_delete_role(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_role(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_secret_id_bound_cidrs**
> app_role_delete_secret_id_bound_cidrs(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_secret_id_bound_cidrs(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_secret_id_bound_cidrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_secret_id_num_uses**
> app_role_delete_secret_id_num_uses(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_secret_id_num_uses(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_secret_id_num_uses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_secret_id_ttl**
> app_role_delete_secret_id_ttl(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_secret_id_ttl(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_secret_id_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_token_bound_cidrs**
> app_role_delete_token_bound_cidrs(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_token_bound_cidrs(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_token_bound_cidrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_token_max_ttl**
> app_role_delete_token_max_ttl(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_token_max_ttl(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_token_max_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_token_num_uses**
> app_role_delete_token_num_uses(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_token_num_uses(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_token_num_uses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_delete_token_ttl**
> app_role_delete_token_ttl(role_name, approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_delete_token_ttl(role_name, approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_delete_token_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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

# **app_role_destroy_secret_id**
> app_role_destroy_secret_id(role_name, approle_mount_path, app_role_destroy_secret_id_request)



### Example


```python
import ahvac
from ahvac.models.app_role_destroy_secret_id_request import AppRoleDestroySecretIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_destroy_secret_id_request = ahvac.AppRoleDestroySecretIdRequest() # AppRoleDestroySecretIdRequest | 

    try:
        await api_instance.app_role_destroy_secret_id(role_name, approle_mount_path, app_role_destroy_secret_id_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_destroy_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_destroy_secret_id_request** | [**AppRoleDestroySecretIdRequest**](AppRoleDestroySecretIdRequest.md)|  | 

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

# **app_role_destroy_secret_id2**
> app_role_destroy_secret_id2(role_name, approle_mount_path, secret_id=secret_id)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    secret_id = 'secret_id_example' # str | SecretID attached to the role. (optional)

    try:
        await api_instance.app_role_destroy_secret_id2(role_name, approle_mount_path, secret_id=secret_id)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_destroy_secret_id2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **secret_id** | **str**| SecretID attached to the role. | [optional] 

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

# **app_role_destroy_secret_id_by_accessor**
> app_role_destroy_secret_id_by_accessor(role_name, approle_mount_path, app_role_destroy_secret_id_by_accessor_request)



### Example


```python
import ahvac
from ahvac.models.app_role_destroy_secret_id_by_accessor_request import AppRoleDestroySecretIdByAccessorRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_destroy_secret_id_by_accessor_request = ahvac.AppRoleDestroySecretIdByAccessorRequest() # AppRoleDestroySecretIdByAccessorRequest | 

    try:
        await api_instance.app_role_destroy_secret_id_by_accessor(role_name, approle_mount_path, app_role_destroy_secret_id_by_accessor_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_destroy_secret_id_by_accessor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_destroy_secret_id_by_accessor_request** | [**AppRoleDestroySecretIdByAccessorRequest**](AppRoleDestroySecretIdByAccessorRequest.md)|  | 

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

# **app_role_destroy_secret_id_by_accessor2**
> app_role_destroy_secret_id_by_accessor2(role_name, approle_mount_path, secret_id_accessor=secret_id_accessor)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    secret_id_accessor = 'secret_id_accessor_example' # str | Accessor of the SecretID (optional)

    try:
        await api_instance.app_role_destroy_secret_id_by_accessor2(role_name, approle_mount_path, secret_id_accessor=secret_id_accessor)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_destroy_secret_id_by_accessor2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **secret_id_accessor** | **str**| Accessor of the SecretID | [optional] 

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

# **app_role_list_roles**
> StandardListResponse app_role_list_roles(approle_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.app_role_list_roles(approle_mount_path, list)
        print("The response of AuthApi->app_role_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
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

# **app_role_list_secret_ids**
> StandardListResponse app_role_list_secret_ids(role_name, approle_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.app_role_list_secret_ids(role_name, approle_mount_path, list)
        print("The response of AuthApi->app_role_list_secret_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_list_secret_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
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

# **app_role_login**
> app_role_login(approle_mount_path, app_role_login_request)



### Example


```python
import ahvac
from ahvac.models.app_role_login_request import AppRoleLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_login_request = ahvac.AppRoleLoginRequest() # AppRoleLoginRequest | 

    try:
        await api_instance.app_role_login(approle_mount_path, app_role_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_login_request** | [**AppRoleLoginRequest**](AppRoleLoginRequest.md)|  | 

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

# **app_role_look_up_secret_id**
> AppRoleLookUpSecretIdResponse app_role_look_up_secret_id(role_name, approle_mount_path, app_role_look_up_secret_id_request)



### Example


```python
import ahvac
from ahvac.models.app_role_look_up_secret_id_request import AppRoleLookUpSecretIdRequest
from ahvac.models.app_role_look_up_secret_id_response import AppRoleLookUpSecretIdResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_look_up_secret_id_request = ahvac.AppRoleLookUpSecretIdRequest() # AppRoleLookUpSecretIdRequest | 

    try:
        api_response = await api_instance.app_role_look_up_secret_id(role_name, approle_mount_path, app_role_look_up_secret_id_request)
        print("The response of AuthApi->app_role_look_up_secret_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_look_up_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_look_up_secret_id_request** | [**AppRoleLookUpSecretIdRequest**](AppRoleLookUpSecretIdRequest.md)|  | 

### Return type

[**AppRoleLookUpSecretIdResponse**](AppRoleLookUpSecretIdResponse.md)

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

# **app_role_look_up_secret_id_by_accessor**
> AppRoleLookUpSecretIdByAccessorResponse app_role_look_up_secret_id_by_accessor(role_name, approle_mount_path, app_role_look_up_secret_id_by_accessor_request)



### Example


```python
import ahvac
from ahvac.models.app_role_look_up_secret_id_by_accessor_request import AppRoleLookUpSecretIdByAccessorRequest
from ahvac.models.app_role_look_up_secret_id_by_accessor_response import AppRoleLookUpSecretIdByAccessorResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_look_up_secret_id_by_accessor_request = ahvac.AppRoleLookUpSecretIdByAccessorRequest() # AppRoleLookUpSecretIdByAccessorRequest | 

    try:
        api_response = await api_instance.app_role_look_up_secret_id_by_accessor(role_name, approle_mount_path, app_role_look_up_secret_id_by_accessor_request)
        print("The response of AuthApi->app_role_look_up_secret_id_by_accessor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_look_up_secret_id_by_accessor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_look_up_secret_id_by_accessor_request** | [**AppRoleLookUpSecretIdByAccessorRequest**](AppRoleLookUpSecretIdByAccessorRequest.md)|  | 

### Return type

[**AppRoleLookUpSecretIdByAccessorResponse**](AppRoleLookUpSecretIdByAccessorResponse.md)

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

# **app_role_read_bind_secret_id**
> AppRoleReadBindSecretIdResponse app_role_read_bind_secret_id(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_bind_secret_id_response import AppRoleReadBindSecretIdResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_bind_secret_id(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_bind_secret_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_bind_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadBindSecretIdResponse**](AppRoleReadBindSecretIdResponse.md)

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

# **app_role_read_bound_cidr_list**
> AppRoleReadBoundCidrListResponse app_role_read_bound_cidr_list(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_bound_cidr_list_response import AppRoleReadBoundCidrListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_bound_cidr_list(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_bound_cidr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_bound_cidr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadBoundCidrListResponse**](AppRoleReadBoundCidrListResponse.md)

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

# **app_role_read_local_secret_ids**
> AppRoleReadLocalSecretIdsResponse app_role_read_local_secret_ids(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_local_secret_ids_response import AppRoleReadLocalSecretIdsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_local_secret_ids(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_local_secret_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_local_secret_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadLocalSecretIdsResponse**](AppRoleReadLocalSecretIdsResponse.md)

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

# **app_role_read_period**
> AppRoleReadPeriodResponse app_role_read_period(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_period_response import AppRoleReadPeriodResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_period(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadPeriodResponse**](AppRoleReadPeriodResponse.md)

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

# **app_role_read_policies**
> AppRoleReadPoliciesResponse app_role_read_policies(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_policies_response import AppRoleReadPoliciesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_policies(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadPoliciesResponse**](AppRoleReadPoliciesResponse.md)

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

# **app_role_read_role**
> AppRoleReadRoleResponse app_role_read_role(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_role_response import AppRoleReadRoleResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_role(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadRoleResponse**](AppRoleReadRoleResponse.md)

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

# **app_role_read_role_id**
> AppRoleReadRoleIdResponse app_role_read_role_id(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_role_id_response import AppRoleReadRoleIdResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_role_id(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_role_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_role_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadRoleIdResponse**](AppRoleReadRoleIdResponse.md)

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

# **app_role_read_secret_id_bound_cidrs**
> AppRoleReadSecretIdBoundCidrsResponse app_role_read_secret_id_bound_cidrs(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_secret_id_bound_cidrs_response import AppRoleReadSecretIdBoundCidrsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_secret_id_bound_cidrs(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_secret_id_bound_cidrs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_secret_id_bound_cidrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadSecretIdBoundCidrsResponse**](AppRoleReadSecretIdBoundCidrsResponse.md)

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

# **app_role_read_secret_id_num_uses**
> AppRoleReadSecretIdNumUsesResponse app_role_read_secret_id_num_uses(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_secret_id_num_uses_response import AppRoleReadSecretIdNumUsesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_secret_id_num_uses(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_secret_id_num_uses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_secret_id_num_uses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadSecretIdNumUsesResponse**](AppRoleReadSecretIdNumUsesResponse.md)

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

# **app_role_read_secret_id_ttl**
> AppRoleReadSecretIdTtlResponse app_role_read_secret_id_ttl(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_secret_id_ttl_response import AppRoleReadSecretIdTtlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_secret_id_ttl(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_secret_id_ttl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_secret_id_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadSecretIdTtlResponse**](AppRoleReadSecretIdTtlResponse.md)

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

# **app_role_read_token_bound_cidrs**
> AppRoleReadTokenBoundCidrsResponse app_role_read_token_bound_cidrs(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_token_bound_cidrs_response import AppRoleReadTokenBoundCidrsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_token_bound_cidrs(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_token_bound_cidrs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_token_bound_cidrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadTokenBoundCidrsResponse**](AppRoleReadTokenBoundCidrsResponse.md)

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

# **app_role_read_token_max_ttl**
> AppRoleReadTokenMaxTtlResponse app_role_read_token_max_ttl(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_token_max_ttl_response import AppRoleReadTokenMaxTtlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_token_max_ttl(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_token_max_ttl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_token_max_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadTokenMaxTtlResponse**](AppRoleReadTokenMaxTtlResponse.md)

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

# **app_role_read_token_num_uses**
> AppRoleReadTokenNumUsesResponse app_role_read_token_num_uses(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_token_num_uses_response import AppRoleReadTokenNumUsesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_token_num_uses(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_token_num_uses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_token_num_uses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadTokenNumUsesResponse**](AppRoleReadTokenNumUsesResponse.md)

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

# **app_role_read_token_ttl**
> AppRoleReadTokenTtlResponse app_role_read_token_ttl(role_name, approle_mount_path)



### Example


```python
import ahvac
from ahvac.models.app_role_read_token_ttl_response import AppRoleReadTokenTtlResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        api_response = await api_instance.app_role_read_token_ttl(role_name, approle_mount_path)
        print("The response of AuthApi->app_role_read_token_ttl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_read_token_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

### Return type

[**AppRoleReadTokenTtlResponse**](AppRoleReadTokenTtlResponse.md)

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

# **app_role_tidy_secret_id**
> app_role_tidy_secret_id(approle_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')

    try:
        await api_instance.app_role_tidy_secret_id(approle_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_tidy_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_role_write_bind_secret_id**
> app_role_write_bind_secret_id(role_name, approle_mount_path, app_role_write_bind_secret_id_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_bind_secret_id_request import AppRoleWriteBindSecretIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_bind_secret_id_request = ahvac.AppRoleWriteBindSecretIdRequest() # AppRoleWriteBindSecretIdRequest | 

    try:
        await api_instance.app_role_write_bind_secret_id(role_name, approle_mount_path, app_role_write_bind_secret_id_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_bind_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_bind_secret_id_request** | [**AppRoleWriteBindSecretIdRequest**](AppRoleWriteBindSecretIdRequest.md)|  | 

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

# **app_role_write_bound_cidr_list**
> app_role_write_bound_cidr_list(role_name, approle_mount_path, app_role_write_bound_cidr_list_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_bound_cidr_list_request import AppRoleWriteBoundCidrListRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_bound_cidr_list_request = ahvac.AppRoleWriteBoundCidrListRequest() # AppRoleWriteBoundCidrListRequest | 

    try:
        await api_instance.app_role_write_bound_cidr_list(role_name, approle_mount_path, app_role_write_bound_cidr_list_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_bound_cidr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_bound_cidr_list_request** | [**AppRoleWriteBoundCidrListRequest**](AppRoleWriteBoundCidrListRequest.md)|  | 

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

# **app_role_write_custom_secret_id**
> AppRoleWriteCustomSecretIdResponse app_role_write_custom_secret_id(role_name, approle_mount_path, app_role_write_custom_secret_id_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_custom_secret_id_request import AppRoleWriteCustomSecretIdRequest
from ahvac.models.app_role_write_custom_secret_id_response import AppRoleWriteCustomSecretIdResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_custom_secret_id_request = ahvac.AppRoleWriteCustomSecretIdRequest() # AppRoleWriteCustomSecretIdRequest | 

    try:
        api_response = await api_instance.app_role_write_custom_secret_id(role_name, approle_mount_path, app_role_write_custom_secret_id_request)
        print("The response of AuthApi->app_role_write_custom_secret_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_custom_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_custom_secret_id_request** | [**AppRoleWriteCustomSecretIdRequest**](AppRoleWriteCustomSecretIdRequest.md)|  | 

### Return type

[**AppRoleWriteCustomSecretIdResponse**](AppRoleWriteCustomSecretIdResponse.md)

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

# **app_role_write_period**
> app_role_write_period(role_name, approle_mount_path, app_role_write_period_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_period_request import AppRoleWritePeriodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_period_request = ahvac.AppRoleWritePeriodRequest() # AppRoleWritePeriodRequest | 

    try:
        await api_instance.app_role_write_period(role_name, approle_mount_path, app_role_write_period_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_period_request** | [**AppRoleWritePeriodRequest**](AppRoleWritePeriodRequest.md)|  | 

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

# **app_role_write_policies**
> app_role_write_policies(role_name, approle_mount_path, app_role_write_policies_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_policies_request import AppRoleWritePoliciesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_policies_request = ahvac.AppRoleWritePoliciesRequest() # AppRoleWritePoliciesRequest | 

    try:
        await api_instance.app_role_write_policies(role_name, approle_mount_path, app_role_write_policies_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_policies_request** | [**AppRoleWritePoliciesRequest**](AppRoleWritePoliciesRequest.md)|  | 

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

# **app_role_write_role**
> app_role_write_role(role_name, approle_mount_path, app_role_write_role_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_role_request import AppRoleWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_role_request = ahvac.AppRoleWriteRoleRequest() # AppRoleWriteRoleRequest | 

    try:
        await api_instance.app_role_write_role(role_name, approle_mount_path, app_role_write_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_role_request** | [**AppRoleWriteRoleRequest**](AppRoleWriteRoleRequest.md)|  | 

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

# **app_role_write_role_id**
> app_role_write_role_id(role_name, approle_mount_path, app_role_write_role_id_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_role_id_request import AppRoleWriteRoleIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_role_id_request = ahvac.AppRoleWriteRoleIdRequest() # AppRoleWriteRoleIdRequest | 

    try:
        await api_instance.app_role_write_role_id(role_name, approle_mount_path, app_role_write_role_id_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_role_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_role_id_request** | [**AppRoleWriteRoleIdRequest**](AppRoleWriteRoleIdRequest.md)|  | 

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

# **app_role_write_secret_id**
> AppRoleWriteSecretIdResponse app_role_write_secret_id(role_name, approle_mount_path, app_role_write_secret_id_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_secret_id_request import AppRoleWriteSecretIdRequest
from ahvac.models.app_role_write_secret_id_response import AppRoleWriteSecretIdResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_secret_id_request = ahvac.AppRoleWriteSecretIdRequest() # AppRoleWriteSecretIdRequest | 

    try:
        api_response = await api_instance.app_role_write_secret_id(role_name, approle_mount_path, app_role_write_secret_id_request)
        print("The response of AuthApi->app_role_write_secret_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_secret_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_secret_id_request** | [**AppRoleWriteSecretIdRequest**](AppRoleWriteSecretIdRequest.md)|  | 

### Return type

[**AppRoleWriteSecretIdResponse**](AppRoleWriteSecretIdResponse.md)

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

# **app_role_write_secret_id_bound_cidrs**
> app_role_write_secret_id_bound_cidrs(role_name, approle_mount_path, app_role_write_secret_id_bound_cidrs_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_secret_id_bound_cidrs_request import AppRoleWriteSecretIdBoundCidrsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_secret_id_bound_cidrs_request = ahvac.AppRoleWriteSecretIdBoundCidrsRequest() # AppRoleWriteSecretIdBoundCidrsRequest | 

    try:
        await api_instance.app_role_write_secret_id_bound_cidrs(role_name, approle_mount_path, app_role_write_secret_id_bound_cidrs_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_secret_id_bound_cidrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_secret_id_bound_cidrs_request** | [**AppRoleWriteSecretIdBoundCidrsRequest**](AppRoleWriteSecretIdBoundCidrsRequest.md)|  | 

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

# **app_role_write_secret_id_num_uses**
> app_role_write_secret_id_num_uses(role_name, approle_mount_path, app_role_write_secret_id_num_uses_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_secret_id_num_uses_request import AppRoleWriteSecretIdNumUsesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_secret_id_num_uses_request = ahvac.AppRoleWriteSecretIdNumUsesRequest() # AppRoleWriteSecretIdNumUsesRequest | 

    try:
        await api_instance.app_role_write_secret_id_num_uses(role_name, approle_mount_path, app_role_write_secret_id_num_uses_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_secret_id_num_uses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_secret_id_num_uses_request** | [**AppRoleWriteSecretIdNumUsesRequest**](AppRoleWriteSecretIdNumUsesRequest.md)|  | 

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

# **app_role_write_secret_id_ttl**
> app_role_write_secret_id_ttl(role_name, approle_mount_path, app_role_write_secret_id_ttl_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_secret_id_ttl_request import AppRoleWriteSecretIdTtlRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_secret_id_ttl_request = ahvac.AppRoleWriteSecretIdTtlRequest() # AppRoleWriteSecretIdTtlRequest | 

    try:
        await api_instance.app_role_write_secret_id_ttl(role_name, approle_mount_path, app_role_write_secret_id_ttl_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_secret_id_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_secret_id_ttl_request** | [**AppRoleWriteSecretIdTtlRequest**](AppRoleWriteSecretIdTtlRequest.md)|  | 

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

# **app_role_write_token_bound_cidrs**
> app_role_write_token_bound_cidrs(role_name, approle_mount_path, app_role_write_token_bound_cidrs_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_token_bound_cidrs_request import AppRoleWriteTokenBoundCidrsRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_token_bound_cidrs_request = ahvac.AppRoleWriteTokenBoundCidrsRequest() # AppRoleWriteTokenBoundCidrsRequest | 

    try:
        await api_instance.app_role_write_token_bound_cidrs(role_name, approle_mount_path, app_role_write_token_bound_cidrs_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_token_bound_cidrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_token_bound_cidrs_request** | [**AppRoleWriteTokenBoundCidrsRequest**](AppRoleWriteTokenBoundCidrsRequest.md)|  | 

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

# **app_role_write_token_max_ttl**
> app_role_write_token_max_ttl(role_name, approle_mount_path, app_role_write_token_max_ttl_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_token_max_ttl_request import AppRoleWriteTokenMaxTtlRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_token_max_ttl_request = ahvac.AppRoleWriteTokenMaxTtlRequest() # AppRoleWriteTokenMaxTtlRequest | 

    try:
        await api_instance.app_role_write_token_max_ttl(role_name, approle_mount_path, app_role_write_token_max_ttl_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_token_max_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_token_max_ttl_request** | [**AppRoleWriteTokenMaxTtlRequest**](AppRoleWriteTokenMaxTtlRequest.md)|  | 

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

# **app_role_write_token_num_uses**
> app_role_write_token_num_uses(role_name, approle_mount_path, app_role_write_token_num_uses_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_token_num_uses_request import AppRoleWriteTokenNumUsesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_token_num_uses_request = ahvac.AppRoleWriteTokenNumUsesRequest() # AppRoleWriteTokenNumUsesRequest | 

    try:
        await api_instance.app_role_write_token_num_uses(role_name, approle_mount_path, app_role_write_token_num_uses_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_token_num_uses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_token_num_uses_request** | [**AppRoleWriteTokenNumUsesRequest**](AppRoleWriteTokenNumUsesRequest.md)|  | 

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

# **app_role_write_token_ttl**
> app_role_write_token_ttl(role_name, approle_mount_path, app_role_write_token_ttl_request)



### Example


```python
import ahvac
from ahvac.models.app_role_write_token_ttl_request import AppRoleWriteTokenTtlRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role. Must be less than 4096 bytes.
    approle_mount_path = 'approle' # str | Path that the backend was mounted at (default to 'approle')
    app_role_write_token_ttl_request = ahvac.AppRoleWriteTokenTtlRequest() # AppRoleWriteTokenTtlRequest | 

    try:
        await api_instance.app_role_write_token_ttl(role_name, approle_mount_path, app_role_write_token_ttl_request)
    except Exception as e:
        print("Exception when calling AuthApi->app_role_write_token_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role. Must be less than 4096 bytes. | 
 **approle_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;approle&#39;]
 **app_role_write_token_ttl_request** | [**AppRoleWriteTokenTtlRequest**](AppRoleWriteTokenTtlRequest.md)|  | 

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

# **aws_configure_certificate**
> aws_configure_certificate(cert_name, aws_mount_path, aws_configure_certificate_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_certificate_request import AwsConfigureCertificateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    cert_name = 'cert_name_example' # str | Name of the certificate.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_certificate_request = ahvac.AwsConfigureCertificateRequest() # AwsConfigureCertificateRequest | 

    try:
        await api_instance.aws_configure_certificate(cert_name, aws_mount_path, aws_configure_certificate_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_configure_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_name** | **str**| Name of the certificate. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_certificate_request** | [**AwsConfigureCertificateRequest**](AwsConfigureCertificateRequest.md)|  | 

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

# **aws_configure_client**
> aws_configure_client(aws_mount_path, aws_configure_client_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_client_request import AwsConfigureClientRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_client_request = ahvac.AwsConfigureClientRequest() # AwsConfigureClientRequest | 

    try:
        await api_instance.aws_configure_client(aws_mount_path, aws_configure_client_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_configure_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_client_request** | [**AwsConfigureClientRequest**](AwsConfigureClientRequest.md)|  | 

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

# **aws_configure_identity_access_list_tidy_operation**
> aws_configure_identity_access_list_tidy_operation(aws_mount_path, aws_configure_identity_access_list_tidy_operation_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_identity_access_list_tidy_operation_request import AwsConfigureIdentityAccessListTidyOperationRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_identity_access_list_tidy_operation_request = ahvac.AwsConfigureIdentityAccessListTidyOperationRequest() # AwsConfigureIdentityAccessListTidyOperationRequest | 

    try:
        await api_instance.aws_configure_identity_access_list_tidy_operation(aws_mount_path, aws_configure_identity_access_list_tidy_operation_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_configure_identity_access_list_tidy_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_identity_access_list_tidy_operation_request** | [**AwsConfigureIdentityAccessListTidyOperationRequest**](AwsConfigureIdentityAccessListTidyOperationRequest.md)|  | 

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

# **aws_configure_identity_integration**
> aws_configure_identity_integration(aws_mount_path, aws_configure_identity_integration_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_identity_integration_request import AwsConfigureIdentityIntegrationRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_identity_integration_request = ahvac.AwsConfigureIdentityIntegrationRequest() # AwsConfigureIdentityIntegrationRequest | 

    try:
        await api_instance.aws_configure_identity_integration(aws_mount_path, aws_configure_identity_integration_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_configure_identity_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_identity_integration_request** | [**AwsConfigureIdentityIntegrationRequest**](AwsConfigureIdentityIntegrationRequest.md)|  | 

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

# **aws_configure_identity_whitelist_tidy_operation**
> aws_configure_identity_whitelist_tidy_operation(aws_mount_path, aws_configure_identity_whitelist_tidy_operation_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_identity_whitelist_tidy_operation_request import AwsConfigureIdentityWhitelistTidyOperationRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_identity_whitelist_tidy_operation_request = ahvac.AwsConfigureIdentityWhitelistTidyOperationRequest() # AwsConfigureIdentityWhitelistTidyOperationRequest | 

    try:
        await api_instance.aws_configure_identity_whitelist_tidy_operation(aws_mount_path, aws_configure_identity_whitelist_tidy_operation_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_configure_identity_whitelist_tidy_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_identity_whitelist_tidy_operation_request** | [**AwsConfigureIdentityWhitelistTidyOperationRequest**](AwsConfigureIdentityWhitelistTidyOperationRequest.md)|  | 

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

# **aws_configure_role_tag_blacklist_tidy_operation**
> aws_configure_role_tag_blacklist_tidy_operation(aws_mount_path, aws_configure_role_tag_blacklist_tidy_operation_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_role_tag_blacklist_tidy_operation_request import AwsConfigureRoleTagBlacklistTidyOperationRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_role_tag_blacklist_tidy_operation_request = ahvac.AwsConfigureRoleTagBlacklistTidyOperationRequest() # AwsConfigureRoleTagBlacklistTidyOperationRequest | 

    try:
        await api_instance.aws_configure_role_tag_blacklist_tidy_operation(aws_mount_path, aws_configure_role_tag_blacklist_tidy_operation_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_configure_role_tag_blacklist_tidy_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_role_tag_blacklist_tidy_operation_request** | [**AwsConfigureRoleTagBlacklistTidyOperationRequest**](AwsConfigureRoleTagBlacklistTidyOperationRequest.md)|  | 

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

# **aws_configure_role_tag_deny_list_tidy_operation**
> aws_configure_role_tag_deny_list_tidy_operation(aws_mount_path, aws_configure_role_tag_deny_list_tidy_operation_request)



### Example


```python
import ahvac
from ahvac.models.aws_configure_role_tag_deny_list_tidy_operation_request import AwsConfigureRoleTagDenyListTidyOperationRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_configure_role_tag_deny_list_tidy_operation_request = ahvac.AwsConfigureRoleTagDenyListTidyOperationRequest() # AwsConfigureRoleTagDenyListTidyOperationRequest | 

    try:
        await api_instance.aws_configure_role_tag_deny_list_tidy_operation(aws_mount_path, aws_configure_role_tag_deny_list_tidy_operation_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_configure_role_tag_deny_list_tidy_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_configure_role_tag_deny_list_tidy_operation_request** | [**AwsConfigureRoleTagDenyListTidyOperationRequest**](AwsConfigureRoleTagDenyListTidyOperationRequest.md)|  | 

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

# **aws_delete_auth_role**
> aws_delete_auth_role(role, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_auth_role(role, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
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

# **aws_delete_certificate_configuration**
> aws_delete_certificate_configuration(cert_name, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    cert_name = 'cert_name_example' # str | Name of the certificate.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_certificate_configuration(cert_name, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_certificate_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_name** | **str**| Name of the certificate. | 
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

# **aws_delete_client_configuration**
> aws_delete_client_configuration(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_client_configuration(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_client_configuration: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_delete_identity_access_list**
> aws_delete_identity_access_list(instance_id, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    instance_id = 'instance_id_example' # str | EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_identity_access_list(instance_id, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_identity_access_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID. | 
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

# **aws_delete_identity_access_list_tidy_settings**
> aws_delete_identity_access_list_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_identity_access_list_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_identity_access_list_tidy_settings: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_delete_identity_whitelist**
> aws_delete_identity_whitelist(instance_id, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    instance_id = 'instance_id_example' # str | EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_identity_whitelist(instance_id, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_identity_whitelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID. | 
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

# **aws_delete_identity_whitelist_tidy_settings**
> aws_delete_identity_whitelist_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_identity_whitelist_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_identity_whitelist_tidy_settings: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_delete_role_tag_blacklist**
> aws_delete_role_tag_blacklist(role_tag, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_tag = 'role_tag_example' # str | Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_role_tag_blacklist(role_tag, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_role_tag_blacklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_tag** | **str**| Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | 
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

# **aws_delete_role_tag_blacklist_tidy_settings**
> aws_delete_role_tag_blacklist_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_role_tag_blacklist_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_role_tag_blacklist_tidy_settings: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_delete_role_tag_deny_list**
> aws_delete_role_tag_deny_list(role_tag, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_tag = 'role_tag_example' # str | Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_role_tag_deny_list(role_tag, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_role_tag_deny_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_tag** | **str**| Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | 
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

# **aws_delete_role_tag_deny_list_tidy_settings**
> aws_delete_role_tag_deny_list_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_role_tag_deny_list_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_role_tag_deny_list_tidy_settings: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_delete_sts_role**
> aws_delete_sts_role(account_id, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    account_id = 'account_id_example' # str | AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_delete_sts_role(account_id, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_delete_sts_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account. | 
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

# **aws_list_auth_roles**
> StandardListResponse aws_list_auth_roles(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_auth_roles(aws_mount_path, list)
        print("The response of AuthApi->aws_list_auth_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_auth_roles: %s\n" % e)
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

# **aws_list_auth_roles2**
> StandardListResponse aws_list_auth_roles2(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_auth_roles2(aws_mount_path, list)
        print("The response of AuthApi->aws_list_auth_roles2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_auth_roles2: %s\n" % e)
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

# **aws_list_certificate_configurations**
> StandardListResponse aws_list_certificate_configurations(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_certificate_configurations(aws_mount_path, list)
        print("The response of AuthApi->aws_list_certificate_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_certificate_configurations: %s\n" % e)
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

# **aws_list_identity_access_list**
> StandardListResponse aws_list_identity_access_list(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_identity_access_list(aws_mount_path, list)
        print("The response of AuthApi->aws_list_identity_access_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_identity_access_list: %s\n" % e)
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

# **aws_list_identity_whitelist**
> StandardListResponse aws_list_identity_whitelist(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_identity_whitelist(aws_mount_path, list)
        print("The response of AuthApi->aws_list_identity_whitelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_identity_whitelist: %s\n" % e)
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

# **aws_list_role_tag_blacklists**
> StandardListResponse aws_list_role_tag_blacklists(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_role_tag_blacklists(aws_mount_path, list)
        print("The response of AuthApi->aws_list_role_tag_blacklists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_role_tag_blacklists: %s\n" % e)
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

# **aws_list_role_tag_deny_lists**
> StandardListResponse aws_list_role_tag_deny_lists(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_role_tag_deny_lists(aws_mount_path, list)
        print("The response of AuthApi->aws_list_role_tag_deny_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_role_tag_deny_lists: %s\n" % e)
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

# **aws_list_sts_role_relationships**
> StandardListResponse aws_list_sts_role_relationships(aws_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.aws_list_sts_role_relationships(aws_mount_path, list)
        print("The response of AuthApi->aws_list_sts_role_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->aws_list_sts_role_relationships: %s\n" % e)
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

# **aws_login**
> aws_login(aws_mount_path, aws_login_request)



### Example


```python
import ahvac
from ahvac.models.aws_login_request import AwsLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_login_request = ahvac.AwsLoginRequest() # AwsLoginRequest | 

    try:
        await api_instance.aws_login(aws_mount_path, aws_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_login_request** | [**AwsLoginRequest**](AwsLoginRequest.md)|  | 

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

# **aws_read_auth_role**
> aws_read_auth_role(role, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_auth_role(role, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
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

# **aws_read_certificate_configuration**
> aws_read_certificate_configuration(cert_name, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    cert_name = 'cert_name_example' # str | Name of the certificate.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_certificate_configuration(cert_name, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_certificate_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_name** | **str**| Name of the certificate. | 
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

# **aws_read_client_configuration**
> aws_read_client_configuration(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_client_configuration(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_client_configuration: %s\n" % e)
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

# **aws_read_identity_access_list**
> aws_read_identity_access_list(instance_id, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    instance_id = 'instance_id_example' # str | EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_identity_access_list(instance_id, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_identity_access_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID. | 
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

# **aws_read_identity_access_list_tidy_settings**
> aws_read_identity_access_list_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_identity_access_list_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_identity_access_list_tidy_settings: %s\n" % e)
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

# **aws_read_identity_integration_configuration**
> aws_read_identity_integration_configuration(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_identity_integration_configuration(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_identity_integration_configuration: %s\n" % e)
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

# **aws_read_identity_whitelist**
> aws_read_identity_whitelist(instance_id, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    instance_id = 'instance_id_example' # str | EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_identity_whitelist(instance_id, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_identity_whitelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| EC2 instance ID. A successful login operation from an EC2 instance gets cached in this accesslist, keyed off of instance ID. | 
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

# **aws_read_identity_whitelist_tidy_settings**
> aws_read_identity_whitelist_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_identity_whitelist_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_identity_whitelist_tidy_settings: %s\n" % e)
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

# **aws_read_role_tag_blacklist**
> aws_read_role_tag_blacklist(role_tag, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_tag = 'role_tag_example' # str | Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_role_tag_blacklist(role_tag, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_role_tag_blacklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_tag** | **str**| Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | 
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

# **aws_read_role_tag_blacklist_tidy_settings**
> aws_read_role_tag_blacklist_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_role_tag_blacklist_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_role_tag_blacklist_tidy_settings: %s\n" % e)
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

# **aws_read_role_tag_deny_list**
> aws_read_role_tag_deny_list(role_tag, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_tag = 'role_tag_example' # str | Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_role_tag_deny_list(role_tag, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_role_tag_deny_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_tag** | **str**| Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | 
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

# **aws_read_role_tag_deny_list_tidy_settings**
> aws_read_role_tag_deny_list_tidy_settings(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_role_tag_deny_list_tidy_settings(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_role_tag_deny_list_tidy_settings: %s\n" % e)
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

# **aws_read_sts_role**
> aws_read_sts_role(account_id, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    account_id = 'account_id_example' # str | AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_read_sts_role(account_id, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_read_sts_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account. | 
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

# **aws_rotate_root_credentials**
> aws_rotate_root_credentials(aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_rotate_root_credentials(aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_rotate_root_credentials: %s\n" % e)
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

# **aws_tidy_identity_access_list**
> aws_tidy_identity_access_list(aws_mount_path, aws_tidy_identity_access_list_request)



### Example


```python
import ahvac
from ahvac.models.aws_tidy_identity_access_list_request import AwsTidyIdentityAccessListRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_tidy_identity_access_list_request = ahvac.AwsTidyIdentityAccessListRequest() # AwsTidyIdentityAccessListRequest | 

    try:
        await api_instance.aws_tidy_identity_access_list(aws_mount_path, aws_tidy_identity_access_list_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_tidy_identity_access_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_tidy_identity_access_list_request** | [**AwsTidyIdentityAccessListRequest**](AwsTidyIdentityAccessListRequest.md)|  | 

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

# **aws_tidy_identity_whitelist**
> aws_tidy_identity_whitelist(aws_mount_path, aws_tidy_identity_whitelist_request)



### Example


```python
import ahvac
from ahvac.models.aws_tidy_identity_whitelist_request import AwsTidyIdentityWhitelistRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_tidy_identity_whitelist_request = ahvac.AwsTidyIdentityWhitelistRequest() # AwsTidyIdentityWhitelistRequest | 

    try:
        await api_instance.aws_tidy_identity_whitelist(aws_mount_path, aws_tidy_identity_whitelist_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_tidy_identity_whitelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_tidy_identity_whitelist_request** | [**AwsTidyIdentityWhitelistRequest**](AwsTidyIdentityWhitelistRequest.md)|  | 

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

# **aws_tidy_role_tag_blacklist**
> aws_tidy_role_tag_blacklist(aws_mount_path, aws_tidy_role_tag_blacklist_request)



### Example


```python
import ahvac
from ahvac.models.aws_tidy_role_tag_blacklist_request import AwsTidyRoleTagBlacklistRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_tidy_role_tag_blacklist_request = ahvac.AwsTidyRoleTagBlacklistRequest() # AwsTidyRoleTagBlacklistRequest | 

    try:
        await api_instance.aws_tidy_role_tag_blacklist(aws_mount_path, aws_tidy_role_tag_blacklist_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_tidy_role_tag_blacklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_tidy_role_tag_blacklist_request** | [**AwsTidyRoleTagBlacklistRequest**](AwsTidyRoleTagBlacklistRequest.md)|  | 

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

# **aws_tidy_role_tag_deny_list**
> aws_tidy_role_tag_deny_list(aws_mount_path, aws_tidy_role_tag_deny_list_request)



### Example


```python
import ahvac
from ahvac.models.aws_tidy_role_tag_deny_list_request import AwsTidyRoleTagDenyListRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_tidy_role_tag_deny_list_request = ahvac.AwsTidyRoleTagDenyListRequest() # AwsTidyRoleTagDenyListRequest | 

    try:
        await api_instance.aws_tidy_role_tag_deny_list(aws_mount_path, aws_tidy_role_tag_deny_list_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_tidy_role_tag_deny_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_tidy_role_tag_deny_list_request** | [**AwsTidyRoleTagDenyListRequest**](AwsTidyRoleTagDenyListRequest.md)|  | 

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

# **aws_write_auth_role**
> aws_write_auth_role(role, aws_mount_path, aws_write_auth_role_request)



### Example


```python
import ahvac
from ahvac.models.aws_write_auth_role_request import AwsWriteAuthRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_write_auth_role_request = ahvac.AwsWriteAuthRoleRequest() # AwsWriteAuthRoleRequest | 

    try:
        await api_instance.aws_write_auth_role(role, aws_mount_path, aws_write_auth_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_write_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_write_auth_role_request** | [**AwsWriteAuthRoleRequest**](AwsWriteAuthRoleRequest.md)|  | 

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

# **aws_write_role_tag**
> aws_write_role_tag(role, aws_mount_path, aws_write_role_tag_request)



### Example


```python
import ahvac
from ahvac.models.aws_write_role_tag_request import AwsWriteRoleTagRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_write_role_tag_request = ahvac.AwsWriteRoleTagRequest() # AwsWriteRoleTagRequest | 

    try:
        await api_instance.aws_write_role_tag(role, aws_mount_path, aws_write_role_tag_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_write_role_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_write_role_tag_request** | [**AwsWriteRoleTagRequest**](AwsWriteRoleTagRequest.md)|  | 

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

# **aws_write_role_tag_blacklist**
> aws_write_role_tag_blacklist(role_tag, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_tag = 'role_tag_example' # str | Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_write_role_tag_blacklist(role_tag, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_write_role_tag_blacklist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_tag** | **str**| Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | 
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

# **aws_write_role_tag_deny_list**
> aws_write_role_tag_deny_list(role_tag, aws_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role_tag = 'role_tag_example' # str | Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')

    try:
        await api_instance.aws_write_role_tag_deny_list(role_tag, aws_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->aws_write_role_tag_deny_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_tag** | **str**| Role tag to be deny listed. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | 
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

# **aws_write_sts_role**
> aws_write_sts_role(account_id, aws_mount_path, aws_write_sts_role_request)



### Example


```python
import ahvac
from ahvac.models.aws_write_sts_role_request import AwsWriteStsRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    account_id = 'account_id_example' # str | AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account.
    aws_mount_path = 'aws' # str | Path that the backend was mounted at (default to 'aws')
    aws_write_sts_role_request = ahvac.AwsWriteStsRoleRequest() # AwsWriteStsRoleRequest | 

    try:
        await api_instance.aws_write_sts_role(account_id, aws_mount_path, aws_write_sts_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->aws_write_sts_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account. | 
 **aws_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;aws&#39;]
 **aws_write_sts_role_request** | [**AwsWriteStsRoleRequest**](AwsWriteStsRoleRequest.md)|  | 

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

# **azure_configure_auth**
> azure_configure_auth(azure_mount_path, azure_configure_auth_request)



### Example


```python
import ahvac
from ahvac.models.azure_configure_auth_request import AzureConfigureAuthRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')
    azure_configure_auth_request = ahvac.AzureConfigureAuthRequest() # AzureConfigureAuthRequest | 

    try:
        await api_instance.azure_configure_auth(azure_mount_path, azure_configure_auth_request)
    except Exception as e:
        print("Exception when calling AuthApi->azure_configure_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]
 **azure_configure_auth_request** | [**AzureConfigureAuthRequest**](AzureConfigureAuthRequest.md)|  | 

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

# **azure_delete_auth_configuration**
> azure_delete_auth_configuration(azure_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_delete_auth_configuration(azure_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->azure_delete_auth_configuration: %s\n" % e)
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

# **azure_delete_auth_role**
> azure_delete_auth_role(name, azure_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_delete_auth_role(name, azure_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->azure_delete_auth_role: %s\n" % e)
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

# **azure_list_auth_roles**
> StandardListResponse azure_list_auth_roles(azure_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.azure_list_auth_roles(azure_mount_path, list)
        print("The response of AuthApi->azure_list_auth_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->azure_list_auth_roles: %s\n" % e)
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

# **azure_login**
> azure_login(azure_mount_path, azure_login_request)



### Example


```python
import ahvac
from ahvac.models.azure_login_request import AzureLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')
    azure_login_request = ahvac.AzureLoginRequest() # AzureLoginRequest | 

    try:
        await api_instance.azure_login(azure_mount_path, azure_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->azure_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]
 **azure_login_request** | [**AzureLoginRequest**](AzureLoginRequest.md)|  | 

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

# **azure_read_auth_configuration**
> azure_read_auth_configuration(azure_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_read_auth_configuration(azure_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->azure_read_auth_configuration: %s\n" % e)
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

# **azure_read_auth_role**
> azure_read_auth_role(name, azure_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_read_auth_role(name, azure_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->azure_read_auth_role: %s\n" % e)
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

# **azure_rotate_root_credentials**
> azure_rotate_root_credentials(azure_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')

    try:
        await api_instance.azure_rotate_root_credentials(azure_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->azure_rotate_root_credentials: %s\n" % e)
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

# **azure_write_auth_role**
> azure_write_auth_role(name, azure_mount_path, azure_write_auth_role_request)



### Example


```python
import ahvac
from ahvac.models.azure_write_auth_role_request import AzureWriteAuthRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    azure_mount_path = 'azure' # str | Path that the backend was mounted at (default to 'azure')
    azure_write_auth_role_request = ahvac.AzureWriteAuthRoleRequest() # AzureWriteAuthRoleRequest | 

    try:
        await api_instance.azure_write_auth_role(name, azure_mount_path, azure_write_auth_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->azure_write_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **azure_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;azure&#39;]
 **azure_write_auth_role_request** | [**AzureWriteAuthRoleRequest**](AzureWriteAuthRoleRequest.md)|  | 

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

# **centrify_configure**
> centrify_configure(centrify_mount_path, centrify_configure_request)



### Example


```python
import ahvac
from ahvac.models.centrify_configure_request import CentrifyConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    centrify_mount_path = 'centrify' # str | Path that the backend was mounted at (default to 'centrify')
    centrify_configure_request = ahvac.CentrifyConfigureRequest() # CentrifyConfigureRequest | 

    try:
        await api_instance.centrify_configure(centrify_mount_path, centrify_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->centrify_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **centrify_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;centrify&#39;]
 **centrify_configure_request** | [**CentrifyConfigureRequest**](CentrifyConfigureRequest.md)|  | 

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

# **centrify_login**
> centrify_login(centrify_mount_path, centrify_login_request)

Log in with a username and password.

### Example


```python
import ahvac
from ahvac.models.centrify_login_request import CentrifyLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    centrify_mount_path = 'centrify' # str | Path that the backend was mounted at (default to 'centrify')
    centrify_login_request = ahvac.CentrifyLoginRequest() # CentrifyLoginRequest | 

    try:
        # Log in with a username and password.
        await api_instance.centrify_login(centrify_mount_path, centrify_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->centrify_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **centrify_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;centrify&#39;]
 **centrify_login_request** | [**CentrifyLoginRequest**](CentrifyLoginRequest.md)|  | 

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

# **centrify_read_configuration**
> centrify_read_configuration(centrify_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    centrify_mount_path = 'centrify' # str | Path that the backend was mounted at (default to 'centrify')

    try:
        await api_instance.centrify_read_configuration(centrify_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->centrify_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **centrify_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;centrify&#39;]

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

# **cert_configure**
> cert_configure(cert_mount_path, cert_configure_request)



### Example


```python
import ahvac
from ahvac.models.cert_configure_request import CertConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')
    cert_configure_request = ahvac.CertConfigureRequest() # CertConfigureRequest | 

    try:
        await api_instance.cert_configure(cert_mount_path, cert_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->cert_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]
 **cert_configure_request** | [**CertConfigureRequest**](CertConfigureRequest.md)|  | 

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

# **cert_delete_certificate**
> cert_delete_certificate(name, cert_mount_path)

Manage trusted certificates used for authentication.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | The name of the certificate
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')

    try:
        # Manage trusted certificates used for authentication.
        await api_instance.cert_delete_certificate(name, cert_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cert_delete_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the certificate | 
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]

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

# **cert_delete_crl**
> cert_delete_crl(name, cert_mount_path)

Manage Certificate Revocation Lists checked during authentication.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | The name of the certificate
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')

    try:
        # Manage Certificate Revocation Lists checked during authentication.
        await api_instance.cert_delete_crl(name, cert_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cert_delete_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the certificate | 
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]

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

# **cert_list_certificates**
> StandardListResponse cert_list_certificates(cert_mount_path, list)

Manage trusted certificates used for authentication.

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
    api_instance = ahvac.AuthApi(api_client)
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage trusted certificates used for authentication.
        api_response = await api_instance.cert_list_certificates(cert_mount_path, list)
        print("The response of AuthApi->cert_list_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->cert_list_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]
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

# **cert_list_crls**
> StandardListResponse cert_list_crls(cert_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.cert_list_crls(cert_mount_path, list)
        print("The response of AuthApi->cert_list_crls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->cert_list_crls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]
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

# **cert_login**
> cert_login(cert_mount_path, cert_login_request)



### Example


```python
import ahvac
from ahvac.models.cert_login_request import CertLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')
    cert_login_request = ahvac.CertLoginRequest() # CertLoginRequest | 

    try:
        await api_instance.cert_login(cert_mount_path, cert_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->cert_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]
 **cert_login_request** | [**CertLoginRequest**](CertLoginRequest.md)|  | 

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

# **cert_read_certificate**
> cert_read_certificate(name, cert_mount_path)

Manage trusted certificates used for authentication.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | The name of the certificate
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')

    try:
        # Manage trusted certificates used for authentication.
        await api_instance.cert_read_certificate(name, cert_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cert_read_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the certificate | 
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]

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

# **cert_read_configuration**
> cert_read_configuration(cert_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')

    try:
        await api_instance.cert_read_configuration(cert_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cert_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]

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

# **cert_read_crl**
> cert_read_crl(name, cert_mount_path)

Manage Certificate Revocation Lists checked during authentication.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | The name of the certificate
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')

    try:
        # Manage Certificate Revocation Lists checked during authentication.
        await api_instance.cert_read_crl(name, cert_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cert_read_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the certificate | 
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]

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

# **cert_write_certificate**
> cert_write_certificate(name, cert_mount_path, cert_write_certificate_request)

Manage trusted certificates used for authentication.

### Example


```python
import ahvac
from ahvac.models.cert_write_certificate_request import CertWriteCertificateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | The name of the certificate
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')
    cert_write_certificate_request = ahvac.CertWriteCertificateRequest() # CertWriteCertificateRequest | 

    try:
        # Manage trusted certificates used for authentication.
        await api_instance.cert_write_certificate(name, cert_mount_path, cert_write_certificate_request)
    except Exception as e:
        print("Exception when calling AuthApi->cert_write_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the certificate | 
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]
 **cert_write_certificate_request** | [**CertWriteCertificateRequest**](CertWriteCertificateRequest.md)|  | 

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

# **cert_write_crl**
> cert_write_crl(name, cert_mount_path, cert_write_crl_request)

Manage Certificate Revocation Lists checked during authentication.

### Example


```python
import ahvac
from ahvac.models.cert_write_crl_request import CertWriteCrlRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | The name of the certificate
    cert_mount_path = 'cert' # str | Path that the backend was mounted at (default to 'cert')
    cert_write_crl_request = ahvac.CertWriteCrlRequest() # CertWriteCrlRequest | 

    try:
        # Manage Certificate Revocation Lists checked during authentication.
        await api_instance.cert_write_crl(name, cert_mount_path, cert_write_crl_request)
    except Exception as e:
        print("Exception when calling AuthApi->cert_write_crl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the certificate | 
 **cert_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cert&#39;]
 **cert_write_crl_request** | [**CertWriteCrlRequest**](CertWriteCrlRequest.md)|  | 

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

# **cloud_foundry_configure**
> cloud_foundry_configure(cf_mount_path, cloud_foundry_configure_request)



### Example


```python
import ahvac
from ahvac.models.cloud_foundry_configure_request import CloudFoundryConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')
    cloud_foundry_configure_request = ahvac.CloudFoundryConfigureRequest() # CloudFoundryConfigureRequest | 

    try:
        await api_instance.cloud_foundry_configure(cf_mount_path, cloud_foundry_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]
 **cloud_foundry_configure_request** | [**CloudFoundryConfigureRequest**](CloudFoundryConfigureRequest.md)|  | 

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

# **cloud_foundry_delete_configuration**
> cloud_foundry_delete_configuration(cf_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')

    try:
        await api_instance.cloud_foundry_delete_configuration(cf_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]

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

# **cloud_foundry_delete_role**
> cloud_foundry_delete_role(role, cf_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | The name of the role.
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')

    try:
        await api_instance.cloud_foundry_delete_role(role, cf_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of the role. | 
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]

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

# **cloud_foundry_list_roles**
> StandardListResponse cloud_foundry_list_roles(cf_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.cloud_foundry_list_roles(cf_mount_path, list)
        print("The response of AuthApi->cloud_foundry_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]
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

# **cloud_foundry_login**
> cloud_foundry_login(cf_mount_path, cloud_foundry_login_request)



### Example


```python
import ahvac
from ahvac.models.cloud_foundry_login_request import CloudFoundryLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')
    cloud_foundry_login_request = ahvac.CloudFoundryLoginRequest() # CloudFoundryLoginRequest | 

    try:
        await api_instance.cloud_foundry_login(cf_mount_path, cloud_foundry_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]
 **cloud_foundry_login_request** | [**CloudFoundryLoginRequest**](CloudFoundryLoginRequest.md)|  | 

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

# **cloud_foundry_read_configuration**
> cloud_foundry_read_configuration(cf_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')

    try:
        await api_instance.cloud_foundry_read_configuration(cf_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]

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

# **cloud_foundry_read_role**
> cloud_foundry_read_role(role, cf_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | The name of the role.
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')

    try:
        await api_instance.cloud_foundry_read_role(role, cf_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of the role. | 
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]

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

# **cloud_foundry_write_role**
> cloud_foundry_write_role(role, cf_mount_path, cloud_foundry_write_role_request)



### Example


```python
import ahvac
from ahvac.models.cloud_foundry_write_role_request import CloudFoundryWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | The name of the role.
    cf_mount_path = 'cf' # str | Path that the backend was mounted at (default to 'cf')
    cloud_foundry_write_role_request = ahvac.CloudFoundryWriteRoleRequest() # CloudFoundryWriteRoleRequest | 

    try:
        await api_instance.cloud_foundry_write_role(role, cf_mount_path, cloud_foundry_write_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->cloud_foundry_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of the role. | 
 **cf_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;cf&#39;]
 **cloud_foundry_write_role_request** | [**CloudFoundryWriteRoleRequest**](CloudFoundryWriteRoleRequest.md)|  | 

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

# **github_configure**
> github_configure(github_mount_path, github_configure_request)



### Example


```python
import ahvac
from ahvac.models.github_configure_request import GithubConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')
    github_configure_request = ahvac.GithubConfigureRequest() # GithubConfigureRequest | 

    try:
        await api_instance.github_configure(github_mount_path, github_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->github_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]
 **github_configure_request** | [**GithubConfigureRequest**](GithubConfigureRequest.md)|  | 

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

# **github_delete_team_mapping**
> github_delete_team_mapping(key, github_mount_path)

Read/write/delete a single teams mapping

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
    api_instance = ahvac.AuthApi(api_client)
    key = 'key_example' # str | Key for the teams mapping
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')

    try:
        # Read/write/delete a single teams mapping
        await api_instance.github_delete_team_mapping(key, github_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->github_delete_team_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key for the teams mapping | 
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]

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

# **github_delete_user_mapping**
> github_delete_user_mapping(key, github_mount_path)

Read/write/delete a single users mapping

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
    api_instance = ahvac.AuthApi(api_client)
    key = 'key_example' # str | Key for the users mapping
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')

    try:
        # Read/write/delete a single users mapping
        await api_instance.github_delete_user_mapping(key, github_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->github_delete_user_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key for the users mapping | 
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]

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

# **github_list_teams**
> StandardListResponse github_list_teams(github_mount_path, list)

Read mappings for teams

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
    api_instance = ahvac.AuthApi(api_client)
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Read mappings for teams
        api_response = await api_instance.github_list_teams(github_mount_path, list)
        print("The response of AuthApi->github_list_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->github_list_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]
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

# **github_list_teams2**
> github_list_teams2(github_mount_path)

Read mappings for teams

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
    api_instance = ahvac.AuthApi(api_client)
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')

    try:
        # Read mappings for teams
        await api_instance.github_list_teams2(github_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->github_list_teams2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]

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

# **github_list_users**
> StandardListResponse github_list_users(github_mount_path, list)

Read mappings for users

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
    api_instance = ahvac.AuthApi(api_client)
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Read mappings for users
        api_response = await api_instance.github_list_users(github_mount_path, list)
        print("The response of AuthApi->github_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->github_list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]
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

# **github_list_users2**
> github_list_users2(github_mount_path)

Read mappings for users

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
    api_instance = ahvac.AuthApi(api_client)
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')

    try:
        # Read mappings for users
        await api_instance.github_list_users2(github_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->github_list_users2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]

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

# **github_login**
> github_login(github_mount_path, github_login_request)



### Example


```python
import ahvac
from ahvac.models.github_login_request import GithubLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')
    github_login_request = ahvac.GithubLoginRequest() # GithubLoginRequest | 

    try:
        await api_instance.github_login(github_mount_path, github_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->github_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]
 **github_login_request** | [**GithubLoginRequest**](GithubLoginRequest.md)|  | 

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

# **github_read_configuration**
> github_read_configuration(github_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')

    try:
        await api_instance.github_read_configuration(github_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->github_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]

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

# **github_read_team_mapping**
> github_read_team_mapping(key, github_mount_path)

Read/write/delete a single teams mapping

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
    api_instance = ahvac.AuthApi(api_client)
    key = 'key_example' # str | Key for the teams mapping
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')

    try:
        # Read/write/delete a single teams mapping
        await api_instance.github_read_team_mapping(key, github_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->github_read_team_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key for the teams mapping | 
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]

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

# **github_read_user_mapping**
> github_read_user_mapping(key, github_mount_path)

Read/write/delete a single users mapping

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
    api_instance = ahvac.AuthApi(api_client)
    key = 'key_example' # str | Key for the users mapping
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')

    try:
        # Read/write/delete a single users mapping
        await api_instance.github_read_user_mapping(key, github_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->github_read_user_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key for the users mapping | 
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]

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

# **github_write_team_mapping**
> github_write_team_mapping(key, github_mount_path, github_write_team_mapping_request)

Read/write/delete a single teams mapping

### Example


```python
import ahvac
from ahvac.models.github_write_team_mapping_request import GithubWriteTeamMappingRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    key = 'key_example' # str | Key for the teams mapping
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')
    github_write_team_mapping_request = ahvac.GithubWriteTeamMappingRequest() # GithubWriteTeamMappingRequest | 

    try:
        # Read/write/delete a single teams mapping
        await api_instance.github_write_team_mapping(key, github_mount_path, github_write_team_mapping_request)
    except Exception as e:
        print("Exception when calling AuthApi->github_write_team_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key for the teams mapping | 
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]
 **github_write_team_mapping_request** | [**GithubWriteTeamMappingRequest**](GithubWriteTeamMappingRequest.md)|  | 

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

# **github_write_user_mapping**
> github_write_user_mapping(key, github_mount_path, github_write_user_mapping_request)

Read/write/delete a single users mapping

### Example


```python
import ahvac
from ahvac.models.github_write_user_mapping_request import GithubWriteUserMappingRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    key = 'key_example' # str | Key for the users mapping
    github_mount_path = 'github' # str | Path that the backend was mounted at (default to 'github')
    github_write_user_mapping_request = ahvac.GithubWriteUserMappingRequest() # GithubWriteUserMappingRequest | 

    try:
        # Read/write/delete a single users mapping
        await api_instance.github_write_user_mapping(key, github_mount_path, github_write_user_mapping_request)
    except Exception as e:
        print("Exception when calling AuthApi->github_write_user_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key for the users mapping | 
 **github_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;github&#39;]
 **github_write_user_mapping_request** | [**GithubWriteUserMappingRequest**](GithubWriteUserMappingRequest.md)|  | 

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

# **google_cloud_configure_auth**
> google_cloud_configure_auth(gcp_mount_path, google_cloud_configure_auth_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_configure_auth_request import GoogleCloudConfigureAuthRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_configure_auth_request = ahvac.GoogleCloudConfigureAuthRequest() # GoogleCloudConfigureAuthRequest | 

    try:
        await api_instance.google_cloud_configure_auth(gcp_mount_path, google_cloud_configure_auth_request)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_configure_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_configure_auth_request** | [**GoogleCloudConfigureAuthRequest**](GoogleCloudConfigureAuthRequest.md)|  | 

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

# **google_cloud_delete_role**
> google_cloud_delete_role(name, gcp_mount_path)

Create a GCP role with associated policies and required attributes.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        # Create a GCP role with associated policies and required attributes.
        await api_instance.google_cloud_delete_role(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_delete_role: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_cloud_edit_labels_for_role**
> google_cloud_edit_labels_for_role(name, gcp_mount_path, google_cloud_edit_labels_for_role_request)

Add or remove labels for an existing 'gce' role

### Example


```python
import ahvac
from ahvac.models.google_cloud_edit_labels_for_role_request import GoogleCloudEditLabelsForRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_edit_labels_for_role_request = ahvac.GoogleCloudEditLabelsForRoleRequest() # GoogleCloudEditLabelsForRoleRequest | 

    try:
        # Add or remove labels for an existing 'gce' role
        await api_instance.google_cloud_edit_labels_for_role(name, gcp_mount_path, google_cloud_edit_labels_for_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_edit_labels_for_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_edit_labels_for_role_request** | [**GoogleCloudEditLabelsForRoleRequest**](GoogleCloudEditLabelsForRoleRequest.md)|  | 

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

# **google_cloud_edit_service_accounts_for_role**
> google_cloud_edit_service_accounts_for_role(name, gcp_mount_path, google_cloud_edit_service_accounts_for_role_request)

Add or remove service accounts for an existing `iam` role

### Example


```python
import ahvac
from ahvac.models.google_cloud_edit_service_accounts_for_role_request import GoogleCloudEditServiceAccountsForRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_edit_service_accounts_for_role_request = ahvac.GoogleCloudEditServiceAccountsForRoleRequest() # GoogleCloudEditServiceAccountsForRoleRequest | 

    try:
        # Add or remove service accounts for an existing `iam` role
        await api_instance.google_cloud_edit_service_accounts_for_role(name, gcp_mount_path, google_cloud_edit_service_accounts_for_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_edit_service_accounts_for_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_edit_service_accounts_for_role_request** | [**GoogleCloudEditServiceAccountsForRoleRequest**](GoogleCloudEditServiceAccountsForRoleRequest.md)|  | 

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

# **google_cloud_list_roles**
> StandardListResponse google_cloud_list_roles(gcp_mount_path, list)

Lists all the roles that are registered with Vault.

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
    api_instance = ahvac.AuthApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Lists all the roles that are registered with Vault.
        api_response = await api_instance.google_cloud_list_roles(gcp_mount_path, list)
        print("The response of AuthApi->google_cloud_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_list_roles: %s\n" % e)
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

# **google_cloud_list_roles2**
> StandardListResponse google_cloud_list_roles2(gcp_mount_path, list)

Lists all the roles that are registered with Vault.

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
    api_instance = ahvac.AuthApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Lists all the roles that are registered with Vault.
        api_response = await api_instance.google_cloud_list_roles2(gcp_mount_path, list)
        print("The response of AuthApi->google_cloud_list_roles2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_list_roles2: %s\n" % e)
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

# **google_cloud_login**
> google_cloud_login(gcp_mount_path, google_cloud_login_request)



### Example


```python
import ahvac
from ahvac.models.google_cloud_login_request import GoogleCloudLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_login_request = ahvac.GoogleCloudLoginRequest() # GoogleCloudLoginRequest | 

    try:
        await api_instance.google_cloud_login(gcp_mount_path, google_cloud_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_login_request** | [**GoogleCloudLoginRequest**](GoogleCloudLoginRequest.md)|  | 

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

# **google_cloud_read_auth_configuration**
> google_cloud_read_auth_configuration(gcp_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        await api_instance.google_cloud_read_auth_configuration(gcp_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_read_auth_configuration: %s\n" % e)
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

# **google_cloud_read_role**
> google_cloud_read_role(name, gcp_mount_path)

Create a GCP role with associated policies and required attributes.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')

    try:
        # Create a GCP role with associated policies and required attributes.
        await api_instance.google_cloud_read_role(name, gcp_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_read_role: %s\n" % e)
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

# **google_cloud_write_role**
> google_cloud_write_role(name, gcp_mount_path, google_cloud_write_role_request)

Create a GCP role with associated policies and required attributes.

### Example


```python
import ahvac
from ahvac.models.google_cloud_write_role_request import GoogleCloudWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    gcp_mount_path = 'gcp' # str | Path that the backend was mounted at (default to 'gcp')
    google_cloud_write_role_request = ahvac.GoogleCloudWriteRoleRequest() # GoogleCloudWriteRoleRequest | 

    try:
        # Create a GCP role with associated policies and required attributes.
        await api_instance.google_cloud_write_role(name, gcp_mount_path, google_cloud_write_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->google_cloud_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **gcp_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;gcp&#39;]
 **google_cloud_write_role_request** | [**GoogleCloudWriteRoleRequest**](GoogleCloudWriteRoleRequest.md)|  | 

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

# **jwt_configure**
> jwt_configure(jwt_mount_path, jwt_configure_request)

Configure the JWT authentication backend.

The JWT authentication backend validates JWTs (or OIDC) using the configured credentials. If using OIDC Discovery, the URL must be provided, along with (optionally) the CA cert to use for the connection. If performing JWT validation locally, a set of public keys must be provided.

### Example


```python
import ahvac
from ahvac.models.jwt_configure_request import JwtConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')
    jwt_configure_request = ahvac.JwtConfigureRequest() # JwtConfigureRequest | 

    try:
        # Configure the JWT authentication backend.
        await api_instance.jwt_configure(jwt_mount_path, jwt_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]
 **jwt_configure_request** | [**JwtConfigureRequest**](JwtConfigureRequest.md)|  | 

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

# **jwt_delete_role**
> jwt_delete_role(name, jwt_mount_path)

Delete an existing role.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')

    try:
        # Delete an existing role.
        await api_instance.jwt_delete_role(name, jwt_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]

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

# **jwt_list_roles**
> StandardListResponse jwt_list_roles(jwt_mount_path, list)

Lists all the roles registered with the backend.

The list will contain the names of the roles.

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
    api_instance = ahvac.AuthApi(api_client)
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Lists all the roles registered with the backend.
        api_response = await api_instance.jwt_list_roles(jwt_mount_path, list)
        print("The response of AuthApi->jwt_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]
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

# **jwt_login**
> jwt_login(jwt_mount_path, jwt_login_request)

Authenticates to Vault using a JWT (or OIDC) token.

### Example


```python
import ahvac
from ahvac.models.jwt_login_request import JwtLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')
    jwt_login_request = ahvac.JwtLoginRequest() # JwtLoginRequest | 

    try:
        # Authenticates to Vault using a JWT (or OIDC) token.
        await api_instance.jwt_login(jwt_mount_path, jwt_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]
 **jwt_login_request** | [**JwtLoginRequest**](JwtLoginRequest.md)|  | 

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

# **jwt_oidc_callback**
> jwt_oidc_callback(jwt_mount_path, client_nonce=client_nonce, code=code, state=state)

Callback endpoint to complete an OIDC login.

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
    api_instance = ahvac.AuthApi(api_client)
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')
    client_nonce = 'client_nonce_example' # str |  (optional)
    code = 'code_example' # str |  (optional)
    state = 'state_example' # str |  (optional)

    try:
        # Callback endpoint to complete an OIDC login.
        await api_instance.jwt_oidc_callback(jwt_mount_path, client_nonce=client_nonce, code=code, state=state)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_oidc_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]
 **client_nonce** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 

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

# **jwt_oidc_callback_form_post**
> jwt_oidc_callback_form_post(jwt_mount_path, jwt_oidc_callback_form_post_request)

Callback endpoint to handle form_posts.

### Example


```python
import ahvac
from ahvac.models.jwt_oidc_callback_form_post_request import JwtOidcCallbackFormPostRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')
    jwt_oidc_callback_form_post_request = ahvac.JwtOidcCallbackFormPostRequest() # JwtOidcCallbackFormPostRequest | 

    try:
        # Callback endpoint to handle form_posts.
        await api_instance.jwt_oidc_callback_form_post(jwt_mount_path, jwt_oidc_callback_form_post_request)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_oidc_callback_form_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]
 **jwt_oidc_callback_form_post_request** | [**JwtOidcCallbackFormPostRequest**](JwtOidcCallbackFormPostRequest.md)|  | 

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

# **jwt_oidc_request_authorization_url**
> jwt_oidc_request_authorization_url(jwt_mount_path, jwt_oidc_request_authorization_url_request)

Request an authorization URL to start an OIDC login flow.

### Example


```python
import ahvac
from ahvac.models.jwt_oidc_request_authorization_url_request import JwtOidcRequestAuthorizationUrlRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')
    jwt_oidc_request_authorization_url_request = ahvac.JwtOidcRequestAuthorizationUrlRequest() # JwtOidcRequestAuthorizationUrlRequest | 

    try:
        # Request an authorization URL to start an OIDC login flow.
        await api_instance.jwt_oidc_request_authorization_url(jwt_mount_path, jwt_oidc_request_authorization_url_request)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_oidc_request_authorization_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]
 **jwt_oidc_request_authorization_url_request** | [**JwtOidcRequestAuthorizationUrlRequest**](JwtOidcRequestAuthorizationUrlRequest.md)|  | 

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

# **jwt_read_configuration**
> jwt_read_configuration(jwt_mount_path)

Read the current JWT authentication backend configuration.

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
    api_instance = ahvac.AuthApi(api_client)
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')

    try:
        # Read the current JWT authentication backend configuration.
        await api_instance.jwt_read_configuration(jwt_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]

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

# **jwt_read_role**
> jwt_read_role(name, jwt_mount_path)

Read an existing role.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')

    try:
        # Read an existing role.
        await api_instance.jwt_read_role(name, jwt_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]

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

# **jwt_write_role**
> jwt_write_role(name, jwt_mount_path, jwt_write_role_request)

Register an role with the backend.

A role is required to authenticate with this backend. The role binds   JWT token information with token policies and settings.   The bindings, token polices and token settings can all be configured   using this endpoint

### Example


```python
import ahvac
from ahvac.models.jwt_write_role_request import JwtWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    jwt_mount_path = 'jwt' # str | Path that the backend was mounted at (default to 'jwt')
    jwt_write_role_request = ahvac.JwtWriteRoleRequest() # JwtWriteRoleRequest | 

    try:
        # Register an role with the backend.
        await api_instance.jwt_write_role(name, jwt_mount_path, jwt_write_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->jwt_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **jwt_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;jwt&#39;]
 **jwt_write_role_request** | [**JwtWriteRoleRequest**](JwtWriteRoleRequest.md)|  | 

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

# **kerberos_configure**
> kerberos_configure(kerberos_mount_path, kerberos_configure_request)



### Example


```python
import ahvac
from ahvac.models.kerberos_configure_request import KerberosConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')
    kerberos_configure_request = ahvac.KerberosConfigureRequest() # KerberosConfigureRequest | 

    try:
        await api_instance.kerberos_configure(kerberos_mount_path, kerberos_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]
 **kerberos_configure_request** | [**KerberosConfigureRequest**](KerberosConfigureRequest.md)|  | 

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

# **kerberos_configure_ldap**
> kerberos_configure_ldap(kerberos_mount_path, kerberos_configure_ldap_request)



### Example


```python
import ahvac
from ahvac.models.kerberos_configure_ldap_request import KerberosConfigureLdapRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')
    kerberos_configure_ldap_request = ahvac.KerberosConfigureLdapRequest() # KerberosConfigureLdapRequest | 

    try:
        await api_instance.kerberos_configure_ldap(kerberos_mount_path, kerberos_configure_ldap_request)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_configure_ldap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]
 **kerberos_configure_ldap_request** | [**KerberosConfigureLdapRequest**](KerberosConfigureLdapRequest.md)|  | 

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

# **kerberos_delete_group**
> kerberos_delete_group(name, kerberos_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP group.
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')

    try:
        await api_instance.kerberos_delete_group(name, kerberos_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP group. | 
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]

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

# **kerberos_list_groups**
> StandardListResponse kerberos_list_groups(kerberos_mount_path, list)



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
    api_instance = ahvac.AuthApi(api_client)
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.kerberos_list_groups(kerberos_mount_path, list)
        print("The response of AuthApi->kerberos_list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]
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

# **kerberos_login**
> kerberos_login(kerberos_mount_path, kerberos_login_request)



### Example


```python
import ahvac
from ahvac.models.kerberos_login_request import KerberosLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')
    kerberos_login_request = ahvac.KerberosLoginRequest() # KerberosLoginRequest | 

    try:
        await api_instance.kerberos_login(kerberos_mount_path, kerberos_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]
 **kerberos_login_request** | [**KerberosLoginRequest**](KerberosLoginRequest.md)|  | 

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

# **kerberos_login2**
> kerberos_login2(kerberos_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')

    try:
        await api_instance.kerberos_login2(kerberos_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_login2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]

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

# **kerberos_read_configuration**
> kerberos_read_configuration(kerberos_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')

    try:
        await api_instance.kerberos_read_configuration(kerberos_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]

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

# **kerberos_read_group**
> kerberos_read_group(name, kerberos_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP group.
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')

    try:
        await api_instance.kerberos_read_group(name, kerberos_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_read_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP group. | 
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]

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

# **kerberos_read_ldap_configuration**
> kerberos_read_ldap_configuration(kerberos_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')

    try:
        await api_instance.kerberos_read_ldap_configuration(kerberos_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_read_ldap_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]

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

# **kerberos_write_group**
> kerberos_write_group(name, kerberos_mount_path, kerberos_write_group_request)



### Example


```python
import ahvac
from ahvac.models.kerberos_write_group_request import KerberosWriteGroupRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP group.
    kerberos_mount_path = 'kerberos' # str | Path that the backend was mounted at (default to 'kerberos')
    kerberos_write_group_request = ahvac.KerberosWriteGroupRequest() # KerberosWriteGroupRequest | 

    try:
        await api_instance.kerberos_write_group(name, kerberos_mount_path, kerberos_write_group_request)
    except Exception as e:
        print("Exception when calling AuthApi->kerberos_write_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP group. | 
 **kerberos_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kerberos&#39;]
 **kerberos_write_group_request** | [**KerberosWriteGroupRequest**](KerberosWriteGroupRequest.md)|  | 

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

# **kubernetes_configure_auth**
> kubernetes_configure_auth(kubernetes_mount_path, kubernetes_configure_auth_request)



### Example


```python
import ahvac
from ahvac.models.kubernetes_configure_auth_request import KubernetesConfigureAuthRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    kubernetes_configure_auth_request = ahvac.KubernetesConfigureAuthRequest() # KubernetesConfigureAuthRequest | 

    try:
        await api_instance.kubernetes_configure_auth(kubernetes_mount_path, kubernetes_configure_auth_request)
    except Exception as e:
        print("Exception when calling AuthApi->kubernetes_configure_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]
 **kubernetes_configure_auth_request** | [**KubernetesConfigureAuthRequest**](KubernetesConfigureAuthRequest.md)|  | 

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

# **kubernetes_delete_auth_role**
> kubernetes_delete_auth_role(name, kubernetes_mount_path)

Register an role with the backend.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        # Register an role with the backend.
        await api_instance.kubernetes_delete_auth_role(name, kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kubernetes_delete_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
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

# **kubernetes_list_auth_roles**
> StandardListResponse kubernetes_list_auth_roles(kubernetes_mount_path, list)

Lists all the roles registered with the backend.

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
    api_instance = ahvac.AuthApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Lists all the roles registered with the backend.
        api_response = await api_instance.kubernetes_list_auth_roles(kubernetes_mount_path, list)
        print("The response of AuthApi->kubernetes_list_auth_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->kubernetes_list_auth_roles: %s\n" % e)
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

# **kubernetes_login**
> kubernetes_login(kubernetes_mount_path, kubernetes_login_request)

Authenticates Kubernetes service accounts with Vault.

### Example


```python
import ahvac
from ahvac.models.kubernetes_login_request import KubernetesLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    kubernetes_login_request = ahvac.KubernetesLoginRequest() # KubernetesLoginRequest | 

    try:
        # Authenticates Kubernetes service accounts with Vault.
        await api_instance.kubernetes_login(kubernetes_mount_path, kubernetes_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->kubernetes_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]
 **kubernetes_login_request** | [**KubernetesLoginRequest**](KubernetesLoginRequest.md)|  | 

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

# **kubernetes_read_auth_configuration**
> kubernetes_read_auth_configuration(kubernetes_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        await api_instance.kubernetes_read_auth_configuration(kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kubernetes_read_auth_configuration: %s\n" % e)
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

# **kubernetes_read_auth_role**
> kubernetes_read_auth_role(name, kubernetes_mount_path)

Register an role with the backend.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')

    try:
        # Register an role with the backend.
        await api_instance.kubernetes_read_auth_role(name, kubernetes_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->kubernetes_read_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
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

# **kubernetes_write_auth_role**
> kubernetes_write_auth_role(name, kubernetes_mount_path, kubernetes_write_auth_role_request)

Register an role with the backend.

### Example


```python
import ahvac
from ahvac.models.kubernetes_write_auth_role_request import KubernetesWriteAuthRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the role.
    kubernetes_mount_path = 'kubernetes' # str | Path that the backend was mounted at (default to 'kubernetes')
    kubernetes_write_auth_role_request = ahvac.KubernetesWriteAuthRoleRequest() # KubernetesWriteAuthRoleRequest | 

    try:
        # Register an role with the backend.
        await api_instance.kubernetes_write_auth_role(name, kubernetes_mount_path, kubernetes_write_auth_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->kubernetes_write_auth_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **kubernetes_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;kubernetes&#39;]
 **kubernetes_write_auth_role_request** | [**KubernetesWriteAuthRoleRequest**](KubernetesWriteAuthRoleRequest.md)|  | 

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

# **ldap_configure_auth**
> ldap_configure_auth(ldap_mount_path, ldap_configure_auth_request)



### Example


```python
import ahvac
from ahvac.models.ldap_configure_auth_request import LdapConfigureAuthRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_configure_auth_request = ahvac.LdapConfigureAuthRequest() # LdapConfigureAuthRequest | 

    try:
        await api_instance.ldap_configure_auth(ldap_mount_path, ldap_configure_auth_request)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_configure_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_configure_auth_request** | [**LdapConfigureAuthRequest**](LdapConfigureAuthRequest.md)|  | 

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

# **ldap_delete_group**
> ldap_delete_group(name, ldap_mount_path)

Manage additional groups for users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP group.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        # Manage additional groups for users allowed to authenticate.
        await api_instance.ldap_delete_group(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP group. | 
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

# **ldap_delete_user**
> ldap_delete_user(name, ldap_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP user.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        # Manage users allowed to authenticate.
        await api_instance.ldap_delete_user(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP user. | 
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

# **ldap_list_groups**
> StandardListResponse ldap_list_groups(ldap_mount_path, list)

Manage additional groups for users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage additional groups for users allowed to authenticate.
        api_response = await api_instance.ldap_list_groups(ldap_mount_path, list)
        print("The response of AuthApi->ldap_list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_list_groups: %s\n" % e)
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

# **ldap_list_users**
> StandardListResponse ldap_list_users(ldap_mount_path, list)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage users allowed to authenticate.
        api_response = await api_instance.ldap_list_users(ldap_mount_path, list)
        print("The response of AuthApi->ldap_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_list_users: %s\n" % e)
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

# **ldap_login**
> ldap_login(username, ldap_mount_path, ldap_login_request)

Log in with a username and password.

### Example


```python
import ahvac
from ahvac.models.ldap_login_request import LdapLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | DN (distinguished name) to be used for login.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_login_request = ahvac.LdapLoginRequest() # LdapLoginRequest | 

    try:
        # Log in with a username and password.
        await api_instance.ldap_login(username, ldap_mount_path, ldap_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| DN (distinguished name) to be used for login. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_login_request** | [**LdapLoginRequest**](LdapLoginRequest.md)|  | 

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

# **ldap_read_auth_configuration**
> ldap_read_auth_configuration(ldap_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        await api_instance.ldap_read_auth_configuration(ldap_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_read_auth_configuration: %s\n" % e)
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

# **ldap_read_group**
> ldap_read_group(name, ldap_mount_path)

Manage additional groups for users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP group.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        # Manage additional groups for users allowed to authenticate.
        await api_instance.ldap_read_group(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_read_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP group. | 
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

# **ldap_read_user**
> ldap_read_user(name, ldap_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP user.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')

    try:
        # Manage users allowed to authenticate.
        await api_instance.ldap_read_user(name, ldap_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_read_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP user. | 
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

# **ldap_write_group**
> ldap_write_group(name, ldap_mount_path, ldap_write_group_request)

Manage additional groups for users allowed to authenticate.

### Example


```python
import ahvac
from ahvac.models.ldap_write_group_request import LdapWriteGroupRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP group.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_write_group_request = ahvac.LdapWriteGroupRequest() # LdapWriteGroupRequest | 

    try:
        # Manage additional groups for users allowed to authenticate.
        await api_instance.ldap_write_group(name, ldap_mount_path, ldap_write_group_request)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_write_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP group. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_write_group_request** | [**LdapWriteGroupRequest**](LdapWriteGroupRequest.md)|  | 

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

# **ldap_write_user**
> ldap_write_user(name, ldap_mount_path, ldap_write_user_request)

Manage users allowed to authenticate.

### Example


```python
import ahvac
from ahvac.models.ldap_write_user_request import LdapWriteUserRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the LDAP user.
    ldap_mount_path = 'ldap' # str | Path that the backend was mounted at (default to 'ldap')
    ldap_write_user_request = ahvac.LdapWriteUserRequest() # LdapWriteUserRequest | 

    try:
        # Manage users allowed to authenticate.
        await api_instance.ldap_write_user(name, ldap_mount_path, ldap_write_user_request)
    except Exception as e:
        print("Exception when calling AuthApi->ldap_write_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP user. | 
 **ldap_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;ldap&#39;]
 **ldap_write_user_request** | [**LdapWriteUserRequest**](LdapWriteUserRequest.md)|  | 

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

# **oci_configure**
> oci_configure(oci_mount_path, oci_configure_request)



### Example


```python
import ahvac
from ahvac.models.oci_configure_request import OciConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')
    oci_configure_request = ahvac.OciConfigureRequest() # OciConfigureRequest | 

    try:
        await api_instance.oci_configure(oci_mount_path, oci_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->oci_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]
 **oci_configure_request** | [**OciConfigureRequest**](OciConfigureRequest.md)|  | 

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

# **oci_delete_configuration**
> oci_delete_configuration(oci_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')

    try:
        await api_instance.oci_delete_configuration(oci_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->oci_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]

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

# **oci_delete_role**
> oci_delete_role(role, oci_mount_path)

Create a role and associate policies to it.

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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')

    try:
        # Create a role and associate policies to it.
        await api_instance.oci_delete_role(role, oci_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->oci_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]

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

# **oci_list_roles**
> StandardListResponse oci_list_roles(oci_mount_path, list)

Lists all the roles that are registered with Vault.

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
    api_instance = ahvac.AuthApi(api_client)
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Lists all the roles that are registered with Vault.
        api_response = await api_instance.oci_list_roles(oci_mount_path, list)
        print("The response of AuthApi->oci_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oci_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]
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

# **oci_login**
> oci_login(role, oci_mount_path, oci_login_request)

Authenticates to Vault using OCI credentials

### Example


```python
import ahvac
from ahvac.models.oci_login_request import OciLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')
    oci_login_request = ahvac.OciLoginRequest() # OciLoginRequest | 

    try:
        # Authenticates to Vault using OCI credentials
        await api_instance.oci_login(role, oci_mount_path, oci_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->oci_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]
 **oci_login_request** | [**OciLoginRequest**](OciLoginRequest.md)|  | 

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

# **oci_read_configuration**
> oci_read_configuration(oci_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')

    try:
        await api_instance.oci_read_configuration(oci_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->oci_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]

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

# **oci_read_role**
> oci_read_role(role, oci_mount_path)

Create a role and associate policies to it.

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
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')

    try:
        # Create a role and associate policies to it.
        await api_instance.oci_read_role(role, oci_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->oci_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]

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

# **oci_write_role**
> oci_write_role(role, oci_mount_path, oci_write_role_request)

Create a role and associate policies to it.

### Example


```python
import ahvac
from ahvac.models.oci_write_role_request import OciWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role = 'role_example' # str | Name of the role.
    oci_mount_path = 'oci' # str | Path that the backend was mounted at (default to 'oci')
    oci_write_role_request = ahvac.OciWriteRoleRequest() # OciWriteRoleRequest | 

    try:
        # Create a role and associate policies to it.
        await api_instance.oci_write_role(role, oci_mount_path, oci_write_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->oci_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Name of the role. | 
 **oci_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;oci&#39;]
 **oci_write_role_request** | [**OciWriteRoleRequest**](OciWriteRoleRequest.md)|  | 

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

# **okta_configure**
> okta_configure(okta_mount_path, okta_configure_request)



### Example


```python
import ahvac
from ahvac.models.okta_configure_request import OktaConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')
    okta_configure_request = ahvac.OktaConfigureRequest() # OktaConfigureRequest | 

    try:
        await api_instance.okta_configure(okta_mount_path, okta_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->okta_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]
 **okta_configure_request** | [**OktaConfigureRequest**](OktaConfigureRequest.md)|  | 

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

# **okta_delete_group**
> okta_delete_group(name, okta_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the Okta group.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')

    try:
        # Manage users allowed to authenticate.
        await api_instance.okta_delete_group(name, okta_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->okta_delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Okta group. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]

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

# **okta_delete_user**
> okta_delete_user(name, okta_mount_path)

Manage additional groups for users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the user.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')

    try:
        # Manage additional groups for users allowed to authenticate.
        await api_instance.okta_delete_user(name, okta_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->okta_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the user. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]

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

# **okta_list_groups**
> StandardListResponse okta_list_groups(okta_mount_path, list)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage users allowed to authenticate.
        api_response = await api_instance.okta_list_groups(okta_mount_path, list)
        print("The response of AuthApi->okta_list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->okta_list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]
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

# **okta_list_users**
> StandardListResponse okta_list_users(okta_mount_path, list)

Manage additional groups for users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage additional groups for users allowed to authenticate.
        api_response = await api_instance.okta_list_users(okta_mount_path, list)
        print("The response of AuthApi->okta_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->okta_list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]
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

# **okta_login**
> okta_login(username, okta_mount_path, okta_login_request)

Log in with a username and password.

### Example


```python
import ahvac
from ahvac.models.okta_login_request import OktaLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | Username to be used for login.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')
    okta_login_request = ahvac.OktaLoginRequest() # OktaLoginRequest | 

    try:
        # Log in with a username and password.
        await api_instance.okta_login(username, okta_mount_path, okta_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->okta_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to be used for login. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]
 **okta_login_request** | [**OktaLoginRequest**](OktaLoginRequest.md)|  | 

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

# **okta_read_configuration**
> okta_read_configuration(okta_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')

    try:
        await api_instance.okta_read_configuration(okta_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->okta_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]

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

# **okta_read_group**
> okta_read_group(name, okta_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the Okta group.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')

    try:
        # Manage users allowed to authenticate.
        await api_instance.okta_read_group(name, okta_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->okta_read_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Okta group. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]

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

# **okta_read_user**
> okta_read_user(name, okta_mount_path)

Manage additional groups for users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the user.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')

    try:
        # Manage additional groups for users allowed to authenticate.
        await api_instance.okta_read_user(name, okta_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->okta_read_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the user. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]

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

# **okta_verify**
> okta_verify(nonce, okta_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    nonce = 'nonce_example' # str | Nonce provided during a login request to retrieve the number verification challenge for the matching request.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')

    try:
        await api_instance.okta_verify(nonce, okta_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->okta_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nonce** | **str**| Nonce provided during a login request to retrieve the number verification challenge for the matching request. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]

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

# **okta_write_group**
> okta_write_group(name, okta_mount_path, okta_write_group_request)

Manage users allowed to authenticate.

### Example


```python
import ahvac
from ahvac.models.okta_write_group_request import OktaWriteGroupRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the Okta group.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')
    okta_write_group_request = ahvac.OktaWriteGroupRequest() # OktaWriteGroupRequest | 

    try:
        # Manage users allowed to authenticate.
        await api_instance.okta_write_group(name, okta_mount_path, okta_write_group_request)
    except Exception as e:
        print("Exception when calling AuthApi->okta_write_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Okta group. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]
 **okta_write_group_request** | [**OktaWriteGroupRequest**](OktaWriteGroupRequest.md)|  | 

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

# **okta_write_user**
> okta_write_user(name, okta_mount_path, okta_write_user_request)

Manage additional groups for users allowed to authenticate.

### Example


```python
import ahvac
from ahvac.models.okta_write_user_request import OktaWriteUserRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the user.
    okta_mount_path = 'okta' # str | Path that the backend was mounted at (default to 'okta')
    okta_write_user_request = ahvac.OktaWriteUserRequest() # OktaWriteUserRequest | 

    try:
        # Manage additional groups for users allowed to authenticate.
        await api_instance.okta_write_user(name, okta_mount_path, okta_write_user_request)
    except Exception as e:
        print("Exception when calling AuthApi->okta_write_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the user. | 
 **okta_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;okta&#39;]
 **okta_write_user_request** | [**OktaWriteUserRequest**](OktaWriteUserRequest.md)|  | 

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

# **radius_configure**
> radius_configure(radius_mount_path, radius_configure_request)



### Example


```python
import ahvac
from ahvac.models.radius_configure_request import RadiusConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')
    radius_configure_request = ahvac.RadiusConfigureRequest() # RadiusConfigureRequest | 

    try:
        await api_instance.radius_configure(radius_mount_path, radius_configure_request)
    except Exception as e:
        print("Exception when calling AuthApi->radius_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]
 **radius_configure_request** | [**RadiusConfigureRequest**](RadiusConfigureRequest.md)|  | 

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

# **radius_delete_user**
> radius_delete_user(name, radius_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the RADIUS user.
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')

    try:
        # Manage users allowed to authenticate.
        await api_instance.radius_delete_user(name, radius_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->radius_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the RADIUS user. | 
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]

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

# **radius_list_users**
> StandardListResponse radius_list_users(radius_mount_path, list)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage users allowed to authenticate.
        api_response = await api_instance.radius_list_users(radius_mount_path, list)
        print("The response of AuthApi->radius_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->radius_list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]
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

# **radius_login**
> radius_login(radius_mount_path, radius_login_request)

Log in with a username and password.

### Example


```python
import ahvac
from ahvac.models.radius_login_request import RadiusLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')
    radius_login_request = ahvac.RadiusLoginRequest() # RadiusLoginRequest | 

    try:
        # Log in with a username and password.
        await api_instance.radius_login(radius_mount_path, radius_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->radius_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]
 **radius_login_request** | [**RadiusLoginRequest**](RadiusLoginRequest.md)|  | 

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

# **radius_login_with_username**
> radius_login_with_username(urlusername, radius_mount_path, radius_login_with_username_request)

Log in with a username and password.

### Example


```python
import ahvac
from ahvac.models.radius_login_with_username_request import RadiusLoginWithUsernameRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    urlusername = 'urlusername_example' # str | Username to be used for login. (URL parameter)
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')
    radius_login_with_username_request = ahvac.RadiusLoginWithUsernameRequest() # RadiusLoginWithUsernameRequest | 

    try:
        # Log in with a username and password.
        await api_instance.radius_login_with_username(urlusername, radius_mount_path, radius_login_with_username_request)
    except Exception as e:
        print("Exception when calling AuthApi->radius_login_with_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urlusername** | **str**| Username to be used for login. (URL parameter) | 
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]
 **radius_login_with_username_request** | [**RadiusLoginWithUsernameRequest**](RadiusLoginWithUsernameRequest.md)|  | 

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

# **radius_read_configuration**
> radius_read_configuration(radius_mount_path)



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
    api_instance = ahvac.AuthApi(api_client)
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')

    try:
        await api_instance.radius_read_configuration(radius_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->radius_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]

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

# **radius_read_user**
> radius_read_user(name, radius_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the RADIUS user.
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')

    try:
        # Manage users allowed to authenticate.
        await api_instance.radius_read_user(name, radius_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->radius_read_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the RADIUS user. | 
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]

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

# **radius_write_user**
> radius_write_user(name, radius_mount_path, radius_write_user_request)

Manage users allowed to authenticate.

### Example


```python
import ahvac
from ahvac.models.radius_write_user_request import RadiusWriteUserRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    name = 'name_example' # str | Name of the RADIUS user.
    radius_mount_path = 'radius' # str | Path that the backend was mounted at (default to 'radius')
    radius_write_user_request = ahvac.RadiusWriteUserRequest() # RadiusWriteUserRequest | 

    try:
        # Manage users allowed to authenticate.
        await api_instance.radius_write_user(name, radius_mount_path, radius_write_user_request)
    except Exception as e:
        print("Exception when calling AuthApi->radius_write_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the RADIUS user. | 
 **radius_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;radius&#39;]
 **radius_write_user_request** | [**RadiusWriteUserRequest**](RadiusWriteUserRequest.md)|  | 

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

# **token_create**
> token_create(token_create_request)

The token create path is used to create new tokens.

### Example


```python
import ahvac
from ahvac.models.token_create_request import TokenCreateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_create_request = ahvac.TokenCreateRequest() # TokenCreateRequest | 

    try:
        # The token create path is used to create new tokens.
        await api_instance.token_create(token_create_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_create_request** | [**TokenCreateRequest**](TokenCreateRequest.md)|  | 

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

# **token_create_against_role**
> token_create_against_role(role_name, token_create_against_role_request)

This token create path is used to create new tokens adhering to the given role.

### Example


```python
import ahvac
from ahvac.models.token_create_against_role_request import TokenCreateAgainstRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role
    token_create_against_role_request = ahvac.TokenCreateAgainstRoleRequest() # TokenCreateAgainstRoleRequest | 

    try:
        # This token create path is used to create new tokens adhering to the given role.
        await api_instance.token_create_against_role(role_name, token_create_against_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_create_against_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 
 **token_create_against_role_request** | [**TokenCreateAgainstRoleRequest**](TokenCreateAgainstRoleRequest.md)|  | 

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

# **token_create_orphan**
> token_create_orphan(token_create_orphan_request)

The token create path is used to create new orphan tokens.

### Example


```python
import ahvac
from ahvac.models.token_create_orphan_request import TokenCreateOrphanRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_create_orphan_request = ahvac.TokenCreateOrphanRequest() # TokenCreateOrphanRequest | 

    try:
        # The token create path is used to create new orphan tokens.
        await api_instance.token_create_orphan(token_create_orphan_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_create_orphan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_create_orphan_request** | [**TokenCreateOrphanRequest**](TokenCreateOrphanRequest.md)|  | 

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

# **token_delete_role**
> token_delete_role(role_name)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role

    try:
        await api_instance.token_delete_role(role_name)
    except Exception as e:
        print("Exception when calling AuthApi->token_delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 

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

# **token_list_accessors**
> StandardListResponse token_list_accessors(list)

List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires 'sudo' capability in addition to 'list'.

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
    api_instance = ahvac.AuthApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires 'sudo' capability in addition to 'list'.
        api_response = await api_instance.token_list_accessors(list)
        print("The response of AuthApi->token_list_accessors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->token_list_accessors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **token_list_roles**
> StandardListResponse token_list_roles(list)

This endpoint lists configured roles.

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
    api_instance = ahvac.AuthApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # This endpoint lists configured roles.
        api_response = await api_instance.token_list_roles(list)
        print("The response of AuthApi->token_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->token_list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **token_look_up**
> token_look_up(token_look_up_request)



### Example


```python
import ahvac
from ahvac.models.token_look_up_request import TokenLookUpRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_look_up_request = ahvac.TokenLookUpRequest() # TokenLookUpRequest | 

    try:
        await api_instance.token_look_up(token_look_up_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_look_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_look_up_request** | [**TokenLookUpRequest**](TokenLookUpRequest.md)|  | 

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

# **token_look_up2**
> token_look_up2(token=token)



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
    api_instance = ahvac.AuthApi(api_client)
    token = 'token_example' # str | Token to lookup (optional)

    try:
        await api_instance.token_look_up2(token=token)
    except Exception as e:
        print("Exception when calling AuthApi->token_look_up2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token to lookup | [optional] 

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

# **token_look_up_accessor**
> token_look_up_accessor(token_look_up_accessor_request)

This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.

### Example


```python
import ahvac
from ahvac.models.token_look_up_accessor_request import TokenLookUpAccessorRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_look_up_accessor_request = ahvac.TokenLookUpAccessorRequest() # TokenLookUpAccessorRequest | 

    try:
        # This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.
        await api_instance.token_look_up_accessor(token_look_up_accessor_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_look_up_accessor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_look_up_accessor_request** | [**TokenLookUpAccessorRequest**](TokenLookUpAccessorRequest.md)|  | 

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

# **token_look_up_self**
> token_look_up_self()



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
    api_instance = ahvac.AuthApi(api_client)

    try:
        await api_instance.token_look_up_self()
    except Exception as e:
        print("Exception when calling AuthApi->token_look_up_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **token_look_up_self2**
> token_look_up_self2(token_look_up_self2_request)



### Example


```python
import ahvac
from ahvac.models.token_look_up_self2_request import TokenLookUpSelf2Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_look_up_self2_request = ahvac.TokenLookUpSelf2Request() # TokenLookUpSelf2Request | 

    try:
        await api_instance.token_look_up_self2(token_look_up_self2_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_look_up_self2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_look_up_self2_request** | [**TokenLookUpSelf2Request**](TokenLookUpSelf2Request.md)|  | 

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

# **token_read_role**
> token_read_role(role_name)



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
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role

    try:
        await api_instance.token_read_role(role_name)
    except Exception as e:
        print("Exception when calling AuthApi->token_read_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 

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

# **token_renew**
> token_renew(token_renew_request)

This endpoint will renew the given token and prevent expiration.

### Example


```python
import ahvac
from ahvac.models.token_renew_request import TokenRenewRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_renew_request = ahvac.TokenRenewRequest() # TokenRenewRequest | 

    try:
        # This endpoint will renew the given token and prevent expiration.
        await api_instance.token_renew(token_renew_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_renew: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_renew_request** | [**TokenRenewRequest**](TokenRenewRequest.md)|  | 

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

# **token_renew_accessor**
> token_renew_accessor(token_renew_accessor_request)

This endpoint will renew a token associated with the given accessor and its properties. Response will not contain the token ID.

### Example


```python
import ahvac
from ahvac.models.token_renew_accessor_request import TokenRenewAccessorRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_renew_accessor_request = ahvac.TokenRenewAccessorRequest() # TokenRenewAccessorRequest | 

    try:
        # This endpoint will renew a token associated with the given accessor and its properties. Response will not contain the token ID.
        await api_instance.token_renew_accessor(token_renew_accessor_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_renew_accessor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_renew_accessor_request** | [**TokenRenewAccessorRequest**](TokenRenewAccessorRequest.md)|  | 

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

# **token_renew_self**
> token_renew_self(token_renew_self_request)

This endpoint will renew the token used to call it and prevent expiration.

### Example


```python
import ahvac
from ahvac.models.token_renew_self_request import TokenRenewSelfRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_renew_self_request = ahvac.TokenRenewSelfRequest() # TokenRenewSelfRequest | 

    try:
        # This endpoint will renew the token used to call it and prevent expiration.
        await api_instance.token_renew_self(token_renew_self_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_renew_self: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_renew_self_request** | [**TokenRenewSelfRequest**](TokenRenewSelfRequest.md)|  | 

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

# **token_revoke**
> token_revoke(token_revoke_request)

This endpoint will delete the given token and all of its child tokens.

### Example


```python
import ahvac
from ahvac.models.token_revoke_request import TokenRevokeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_revoke_request = ahvac.TokenRevokeRequest() # TokenRevokeRequest | 

    try:
        # This endpoint will delete the given token and all of its child tokens.
        await api_instance.token_revoke(token_revoke_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_revoke_request** | [**TokenRevokeRequest**](TokenRevokeRequest.md)|  | 

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

# **token_revoke_accessor**
> token_revoke_accessor(token_revoke_accessor_request)

This endpoint will delete the token associated with the accessor and all of its child tokens.

### Example


```python
import ahvac
from ahvac.models.token_revoke_accessor_request import TokenRevokeAccessorRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_revoke_accessor_request = ahvac.TokenRevokeAccessorRequest() # TokenRevokeAccessorRequest | 

    try:
        # This endpoint will delete the token associated with the accessor and all of its child tokens.
        await api_instance.token_revoke_accessor(token_revoke_accessor_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_revoke_accessor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_revoke_accessor_request** | [**TokenRevokeAccessorRequest**](TokenRevokeAccessorRequest.md)|  | 

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

# **token_revoke_orphan**
> token_revoke_orphan(token_revoke_orphan_request)

This endpoint will delete the token and orphan its child tokens.

### Example


```python
import ahvac
from ahvac.models.token_revoke_orphan_request import TokenRevokeOrphanRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    token_revoke_orphan_request = ahvac.TokenRevokeOrphanRequest() # TokenRevokeOrphanRequest | 

    try:
        # This endpoint will delete the token and orphan its child tokens.
        await api_instance.token_revoke_orphan(token_revoke_orphan_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_revoke_orphan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_revoke_orphan_request** | [**TokenRevokeOrphanRequest**](TokenRevokeOrphanRequest.md)|  | 

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

# **token_revoke_self**
> token_revoke_self()

This endpoint will delete the token used to call it and all of its child tokens.

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
    api_instance = ahvac.AuthApi(api_client)

    try:
        # This endpoint will delete the token used to call it and all of its child tokens.
        await api_instance.token_revoke_self()
    except Exception as e:
        print("Exception when calling AuthApi->token_revoke_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **token_tidy**
> token_tidy()

This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.

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
    api_instance = ahvac.AuthApi(api_client)

    try:
        # This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.
        await api_instance.token_tidy()
    except Exception as e:
        print("Exception when calling AuthApi->token_tidy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **token_write_role**
> token_write_role(role_name, token_write_role_request)



### Example


```python
import ahvac
from ahvac.models.token_write_role_request import TokenWriteRoleRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    role_name = 'role_name_example' # str | Name of the role
    token_write_role_request = ahvac.TokenWriteRoleRequest() # TokenWriteRoleRequest | 

    try:
        await api_instance.token_write_role(role_name, token_write_role_request)
    except Exception as e:
        print("Exception when calling AuthApi->token_write_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 
 **token_write_role_request** | [**TokenWriteRoleRequest**](TokenWriteRoleRequest.md)|  | 

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

# **userpass_delete_user**
> userpass_delete_user(username, userpass_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | Username for this user.
    userpass_mount_path = 'userpass' # str | Path that the backend was mounted at (default to 'userpass')

    try:
        # Manage users allowed to authenticate.
        await api_instance.userpass_delete_user(username, userpass_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->userpass_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for this user. | 
 **userpass_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;userpass&#39;]

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

# **userpass_list_users**
> StandardListResponse userpass_list_users(userpass_mount_path, list)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    userpass_mount_path = 'userpass' # str | Path that the backend was mounted at (default to 'userpass')
    list = 'list_example' # str | Must be set to `true`

    try:
        # Manage users allowed to authenticate.
        api_response = await api_instance.userpass_list_users(userpass_mount_path, list)
        print("The response of AuthApi->userpass_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->userpass_list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userpass_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;userpass&#39;]
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

# **userpass_login**
> userpass_login(username, userpass_mount_path, userpass_login_request)

Log in with a username and password.

### Example


```python
import ahvac
from ahvac.models.userpass_login_request import UserpassLoginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | Username of the user.
    userpass_mount_path = 'userpass' # str | Path that the backend was mounted at (default to 'userpass')
    userpass_login_request = ahvac.UserpassLoginRequest() # UserpassLoginRequest | 

    try:
        # Log in with a username and password.
        await api_instance.userpass_login(username, userpass_mount_path, userpass_login_request)
    except Exception as e:
        print("Exception when calling AuthApi->userpass_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the user. | 
 **userpass_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;userpass&#39;]
 **userpass_login_request** | [**UserpassLoginRequest**](UserpassLoginRequest.md)|  | 

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

# **userpass_read_user**
> userpass_read_user(username, userpass_mount_path)

Manage users allowed to authenticate.

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
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | Username for this user.
    userpass_mount_path = 'userpass' # str | Path that the backend was mounted at (default to 'userpass')

    try:
        # Manage users allowed to authenticate.
        await api_instance.userpass_read_user(username, userpass_mount_path)
    except Exception as e:
        print("Exception when calling AuthApi->userpass_read_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for this user. | 
 **userpass_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;userpass&#39;]

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

# **userpass_reset_password**
> userpass_reset_password(username, userpass_mount_path, userpass_reset_password_request)

Reset user's password.

### Example


```python
import ahvac
from ahvac.models.userpass_reset_password_request import UserpassResetPasswordRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | Username for this user.
    userpass_mount_path = 'userpass' # str | Path that the backend was mounted at (default to 'userpass')
    userpass_reset_password_request = ahvac.UserpassResetPasswordRequest() # UserpassResetPasswordRequest | 

    try:
        # Reset user's password.
        await api_instance.userpass_reset_password(username, userpass_mount_path, userpass_reset_password_request)
    except Exception as e:
        print("Exception when calling AuthApi->userpass_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for this user. | 
 **userpass_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;userpass&#39;]
 **userpass_reset_password_request** | [**UserpassResetPasswordRequest**](UserpassResetPasswordRequest.md)|  | 

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

# **userpass_update_policies**
> userpass_update_policies(username, userpass_mount_path, userpass_update_policies_request)

Update the policies associated with the username.

### Example


```python
import ahvac
from ahvac.models.userpass_update_policies_request import UserpassUpdatePoliciesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | Username for this user.
    userpass_mount_path = 'userpass' # str | Path that the backend was mounted at (default to 'userpass')
    userpass_update_policies_request = ahvac.UserpassUpdatePoliciesRequest() # UserpassUpdatePoliciesRequest | 

    try:
        # Update the policies associated with the username.
        await api_instance.userpass_update_policies(username, userpass_mount_path, userpass_update_policies_request)
    except Exception as e:
        print("Exception when calling AuthApi->userpass_update_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for this user. | 
 **userpass_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;userpass&#39;]
 **userpass_update_policies_request** | [**UserpassUpdatePoliciesRequest**](UserpassUpdatePoliciesRequest.md)|  | 

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

# **userpass_write_user**
> userpass_write_user(username, userpass_mount_path, userpass_write_user_request)

Manage users allowed to authenticate.

### Example


```python
import ahvac
from ahvac.models.userpass_write_user_request import UserpassWriteUserRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.AuthApi(api_client)
    username = 'username_example' # str | Username for this user.
    userpass_mount_path = 'userpass' # str | Path that the backend was mounted at (default to 'userpass')
    userpass_write_user_request = ahvac.UserpassWriteUserRequest() # UserpassWriteUserRequest | 

    try:
        # Manage users allowed to authenticate.
        await api_instance.userpass_write_user(username, userpass_mount_path, userpass_write_user_request)
    except Exception as e:
        print("Exception when calling AuthApi->userpass_write_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for this user. | 
 **userpass_mount_path** | **str**| Path that the backend was mounted at | [default to &#39;userpass&#39;]
 **userpass_write_user_request** | [**UserpassWriteUserRequest**](UserpassWriteUserRequest.md)|  | 

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

