# ahvac.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auditing_calculate_hash**](SystemApi.md#auditing_calculate_hash) | **POST** /sys/audit-hash/{path} | 
[**auditing_disable_device**](SystemApi.md#auditing_disable_device) | **DELETE** /sys/audit/{path} | Disable the audit device at the given path.
[**auditing_disable_request_header**](SystemApi.md#auditing_disable_request_header) | **DELETE** /sys/config/auditing/request-headers/{header} | Disable auditing of the given request header.
[**auditing_enable_device**](SystemApi.md#auditing_enable_device) | **POST** /sys/audit/{path} | Enable a new audit device at the supplied path.
[**auditing_enable_request_header**](SystemApi.md#auditing_enable_request_header) | **POST** /sys/config/auditing/request-headers/{header} | Enable auditing of a header.
[**auditing_list_enabled_devices**](SystemApi.md#auditing_list_enabled_devices) | **GET** /sys/audit | List the enabled audit devices.
[**auditing_list_request_headers**](SystemApi.md#auditing_list_request_headers) | **GET** /sys/config/auditing/request-headers | List the request headers that are configured to be audited.
[**auditing_read_request_header_information**](SystemApi.md#auditing_read_request_header_information) | **GET** /sys/config/auditing/request-headers/{header} | List the information for the given request header.
[**auth_disable_method**](SystemApi.md#auth_disable_method) | **DELETE** /sys/auth/{path} | Disable the auth method at the given auth path
[**auth_enable_method**](SystemApi.md#auth_enable_method) | **POST** /sys/auth/{path} | Enables a new auth method.
[**auth_list_enabled_methods**](SystemApi.md#auth_list_enabled_methods) | **GET** /sys/auth | 
[**auth_read_configuration**](SystemApi.md#auth_read_configuration) | **GET** /sys/auth/{path} | Read the configuration of the auth engine at the given path.
[**auth_read_tuning_information**](SystemApi.md#auth_read_tuning_information) | **GET** /sys/auth/{path}/tune | Reads the given auth path&#39;s configuration.
[**auth_tune_configuration_parameters**](SystemApi.md#auth_tune_configuration_parameters) | **POST** /sys/auth/{path}/tune | Tune configuration parameters for a given auth path.
[**collect_host_information**](SystemApi.md#collect_host_information) | **GET** /sys/host-info | Information about the host instance that this Vault server is running on.
[**collect_in_flight_request_information**](SystemApi.md#collect_in_flight_request_information) | **GET** /sys/in-flight-req | reports in-flight requests
[**cors_configure**](SystemApi.md#cors_configure) | **POST** /sys/config/cors | Configure the CORS settings.
[**cors_delete_configuration**](SystemApi.md#cors_delete_configuration) | **DELETE** /sys/config/cors | Remove any CORS settings.
[**cors_read_configuration**](SystemApi.md#cors_read_configuration) | **GET** /sys/config/cors | Return the current CORS settings.
[**decode**](SystemApi.md#decode) | **POST** /sys/decode-token | Decodes the encoded token with the otp.
[**encryption_key_configure_rotation**](SystemApi.md#encryption_key_configure_rotation) | **POST** /sys/rotate/config | 
[**encryption_key_read_rotation_configuration**](SystemApi.md#encryption_key_read_rotation_configuration) | **GET** /sys/rotate/config | 
[**encryption_key_rotate**](SystemApi.md#encryption_key_rotate) | **POST** /sys/rotate | 
[**encryption_key_status**](SystemApi.md#encryption_key_status) | **GET** /sys/key-status | Provides information about the backend encryption key.
[**enterprise_stub_delete_config_control_group**](SystemApi.md#enterprise_stub_delete_config_control_group) | **DELETE** /sys/config/control-group | 
[**enterprise_stub_delete_managed_keys_type_name**](SystemApi.md#enterprise_stub_delete_managed_keys_type_name) | **DELETE** /sys/managed-keys/{type}/{name} | 
[**enterprise_stub_delete_mfa_method_duo_name**](SystemApi.md#enterprise_stub_delete_mfa_method_duo_name) | **DELETE** /sys/mfa/method/duo/{name} | 
[**enterprise_stub_delete_mfa_method_okta_name**](SystemApi.md#enterprise_stub_delete_mfa_method_okta_name) | **DELETE** /sys/mfa/method/okta/{name} | 
[**enterprise_stub_delete_mfa_method_pingid_name**](SystemApi.md#enterprise_stub_delete_mfa_method_pingid_name) | **DELETE** /sys/mfa/method/pingid/{name} | 
[**enterprise_stub_delete_mfa_method_totp_name**](SystemApi.md#enterprise_stub_delete_mfa_method_totp_name) | **DELETE** /sys/mfa/method/totp/{name} | 
[**enterprise_stub_delete_namespaces_path**](SystemApi.md#enterprise_stub_delete_namespaces_path) | **DELETE** /sys/namespaces/{path} | 
[**enterprise_stub_delete_policies_egp_name**](SystemApi.md#enterprise_stub_delete_policies_egp_name) | **DELETE** /sys/policies/egp/{name} | 
[**enterprise_stub_delete_policies_rgp_name**](SystemApi.md#enterprise_stub_delete_policies_rgp_name) | **DELETE** /sys/policies/rgp/{name} | 
[**enterprise_stub_delete_quotas_lease_count_name**](SystemApi.md#enterprise_stub_delete_quotas_lease_count_name) | **DELETE** /sys/quotas/lease-count/{name} | 
[**enterprise_stub_delete_replication_performance_primary_paths_filter_id**](SystemApi.md#enterprise_stub_delete_replication_performance_primary_paths_filter_id) | **DELETE** /sys/replication/performance/primary/paths-filter/{id} | 
[**enterprise_stub_delete_storage_raft_snapshot_auto_config_name**](SystemApi.md#enterprise_stub_delete_storage_raft_snapshot_auto_config_name) | **DELETE** /sys/storage/raft/snapshot-auto/config/{name} | 
[**enterprise_stub_list_managed_keys_type**](SystemApi.md#enterprise_stub_list_managed_keys_type) | **GET** /sys/managed-keys/{type}/ | 
[**enterprise_stub_list_mfa_method**](SystemApi.md#enterprise_stub_list_mfa_method) | **GET** /sys/mfa/method/ | 
[**enterprise_stub_list_namespaces**](SystemApi.md#enterprise_stub_list_namespaces) | **GET** /sys/namespaces/ | 
[**enterprise_stub_list_policies_egp**](SystemApi.md#enterprise_stub_list_policies_egp) | **GET** /sys/policies/egp/ | 
[**enterprise_stub_list_policies_rgp**](SystemApi.md#enterprise_stub_list_policies_rgp) | **GET** /sys/policies/rgp/ | 
[**enterprise_stub_list_quotas_lease_count**](SystemApi.md#enterprise_stub_list_quotas_lease_count) | **GET** /sys/quotas/lease-count/ | 
[**enterprise_stub_list_storage_raft_snapshot_auto_config**](SystemApi.md#enterprise_stub_list_storage_raft_snapshot_auto_config) | **GET** /sys/storage/raft/snapshot-auto/config/ | 
[**enterprise_stub_read_config_control_group**](SystemApi.md#enterprise_stub_read_config_control_group) | **GET** /sys/config/control-group | 
[**enterprise_stub_read_config_group_policy_application**](SystemApi.md#enterprise_stub_read_config_group_policy_application) | **GET** /sys/config/group-policy-application | 
[**enterprise_stub_read_license_status**](SystemApi.md#enterprise_stub_read_license_status) | **GET** /sys/license/status | 
[**enterprise_stub_read_managed_keys_type_name**](SystemApi.md#enterprise_stub_read_managed_keys_type_name) | **GET** /sys/managed-keys/{type}/{name} | 
[**enterprise_stub_read_mfa_method_duo_name**](SystemApi.md#enterprise_stub_read_mfa_method_duo_name) | **GET** /sys/mfa/method/duo/{name} | 
[**enterprise_stub_read_mfa_method_okta_name**](SystemApi.md#enterprise_stub_read_mfa_method_okta_name) | **GET** /sys/mfa/method/okta/{name} | 
[**enterprise_stub_read_mfa_method_pingid_name**](SystemApi.md#enterprise_stub_read_mfa_method_pingid_name) | **GET** /sys/mfa/method/pingid/{name} | 
[**enterprise_stub_read_mfa_method_totp_name**](SystemApi.md#enterprise_stub_read_mfa_method_totp_name) | **GET** /sys/mfa/method/totp/{name} | 
[**enterprise_stub_read_mfa_method_totp_name_generate**](SystemApi.md#enterprise_stub_read_mfa_method_totp_name_generate) | **GET** /sys/mfa/method/totp/{name}/generate | 
[**enterprise_stub_read_namespaces_path**](SystemApi.md#enterprise_stub_read_namespaces_path) | **GET** /sys/namespaces/{path} | 
[**enterprise_stub_read_plugins_reload_backend_status**](SystemApi.md#enterprise_stub_read_plugins_reload_backend_status) | **GET** /sys/plugins/reload/backend/status | 
[**enterprise_stub_read_policies_egp_name**](SystemApi.md#enterprise_stub_read_policies_egp_name) | **GET** /sys/policies/egp/{name} | 
[**enterprise_stub_read_policies_rgp_name**](SystemApi.md#enterprise_stub_read_policies_rgp_name) | **GET** /sys/policies/rgp/{name} | 
[**enterprise_stub_read_quotas_lease_count_name**](SystemApi.md#enterprise_stub_read_quotas_lease_count_name) | **GET** /sys/quotas/lease-count/{name} | 
[**enterprise_stub_read_replication_dr_secondary_license_status**](SystemApi.md#enterprise_stub_read_replication_dr_secondary_license_status) | **GET** /sys/replication/dr/secondary/license/status | 
[**enterprise_stub_read_replication_dr_status**](SystemApi.md#enterprise_stub_read_replication_dr_status) | **GET** /sys/replication/dr/status | 
[**enterprise_stub_read_replication_performance_primary_dynamic_filter_id**](SystemApi.md#enterprise_stub_read_replication_performance_primary_dynamic_filter_id) | **GET** /sys/replication/performance/primary/dynamic-filter/{id} | 
[**enterprise_stub_read_replication_performance_primary_paths_filter_id**](SystemApi.md#enterprise_stub_read_replication_performance_primary_paths_filter_id) | **GET** /sys/replication/performance/primary/paths-filter/{id} | 
[**enterprise_stub_read_replication_performance_secondary_dynamic_filter_id**](SystemApi.md#enterprise_stub_read_replication_performance_secondary_dynamic_filter_id) | **GET** /sys/replication/performance/secondary/dynamic-filter/{id} | 
[**enterprise_stub_read_replication_performance_status**](SystemApi.md#enterprise_stub_read_replication_performance_status) | **GET** /sys/replication/performance/status | 
[**enterprise_stub_read_sealwrap_rewrap**](SystemApi.md#enterprise_stub_read_sealwrap_rewrap) | **GET** /sys/sealwrap/rewrap | 
[**enterprise_stub_read_storage_raft_snapshot_auto_config_name**](SystemApi.md#enterprise_stub_read_storage_raft_snapshot_auto_config_name) | **GET** /sys/storage/raft/snapshot-auto/config/{name} | 
[**enterprise_stub_read_storage_raft_snapshot_auto_status_name**](SystemApi.md#enterprise_stub_read_storage_raft_snapshot_auto_status_name) | **GET** /sys/storage/raft/snapshot-auto/status/{name} | 
[**enterprise_stub_write_config_control_group**](SystemApi.md#enterprise_stub_write_config_control_group) | **POST** /sys/config/control-group | 
[**enterprise_stub_write_config_group_policy_application**](SystemApi.md#enterprise_stub_write_config_group_policy_application) | **POST** /sys/config/group-policy-application | 
[**enterprise_stub_write_control_group_authorize**](SystemApi.md#enterprise_stub_write_control_group_authorize) | **POST** /sys/control-group/authorize | 
[**enterprise_stub_write_control_group_request**](SystemApi.md#enterprise_stub_write_control_group_request) | **POST** /sys/control-group/request | 
[**enterprise_stub_write_managed_keys_type_name**](SystemApi.md#enterprise_stub_write_managed_keys_type_name) | **POST** /sys/managed-keys/{type}/{name} | 
[**enterprise_stub_write_managed_keys_type_name_test_sign**](SystemApi.md#enterprise_stub_write_managed_keys_type_name_test_sign) | **POST** /sys/managed-keys/{type}/{name}/test/sign | 
[**enterprise_stub_write_mfa_method_duo_name**](SystemApi.md#enterprise_stub_write_mfa_method_duo_name) | **POST** /sys/mfa/method/duo/{name} | 
[**enterprise_stub_write_mfa_method_okta_name**](SystemApi.md#enterprise_stub_write_mfa_method_okta_name) | **POST** /sys/mfa/method/okta/{name} | 
[**enterprise_stub_write_mfa_method_pingid_name**](SystemApi.md#enterprise_stub_write_mfa_method_pingid_name) | **POST** /sys/mfa/method/pingid/{name} | 
[**enterprise_stub_write_mfa_method_totp_name**](SystemApi.md#enterprise_stub_write_mfa_method_totp_name) | **POST** /sys/mfa/method/totp/{name} | 
[**enterprise_stub_write_mfa_method_totp_name_admin_destroy**](SystemApi.md#enterprise_stub_write_mfa_method_totp_name_admin_destroy) | **POST** /sys/mfa/method/totp/{name}/admin-destroy | 
[**enterprise_stub_write_mfa_method_totp_name_admin_generate**](SystemApi.md#enterprise_stub_write_mfa_method_totp_name_admin_generate) | **POST** /sys/mfa/method/totp/{name}/admin-generate | 
[**enterprise_stub_write_namespaces_api_lock_lock**](SystemApi.md#enterprise_stub_write_namespaces_api_lock_lock) | **POST** /sys/namespaces/api-lock/lock | 
[**enterprise_stub_write_namespaces_api_lock_lock_path**](SystemApi.md#enterprise_stub_write_namespaces_api_lock_lock_path) | **POST** /sys/namespaces/api-lock/lock/{path} | 
[**enterprise_stub_write_namespaces_api_lock_unlock**](SystemApi.md#enterprise_stub_write_namespaces_api_lock_unlock) | **POST** /sys/namespaces/api-lock/unlock | 
[**enterprise_stub_write_namespaces_api_lock_unlock_path**](SystemApi.md#enterprise_stub_write_namespaces_api_lock_unlock_path) | **POST** /sys/namespaces/api-lock/unlock/{path} | 
[**enterprise_stub_write_namespaces_path**](SystemApi.md#enterprise_stub_write_namespaces_path) | **POST** /sys/namespaces/{path} | 
[**enterprise_stub_write_policies_egp_name**](SystemApi.md#enterprise_stub_write_policies_egp_name) | **POST** /sys/policies/egp/{name} | 
[**enterprise_stub_write_policies_rgp_name**](SystemApi.md#enterprise_stub_write_policies_rgp_name) | **POST** /sys/policies/rgp/{name} | 
[**enterprise_stub_write_quotas_lease_count_name**](SystemApi.md#enterprise_stub_write_quotas_lease_count_name) | **POST** /sys/quotas/lease-count/{name} | 
[**enterprise_stub_write_replication_dr_primary_demote**](SystemApi.md#enterprise_stub_write_replication_dr_primary_demote) | **POST** /sys/replication/dr/primary/demote | 
[**enterprise_stub_write_replication_dr_primary_disable**](SystemApi.md#enterprise_stub_write_replication_dr_primary_disable) | **POST** /sys/replication/dr/primary/disable | 
[**enterprise_stub_write_replication_dr_primary_enable**](SystemApi.md#enterprise_stub_write_replication_dr_primary_enable) | **POST** /sys/replication/dr/primary/enable | 
[**enterprise_stub_write_replication_dr_primary_revoke_secondary**](SystemApi.md#enterprise_stub_write_replication_dr_primary_revoke_secondary) | **POST** /sys/replication/dr/primary/revoke-secondary | 
[**enterprise_stub_write_replication_dr_primary_secondary_token**](SystemApi.md#enterprise_stub_write_replication_dr_primary_secondary_token) | **POST** /sys/replication/dr/primary/secondary-token | 
[**enterprise_stub_write_replication_dr_secondary_config_reload_subsystem**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_config_reload_subsystem) | **POST** /sys/replication/dr/secondary/config/reload/{subsystem} | 
[**enterprise_stub_write_replication_dr_secondary_disable**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_disable) | **POST** /sys/replication/dr/secondary/disable | 
[**enterprise_stub_write_replication_dr_secondary_enable**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_enable) | **POST** /sys/replication/dr/secondary/enable | 
[**enterprise_stub_write_replication_dr_secondary_generate_public_key**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_generate_public_key) | **POST** /sys/replication/dr/secondary/generate-public-key | 
[**enterprise_stub_write_replication_dr_secondary_operation_token_delete**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_operation_token_delete) | **POST** /sys/replication/dr/secondary/operation-token/delete | 
[**enterprise_stub_write_replication_dr_secondary_promote**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_promote) | **POST** /sys/replication/dr/secondary/promote | 
[**enterprise_stub_write_replication_dr_secondary_recover**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_recover) | **POST** /sys/replication/dr/secondary/recover | 
[**enterprise_stub_write_replication_dr_secondary_reindex**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_reindex) | **POST** /sys/replication/dr/secondary/reindex | 
[**enterprise_stub_write_replication_dr_secondary_update_primary**](SystemApi.md#enterprise_stub_write_replication_dr_secondary_update_primary) | **POST** /sys/replication/dr/secondary/update-primary | 
[**enterprise_stub_write_replication_performance_primary_demote**](SystemApi.md#enterprise_stub_write_replication_performance_primary_demote) | **POST** /sys/replication/performance/primary/demote | 
[**enterprise_stub_write_replication_performance_primary_disable**](SystemApi.md#enterprise_stub_write_replication_performance_primary_disable) | **POST** /sys/replication/performance/primary/disable | 
[**enterprise_stub_write_replication_performance_primary_enable**](SystemApi.md#enterprise_stub_write_replication_performance_primary_enable) | **POST** /sys/replication/performance/primary/enable | 
[**enterprise_stub_write_replication_performance_primary_paths_filter_id**](SystemApi.md#enterprise_stub_write_replication_performance_primary_paths_filter_id) | **POST** /sys/replication/performance/primary/paths-filter/{id} | 
[**enterprise_stub_write_replication_performance_primary_revoke_secondary**](SystemApi.md#enterprise_stub_write_replication_performance_primary_revoke_secondary) | **POST** /sys/replication/performance/primary/revoke-secondary | 
[**enterprise_stub_write_replication_performance_primary_secondary_token**](SystemApi.md#enterprise_stub_write_replication_performance_primary_secondary_token) | **POST** /sys/replication/performance/primary/secondary-token | 
[**enterprise_stub_write_replication_performance_secondary_disable**](SystemApi.md#enterprise_stub_write_replication_performance_secondary_disable) | **POST** /sys/replication/performance/secondary/disable | 
[**enterprise_stub_write_replication_performance_secondary_enable**](SystemApi.md#enterprise_stub_write_replication_performance_secondary_enable) | **POST** /sys/replication/performance/secondary/enable | 
[**enterprise_stub_write_replication_performance_secondary_generate_public_key**](SystemApi.md#enterprise_stub_write_replication_performance_secondary_generate_public_key) | **POST** /sys/replication/performance/secondary/generate-public-key | 
[**enterprise_stub_write_replication_performance_secondary_promote**](SystemApi.md#enterprise_stub_write_replication_performance_secondary_promote) | **POST** /sys/replication/performance/secondary/promote | 
[**enterprise_stub_write_replication_performance_secondary_update_primary**](SystemApi.md#enterprise_stub_write_replication_performance_secondary_update_primary) | **POST** /sys/replication/performance/secondary/update-primary | 
[**enterprise_stub_write_replication_primary_demote**](SystemApi.md#enterprise_stub_write_replication_primary_demote) | **POST** /sys/replication/primary/demote | 
[**enterprise_stub_write_replication_primary_disable**](SystemApi.md#enterprise_stub_write_replication_primary_disable) | **POST** /sys/replication/primary/disable | 
[**enterprise_stub_write_replication_primary_enable**](SystemApi.md#enterprise_stub_write_replication_primary_enable) | **POST** /sys/replication/primary/enable | 
[**enterprise_stub_write_replication_primary_revoke_secondary**](SystemApi.md#enterprise_stub_write_replication_primary_revoke_secondary) | **POST** /sys/replication/primary/revoke-secondary | 
[**enterprise_stub_write_replication_primary_secondary_token**](SystemApi.md#enterprise_stub_write_replication_primary_secondary_token) | **POST** /sys/replication/primary/secondary-token | 
[**enterprise_stub_write_replication_recover**](SystemApi.md#enterprise_stub_write_replication_recover) | **POST** /sys/replication/recover | 
[**enterprise_stub_write_replication_reindex**](SystemApi.md#enterprise_stub_write_replication_reindex) | **POST** /sys/replication/reindex | 
[**enterprise_stub_write_replication_secondary_disable**](SystemApi.md#enterprise_stub_write_replication_secondary_disable) | **POST** /sys/replication/secondary/disable | 
[**enterprise_stub_write_replication_secondary_enable**](SystemApi.md#enterprise_stub_write_replication_secondary_enable) | **POST** /sys/replication/secondary/enable | 
[**enterprise_stub_write_replication_secondary_promote**](SystemApi.md#enterprise_stub_write_replication_secondary_promote) | **POST** /sys/replication/secondary/promote | 
[**enterprise_stub_write_replication_secondary_update_primary**](SystemApi.md#enterprise_stub_write_replication_secondary_update_primary) | **POST** /sys/replication/secondary/update-primary | 
[**enterprise_stub_write_sealwrap_rewrap**](SystemApi.md#enterprise_stub_write_sealwrap_rewrap) | **POST** /sys/sealwrap/rewrap | 
[**enterprise_stub_write_storage_raft_snapshot_auto_config_name**](SystemApi.md#enterprise_stub_write_storage_raft_snapshot_auto_config_name) | **POST** /sys/storage/raft/snapshot-auto/config/{name} | 
[**generate_hash**](SystemApi.md#generate_hash) | **POST** /sys/tools/hash | 
[**generate_hash_with_algorithm**](SystemApi.md#generate_hash_with_algorithm) | **POST** /sys/tools/hash/{urlalgorithm} | 
[**generate_random**](SystemApi.md#generate_random) | **POST** /sys/tools/random | 
[**generate_random_with_bytes**](SystemApi.md#generate_random_with_bytes) | **POST** /sys/tools/random/{urlbytes} | 
[**generate_random_with_source**](SystemApi.md#generate_random_with_source) | **POST** /sys/tools/random/{source} | 
[**generate_random_with_source_and_bytes**](SystemApi.md#generate_random_with_source_and_bytes) | **POST** /sys/tools/random/{source}/{urlbytes} | 
[**ha_status**](SystemApi.md#ha_status) | **GET** /sys/ha-status | Check the HA status of a Vault cluster
[**initialize**](SystemApi.md#initialize) | **POST** /sys/init | Initialize a new Vault.
[**internal_client_activity_configure**](SystemApi.md#internal_client_activity_configure) | **POST** /sys/internal/counters/config | Enable or disable collection of client count, set retention period, or set default reporting period.
[**internal_client_activity_export**](SystemApi.md#internal_client_activity_export) | **GET** /sys/internal/counters/activity/export | Report the client count metrics, for this namespace and all child namespaces.
[**internal_client_activity_read_configuration**](SystemApi.md#internal_client_activity_read_configuration) | **GET** /sys/internal/counters/config | Read the client count tracking configuration.
[**internal_client_activity_report_counts**](SystemApi.md#internal_client_activity_report_counts) | **GET** /sys/internal/counters/activity | Report the client count metrics, for this namespace and all child namespaces.
[**internal_client_activity_report_counts_this_month**](SystemApi.md#internal_client_activity_report_counts_this_month) | **GET** /sys/internal/counters/activity/monthly | Report the number of clients for this month, for this namespace and all child namespaces.
[**internal_count_entities**](SystemApi.md#internal_count_entities) | **GET** /sys/internal/counters/entities | Backwards compatibility is not guaranteed for this API
[**internal_count_requests**](SystemApi.md#internal_count_requests) | **GET** /sys/internal/counters/requests | Backwards compatibility is not guaranteed for this API
[**internal_count_tokens**](SystemApi.md#internal_count_tokens) | **GET** /sys/internal/counters/tokens | Backwards compatibility is not guaranteed for this API
[**internal_generate_open_api_document**](SystemApi.md#internal_generate_open_api_document) | **GET** /sys/internal/specs/openapi | 
[**internal_generate_open_api_document_with_parameters**](SystemApi.md#internal_generate_open_api_document_with_parameters) | **POST** /sys/internal/specs/openapi | 
[**internal_inspect_router**](SystemApi.md#internal_inspect_router) | **GET** /sys/internal/inspect/router/{tag} | Expose the route entry and mount entry tables present in the router
[**internal_ui_list_enabled_feature_flags**](SystemApi.md#internal_ui_list_enabled_feature_flags) | **GET** /sys/internal/ui/feature-flags | Lists enabled feature flags.
[**internal_ui_list_enabled_visible_mounts**](SystemApi.md#internal_ui_list_enabled_visible_mounts) | **GET** /sys/internal/ui/mounts | Lists all enabled and visible auth and secrets mounts.
[**internal_ui_list_namespaces**](SystemApi.md#internal_ui_list_namespaces) | **GET** /sys/internal/ui/namespaces | Backwards compatibility is not guaranteed for this API
[**internal_ui_read_mount_information**](SystemApi.md#internal_ui_read_mount_information) | **GET** /sys/internal/ui/mounts/{path} | Return information about the given mount.
[**internal_ui_read_resultant_acl**](SystemApi.md#internal_ui_read_resultant_acl) | **GET** /sys/internal/ui/resultant-acl | Backwards compatibility is not guaranteed for this API
[**leader_status**](SystemApi.md#leader_status) | **GET** /sys/leader | Returns the high availability status and current leader instance of Vault.
[**leases_count**](SystemApi.md#leases_count) | **GET** /sys/leases/count | 
[**leases_force_revoke_lease_with_prefix**](SystemApi.md#leases_force_revoke_lease_with_prefix) | **POST** /sys/leases/revoke-force/{prefix} | Revokes all secrets or tokens generated under a given prefix immediately
[**leases_force_revoke_lease_with_prefix2**](SystemApi.md#leases_force_revoke_lease_with_prefix2) | **POST** /sys/revoke-force/{prefix} | Revokes all secrets or tokens generated under a given prefix immediately
[**leases_list**](SystemApi.md#leases_list) | **GET** /sys/leases | 
[**leases_look_up**](SystemApi.md#leases_look_up) | **GET** /sys/leases/lookup/{prefix}/ | 
[**leases_read_lease**](SystemApi.md#leases_read_lease) | **POST** /sys/leases/lookup | 
[**leases_renew_lease**](SystemApi.md#leases_renew_lease) | **POST** /sys/leases/renew | Renews a lease, requesting to extend the lease.
[**leases_renew_lease2**](SystemApi.md#leases_renew_lease2) | **POST** /sys/renew | Renews a lease, requesting to extend the lease.
[**leases_renew_lease_with_id**](SystemApi.md#leases_renew_lease_with_id) | **POST** /sys/leases/renew/{url_lease_id} | Renews a lease, requesting to extend the lease.
[**leases_renew_lease_with_id2**](SystemApi.md#leases_renew_lease_with_id2) | **POST** /sys/renew/{url_lease_id} | Renews a lease, requesting to extend the lease.
[**leases_revoke_lease**](SystemApi.md#leases_revoke_lease) | **POST** /sys/leases/revoke | Revokes a lease immediately.
[**leases_revoke_lease2**](SystemApi.md#leases_revoke_lease2) | **POST** /sys/revoke | Revokes a lease immediately.
[**leases_revoke_lease_with_id**](SystemApi.md#leases_revoke_lease_with_id) | **POST** /sys/leases/revoke/{url_lease_id} | Revokes a lease immediately.
[**leases_revoke_lease_with_id2**](SystemApi.md#leases_revoke_lease_with_id2) | **POST** /sys/revoke/{url_lease_id} | Revokes a lease immediately.
[**leases_revoke_lease_with_prefix**](SystemApi.md#leases_revoke_lease_with_prefix) | **POST** /sys/leases/revoke-prefix/{prefix} | Revokes all secrets (via a lease ID prefix) or tokens (via the tokens&#39; path property) generated under a given prefix immediately.
[**leases_revoke_lease_with_prefix2**](SystemApi.md#leases_revoke_lease_with_prefix2) | **POST** /sys/revoke-prefix/{prefix} | Revokes all secrets (via a lease ID prefix) or tokens (via the tokens&#39; path property) generated under a given prefix immediately.
[**leases_tidy**](SystemApi.md#leases_tidy) | **POST** /sys/leases/tidy | 
[**list_experimental_features**](SystemApi.md#list_experimental_features) | **GET** /sys/experiments | Returns the available and enabled experiments
[**locked_users_list**](SystemApi.md#locked_users_list) | **GET** /sys/locked-users | Report the locked user count metrics, for this namespace and all child namespaces.
[**locked_users_unlock**](SystemApi.md#locked_users_unlock) | **POST** /sys/locked-users/{mount_accessor}/unlock/{alias_identifier} | Unlocks the user with given mount_accessor and alias_identifier
[**loggers_read_verbosity_level**](SystemApi.md#loggers_read_verbosity_level) | **GET** /sys/loggers | Read the log level for all existing loggers.
[**loggers_read_verbosity_level_for**](SystemApi.md#loggers_read_verbosity_level_for) | **GET** /sys/loggers/{name} | Read the log level for a single logger.
[**loggers_revert_verbosity_level**](SystemApi.md#loggers_revert_verbosity_level) | **DELETE** /sys/loggers | Revert the all loggers to use log level provided in config.
[**loggers_revert_verbosity_level_for**](SystemApi.md#loggers_revert_verbosity_level_for) | **DELETE** /sys/loggers/{name} | Revert a single logger to use log level provided in config.
[**loggers_update_verbosity_level**](SystemApi.md#loggers_update_verbosity_level) | **POST** /sys/loggers | Modify the log level for all existing loggers.
[**loggers_update_verbosity_level_for**](SystemApi.md#loggers_update_verbosity_level_for) | **POST** /sys/loggers/{name} | Modify the log level of a single logger.
[**metrics**](SystemApi.md#metrics) | **GET** /sys/metrics | 
[**mfa_validate**](SystemApi.md#mfa_validate) | **POST** /sys/mfa/validate | Validates the login for the given MFA methods. Upon successful validation, it returns an auth response containing the client token
[**monitor**](SystemApi.md#monitor) | **GET** /sys/monitor | 
[**mounts_disable_secrets_engine**](SystemApi.md#mounts_disable_secrets_engine) | **DELETE** /sys/mounts/{path} | Disable the mount point specified at the given path.
[**mounts_enable_secrets_engine**](SystemApi.md#mounts_enable_secrets_engine) | **POST** /sys/mounts/{path} | Enable a new secrets engine at the given path.
[**mounts_list_secrets_engines**](SystemApi.md#mounts_list_secrets_engines) | **GET** /sys/mounts | 
[**mounts_read_configuration**](SystemApi.md#mounts_read_configuration) | **GET** /sys/mounts/{path} | Read the configuration of the secret engine at the given path.
[**mounts_read_tuning_information**](SystemApi.md#mounts_read_tuning_information) | **GET** /sys/mounts/{path}/tune | 
[**mounts_tune_configuration_parameters**](SystemApi.md#mounts_tune_configuration_parameters) | **POST** /sys/mounts/{path}/tune | 
[**plugins_catalog_list_plugins**](SystemApi.md#plugins_catalog_list_plugins) | **GET** /sys/plugins/catalog | 
[**plugins_catalog_list_plugins_with_type**](SystemApi.md#plugins_catalog_list_plugins_with_type) | **GET** /sys/plugins/catalog/{type}/ | List the plugins in the catalog.
[**plugins_catalog_read_plugin_configuration**](SystemApi.md#plugins_catalog_read_plugin_configuration) | **GET** /sys/plugins/catalog/{name} | Return the configuration data for the plugin with the given name.
[**plugins_catalog_read_plugin_configuration_with_type**](SystemApi.md#plugins_catalog_read_plugin_configuration_with_type) | **GET** /sys/plugins/catalog/{type}/{name} | Return the configuration data for the plugin with the given name.
[**plugins_catalog_register_plugin**](SystemApi.md#plugins_catalog_register_plugin) | **POST** /sys/plugins/catalog/{name} | Register a new plugin, or updates an existing one with the supplied name.
[**plugins_catalog_register_plugin_with_type**](SystemApi.md#plugins_catalog_register_plugin_with_type) | **POST** /sys/plugins/catalog/{type}/{name} | Register a new plugin, or updates an existing one with the supplied name.
[**plugins_catalog_remove_plugin**](SystemApi.md#plugins_catalog_remove_plugin) | **DELETE** /sys/plugins/catalog/{name} | Remove the plugin with the given name.
[**plugins_catalog_remove_plugin_with_type**](SystemApi.md#plugins_catalog_remove_plugin_with_type) | **DELETE** /sys/plugins/catalog/{type}/{name} | Remove the plugin with the given name.
[**plugins_reload_backends**](SystemApi.md#plugins_reload_backends) | **POST** /sys/plugins/reload/backend | Reload mounted plugin backends.
[**plugins_runtimes_catalog_list_plugins_runtimes**](SystemApi.md#plugins_runtimes_catalog_list_plugins_runtimes) | **GET** /sys/plugins/runtimes/catalog/ | 
[**plugins_runtimes_catalog_read_plugin_runtime_configuration**](SystemApi.md#plugins_runtimes_catalog_read_plugin_runtime_configuration) | **GET** /sys/plugins/runtimes/catalog/{type}/{name} | Return the configuration data for the plugin runtime with the given name.
[**plugins_runtimes_catalog_register_plugin_runtime**](SystemApi.md#plugins_runtimes_catalog_register_plugin_runtime) | **POST** /sys/plugins/runtimes/catalog/{type}/{name} | Register a new plugin runtime, or updates an existing one with the supplied name.
[**plugins_runtimes_catalog_remove_plugin_runtime**](SystemApi.md#plugins_runtimes_catalog_remove_plugin_runtime) | **DELETE** /sys/plugins/runtimes/catalog/{type}/{name} | Remove the plugin runtime with the given name.
[**policies_delete_acl_policy**](SystemApi.md#policies_delete_acl_policy) | **DELETE** /sys/policies/acl/{name} | Delete the ACL policy with the given name.
[**policies_delete_acl_policy2**](SystemApi.md#policies_delete_acl_policy2) | **DELETE** /sys/policy/{name} | Delete the policy with the given name.
[**policies_delete_password_policy**](SystemApi.md#policies_delete_password_policy) | **DELETE** /sys/policies/password/{name} | Delete a password policy.
[**policies_generate_password_from_password_policy**](SystemApi.md#policies_generate_password_from_password_policy) | **GET** /sys/policies/password/{name}/generate | Generate a password from an existing password policy.
[**policies_list_acl_policies**](SystemApi.md#policies_list_acl_policies) | **GET** /sys/policies/acl/ | 
[**policies_list_acl_policies2**](SystemApi.md#policies_list_acl_policies2) | **GET** /sys/policy | 
[**policies_list_acl_policies3**](SystemApi.md#policies_list_acl_policies3) | **GET** /sys/policy/ | 
[**policies_list_password_policies**](SystemApi.md#policies_list_password_policies) | **GET** /sys/policies/password/ | List the existing password policies.
[**policies_read_acl_policy**](SystemApi.md#policies_read_acl_policy) | **GET** /sys/policies/acl/{name} | Retrieve information about the named ACL policy.
[**policies_read_acl_policy2**](SystemApi.md#policies_read_acl_policy2) | **GET** /sys/policy/{name} | Retrieve the policy body for the named policy.
[**policies_read_password_policy**](SystemApi.md#policies_read_password_policy) | **GET** /sys/policies/password/{name} | Retrieve an existing password policy.
[**policies_write_acl_policy**](SystemApi.md#policies_write_acl_policy) | **POST** /sys/policies/acl/{name} | Add a new or update an existing ACL policy.
[**policies_write_acl_policy2**](SystemApi.md#policies_write_acl_policy2) | **POST** /sys/policy/{name} | Add a new or update an existing policy.
[**policies_write_password_policy**](SystemApi.md#policies_write_password_policy) | **POST** /sys/policies/password/{name} | Add a new or update an existing password policy.
[**pprof_blocking**](SystemApi.md#pprof_blocking) | **GET** /sys/pprof/block | Returns stack traces that led to blocking on synchronization primitives
[**pprof_command_line**](SystemApi.md#pprof_command_line) | **GET** /sys/pprof/cmdline | Returns the running program&#39;s command line.
[**pprof_cpu_profile**](SystemApi.md#pprof_cpu_profile) | **GET** /sys/pprof/profile | Returns a pprof-formatted cpu profile payload.
[**pprof_execution_trace**](SystemApi.md#pprof_execution_trace) | **GET** /sys/pprof/trace | Returns the execution trace in binary form.
[**pprof_goroutines**](SystemApi.md#pprof_goroutines) | **GET** /sys/pprof/goroutine | Returns stack traces of all current goroutines.
[**pprof_index**](SystemApi.md#pprof_index) | **GET** /sys/pprof | Returns an HTML page listing the available profiles.
[**pprof_memory_allocations**](SystemApi.md#pprof_memory_allocations) | **GET** /sys/pprof/allocs | Returns a sampling of all past memory allocations.
[**pprof_memory_allocations_live**](SystemApi.md#pprof_memory_allocations_live) | **GET** /sys/pprof/heap | Returns a sampling of memory allocations of live object.
[**pprof_mutexes**](SystemApi.md#pprof_mutexes) | **GET** /sys/pprof/mutex | Returns stack traces of holders of contended mutexes
[**pprof_symbols**](SystemApi.md#pprof_symbols) | **GET** /sys/pprof/symbol | Returns the program counters listed in the request.
[**pprof_thread_creations**](SystemApi.md#pprof_thread_creations) | **GET** /sys/pprof/threadcreate | Returns stack traces that led to the creation of new OS threads
[**query_token_accessor_capabilities**](SystemApi.md#query_token_accessor_capabilities) | **POST** /sys/capabilities-accessor | 
[**query_token_capabilities**](SystemApi.md#query_token_capabilities) | **POST** /sys/capabilities | 
[**query_token_self_capabilities**](SystemApi.md#query_token_self_capabilities) | **POST** /sys/capabilities-self | 
[**rate_limit_quotas_configure**](SystemApi.md#rate_limit_quotas_configure) | **POST** /sys/quotas/config | 
[**rate_limit_quotas_delete**](SystemApi.md#rate_limit_quotas_delete) | **DELETE** /sys/quotas/rate-limit/{name} | 
[**rate_limit_quotas_list**](SystemApi.md#rate_limit_quotas_list) | **GET** /sys/quotas/rate-limit/ | 
[**rate_limit_quotas_read**](SystemApi.md#rate_limit_quotas_read) | **GET** /sys/quotas/rate-limit/{name} | 
[**rate_limit_quotas_read_configuration**](SystemApi.md#rate_limit_quotas_read_configuration) | **GET** /sys/quotas/config | 
[**rate_limit_quotas_write**](SystemApi.md#rate_limit_quotas_write) | **POST** /sys/quotas/rate-limit/{name} | 
[**raw_delete**](SystemApi.md#raw_delete) | **DELETE** /sys/raw/{path} | Delete the key with given path.
[**raw_list**](SystemApi.md#raw_list) | **GET** /sys/raw/{path}/ | Return a list keys for a given path prefix.
[**raw_read**](SystemApi.md#raw_read) | **GET** /sys/raw/{path} | Read the value of the key at the given path.
[**raw_write**](SystemApi.md#raw_write) | **POST** /sys/raw/{path} | Update the value of the key at the given path.
[**read_health_status**](SystemApi.md#read_health_status) | **GET** /sys/health | Returns the health status of Vault.
[**read_initialization_status**](SystemApi.md#read_initialization_status) | **GET** /sys/init | Returns the initialization status of Vault.
[**read_replication_status**](SystemApi.md#read_replication_status) | **GET** /sys/replication/status | 
[**read_sanitized_configuration_state**](SystemApi.md#read_sanitized_configuration_state) | **GET** /sys/config/state/sanitized | Return a sanitized version of the Vault server configuration.
[**read_wrapping_properties**](SystemApi.md#read_wrapping_properties) | **POST** /sys/wrapping/lookup | Look up wrapping properties for the given token.
[**read_wrapping_properties2**](SystemApi.md#read_wrapping_properties2) | **GET** /sys/wrapping/lookup | Look up wrapping properties for the requester&#39;s token.
[**rekey_attempt_cancel**](SystemApi.md#rekey_attempt_cancel) | **DELETE** /sys/rekey/init | Cancels any in-progress rekey.
[**rekey_attempt_initialize**](SystemApi.md#rekey_attempt_initialize) | **POST** /sys/rekey/init | Initializes a new rekey attempt.
[**rekey_attempt_read_progress**](SystemApi.md#rekey_attempt_read_progress) | **GET** /sys/rekey/init | Reads the configuration and progress of the current rekey attempt.
[**rekey_attempt_update**](SystemApi.md#rekey_attempt_update) | **POST** /sys/rekey/update | Enter a single unseal key share to progress the rekey of the Vault.
[**rekey_delete_backup_key**](SystemApi.md#rekey_delete_backup_key) | **DELETE** /sys/rekey/backup | Delete the backup copy of PGP-encrypted unseal keys.
[**rekey_delete_backup_recovery_key**](SystemApi.md#rekey_delete_backup_recovery_key) | **DELETE** /sys/rekey/recovery-key-backup | 
[**rekey_read_backup_key**](SystemApi.md#rekey_read_backup_key) | **GET** /sys/rekey/backup | Return the backup copy of PGP-encrypted unseal keys.
[**rekey_read_backup_recovery_key**](SystemApi.md#rekey_read_backup_recovery_key) | **GET** /sys/rekey/recovery-key-backup | 
[**rekey_verification_cancel**](SystemApi.md#rekey_verification_cancel) | **DELETE** /sys/rekey/verify | Cancel any in-progress rekey verification operation.
[**rekey_verification_read_progress**](SystemApi.md#rekey_verification_read_progress) | **GET** /sys/rekey/verify | Read the configuration and progress of the current rekey verification attempt.
[**rekey_verification_update**](SystemApi.md#rekey_verification_update) | **POST** /sys/rekey/verify | Enter a single new key share to progress the rekey verification operation.
[**reload_subsystem**](SystemApi.md#reload_subsystem) | **POST** /sys/config/reload/{subsystem} | Reload the given subsystem
[**remount**](SystemApi.md#remount) | **POST** /sys/remount | Initiate a mount migration
[**remount_status**](SystemApi.md#remount_status) | **GET** /sys/remount/status/{migration_id} | Check status of a mount migration
[**rewrap**](SystemApi.md#rewrap) | **POST** /sys/wrapping/rewrap | 
[**root_token_generation_cancel**](SystemApi.md#root_token_generation_cancel) | **DELETE** /sys/generate-root/attempt | Cancels any in-progress root generation attempt.
[**root_token_generation_cancel2**](SystemApi.md#root_token_generation_cancel2) | **DELETE** /sys/generate-root | Cancels any in-progress root generation attempt.
[**root_token_generation_initialize**](SystemApi.md#root_token_generation_initialize) | **POST** /sys/generate-root/attempt | Initializes a new root generation attempt.
[**root_token_generation_initialize2**](SystemApi.md#root_token_generation_initialize2) | **POST** /sys/generate-root | Initializes a new root generation attempt.
[**root_token_generation_read_progress**](SystemApi.md#root_token_generation_read_progress) | **GET** /sys/generate-root/attempt | Read the configuration and progress of the current root generation attempt.
[**root_token_generation_read_progress2**](SystemApi.md#root_token_generation_read_progress2) | **GET** /sys/generate-root | Read the configuration and progress of the current root generation attempt.
[**root_token_generation_update**](SystemApi.md#root_token_generation_update) | **POST** /sys/generate-root/update | Enter a single unseal key share to progress the root generation attempt.
[**seal**](SystemApi.md#seal) | **POST** /sys/seal | Seal the Vault.
[**seal_status**](SystemApi.md#seal_status) | **GET** /sys/seal-status | Check the seal status of a Vault.
[**step_down_leader**](SystemApi.md#step_down_leader) | **POST** /sys/step-down | Cause the node to give up active status.
[**ui_headers_configure**](SystemApi.md#ui_headers_configure) | **POST** /sys/config/ui/headers/{header} | Configure the values to be returned for the UI header.
[**ui_headers_delete_configuration**](SystemApi.md#ui_headers_delete_configuration) | **DELETE** /sys/config/ui/headers/{header} | Remove a UI header.
[**ui_headers_list**](SystemApi.md#ui_headers_list) | **GET** /sys/config/ui/headers/ | Return a list of configured UI headers.
[**ui_headers_read_configuration**](SystemApi.md#ui_headers_read_configuration) | **GET** /sys/config/ui/headers/{header} | Return the given UI header&#39;s configuration
[**unseal**](SystemApi.md#unseal) | **POST** /sys/unseal | Unseal the Vault.
[**unwrap**](SystemApi.md#unwrap) | **POST** /sys/wrapping/unwrap | 
[**version_history**](SystemApi.md#version_history) | **GET** /sys/version-history/ | Returns map of historical version change entries
[**wrap**](SystemApi.md#wrap) | **POST** /sys/wrapping/wrap | 


# **auditing_calculate_hash**
> AuditingCalculateHashResponse auditing_calculate_hash(path, auditing_calculate_hash_request)



### Example


```python
import ahvac
from ahvac.models.auditing_calculate_hash_request import AuditingCalculateHashRequest
from ahvac.models.auditing_calculate_hash_response import AuditingCalculateHashResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The name of the backend. Cannot be delimited. Example: \"mysql\"
    auditing_calculate_hash_request = ahvac.AuditingCalculateHashRequest() # AuditingCalculateHashRequest | 

    try:
        api_response = await api_instance.auditing_calculate_hash(path, auditing_calculate_hash_request)
        print("The response of SystemApi->auditing_calculate_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->auditing_calculate_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The name of the backend. Cannot be delimited. Example: \&quot;mysql\&quot; | 
 **auditing_calculate_hash_request** | [**AuditingCalculateHashRequest**](AuditingCalculateHashRequest.md)|  | 

### Return type

[**AuditingCalculateHashResponse**](AuditingCalculateHashResponse.md)

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

# **auditing_disable_device**
> auditing_disable_device(path)

Disable the audit device at the given path.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The name of the backend. Cannot be delimited. Example: \"mysql\"

    try:
        # Disable the audit device at the given path.
        await api_instance.auditing_disable_device(path)
    except Exception as e:
        print("Exception when calling SystemApi->auditing_disable_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The name of the backend. Cannot be delimited. Example: \&quot;mysql\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auditing_disable_request_header**
> auditing_disable_request_header(header)

Disable auditing of the given request header.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    header = 'header_example' # str | 

    try:
        # Disable auditing of the given request header.
        await api_instance.auditing_disable_request_header(header)
    except Exception as e:
        print("Exception when calling SystemApi->auditing_disable_request_header: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auditing_enable_device**
> auditing_enable_device(path, auditing_enable_device_request)

Enable a new audit device at the supplied path.

### Example


```python
import ahvac
from ahvac.models.auditing_enable_device_request import AuditingEnableDeviceRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The name of the backend. Cannot be delimited. Example: \"mysql\"
    auditing_enable_device_request = ahvac.AuditingEnableDeviceRequest() # AuditingEnableDeviceRequest | 

    try:
        # Enable a new audit device at the supplied path.
        await api_instance.auditing_enable_device(path, auditing_enable_device_request)
    except Exception as e:
        print("Exception when calling SystemApi->auditing_enable_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The name of the backend. Cannot be delimited. Example: \&quot;mysql\&quot; | 
 **auditing_enable_device_request** | [**AuditingEnableDeviceRequest**](AuditingEnableDeviceRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auditing_enable_request_header**
> auditing_enable_request_header(header, auditing_enable_request_header_request)

Enable auditing of a header.

### Example


```python
import ahvac
from ahvac.models.auditing_enable_request_header_request import AuditingEnableRequestHeaderRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    header = 'header_example' # str | 
    auditing_enable_request_header_request = ahvac.AuditingEnableRequestHeaderRequest() # AuditingEnableRequestHeaderRequest | 

    try:
        # Enable auditing of a header.
        await api_instance.auditing_enable_request_header(header, auditing_enable_request_header_request)
    except Exception as e:
        print("Exception when calling SystemApi->auditing_enable_request_header: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**|  | 
 **auditing_enable_request_header_request** | [**AuditingEnableRequestHeaderRequest**](AuditingEnableRequestHeaderRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auditing_list_enabled_devices**
> auditing_list_enabled_devices()

List the enabled audit devices.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # List the enabled audit devices.
        await api_instance.auditing_list_enabled_devices()
    except Exception as e:
        print("Exception when calling SystemApi->auditing_list_enabled_devices: %s\n" % e)
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

# **auditing_list_request_headers**
> AuditingListRequestHeadersResponse auditing_list_request_headers()

List the request headers that are configured to be audited.

### Example


```python
import ahvac
from ahvac.models.auditing_list_request_headers_response import AuditingListRequestHeadersResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # List the request headers that are configured to be audited.
        api_response = await api_instance.auditing_list_request_headers()
        print("The response of SystemApi->auditing_list_request_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->auditing_list_request_headers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditingListRequestHeadersResponse**](AuditingListRequestHeadersResponse.md)

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

# **auditing_read_request_header_information**
> auditing_read_request_header_information(header)

List the information for the given request header.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    header = 'header_example' # str | 

    try:
        # List the information for the given request header.
        await api_instance.auditing_read_request_header_information(header)
    except Exception as e:
        print("Exception when calling SystemApi->auditing_read_request_header_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**|  | 

### Return type

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

# **auth_disable_method**
> auth_disable_method(path)

Disable the auth method at the given auth path

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Cannot be delimited. Example: \"user\"

    try:
        # Disable the auth method at the given auth path
        await api_instance.auth_disable_method(path)
    except Exception as e:
        print("Exception when calling SystemApi->auth_disable_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Cannot be delimited. Example: \&quot;user\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_enable_method**
> auth_enable_method(path, auth_enable_method_request)

Enables a new auth method.

After enabling, the auth method can be accessed and configured via the auth path specified as part of the URL. This auth path will be nested under the auth prefix.  For example, enable the \"foo\" auth method will make it accessible at /auth/foo.

### Example


```python
import ahvac
from ahvac.models.auth_enable_method_request import AuthEnableMethodRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Cannot be delimited. Example: \"user\"
    auth_enable_method_request = ahvac.AuthEnableMethodRequest() # AuthEnableMethodRequest | 

    try:
        # Enables a new auth method.
        await api_instance.auth_enable_method(path, auth_enable_method_request)
    except Exception as e:
        print("Exception when calling SystemApi->auth_enable_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Cannot be delimited. Example: \&quot;user\&quot; | 
 **auth_enable_method_request** | [**AuthEnableMethodRequest**](AuthEnableMethodRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_list_enabled_methods**
> auth_list_enabled_methods()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.auth_list_enabled_methods()
    except Exception as e:
        print("Exception when calling SystemApi->auth_list_enabled_methods: %s\n" % e)
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

# **auth_read_configuration**
> AuthReadConfigurationResponse auth_read_configuration(path)

Read the configuration of the auth engine at the given path.

### Example


```python
import ahvac
from ahvac.models.auth_read_configuration_response import AuthReadConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Cannot be delimited. Example: \"user\"

    try:
        # Read the configuration of the auth engine at the given path.
        api_response = await api_instance.auth_read_configuration(path)
        print("The response of SystemApi->auth_read_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->auth_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Cannot be delimited. Example: \&quot;user\&quot; | 

### Return type

[**AuthReadConfigurationResponse**](AuthReadConfigurationResponse.md)

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

# **auth_read_tuning_information**
> AuthReadTuningInformationResponse auth_read_tuning_information(path)

Reads the given auth path's configuration.

This endpoint requires sudo capability on the final path, but the same functionality can be achieved without sudo via `sys/mounts/auth/[auth-path]/tune`.

### Example


```python
import ahvac
from ahvac.models.auth_read_tuning_information_response import AuthReadTuningInformationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | Tune the configuration parameters for an auth path.

    try:
        # Reads the given auth path's configuration.
        api_response = await api_instance.auth_read_tuning_information(path)
        print("The response of SystemApi->auth_read_tuning_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->auth_read_tuning_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Tune the configuration parameters for an auth path. | 

### Return type

[**AuthReadTuningInformationResponse**](AuthReadTuningInformationResponse.md)

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

# **auth_tune_configuration_parameters**
> auth_tune_configuration_parameters(path, auth_tune_configuration_parameters_request)

Tune configuration parameters for a given auth path.

This endpoint requires sudo capability on the final path, but the same functionality can be achieved without sudo via `sys/mounts/auth/[auth-path]/tune`.

### Example


```python
import ahvac
from ahvac.models.auth_tune_configuration_parameters_request import AuthTuneConfigurationParametersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | Tune the configuration parameters for an auth path.
    auth_tune_configuration_parameters_request = ahvac.AuthTuneConfigurationParametersRequest() # AuthTuneConfigurationParametersRequest | 

    try:
        # Tune configuration parameters for a given auth path.
        await api_instance.auth_tune_configuration_parameters(path, auth_tune_configuration_parameters_request)
    except Exception as e:
        print("Exception when calling SystemApi->auth_tune_configuration_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Tune the configuration parameters for an auth path. | 
 **auth_tune_configuration_parameters_request** | [**AuthTuneConfigurationParametersRequest**](AuthTuneConfigurationParametersRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_host_information**
> CollectHostInformationResponse collect_host_information()

Information about the host instance that this Vault server is running on.

Information about the host instance that this Vault server is running on.   The information that gets collected includes host hardware information, and CPU,   disk, and memory utilization

### Example


```python
import ahvac
from ahvac.models.collect_host_information_response import CollectHostInformationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Information about the host instance that this Vault server is running on.
        api_response = await api_instance.collect_host_information()
        print("The response of SystemApi->collect_host_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->collect_host_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CollectHostInformationResponse**](CollectHostInformationResponse.md)

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

# **collect_in_flight_request_information**
> collect_in_flight_request_information()

reports in-flight requests

This path responds to the following HTTP methods.   GET /    Returns a map of in-flight requests.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # reports in-flight requests
        await api_instance.collect_in_flight_request_information()
    except Exception as e:
        print("Exception when calling SystemApi->collect_in_flight_request_information: %s\n" % e)
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

# **cors_configure**
> cors_configure(cors_configure_request)

Configure the CORS settings.

### Example


```python
import ahvac
from ahvac.models.cors_configure_request import CorsConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    cors_configure_request = ahvac.CorsConfigureRequest() # CorsConfigureRequest | 

    try:
        # Configure the CORS settings.
        await api_instance.cors_configure(cors_configure_request)
    except Exception as e:
        print("Exception when calling SystemApi->cors_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cors_configure_request** | [**CorsConfigureRequest**](CorsConfigureRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cors_delete_configuration**
> cors_delete_configuration()

Remove any CORS settings.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Remove any CORS settings.
        await api_instance.cors_delete_configuration()
    except Exception as e:
        print("Exception when calling SystemApi->cors_delete_configuration: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cors_read_configuration**
> CorsReadConfigurationResponse cors_read_configuration()

Return the current CORS settings.

### Example


```python
import ahvac
from ahvac.models.cors_read_configuration_response import CorsReadConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Return the current CORS settings.
        api_response = await api_instance.cors_read_configuration()
        print("The response of SystemApi->cors_read_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->cors_read_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CorsReadConfigurationResponse**](CorsReadConfigurationResponse.md)

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

# **decode**
> decode(decode_request)

Decodes the encoded token with the otp.

### Example


```python
import ahvac
from ahvac.models.decode_request import DecodeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    decode_request = ahvac.DecodeRequest() # DecodeRequest | 

    try:
        # Decodes the encoded token with the otp.
        await api_instance.decode(decode_request)
    except Exception as e:
        print("Exception when calling SystemApi->decode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decode_request** | [**DecodeRequest**](DecodeRequest.md)|  | 

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

# **encryption_key_configure_rotation**
> encryption_key_configure_rotation(encryption_key_configure_rotation_request)



### Example


```python
import ahvac
from ahvac.models.encryption_key_configure_rotation_request import EncryptionKeyConfigureRotationRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    encryption_key_configure_rotation_request = ahvac.EncryptionKeyConfigureRotationRequest() # EncryptionKeyConfigureRotationRequest | 

    try:
        await api_instance.encryption_key_configure_rotation(encryption_key_configure_rotation_request)
    except Exception as e:
        print("Exception when calling SystemApi->encryption_key_configure_rotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encryption_key_configure_rotation_request** | [**EncryptionKeyConfigureRotationRequest**](EncryptionKeyConfigureRotationRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encryption_key_read_rotation_configuration**
> EncryptionKeyReadRotationConfigurationResponse encryption_key_read_rotation_configuration()



### Example


```python
import ahvac
from ahvac.models.encryption_key_read_rotation_configuration_response import EncryptionKeyReadRotationConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        api_response = await api_instance.encryption_key_read_rotation_configuration()
        print("The response of SystemApi->encryption_key_read_rotation_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->encryption_key_read_rotation_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EncryptionKeyReadRotationConfigurationResponse**](EncryptionKeyReadRotationConfigurationResponse.md)

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

# **encryption_key_rotate**
> encryption_key_rotate()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.encryption_key_rotate()
    except Exception as e:
        print("Exception when calling SystemApi->encryption_key_rotate: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encryption_key_status**
> encryption_key_status()

Provides information about the backend encryption key.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Provides information about the backend encryption key.
        await api_instance.encryption_key_status()
    except Exception as e:
        print("Exception when calling SystemApi->encryption_key_status: %s\n" % e)
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

# **enterprise_stub_delete_config_control_group**
> enterprise_stub_delete_config_control_group()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_delete_config_control_group()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_config_control_group: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_stub_delete_managed_keys_type_name**
> enterprise_stub_delete_managed_keys_type_name(name, type)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 
    type = 'type_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_managed_keys_type_name(name, type)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_managed_keys_type_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **type** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_mfa_method_duo_name**
> enterprise_stub_delete_mfa_method_duo_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_mfa_method_duo_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_mfa_method_duo_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_mfa_method_okta_name**
> enterprise_stub_delete_mfa_method_okta_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_mfa_method_okta_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_mfa_method_okta_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_mfa_method_pingid_name**
> enterprise_stub_delete_mfa_method_pingid_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_mfa_method_pingid_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_mfa_method_pingid_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_mfa_method_totp_name**
> enterprise_stub_delete_mfa_method_totp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_mfa_method_totp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_mfa_method_totp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_namespaces_path**
> enterprise_stub_delete_namespaces_path(path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_namespaces_path(path)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_namespaces_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_policies_egp_name**
> enterprise_stub_delete_policies_egp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_policies_egp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_policies_egp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_policies_rgp_name**
> enterprise_stub_delete_policies_rgp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_policies_rgp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_policies_rgp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_quotas_lease_count_name**
> enterprise_stub_delete_quotas_lease_count_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_quotas_lease_count_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_quotas_lease_count_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_replication_performance_primary_paths_filter_id**
> enterprise_stub_delete_replication_performance_primary_paths_filter_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    id = 'id_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_replication_performance_primary_paths_filter_id(id)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_replication_performance_primary_paths_filter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

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

# **enterprise_stub_delete_storage_raft_snapshot_auto_config_name**
> enterprise_stub_delete_storage_raft_snapshot_auto_config_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_delete_storage_raft_snapshot_auto_config_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_delete_storage_raft_snapshot_auto_config_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_list_managed_keys_type**
> StandardListResponse enterprise_stub_list_managed_keys_type(type, list)



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
    api_instance = ahvac.SystemApi(api_client)
    type = 'type_example' # str | 
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.enterprise_stub_list_managed_keys_type(type, list)
        print("The response of SystemApi->enterprise_stub_list_managed_keys_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_list_managed_keys_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
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

# **enterprise_stub_list_mfa_method**
> StandardListResponse enterprise_stub_list_mfa_method(list)



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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.enterprise_stub_list_mfa_method(list)
        print("The response of SystemApi->enterprise_stub_list_mfa_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_list_mfa_method: %s\n" % e)
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

# **enterprise_stub_list_namespaces**
> StandardListResponse enterprise_stub_list_namespaces(list)



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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.enterprise_stub_list_namespaces(list)
        print("The response of SystemApi->enterprise_stub_list_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_list_namespaces: %s\n" % e)
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

# **enterprise_stub_list_policies_egp**
> StandardListResponse enterprise_stub_list_policies_egp(list)



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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.enterprise_stub_list_policies_egp(list)
        print("The response of SystemApi->enterprise_stub_list_policies_egp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_list_policies_egp: %s\n" % e)
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

# **enterprise_stub_list_policies_rgp**
> StandardListResponse enterprise_stub_list_policies_rgp(list)



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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.enterprise_stub_list_policies_rgp(list)
        print("The response of SystemApi->enterprise_stub_list_policies_rgp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_list_policies_rgp: %s\n" % e)
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

# **enterprise_stub_list_quotas_lease_count**
> StandardListResponse enterprise_stub_list_quotas_lease_count(list)



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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.enterprise_stub_list_quotas_lease_count(list)
        print("The response of SystemApi->enterprise_stub_list_quotas_lease_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_list_quotas_lease_count: %s\n" % e)
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

# **enterprise_stub_list_storage_raft_snapshot_auto_config**
> StandardListResponse enterprise_stub_list_storage_raft_snapshot_auto_config(list)



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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.enterprise_stub_list_storage_raft_snapshot_auto_config(list)
        print("The response of SystemApi->enterprise_stub_list_storage_raft_snapshot_auto_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_list_storage_raft_snapshot_auto_config: %s\n" % e)
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

# **enterprise_stub_read_config_control_group**
> enterprise_stub_read_config_control_group()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_config_control_group()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_config_control_group: %s\n" % e)
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

# **enterprise_stub_read_config_group_policy_application**
> enterprise_stub_read_config_group_policy_application()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_config_group_policy_application()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_config_group_policy_application: %s\n" % e)
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

# **enterprise_stub_read_license_status**
> enterprise_stub_read_license_status()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_license_status()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_license_status: %s\n" % e)
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

# **enterprise_stub_read_managed_keys_type_name**
> enterprise_stub_read_managed_keys_type_name(name, type)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 
    type = 'type_example' # str | 

    try:
        await api_instance.enterprise_stub_read_managed_keys_type_name(name, type)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_managed_keys_type_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **type** | **str**|  | 

### Return type

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

# **enterprise_stub_read_mfa_method_duo_name**
> enterprise_stub_read_mfa_method_duo_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_mfa_method_duo_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_mfa_method_duo_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_mfa_method_okta_name**
> enterprise_stub_read_mfa_method_okta_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_mfa_method_okta_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_mfa_method_okta_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_mfa_method_pingid_name**
> enterprise_stub_read_mfa_method_pingid_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_mfa_method_pingid_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_mfa_method_pingid_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_mfa_method_totp_name**
> enterprise_stub_read_mfa_method_totp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_mfa_method_totp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_mfa_method_totp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_mfa_method_totp_name_generate**
> enterprise_stub_read_mfa_method_totp_name_generate(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_mfa_method_totp_name_generate(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_mfa_method_totp_name_generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_namespaces_path**
> enterprise_stub_read_namespaces_path(path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 

    try:
        await api_instance.enterprise_stub_read_namespaces_path(path)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_namespaces_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

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

# **enterprise_stub_read_plugins_reload_backend_status**
> enterprise_stub_read_plugins_reload_backend_status()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_plugins_reload_backend_status()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_plugins_reload_backend_status: %s\n" % e)
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

# **enterprise_stub_read_policies_egp_name**
> enterprise_stub_read_policies_egp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_policies_egp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_policies_egp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_policies_rgp_name**
> enterprise_stub_read_policies_rgp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_policies_rgp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_policies_rgp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_quotas_lease_count_name**
> enterprise_stub_read_quotas_lease_count_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_quotas_lease_count_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_quotas_lease_count_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_replication_dr_secondary_license_status**
> enterprise_stub_read_replication_dr_secondary_license_status()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_replication_dr_secondary_license_status()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_replication_dr_secondary_license_status: %s\n" % e)
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

# **enterprise_stub_read_replication_dr_status**
> enterprise_stub_read_replication_dr_status()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_replication_dr_status()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_replication_dr_status: %s\n" % e)
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

# **enterprise_stub_read_replication_performance_primary_dynamic_filter_id**
> enterprise_stub_read_replication_performance_primary_dynamic_filter_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    id = 'id_example' # str | 

    try:
        await api_instance.enterprise_stub_read_replication_performance_primary_dynamic_filter_id(id)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_replication_performance_primary_dynamic_filter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

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

# **enterprise_stub_read_replication_performance_primary_paths_filter_id**
> enterprise_stub_read_replication_performance_primary_paths_filter_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    id = 'id_example' # str | 

    try:
        await api_instance.enterprise_stub_read_replication_performance_primary_paths_filter_id(id)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_replication_performance_primary_paths_filter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

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

# **enterprise_stub_read_replication_performance_secondary_dynamic_filter_id**
> enterprise_stub_read_replication_performance_secondary_dynamic_filter_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    id = 'id_example' # str | 

    try:
        await api_instance.enterprise_stub_read_replication_performance_secondary_dynamic_filter_id(id)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_replication_performance_secondary_dynamic_filter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

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

# **enterprise_stub_read_replication_performance_status**
> enterprise_stub_read_replication_performance_status()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_replication_performance_status()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_replication_performance_status: %s\n" % e)
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

# **enterprise_stub_read_sealwrap_rewrap**
> enterprise_stub_read_sealwrap_rewrap()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_read_sealwrap_rewrap()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_sealwrap_rewrap: %s\n" % e)
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

# **enterprise_stub_read_storage_raft_snapshot_auto_config_name**
> enterprise_stub_read_storage_raft_snapshot_auto_config_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_storage_raft_snapshot_auto_config_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_storage_raft_snapshot_auto_config_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_read_storage_raft_snapshot_auto_status_name**
> enterprise_stub_read_storage_raft_snapshot_auto_status_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_read_storage_raft_snapshot_auto_status_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_read_storage_raft_snapshot_auto_status_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_config_control_group**
> enterprise_stub_write_config_control_group()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_config_control_group()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_config_control_group: %s\n" % e)
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

# **enterprise_stub_write_config_group_policy_application**
> enterprise_stub_write_config_group_policy_application()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_config_group_policy_application()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_config_group_policy_application: %s\n" % e)
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

# **enterprise_stub_write_control_group_authorize**
> enterprise_stub_write_control_group_authorize()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_control_group_authorize()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_control_group_authorize: %s\n" % e)
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

# **enterprise_stub_write_control_group_request**
> enterprise_stub_write_control_group_request()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_control_group_request()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_control_group_request: %s\n" % e)
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

# **enterprise_stub_write_managed_keys_type_name**
> enterprise_stub_write_managed_keys_type_name(name, type)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 
    type = 'type_example' # str | 

    try:
        await api_instance.enterprise_stub_write_managed_keys_type_name(name, type)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_managed_keys_type_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **type** | **str**|  | 

### Return type

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

# **enterprise_stub_write_managed_keys_type_name_test_sign**
> enterprise_stub_write_managed_keys_type_name_test_sign(name, type)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 
    type = 'type_example' # str | 

    try:
        await api_instance.enterprise_stub_write_managed_keys_type_name_test_sign(name, type)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_managed_keys_type_name_test_sign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **type** | **str**|  | 

### Return type

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

# **enterprise_stub_write_mfa_method_duo_name**
> enterprise_stub_write_mfa_method_duo_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_mfa_method_duo_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_mfa_method_duo_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_mfa_method_okta_name**
> enterprise_stub_write_mfa_method_okta_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_mfa_method_okta_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_mfa_method_okta_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_mfa_method_pingid_name**
> enterprise_stub_write_mfa_method_pingid_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_mfa_method_pingid_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_mfa_method_pingid_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_mfa_method_totp_name**
> enterprise_stub_write_mfa_method_totp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_mfa_method_totp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_mfa_method_totp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_mfa_method_totp_name_admin_destroy**
> enterprise_stub_write_mfa_method_totp_name_admin_destroy(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_mfa_method_totp_name_admin_destroy(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_mfa_method_totp_name_admin_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_mfa_method_totp_name_admin_generate**
> enterprise_stub_write_mfa_method_totp_name_admin_generate(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_mfa_method_totp_name_admin_generate(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_mfa_method_totp_name_admin_generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_namespaces_api_lock_lock**
> enterprise_stub_write_namespaces_api_lock_lock()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_namespaces_api_lock_lock()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_namespaces_api_lock_lock: %s\n" % e)
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

# **enterprise_stub_write_namespaces_api_lock_lock_path**
> enterprise_stub_write_namespaces_api_lock_lock_path(path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 

    try:
        await api_instance.enterprise_stub_write_namespaces_api_lock_lock_path(path)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_namespaces_api_lock_lock_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

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

# **enterprise_stub_write_namespaces_api_lock_unlock**
> enterprise_stub_write_namespaces_api_lock_unlock()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_namespaces_api_lock_unlock()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_namespaces_api_lock_unlock: %s\n" % e)
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

# **enterprise_stub_write_namespaces_api_lock_unlock_path**
> enterprise_stub_write_namespaces_api_lock_unlock_path(path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 

    try:
        await api_instance.enterprise_stub_write_namespaces_api_lock_unlock_path(path)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_namespaces_api_lock_unlock_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

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

# **enterprise_stub_write_namespaces_path**
> enterprise_stub_write_namespaces_path(path)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 

    try:
        await api_instance.enterprise_stub_write_namespaces_path(path)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_namespaces_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

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

# **enterprise_stub_write_policies_egp_name**
> enterprise_stub_write_policies_egp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_policies_egp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_policies_egp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_policies_rgp_name**
> enterprise_stub_write_policies_rgp_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_policies_rgp_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_policies_rgp_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_quotas_lease_count_name**
> enterprise_stub_write_quotas_lease_count_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_quotas_lease_count_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_quotas_lease_count_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **enterprise_stub_write_replication_dr_primary_demote**
> enterprise_stub_write_replication_dr_primary_demote()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_primary_demote()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_primary_demote: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_primary_disable**
> enterprise_stub_write_replication_dr_primary_disable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_primary_disable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_primary_disable: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_primary_enable**
> enterprise_stub_write_replication_dr_primary_enable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_primary_enable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_primary_enable: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_primary_revoke_secondary**
> enterprise_stub_write_replication_dr_primary_revoke_secondary()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_primary_revoke_secondary()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_primary_revoke_secondary: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_primary_secondary_token**
> enterprise_stub_write_replication_dr_primary_secondary_token()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_primary_secondary_token()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_primary_secondary_token: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_config_reload_subsystem**
> enterprise_stub_write_replication_dr_secondary_config_reload_subsystem(subsystem)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    subsystem = 'subsystem_example' # str | 

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_config_reload_subsystem(subsystem)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_config_reload_subsystem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsystem** | **str**|  | 

### Return type

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

# **enterprise_stub_write_replication_dr_secondary_disable**
> enterprise_stub_write_replication_dr_secondary_disable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_disable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_disable: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_enable**
> enterprise_stub_write_replication_dr_secondary_enable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_enable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_enable: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_generate_public_key**
> enterprise_stub_write_replication_dr_secondary_generate_public_key()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_generate_public_key()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_generate_public_key: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_operation_token_delete**
> enterprise_stub_write_replication_dr_secondary_operation_token_delete()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_operation_token_delete()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_operation_token_delete: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_promote**
> enterprise_stub_write_replication_dr_secondary_promote()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_promote()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_promote: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_recover**
> enterprise_stub_write_replication_dr_secondary_recover()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_recover()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_recover: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_reindex**
> enterprise_stub_write_replication_dr_secondary_reindex()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_reindex()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_reindex: %s\n" % e)
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

# **enterprise_stub_write_replication_dr_secondary_update_primary**
> enterprise_stub_write_replication_dr_secondary_update_primary()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_dr_secondary_update_primary()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_dr_secondary_update_primary: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_primary_demote**
> enterprise_stub_write_replication_performance_primary_demote()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_primary_demote()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_primary_demote: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_primary_disable**
> enterprise_stub_write_replication_performance_primary_disable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_primary_disable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_primary_disable: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_primary_enable**
> enterprise_stub_write_replication_performance_primary_enable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_primary_enable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_primary_enable: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_primary_paths_filter_id**
> enterprise_stub_write_replication_performance_primary_paths_filter_id(id)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    id = 'id_example' # str | 

    try:
        await api_instance.enterprise_stub_write_replication_performance_primary_paths_filter_id(id)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_primary_paths_filter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

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

# **enterprise_stub_write_replication_performance_primary_revoke_secondary**
> enterprise_stub_write_replication_performance_primary_revoke_secondary()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_primary_revoke_secondary()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_primary_revoke_secondary: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_primary_secondary_token**
> enterprise_stub_write_replication_performance_primary_secondary_token()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_primary_secondary_token()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_primary_secondary_token: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_secondary_disable**
> enterprise_stub_write_replication_performance_secondary_disable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_secondary_disable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_secondary_disable: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_secondary_enable**
> enterprise_stub_write_replication_performance_secondary_enable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_secondary_enable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_secondary_enable: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_secondary_generate_public_key**
> enterprise_stub_write_replication_performance_secondary_generate_public_key()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_secondary_generate_public_key()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_secondary_generate_public_key: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_secondary_promote**
> enterprise_stub_write_replication_performance_secondary_promote()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_secondary_promote()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_secondary_promote: %s\n" % e)
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

# **enterprise_stub_write_replication_performance_secondary_update_primary**
> enterprise_stub_write_replication_performance_secondary_update_primary()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_performance_secondary_update_primary()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_performance_secondary_update_primary: %s\n" % e)
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

# **enterprise_stub_write_replication_primary_demote**
> enterprise_stub_write_replication_primary_demote()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_primary_demote()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_primary_demote: %s\n" % e)
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

# **enterprise_stub_write_replication_primary_disable**
> enterprise_stub_write_replication_primary_disable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_primary_disable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_primary_disable: %s\n" % e)
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

# **enterprise_stub_write_replication_primary_enable**
> enterprise_stub_write_replication_primary_enable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_primary_enable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_primary_enable: %s\n" % e)
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

# **enterprise_stub_write_replication_primary_revoke_secondary**
> enterprise_stub_write_replication_primary_revoke_secondary()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_primary_revoke_secondary()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_primary_revoke_secondary: %s\n" % e)
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

# **enterprise_stub_write_replication_primary_secondary_token**
> enterprise_stub_write_replication_primary_secondary_token()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_primary_secondary_token()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_primary_secondary_token: %s\n" % e)
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

# **enterprise_stub_write_replication_recover**
> enterprise_stub_write_replication_recover()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_recover()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_recover: %s\n" % e)
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

# **enterprise_stub_write_replication_reindex**
> enterprise_stub_write_replication_reindex()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_reindex()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_reindex: %s\n" % e)
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

# **enterprise_stub_write_replication_secondary_disable**
> enterprise_stub_write_replication_secondary_disable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_secondary_disable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_secondary_disable: %s\n" % e)
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

# **enterprise_stub_write_replication_secondary_enable**
> enterprise_stub_write_replication_secondary_enable()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_secondary_enable()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_secondary_enable: %s\n" % e)
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

# **enterprise_stub_write_replication_secondary_promote**
> enterprise_stub_write_replication_secondary_promote()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_secondary_promote()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_secondary_promote: %s\n" % e)
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

# **enterprise_stub_write_replication_secondary_update_primary**
> enterprise_stub_write_replication_secondary_update_primary()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_replication_secondary_update_primary()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_replication_secondary_update_primary: %s\n" % e)
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

# **enterprise_stub_write_sealwrap_rewrap**
> enterprise_stub_write_sealwrap_rewrap()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.enterprise_stub_write_sealwrap_rewrap()
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_sealwrap_rewrap: %s\n" % e)
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

# **enterprise_stub_write_storage_raft_snapshot_auto_config_name**
> enterprise_stub_write_storage_raft_snapshot_auto_config_name(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | 

    try:
        await api_instance.enterprise_stub_write_storage_raft_snapshot_auto_config_name(name)
    except Exception as e:
        print("Exception when calling SystemApi->enterprise_stub_write_storage_raft_snapshot_auto_config_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

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

# **generate_hash**
> GenerateHashResponse generate_hash(generate_hash_request)



### Example


```python
import ahvac
from ahvac.models.generate_hash_request import GenerateHashRequest
from ahvac.models.generate_hash_response import GenerateHashResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    generate_hash_request = ahvac.GenerateHashRequest() # GenerateHashRequest | 

    try:
        api_response = await api_instance.generate_hash(generate_hash_request)
        print("The response of SystemApi->generate_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->generate_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_hash_request** | [**GenerateHashRequest**](GenerateHashRequest.md)|  | 

### Return type

[**GenerateHashResponse**](GenerateHashResponse.md)

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

# **generate_hash_with_algorithm**
> GenerateHashWithAlgorithmResponse generate_hash_with_algorithm(urlalgorithm, generate_hash_with_algorithm_request)



### Example


```python
import ahvac
from ahvac.models.generate_hash_with_algorithm_request import GenerateHashWithAlgorithmRequest
from ahvac.models.generate_hash_with_algorithm_response import GenerateHashWithAlgorithmResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    urlalgorithm = 'urlalgorithm_example' # str | Algorithm to use (POST URL parameter)
    generate_hash_with_algorithm_request = ahvac.GenerateHashWithAlgorithmRequest() # GenerateHashWithAlgorithmRequest | 

    try:
        api_response = await api_instance.generate_hash_with_algorithm(urlalgorithm, generate_hash_with_algorithm_request)
        print("The response of SystemApi->generate_hash_with_algorithm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->generate_hash_with_algorithm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urlalgorithm** | **str**| Algorithm to use (POST URL parameter) | 
 **generate_hash_with_algorithm_request** | [**GenerateHashWithAlgorithmRequest**](GenerateHashWithAlgorithmRequest.md)|  | 

### Return type

[**GenerateHashWithAlgorithmResponse**](GenerateHashWithAlgorithmResponse.md)

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

# **generate_random**
> GenerateRandomResponse generate_random(generate_random_request)



### Example


```python
import ahvac
from ahvac.models.generate_random_request import GenerateRandomRequest
from ahvac.models.generate_random_response import GenerateRandomResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    generate_random_request = ahvac.GenerateRandomRequest() # GenerateRandomRequest | 

    try:
        api_response = await api_instance.generate_random(generate_random_request)
        print("The response of SystemApi->generate_random:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->generate_random: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_random_request** | [**GenerateRandomRequest**](GenerateRandomRequest.md)|  | 

### Return type

[**GenerateRandomResponse**](GenerateRandomResponse.md)

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

# **generate_random_with_bytes**
> GenerateRandomWithBytesResponse generate_random_with_bytes(urlbytes, generate_random_with_bytes_request)



### Example


```python
import ahvac
from ahvac.models.generate_random_with_bytes_request import GenerateRandomWithBytesRequest
from ahvac.models.generate_random_with_bytes_response import GenerateRandomWithBytesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    urlbytes = 'urlbytes_example' # str | The number of bytes to generate (POST URL parameter)
    generate_random_with_bytes_request = ahvac.GenerateRandomWithBytesRequest() # GenerateRandomWithBytesRequest | 

    try:
        api_response = await api_instance.generate_random_with_bytes(urlbytes, generate_random_with_bytes_request)
        print("The response of SystemApi->generate_random_with_bytes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->generate_random_with_bytes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urlbytes** | **str**| The number of bytes to generate (POST URL parameter) | 
 **generate_random_with_bytes_request** | [**GenerateRandomWithBytesRequest**](GenerateRandomWithBytesRequest.md)|  | 

### Return type

[**GenerateRandomWithBytesResponse**](GenerateRandomWithBytesResponse.md)

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

# **generate_random_with_source**
> GenerateRandomWithSourceResponse generate_random_with_source(source, generate_random_with_source_request)



### Example


```python
import ahvac
from ahvac.models.generate_random_with_source_request import GenerateRandomWithSourceRequest
from ahvac.models.generate_random_with_source_response import GenerateRandomWithSourceResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    source = 'platform' # str | Which system to source random data from, ether \"platform\", \"seal\", or \"all\". (default to 'platform')
    generate_random_with_source_request = ahvac.GenerateRandomWithSourceRequest() # GenerateRandomWithSourceRequest | 

    try:
        api_response = await api_instance.generate_random_with_source(source, generate_random_with_source_request)
        print("The response of SystemApi->generate_random_with_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->generate_random_with_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Which system to source random data from, ether \&quot;platform\&quot;, \&quot;seal\&quot;, or \&quot;all\&quot;. | [default to &#39;platform&#39;]
 **generate_random_with_source_request** | [**GenerateRandomWithSourceRequest**](GenerateRandomWithSourceRequest.md)|  | 

### Return type

[**GenerateRandomWithSourceResponse**](GenerateRandomWithSourceResponse.md)

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

# **generate_random_with_source_and_bytes**
> GenerateRandomWithSourceAndBytesResponse generate_random_with_source_and_bytes(source, urlbytes, generate_random_with_source_and_bytes_request)



### Example


```python
import ahvac
from ahvac.models.generate_random_with_source_and_bytes_request import GenerateRandomWithSourceAndBytesRequest
from ahvac.models.generate_random_with_source_and_bytes_response import GenerateRandomWithSourceAndBytesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    source = 'platform' # str | Which system to source random data from, ether \"platform\", \"seal\", or \"all\". (default to 'platform')
    urlbytes = 'urlbytes_example' # str | The number of bytes to generate (POST URL parameter)
    generate_random_with_source_and_bytes_request = ahvac.GenerateRandomWithSourceAndBytesRequest() # GenerateRandomWithSourceAndBytesRequest | 

    try:
        api_response = await api_instance.generate_random_with_source_and_bytes(source, urlbytes, generate_random_with_source_and_bytes_request)
        print("The response of SystemApi->generate_random_with_source_and_bytes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->generate_random_with_source_and_bytes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Which system to source random data from, ether \&quot;platform\&quot;, \&quot;seal\&quot;, or \&quot;all\&quot;. | [default to &#39;platform&#39;]
 **urlbytes** | **str**| The number of bytes to generate (POST URL parameter) | 
 **generate_random_with_source_and_bytes_request** | [**GenerateRandomWithSourceAndBytesRequest**](GenerateRandomWithSourceAndBytesRequest.md)|  | 

### Return type

[**GenerateRandomWithSourceAndBytesResponse**](GenerateRandomWithSourceAndBytesResponse.md)

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

# **ha_status**
> HaStatusResponse ha_status()

Check the HA status of a Vault cluster

### Example


```python
import ahvac
from ahvac.models.ha_status_response import HaStatusResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Check the HA status of a Vault cluster
        api_response = await api_instance.ha_status()
        print("The response of SystemApi->ha_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->ha_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HaStatusResponse**](HaStatusResponse.md)

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

# **initialize**
> initialize(initialize_request)

Initialize a new Vault.

The Vault must not have been previously initialized. The recovery options, as well as the stored shares option, are only available when using Vault HSM.

### Example


```python
import ahvac
from ahvac.models.initialize_request import InitializeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    initialize_request = ahvac.InitializeRequest() # InitializeRequest | 

    try:
        # Initialize a new Vault.
        await api_instance.initialize(initialize_request)
    except Exception as e:
        print("Exception when calling SystemApi->initialize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initialize_request** | [**InitializeRequest**](InitializeRequest.md)|  | 

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

# **internal_client_activity_configure**
> internal_client_activity_configure(internal_client_activity_configure_request)

Enable or disable collection of client count, set retention period, or set default reporting period.

### Example


```python
import ahvac
from ahvac.models.internal_client_activity_configure_request import InternalClientActivityConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    internal_client_activity_configure_request = ahvac.InternalClientActivityConfigureRequest() # InternalClientActivityConfigureRequest | 

    try:
        # Enable or disable collection of client count, set retention period, or set default reporting period.
        await api_instance.internal_client_activity_configure(internal_client_activity_configure_request)
    except Exception as e:
        print("Exception when calling SystemApi->internal_client_activity_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_client_activity_configure_request** | [**InternalClientActivityConfigureRequest**](InternalClientActivityConfigureRequest.md)|  | 

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

# **internal_client_activity_export**
> internal_client_activity_export()

Report the client count metrics, for this namespace and all child namespaces.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Report the client count metrics, for this namespace and all child namespaces.
        await api_instance.internal_client_activity_export()
    except Exception as e:
        print("Exception when calling SystemApi->internal_client_activity_export: %s\n" % e)
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

# **internal_client_activity_read_configuration**
> internal_client_activity_read_configuration()

Read the client count tracking configuration.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Read the client count tracking configuration.
        await api_instance.internal_client_activity_read_configuration()
    except Exception as e:
        print("Exception when calling SystemApi->internal_client_activity_read_configuration: %s\n" % e)
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

# **internal_client_activity_report_counts**
> internal_client_activity_report_counts()

Report the client count metrics, for this namespace and all child namespaces.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Report the client count metrics, for this namespace and all child namespaces.
        await api_instance.internal_client_activity_report_counts()
    except Exception as e:
        print("Exception when calling SystemApi->internal_client_activity_report_counts: %s\n" % e)
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

# **internal_client_activity_report_counts_this_month**
> internal_client_activity_report_counts_this_month()

Report the number of clients for this month, for this namespace and all child namespaces.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Report the number of clients for this month, for this namespace and all child namespaces.
        await api_instance.internal_client_activity_report_counts_this_month()
    except Exception as e:
        print("Exception when calling SystemApi->internal_client_activity_report_counts_this_month: %s\n" % e)
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

# **internal_count_entities**
> InternalCountEntitiesResponse internal_count_entities()

Backwards compatibility is not guaranteed for this API

### Example


```python
import ahvac
from ahvac.models.internal_count_entities_response import InternalCountEntitiesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Backwards compatibility is not guaranteed for this API
        api_response = await api_instance.internal_count_entities()
        print("The response of SystemApi->internal_count_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->internal_count_entities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalCountEntitiesResponse**](InternalCountEntitiesResponse.md)

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

# **internal_count_requests**
> internal_count_requests()

Backwards compatibility is not guaranteed for this API

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Backwards compatibility is not guaranteed for this API
        await api_instance.internal_count_requests()
    except Exception as e:
        print("Exception when calling SystemApi->internal_count_requests: %s\n" % e)
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

# **internal_count_tokens**
> InternalCountTokensResponse internal_count_tokens()

Backwards compatibility is not guaranteed for this API

### Example


```python
import ahvac
from ahvac.models.internal_count_tokens_response import InternalCountTokensResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Backwards compatibility is not guaranteed for this API
        api_response = await api_instance.internal_count_tokens()
        print("The response of SystemApi->internal_count_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->internal_count_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalCountTokensResponse**](InternalCountTokensResponse.md)

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

# **internal_generate_open_api_document**
> internal_generate_open_api_document(context=context, generic_mount_paths=generic_mount_paths)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    context = 'context_example' # str | Context string appended to every operationId (optional)
    generic_mount_paths = False # bool | Use generic mount paths (optional) (default to False)

    try:
        await api_instance.internal_generate_open_api_document(context=context, generic_mount_paths=generic_mount_paths)
    except Exception as e:
        print("Exception when calling SystemApi->internal_generate_open_api_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| Context string appended to every operationId | [optional] 
 **generic_mount_paths** | **bool**| Use generic mount paths | [optional] [default to False]

### Return type

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

# **internal_generate_open_api_document_with_parameters**
> internal_generate_open_api_document_with_parameters(internal_generate_open_api_document_with_parameters_request)



### Example


```python
import ahvac
from ahvac.models.internal_generate_open_api_document_with_parameters_request import InternalGenerateOpenApiDocumentWithParametersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    internal_generate_open_api_document_with_parameters_request = ahvac.InternalGenerateOpenApiDocumentWithParametersRequest() # InternalGenerateOpenApiDocumentWithParametersRequest | 

    try:
        await api_instance.internal_generate_open_api_document_with_parameters(internal_generate_open_api_document_with_parameters_request)
    except Exception as e:
        print("Exception when calling SystemApi->internal_generate_open_api_document_with_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_generate_open_api_document_with_parameters_request** | [**InternalGenerateOpenApiDocumentWithParametersRequest**](InternalGenerateOpenApiDocumentWithParametersRequest.md)|  | 

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

# **internal_inspect_router**
> internal_inspect_router(tag)

Expose the route entry and mount entry tables present in the router

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    tag = 'tag_example' # str | Name of subtree being observed

    try:
        # Expose the route entry and mount entry tables present in the router
        await api_instance.internal_inspect_router(tag)
    except Exception as e:
        print("Exception when calling SystemApi->internal_inspect_router: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Name of subtree being observed | 

### Return type

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

# **internal_ui_list_enabled_feature_flags**
> InternalUiListEnabledFeatureFlagsResponse internal_ui_list_enabled_feature_flags()

Lists enabled feature flags.

### Example


```python
import ahvac
from ahvac.models.internal_ui_list_enabled_feature_flags_response import InternalUiListEnabledFeatureFlagsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Lists enabled feature flags.
        api_response = await api_instance.internal_ui_list_enabled_feature_flags()
        print("The response of SystemApi->internal_ui_list_enabled_feature_flags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->internal_ui_list_enabled_feature_flags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalUiListEnabledFeatureFlagsResponse**](InternalUiListEnabledFeatureFlagsResponse.md)

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

# **internal_ui_list_enabled_visible_mounts**
> InternalUiListEnabledVisibleMountsResponse internal_ui_list_enabled_visible_mounts()

Lists all enabled and visible auth and secrets mounts.

### Example


```python
import ahvac
from ahvac.models.internal_ui_list_enabled_visible_mounts_response import InternalUiListEnabledVisibleMountsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Lists all enabled and visible auth and secrets mounts.
        api_response = await api_instance.internal_ui_list_enabled_visible_mounts()
        print("The response of SystemApi->internal_ui_list_enabled_visible_mounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->internal_ui_list_enabled_visible_mounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalUiListEnabledVisibleMountsResponse**](InternalUiListEnabledVisibleMountsResponse.md)

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

# **internal_ui_list_namespaces**
> InternalUiListNamespacesResponse internal_ui_list_namespaces()

Backwards compatibility is not guaranteed for this API

### Example


```python
import ahvac
from ahvac.models.internal_ui_list_namespaces_response import InternalUiListNamespacesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Backwards compatibility is not guaranteed for this API
        api_response = await api_instance.internal_ui_list_namespaces()
        print("The response of SystemApi->internal_ui_list_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->internal_ui_list_namespaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalUiListNamespacesResponse**](InternalUiListNamespacesResponse.md)

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

# **internal_ui_read_mount_information**
> InternalUiReadMountInformationResponse internal_ui_read_mount_information(path)

Return information about the given mount.

### Example


```python
import ahvac
from ahvac.models.internal_ui_read_mount_information_response import InternalUiReadMountInformationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path of the mount.

    try:
        # Return information about the given mount.
        api_response = await api_instance.internal_ui_read_mount_information(path)
        print("The response of SystemApi->internal_ui_read_mount_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->internal_ui_read_mount_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the mount. | 

### Return type

[**InternalUiReadMountInformationResponse**](InternalUiReadMountInformationResponse.md)

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

# **internal_ui_read_resultant_acl**
> InternalUiReadResultantAclResponse internal_ui_read_resultant_acl()

Backwards compatibility is not guaranteed for this API

### Example


```python
import ahvac
from ahvac.models.internal_ui_read_resultant_acl_response import InternalUiReadResultantAclResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Backwards compatibility is not guaranteed for this API
        api_response = await api_instance.internal_ui_read_resultant_acl()
        print("The response of SystemApi->internal_ui_read_resultant_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->internal_ui_read_resultant_acl: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InternalUiReadResultantAclResponse**](InternalUiReadResultantAclResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | empty response returned if no client token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leader_status**
> LeaderStatusResponse leader_status()

Returns the high availability status and current leader instance of Vault.

### Example


```python
import ahvac
from ahvac.models.leader_status_response import LeaderStatusResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns the high availability status and current leader instance of Vault.
        api_response = await api_instance.leader_status()
        print("The response of SystemApi->leader_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->leader_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LeaderStatusResponse**](LeaderStatusResponse.md)

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

# **leases_count**
> LeasesCountResponse leases_count()



### Example


```python
import ahvac
from ahvac.models.leases_count_response import LeasesCountResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        api_response = await api_instance.leases_count()
        print("The response of SystemApi->leases_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->leases_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LeasesCountResponse**](LeasesCountResponse.md)

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

# **leases_force_revoke_lease_with_prefix**
> leases_force_revoke_lease_with_prefix(prefix)

Revokes all secrets or tokens generated under a given prefix immediately

Unlike `/sys/leases/revoke-prefix`, this path ignores backend errors encountered during revocation. This is potentially very dangerous and should only be used in specific emergency situations where errors in the backend or the connected backend service prevent normal revocation.  By ignoring these errors, Vault abdicates responsibility for ensuring that the issued credentials or secrets are properly revoked and/or cleaned up. Access to this endpoint should be tightly controlled.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"

    try:
        # Revokes all secrets or tokens generated under a given prefix immediately
        await api_instance.leases_force_revoke_lease_with_prefix(prefix)
    except Exception as e:
        print("Exception when calling SystemApi->leases_force_revoke_lease_with_prefix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_force_revoke_lease_with_prefix2**
> leases_force_revoke_lease_with_prefix2(prefix)

Revokes all secrets or tokens generated under a given prefix immediately

Unlike `/sys/leases/revoke-prefix`, this path ignores backend errors encountered during revocation. This is potentially very dangerous and should only be used in specific emergency situations where errors in the backend or the connected backend service prevent normal revocation.  By ignoring these errors, Vault abdicates responsibility for ensuring that the issued credentials or secrets are properly revoked and/or cleaned up. Access to this endpoint should be tightly controlled.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"

    try:
        # Revokes all secrets or tokens generated under a given prefix immediately
        await api_instance.leases_force_revoke_lease_with_prefix2(prefix)
    except Exception as e:
        print("Exception when calling SystemApi->leases_force_revoke_lease_with_prefix2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_list**
> LeasesListResponse leases_list()



### Example


```python
import ahvac
from ahvac.models.leases_list_response import LeasesListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        api_response = await api_instance.leases_list()
        print("The response of SystemApi->leases_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->leases_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LeasesListResponse**](LeasesListResponse.md)

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

# **leases_look_up**
> LeasesLookUpResponse leases_look_up(prefix, list)



### Example


```python
import ahvac
from ahvac.models.leases_look_up_response import LeasesLookUpResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    prefix = 'prefix_example' # str | The path to list leases under. Example: \"aws/creds/deploy\"
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.leases_look_up(prefix, list)
        print("The response of SystemApi->leases_look_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->leases_look_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to list leases under. Example: \&quot;aws/creds/deploy\&quot; | 
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**LeasesLookUpResponse**](LeasesLookUpResponse.md)

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

# **leases_read_lease**
> LeasesReadLeaseResponse leases_read_lease(leases_read_lease_request)



### Example


```python
import ahvac
from ahvac.models.leases_read_lease_request import LeasesReadLeaseRequest
from ahvac.models.leases_read_lease_response import LeasesReadLeaseResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    leases_read_lease_request = ahvac.LeasesReadLeaseRequest() # LeasesReadLeaseRequest | 

    try:
        api_response = await api_instance.leases_read_lease(leases_read_lease_request)
        print("The response of SystemApi->leases_read_lease:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->leases_read_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leases_read_lease_request** | [**LeasesReadLeaseRequest**](LeasesReadLeaseRequest.md)|  | 

### Return type

[**LeasesReadLeaseResponse**](LeasesReadLeaseResponse.md)

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

# **leases_renew_lease**
> leases_renew_lease(leases_renew_lease_request)

Renews a lease, requesting to extend the lease.

### Example


```python
import ahvac
from ahvac.models.leases_renew_lease_request import LeasesRenewLeaseRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    leases_renew_lease_request = ahvac.LeasesRenewLeaseRequest() # LeasesRenewLeaseRequest | 

    try:
        # Renews a lease, requesting to extend the lease.
        await api_instance.leases_renew_lease(leases_renew_lease_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_renew_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leases_renew_lease_request** | [**LeasesRenewLeaseRequest**](LeasesRenewLeaseRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_renew_lease2**
> leases_renew_lease2(leases_renew_lease2_request)

Renews a lease, requesting to extend the lease.

### Example


```python
import ahvac
from ahvac.models.leases_renew_lease2_request import LeasesRenewLease2Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    leases_renew_lease2_request = ahvac.LeasesRenewLease2Request() # LeasesRenewLease2Request | 

    try:
        # Renews a lease, requesting to extend the lease.
        await api_instance.leases_renew_lease2(leases_renew_lease2_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_renew_lease2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leases_renew_lease2_request** | [**LeasesRenewLease2Request**](LeasesRenewLease2Request.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_renew_lease_with_id**
> leases_renew_lease_with_id(url_lease_id, leases_renew_lease_with_id_request)

Renews a lease, requesting to extend the lease.

### Example


```python
import ahvac
from ahvac.models.leases_renew_lease_with_id_request import LeasesRenewLeaseWithIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
    leases_renew_lease_with_id_request = ahvac.LeasesRenewLeaseWithIdRequest() # LeasesRenewLeaseWithIdRequest | 

    try:
        # Renews a lease, requesting to extend the lease.
        await api_instance.leases_renew_lease_with_id(url_lease_id, leases_renew_lease_with_id_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_renew_lease_with_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **leases_renew_lease_with_id_request** | [**LeasesRenewLeaseWithIdRequest**](LeasesRenewLeaseWithIdRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_renew_lease_with_id2**
> leases_renew_lease_with_id2(url_lease_id, leases_renew_lease_with_id2_request)

Renews a lease, requesting to extend the lease.

### Example


```python
import ahvac
from ahvac.models.leases_renew_lease_with_id2_request import LeasesRenewLeaseWithId2Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
    leases_renew_lease_with_id2_request = ahvac.LeasesRenewLeaseWithId2Request() # LeasesRenewLeaseWithId2Request | 

    try:
        # Renews a lease, requesting to extend the lease.
        await api_instance.leases_renew_lease_with_id2(url_lease_id, leases_renew_lease_with_id2_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_renew_lease_with_id2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **leases_renew_lease_with_id2_request** | [**LeasesRenewLeaseWithId2Request**](LeasesRenewLeaseWithId2Request.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_revoke_lease**
> leases_revoke_lease(leases_revoke_lease_request)

Revokes a lease immediately.

### Example


```python
import ahvac
from ahvac.models.leases_revoke_lease_request import LeasesRevokeLeaseRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    leases_revoke_lease_request = ahvac.LeasesRevokeLeaseRequest() # LeasesRevokeLeaseRequest | 

    try:
        # Revokes a lease immediately.
        await api_instance.leases_revoke_lease(leases_revoke_lease_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_revoke_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leases_revoke_lease_request** | [**LeasesRevokeLeaseRequest**](LeasesRevokeLeaseRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_revoke_lease2**
> leases_revoke_lease2(leases_revoke_lease2_request)

Revokes a lease immediately.

### Example


```python
import ahvac
from ahvac.models.leases_revoke_lease2_request import LeasesRevokeLease2Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    leases_revoke_lease2_request = ahvac.LeasesRevokeLease2Request() # LeasesRevokeLease2Request | 

    try:
        # Revokes a lease immediately.
        await api_instance.leases_revoke_lease2(leases_revoke_lease2_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_revoke_lease2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leases_revoke_lease2_request** | [**LeasesRevokeLease2Request**](LeasesRevokeLease2Request.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_revoke_lease_with_id**
> leases_revoke_lease_with_id(url_lease_id, leases_revoke_lease_with_id_request)

Revokes a lease immediately.

### Example


```python
import ahvac
from ahvac.models.leases_revoke_lease_with_id_request import LeasesRevokeLeaseWithIdRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
    leases_revoke_lease_with_id_request = ahvac.LeasesRevokeLeaseWithIdRequest() # LeasesRevokeLeaseWithIdRequest | 

    try:
        # Revokes a lease immediately.
        await api_instance.leases_revoke_lease_with_id(url_lease_id, leases_revoke_lease_with_id_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_revoke_lease_with_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **leases_revoke_lease_with_id_request** | [**LeasesRevokeLeaseWithIdRequest**](LeasesRevokeLeaseWithIdRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_revoke_lease_with_id2**
> leases_revoke_lease_with_id2(url_lease_id, leases_revoke_lease_with_id2_request)

Revokes a lease immediately.

### Example


```python
import ahvac
from ahvac.models.leases_revoke_lease_with_id2_request import LeasesRevokeLeaseWithId2Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    url_lease_id = 'url_lease_id_example' # str | The lease identifier to renew. This is included with a lease.
    leases_revoke_lease_with_id2_request = ahvac.LeasesRevokeLeaseWithId2Request() # LeasesRevokeLeaseWithId2Request | 

    try:
        # Revokes a lease immediately.
        await api_instance.leases_revoke_lease_with_id2(url_lease_id, leases_revoke_lease_with_id2_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_revoke_lease_with_id2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_lease_id** | **str**| The lease identifier to renew. This is included with a lease. | 
 **leases_revoke_lease_with_id2_request** | [**LeasesRevokeLeaseWithId2Request**](LeasesRevokeLeaseWithId2Request.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_revoke_lease_with_prefix**
> leases_revoke_lease_with_prefix(prefix, leases_revoke_lease_with_prefix_request)

Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.

### Example


```python
import ahvac
from ahvac.models.leases_revoke_lease_with_prefix_request import LeasesRevokeLeaseWithPrefixRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"
    leases_revoke_lease_with_prefix_request = ahvac.LeasesRevokeLeaseWithPrefixRequest() # LeasesRevokeLeaseWithPrefixRequest | 

    try:
        # Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.
        await api_instance.leases_revoke_lease_with_prefix(prefix, leases_revoke_lease_with_prefix_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_revoke_lease_with_prefix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 
 **leases_revoke_lease_with_prefix_request** | [**LeasesRevokeLeaseWithPrefixRequest**](LeasesRevokeLeaseWithPrefixRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_revoke_lease_with_prefix2**
> leases_revoke_lease_with_prefix2(prefix, leases_revoke_lease_with_prefix2_request)

Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.

### Example


```python
import ahvac
from ahvac.models.leases_revoke_lease_with_prefix2_request import LeasesRevokeLeaseWithPrefix2Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    prefix = 'prefix_example' # str | The path to revoke keys under. Example: \"prod/aws/ops\"
    leases_revoke_lease_with_prefix2_request = ahvac.LeasesRevokeLeaseWithPrefix2Request() # LeasesRevokeLeaseWithPrefix2Request | 

    try:
        # Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.
        await api_instance.leases_revoke_lease_with_prefix2(prefix, leases_revoke_lease_with_prefix2_request)
    except Exception as e:
        print("Exception when calling SystemApi->leases_revoke_lease_with_prefix2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The path to revoke keys under. Example: \&quot;prod/aws/ops\&quot; | 
 **leases_revoke_lease_with_prefix2_request** | [**LeasesRevokeLeaseWithPrefix2Request**](LeasesRevokeLeaseWithPrefix2Request.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leases_tidy**
> leases_tidy()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.leases_tidy()
    except Exception as e:
        print("Exception when calling SystemApi->leases_tidy: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_experimental_features**
> list_experimental_features()

Returns the available and enabled experiments

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns the available and enabled experiments
        await api_instance.list_experimental_features()
    except Exception as e:
        print("Exception when calling SystemApi->list_experimental_features: %s\n" % e)
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

# **locked_users_list**
> locked_users_list()

Report the locked user count metrics, for this namespace and all child namespaces.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Report the locked user count metrics, for this namespace and all child namespaces.
        await api_instance.locked_users_list()
    except Exception as e:
        print("Exception when calling SystemApi->locked_users_list: %s\n" % e)
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

# **locked_users_unlock**
> locked_users_unlock(alias_identifier, mount_accessor)

Unlocks the user with given mount_accessor and alias_identifier

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    alias_identifier = 'alias_identifier_example' # str | It is the name of the alias (user). For example, if the alias belongs to userpass backend, the name should be a valid username within userpass auth method. If the alias belongs to an approle auth method, the name should be a valid RoleID
    mount_accessor = 'mount_accessor_example' # str | MountAccessor is the identifier of the mount entry to which the user belongs

    try:
        # Unlocks the user with given mount_accessor and alias_identifier
        await api_instance.locked_users_unlock(alias_identifier, mount_accessor)
    except Exception as e:
        print("Exception when calling SystemApi->locked_users_unlock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias_identifier** | **str**| It is the name of the alias (user). For example, if the alias belongs to userpass backend, the name should be a valid username within userpass auth method. If the alias belongs to an approle auth method, the name should be a valid RoleID | 
 **mount_accessor** | **str**| MountAccessor is the identifier of the mount entry to which the user belongs | 

### Return type

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

# **loggers_read_verbosity_level**
> loggers_read_verbosity_level()

Read the log level for all existing loggers.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Read the log level for all existing loggers.
        await api_instance.loggers_read_verbosity_level()
    except Exception as e:
        print("Exception when calling SystemApi->loggers_read_verbosity_level: %s\n" % e)
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

# **loggers_read_verbosity_level_for**
> loggers_read_verbosity_level_for(name)

Read the log level for a single logger.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the logger to be modified.

    try:
        # Read the log level for a single logger.
        await api_instance.loggers_read_verbosity_level_for(name)
    except Exception as e:
        print("Exception when calling SystemApi->loggers_read_verbosity_level_for: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the logger to be modified. | 

### Return type

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

# **loggers_revert_verbosity_level**
> loggers_revert_verbosity_level()

Revert the all loggers to use log level provided in config.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Revert the all loggers to use log level provided in config.
        await api_instance.loggers_revert_verbosity_level()
    except Exception as e:
        print("Exception when calling SystemApi->loggers_revert_verbosity_level: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loggers_revert_verbosity_level_for**
> loggers_revert_verbosity_level_for(name)

Revert a single logger to use log level provided in config.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the logger to be modified.

    try:
        # Revert a single logger to use log level provided in config.
        await api_instance.loggers_revert_verbosity_level_for(name)
    except Exception as e:
        print("Exception when calling SystemApi->loggers_revert_verbosity_level_for: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the logger to be modified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loggers_update_verbosity_level**
> loggers_update_verbosity_level(loggers_update_verbosity_level_request)

Modify the log level for all existing loggers.

### Example


```python
import ahvac
from ahvac.models.loggers_update_verbosity_level_request import LoggersUpdateVerbosityLevelRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    loggers_update_verbosity_level_request = ahvac.LoggersUpdateVerbosityLevelRequest() # LoggersUpdateVerbosityLevelRequest | 

    try:
        # Modify the log level for all existing loggers.
        await api_instance.loggers_update_verbosity_level(loggers_update_verbosity_level_request)
    except Exception as e:
        print("Exception when calling SystemApi->loggers_update_verbosity_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loggers_update_verbosity_level_request** | [**LoggersUpdateVerbosityLevelRequest**](LoggersUpdateVerbosityLevelRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loggers_update_verbosity_level_for**
> loggers_update_verbosity_level_for(name, loggers_update_verbosity_level_for_request)

Modify the log level of a single logger.

### Example


```python
import ahvac
from ahvac.models.loggers_update_verbosity_level_for_request import LoggersUpdateVerbosityLevelForRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the logger to be modified.
    loggers_update_verbosity_level_for_request = ahvac.LoggersUpdateVerbosityLevelForRequest() # LoggersUpdateVerbosityLevelForRequest | 

    try:
        # Modify the log level of a single logger.
        await api_instance.loggers_update_verbosity_level_for(name, loggers_update_verbosity_level_for_request)
    except Exception as e:
        print("Exception when calling SystemApi->loggers_update_verbosity_level_for: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the logger to be modified. | 
 **loggers_update_verbosity_level_for_request** | [**LoggersUpdateVerbosityLevelForRequest**](LoggersUpdateVerbosityLevelForRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics**
> metrics(format=format)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    format = 'format_example' # str | Format to export metrics into. Currently accepts only \"prometheus\". (optional)

    try:
        await api_instance.metrics(format=format)
    except Exception as e:
        print("Exception when calling SystemApi->metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Format to export metrics into. Currently accepts only \&quot;prometheus\&quot;. | [optional] 

### Return type

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

# **mfa_validate**
> mfa_validate(mfa_validate_request)

Validates the login for the given MFA methods. Upon successful validation, it returns an auth response containing the client token

### Example


```python
import ahvac
from ahvac.models.mfa_validate_request import MfaValidateRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    mfa_validate_request = ahvac.MfaValidateRequest() # MfaValidateRequest | 

    try:
        # Validates the login for the given MFA methods. Upon successful validation, it returns an auth response containing the client token
        await api_instance.mfa_validate(mfa_validate_request)
    except Exception as e:
        print("Exception when calling SystemApi->mfa_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_validate_request** | [**MfaValidateRequest**](MfaValidateRequest.md)|  | 

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

# **monitor**
> monitor(log_format=log_format, log_level=log_level)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    log_format = 'standard' # str | Output format of logs. Supported values are \"standard\" and \"json\". The default is \"standard\". (optional) (default to 'standard')
    log_level = 'log_level_example' # str | Log level to view system logs at. Currently supported values are \"trace\", \"debug\", \"info\", \"warn\", \"error\". (optional)

    try:
        await api_instance.monitor(log_format=log_format, log_level=log_level)
    except Exception as e:
        print("Exception when calling SystemApi->monitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_format** | **str**| Output format of logs. Supported values are \&quot;standard\&quot; and \&quot;json\&quot;. The default is \&quot;standard\&quot;. | [optional] [default to &#39;standard&#39;]
 **log_level** | **str**| Log level to view system logs at. Currently supported values are \&quot;trace\&quot;, \&quot;debug\&quot;, \&quot;info\&quot;, \&quot;warn\&quot;, \&quot;error\&quot;. | [optional] 

### Return type

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

# **mounts_disable_secrets_engine**
> mounts_disable_secrets_engine(path)

Disable the mount point specified at the given path.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Example: \"aws/east\"

    try:
        # Disable the mount point specified at the given path.
        await api_instance.mounts_disable_secrets_engine(path)
    except Exception as e:
        print("Exception when calling SystemApi->mounts_disable_secrets_engine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 

### Return type

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

# **mounts_enable_secrets_engine**
> mounts_enable_secrets_engine(path, mounts_enable_secrets_engine_request)

Enable a new secrets engine at the given path.

### Example


```python
import ahvac
from ahvac.models.mounts_enable_secrets_engine_request import MountsEnableSecretsEngineRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Example: \"aws/east\"
    mounts_enable_secrets_engine_request = ahvac.MountsEnableSecretsEngineRequest() # MountsEnableSecretsEngineRequest | 

    try:
        # Enable a new secrets engine at the given path.
        await api_instance.mounts_enable_secrets_engine(path, mounts_enable_secrets_engine_request)
    except Exception as e:
        print("Exception when calling SystemApi->mounts_enable_secrets_engine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 
 **mounts_enable_secrets_engine_request** | [**MountsEnableSecretsEngineRequest**](MountsEnableSecretsEngineRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_list_secrets_engines**
> mounts_list_secrets_engines()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.mounts_list_secrets_engines()
    except Exception as e:
        print("Exception when calling SystemApi->mounts_list_secrets_engines: %s\n" % e)
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

# **mounts_read_configuration**
> MountsReadConfigurationResponse mounts_read_configuration(path)

Read the configuration of the secret engine at the given path.

### Example


```python
import ahvac
from ahvac.models.mounts_read_configuration_response import MountsReadConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Example: \"aws/east\"

    try:
        # Read the configuration of the secret engine at the given path.
        api_response = await api_instance.mounts_read_configuration(path)
        print("The response of SystemApi->mounts_read_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->mounts_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 

### Return type

[**MountsReadConfigurationResponse**](MountsReadConfigurationResponse.md)

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

# **mounts_read_tuning_information**
> MountsReadTuningInformationResponse mounts_read_tuning_information(path)



### Example


```python
import ahvac
from ahvac.models.mounts_read_tuning_information_response import MountsReadTuningInformationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Example: \"aws/east\"

    try:
        api_response = await api_instance.mounts_read_tuning_information(path)
        print("The response of SystemApi->mounts_read_tuning_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->mounts_read_tuning_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 

### Return type

[**MountsReadTuningInformationResponse**](MountsReadTuningInformationResponse.md)

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

# **mounts_tune_configuration_parameters**
> mounts_tune_configuration_parameters(path, mounts_tune_configuration_parameters_request)



### Example


```python
import ahvac
from ahvac.models.mounts_tune_configuration_parameters_request import MountsTuneConfigurationParametersRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | The path to mount to. Example: \"aws/east\"
    mounts_tune_configuration_parameters_request = ahvac.MountsTuneConfigurationParametersRequest() # MountsTuneConfigurationParametersRequest | 

    try:
        await api_instance.mounts_tune_configuration_parameters(path, mounts_tune_configuration_parameters_request)
    except Exception as e:
        print("Exception when calling SystemApi->mounts_tune_configuration_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to mount to. Example: \&quot;aws/east\&quot; | 
 **mounts_tune_configuration_parameters_request** | [**MountsTuneConfigurationParametersRequest**](MountsTuneConfigurationParametersRequest.md)|  | 

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

# **plugins_catalog_list_plugins**
> PluginsCatalogListPluginsResponse plugins_catalog_list_plugins()



### Example


```python
import ahvac
from ahvac.models.plugins_catalog_list_plugins_response import PluginsCatalogListPluginsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        api_response = await api_instance.plugins_catalog_list_plugins()
        print("The response of SystemApi->plugins_catalog_list_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_list_plugins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PluginsCatalogListPluginsResponse**](PluginsCatalogListPluginsResponse.md)

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

# **plugins_catalog_list_plugins_with_type**
> PluginsCatalogListPluginsWithTypeResponse plugins_catalog_list_plugins_with_type(type, list)

List the plugins in the catalog.

### Example


```python
import ahvac
from ahvac.models.plugins_catalog_list_plugins_with_type_response import PluginsCatalogListPluginsWithTypeResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    type = 'type_example' # str | The type of the plugin, may be auth, secret, or database
    list = 'list_example' # str | Must be set to `true`

    try:
        # List the plugins in the catalog.
        api_response = await api_instance.plugins_catalog_list_plugins_with_type(type, list)
        print("The response of SystemApi->plugins_catalog_list_plugins_with_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_list_plugins_with_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**PluginsCatalogListPluginsWithTypeResponse**](PluginsCatalogListPluginsWithTypeResponse.md)

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

# **plugins_catalog_read_plugin_configuration**
> PluginsCatalogReadPluginConfigurationResponse plugins_catalog_read_plugin_configuration(name)

Return the configuration data for the plugin with the given name.

### Example


```python
import ahvac
from ahvac.models.plugins_catalog_read_plugin_configuration_response import PluginsCatalogReadPluginConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin

    try:
        # Return the configuration data for the plugin with the given name.
        api_response = await api_instance.plugins_catalog_read_plugin_configuration(name)
        print("The response of SystemApi->plugins_catalog_read_plugin_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_read_plugin_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 

### Return type

[**PluginsCatalogReadPluginConfigurationResponse**](PluginsCatalogReadPluginConfigurationResponse.md)

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

# **plugins_catalog_read_plugin_configuration_with_type**
> PluginsCatalogReadPluginConfigurationWithTypeResponse plugins_catalog_read_plugin_configuration_with_type(name, type)

Return the configuration data for the plugin with the given name.

### Example


```python
import ahvac
from ahvac.models.plugins_catalog_read_plugin_configuration_with_type_response import PluginsCatalogReadPluginConfigurationWithTypeResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin
    type = 'type_example' # str | The type of the plugin, may be auth, secret, or database

    try:
        # Return the configuration data for the plugin with the given name.
        api_response = await api_instance.plugins_catalog_read_plugin_configuration_with_type(name, type)
        print("The response of SystemApi->plugins_catalog_read_plugin_configuration_with_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_read_plugin_configuration_with_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 

### Return type

[**PluginsCatalogReadPluginConfigurationWithTypeResponse**](PluginsCatalogReadPluginConfigurationWithTypeResponse.md)

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

# **plugins_catalog_register_plugin**
> plugins_catalog_register_plugin(name, plugins_catalog_register_plugin_request)

Register a new plugin, or updates an existing one with the supplied name.

### Example


```python
import ahvac
from ahvac.models.plugins_catalog_register_plugin_request import PluginsCatalogRegisterPluginRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin
    plugins_catalog_register_plugin_request = ahvac.PluginsCatalogRegisterPluginRequest() # PluginsCatalogRegisterPluginRequest | 

    try:
        # Register a new plugin, or updates an existing one with the supplied name.
        await api_instance.plugins_catalog_register_plugin(name, plugins_catalog_register_plugin_request)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_register_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **plugins_catalog_register_plugin_request** | [**PluginsCatalogRegisterPluginRequest**](PluginsCatalogRegisterPluginRequest.md)|  | 

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

# **plugins_catalog_register_plugin_with_type**
> plugins_catalog_register_plugin_with_type(name, type, plugins_catalog_register_plugin_with_type_request)

Register a new plugin, or updates an existing one with the supplied name.

### Example


```python
import ahvac
from ahvac.models.plugins_catalog_register_plugin_with_type_request import PluginsCatalogRegisterPluginWithTypeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin
    type = 'type_example' # str | The type of the plugin, may be auth, secret, or database
    plugins_catalog_register_plugin_with_type_request = ahvac.PluginsCatalogRegisterPluginWithTypeRequest() # PluginsCatalogRegisterPluginWithTypeRequest | 

    try:
        # Register a new plugin, or updates an existing one with the supplied name.
        await api_instance.plugins_catalog_register_plugin_with_type(name, type, plugins_catalog_register_plugin_with_type_request)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_register_plugin_with_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 
 **plugins_catalog_register_plugin_with_type_request** | [**PluginsCatalogRegisterPluginWithTypeRequest**](PluginsCatalogRegisterPluginWithTypeRequest.md)|  | 

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

# **plugins_catalog_remove_plugin**
> plugins_catalog_remove_plugin(name)

Remove the plugin with the given name.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin

    try:
        # Remove the plugin with the given name.
        await api_instance.plugins_catalog_remove_plugin(name)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_remove_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 

### Return type

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

# **plugins_catalog_remove_plugin_with_type**
> plugins_catalog_remove_plugin_with_type(name, type)

Remove the plugin with the given name.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin
    type = 'type_example' # str | The type of the plugin, may be auth, secret, or database

    try:
        # Remove the plugin with the given name.
        await api_instance.plugins_catalog_remove_plugin_with_type(name, type)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_catalog_remove_plugin_with_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin | 
 **type** | **str**| The type of the plugin, may be auth, secret, or database | 

### Return type

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

# **plugins_reload_backends**
> PluginsReloadBackendsResponse plugins_reload_backends(plugins_reload_backends_request)

Reload mounted plugin backends.

Either the plugin name (`plugin`) or the desired plugin backend mounts (`mounts`) must be provided, but not both. In the case that the plugin name is provided, all mounted paths that use that plugin backend will be reloaded.  If (`scope`) is provided and is (`global`), the plugin(s) are reloaded globally.

### Example


```python
import ahvac
from ahvac.models.plugins_reload_backends_request import PluginsReloadBackendsRequest
from ahvac.models.plugins_reload_backends_response import PluginsReloadBackendsResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    plugins_reload_backends_request = ahvac.PluginsReloadBackendsRequest() # PluginsReloadBackendsRequest | 

    try:
        # Reload mounted plugin backends.
        api_response = await api_instance.plugins_reload_backends(plugins_reload_backends_request)
        print("The response of SystemApi->plugins_reload_backends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_reload_backends: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugins_reload_backends_request** | [**PluginsReloadBackendsRequest**](PluginsReloadBackendsRequest.md)|  | 

### Return type

[**PluginsReloadBackendsResponse**](PluginsReloadBackendsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugins_runtimes_catalog_list_plugins_runtimes**
> PluginsRuntimesCatalogListPluginsRuntimesResponse plugins_runtimes_catalog_list_plugins_runtimes(list)



### Example


```python
import ahvac
from ahvac.models.plugins_runtimes_catalog_list_plugins_runtimes_response import PluginsRuntimesCatalogListPluginsRuntimesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.plugins_runtimes_catalog_list_plugins_runtimes(list)
        print("The response of SystemApi->plugins_runtimes_catalog_list_plugins_runtimes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_runtimes_catalog_list_plugins_runtimes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**PluginsRuntimesCatalogListPluginsRuntimesResponse**](PluginsRuntimesCatalogListPluginsRuntimesResponse.md)

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

# **plugins_runtimes_catalog_read_plugin_runtime_configuration**
> PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse plugins_runtimes_catalog_read_plugin_runtime_configuration(name, type)

Return the configuration data for the plugin runtime with the given name.

### Example


```python
import ahvac
from ahvac.models.plugins_runtimes_catalog_read_plugin_runtime_configuration_response import PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin runtime
    type = 'type_example' # str | The type of the plugin runtime

    try:
        # Return the configuration data for the plugin runtime with the given name.
        api_response = await api_instance.plugins_runtimes_catalog_read_plugin_runtime_configuration(name, type)
        print("The response of SystemApi->plugins_runtimes_catalog_read_plugin_runtime_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_runtimes_catalog_read_plugin_runtime_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin runtime | 
 **type** | **str**| The type of the plugin runtime | 

### Return type

[**PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse**](PluginsRuntimesCatalogReadPluginRuntimeConfigurationResponse.md)

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

# **plugins_runtimes_catalog_register_plugin_runtime**
> plugins_runtimes_catalog_register_plugin_runtime(name, type, plugins_runtimes_catalog_register_plugin_runtime_request)

Register a new plugin runtime, or updates an existing one with the supplied name.

### Example


```python
import ahvac
from ahvac.models.plugins_runtimes_catalog_register_plugin_runtime_request import PluginsRuntimesCatalogRegisterPluginRuntimeRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin runtime
    type = 'type_example' # str | The type of the plugin runtime
    plugins_runtimes_catalog_register_plugin_runtime_request = ahvac.PluginsRuntimesCatalogRegisterPluginRuntimeRequest() # PluginsRuntimesCatalogRegisterPluginRuntimeRequest | 

    try:
        # Register a new plugin runtime, or updates an existing one with the supplied name.
        await api_instance.plugins_runtimes_catalog_register_plugin_runtime(name, type, plugins_runtimes_catalog_register_plugin_runtime_request)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_runtimes_catalog_register_plugin_runtime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin runtime | 
 **type** | **str**| The type of the plugin runtime | 
 **plugins_runtimes_catalog_register_plugin_runtime_request** | [**PluginsRuntimesCatalogRegisterPluginRuntimeRequest**](PluginsRuntimesCatalogRegisterPluginRuntimeRequest.md)|  | 

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

# **plugins_runtimes_catalog_remove_plugin_runtime**
> plugins_runtimes_catalog_remove_plugin_runtime(name, type)

Remove the plugin runtime with the given name.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the plugin runtime
    type = 'type_example' # str | The type of the plugin runtime

    try:
        # Remove the plugin runtime with the given name.
        await api_instance.plugins_runtimes_catalog_remove_plugin_runtime(name, type)
    except Exception as e:
        print("Exception when calling SystemApi->plugins_runtimes_catalog_remove_plugin_runtime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the plugin runtime | 
 **type** | **str**| The type of the plugin runtime | 

### Return type

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

# **policies_delete_acl_policy**
> policies_delete_acl_policy(name)

Delete the ACL policy with the given name.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the policy. Example: \"ops\"

    try:
        # Delete the ACL policy with the given name.
        await api_instance.policies_delete_acl_policy(name)
    except Exception as e:
        print("Exception when calling SystemApi->policies_delete_acl_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_delete_acl_policy2**
> policies_delete_acl_policy2(name)

Delete the policy with the given name.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the policy. Example: \"ops\"

    try:
        # Delete the policy with the given name.
        await api_instance.policies_delete_acl_policy2(name)
    except Exception as e:
        print("Exception when calling SystemApi->policies_delete_acl_policy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_delete_password_policy**
> policies_delete_password_policy(name)

Delete a password policy.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the password policy.

    try:
        # Delete a password policy.
        await api_instance.policies_delete_password_policy(name)
    except Exception as e:
        print("Exception when calling SystemApi->policies_delete_password_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the password policy. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_generate_password_from_password_policy**
> PoliciesGeneratePasswordFromPasswordPolicyResponse policies_generate_password_from_password_policy(name)

Generate a password from an existing password policy.

### Example


```python
import ahvac
from ahvac.models.policies_generate_password_from_password_policy_response import PoliciesGeneratePasswordFromPasswordPolicyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the password policy.

    try:
        # Generate a password from an existing password policy.
        api_response = await api_instance.policies_generate_password_from_password_policy(name)
        print("The response of SystemApi->policies_generate_password_from_password_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_generate_password_from_password_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the password policy. | 

### Return type

[**PoliciesGeneratePasswordFromPasswordPolicyResponse**](PoliciesGeneratePasswordFromPasswordPolicyResponse.md)

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

# **policies_list_acl_policies**
> PoliciesListAclPoliciesResponse policies_list_acl_policies(list)



### Example


```python
import ahvac
from ahvac.models.policies_list_acl_policies_response import PoliciesListAclPoliciesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.policies_list_acl_policies(list)
        print("The response of SystemApi->policies_list_acl_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_list_acl_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**PoliciesListAclPoliciesResponse**](PoliciesListAclPoliciesResponse.md)

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

# **policies_list_acl_policies2**
> PoliciesListAclPolicies2Response policies_list_acl_policies2()



### Example


```python
import ahvac
from ahvac.models.policies_list_acl_policies2_response import PoliciesListAclPolicies2Response
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        api_response = await api_instance.policies_list_acl_policies2()
        print("The response of SystemApi->policies_list_acl_policies2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_list_acl_policies2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PoliciesListAclPolicies2Response**](PoliciesListAclPolicies2Response.md)

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

# **policies_list_acl_policies3**
> PoliciesListAclPolicies3Response policies_list_acl_policies3(list)



### Example


```python
import ahvac
from ahvac.models.policies_list_acl_policies3_response import PoliciesListAclPolicies3Response
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.policies_list_acl_policies3(list)
        print("The response of SystemApi->policies_list_acl_policies3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_list_acl_policies3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**PoliciesListAclPolicies3Response**](PoliciesListAclPolicies3Response.md)

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

# **policies_list_password_policies**
> StandardListResponse policies_list_password_policies(list)

List the existing password policies.

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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # List the existing password policies.
        api_response = await api_instance.policies_list_password_policies(list)
        print("The response of SystemApi->policies_list_password_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_list_password_policies: %s\n" % e)
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

# **policies_read_acl_policy**
> PoliciesReadAclPolicyResponse policies_read_acl_policy(name)

Retrieve information about the named ACL policy.

### Example


```python
import ahvac
from ahvac.models.policies_read_acl_policy_response import PoliciesReadAclPolicyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the policy. Example: \"ops\"

    try:
        # Retrieve information about the named ACL policy.
        api_response = await api_instance.policies_read_acl_policy(name)
        print("The response of SystemApi->policies_read_acl_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_read_acl_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

[**PoliciesReadAclPolicyResponse**](PoliciesReadAclPolicyResponse.md)

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

# **policies_read_acl_policy2**
> PoliciesReadAclPolicy2Response policies_read_acl_policy2(name)

Retrieve the policy body for the named policy.

### Example


```python
import ahvac
from ahvac.models.policies_read_acl_policy2_response import PoliciesReadAclPolicy2Response
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the policy. Example: \"ops\"

    try:
        # Retrieve the policy body for the named policy.
        api_response = await api_instance.policies_read_acl_policy2(name)
        print("The response of SystemApi->policies_read_acl_policy2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_read_acl_policy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 

### Return type

[**PoliciesReadAclPolicy2Response**](PoliciesReadAclPolicy2Response.md)

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

# **policies_read_password_policy**
> PoliciesReadPasswordPolicyResponse policies_read_password_policy(name)

Retrieve an existing password policy.

### Example


```python
import ahvac
from ahvac.models.policies_read_password_policy_response import PoliciesReadPasswordPolicyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the password policy.

    try:
        # Retrieve an existing password policy.
        api_response = await api_instance.policies_read_password_policy(name)
        print("The response of SystemApi->policies_read_password_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->policies_read_password_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the password policy. | 

### Return type

[**PoliciesReadPasswordPolicyResponse**](PoliciesReadPasswordPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_write_acl_policy**
> policies_write_acl_policy(name, policies_write_acl_policy_request)

Add a new or update an existing ACL policy.

### Example


```python
import ahvac
from ahvac.models.policies_write_acl_policy_request import PoliciesWriteAclPolicyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the policy. Example: \"ops\"
    policies_write_acl_policy_request = ahvac.PoliciesWriteAclPolicyRequest() # PoliciesWriteAclPolicyRequest | 

    try:
        # Add a new or update an existing ACL policy.
        await api_instance.policies_write_acl_policy(name, policies_write_acl_policy_request)
    except Exception as e:
        print("Exception when calling SystemApi->policies_write_acl_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 
 **policies_write_acl_policy_request** | [**PoliciesWriteAclPolicyRequest**](PoliciesWriteAclPolicyRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_write_acl_policy2**
> policies_write_acl_policy2(name, policies_write_acl_policy2_request)

Add a new or update an existing policy.

### Example


```python
import ahvac
from ahvac.models.policies_write_acl_policy2_request import PoliciesWriteAclPolicy2Request
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the policy. Example: \"ops\"
    policies_write_acl_policy2_request = ahvac.PoliciesWriteAclPolicy2Request() # PoliciesWriteAclPolicy2Request | 

    try:
        # Add a new or update an existing policy.
        await api_instance.policies_write_acl_policy2(name, policies_write_acl_policy2_request)
    except Exception as e:
        print("Exception when calling SystemApi->policies_write_acl_policy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the policy. Example: \&quot;ops\&quot; | 
 **policies_write_acl_policy2_request** | [**PoliciesWriteAclPolicy2Request**](PoliciesWriteAclPolicy2Request.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_write_password_policy**
> policies_write_password_policy(name, policies_write_password_policy_request)

Add a new or update an existing password policy.

### Example


```python
import ahvac
from ahvac.models.policies_write_password_policy_request import PoliciesWritePasswordPolicyRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | The name of the password policy.
    policies_write_password_policy_request = ahvac.PoliciesWritePasswordPolicyRequest() # PoliciesWritePasswordPolicyRequest | 

    try:
        # Add a new or update an existing password policy.
        await api_instance.policies_write_password_policy(name, policies_write_password_policy_request)
    except Exception as e:
        print("Exception when calling SystemApi->policies_write_password_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the password policy. | 
 **policies_write_password_policy_request** | [**PoliciesWritePasswordPolicyRequest**](PoliciesWritePasswordPolicyRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pprof_blocking**
> pprof_blocking()

Returns stack traces that led to blocking on synchronization primitives

Returns stack traces that led to blocking on synchronization primitives

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns stack traces that led to blocking on synchronization primitives
        await api_instance.pprof_blocking()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_blocking: %s\n" % e)
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

# **pprof_command_line**
> pprof_command_line()

Returns the running program's command line.

Returns the running program's command line, with arguments separated by NUL bytes.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns the running program's command line.
        await api_instance.pprof_command_line()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_command_line: %s\n" % e)
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

# **pprof_cpu_profile**
> pprof_cpu_profile()

Returns a pprof-formatted cpu profile payload.

Returns a pprof-formatted cpu profile payload. Profiling lasts for duration specified in seconds GET parameter, or for 30 seconds if not specified.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns a pprof-formatted cpu profile payload.
        await api_instance.pprof_cpu_profile()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_cpu_profile: %s\n" % e)
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

# **pprof_execution_trace**
> pprof_execution_trace()

Returns the execution trace in binary form.

Returns  the execution trace in binary form. Tracing lasts for duration specified in seconds GET parameter, or for 1 second if not specified.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns the execution trace in binary form.
        await api_instance.pprof_execution_trace()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_execution_trace: %s\n" % e)
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

# **pprof_goroutines**
> pprof_goroutines()

Returns stack traces of all current goroutines.

Returns stack traces of all current goroutines.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns stack traces of all current goroutines.
        await api_instance.pprof_goroutines()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_goroutines: %s\n" % e)
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

# **pprof_index**
> pprof_index()

Returns an HTML page listing the available profiles.

Returns an HTML page listing the available  profiles. This should be mainly accessed via browsers or applications that can  render pages.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns an HTML page listing the available profiles.
        await api_instance.pprof_index()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_index: %s\n" % e)
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

# **pprof_memory_allocations**
> pprof_memory_allocations()

Returns a sampling of all past memory allocations.

Returns a sampling of all past memory allocations.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns a sampling of all past memory allocations.
        await api_instance.pprof_memory_allocations()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_memory_allocations: %s\n" % e)
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

# **pprof_memory_allocations_live**
> pprof_memory_allocations_live()

Returns a sampling of memory allocations of live object.

Returns a sampling of memory allocations of live object.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns a sampling of memory allocations of live object.
        await api_instance.pprof_memory_allocations_live()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_memory_allocations_live: %s\n" % e)
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

# **pprof_mutexes**
> pprof_mutexes()

Returns stack traces of holders of contended mutexes

Returns stack traces of holders of contended mutexes

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns stack traces of holders of contended mutexes
        await api_instance.pprof_mutexes()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_mutexes: %s\n" % e)
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

# **pprof_symbols**
> pprof_symbols()

Returns the program counters listed in the request.

Returns the program counters listed in the request.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns the program counters listed in the request.
        await api_instance.pprof_symbols()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_symbols: %s\n" % e)
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

# **pprof_thread_creations**
> pprof_thread_creations()

Returns stack traces that led to the creation of new OS threads

Returns stack traces that led to the creation of new OS threads

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns stack traces that led to the creation of new OS threads
        await api_instance.pprof_thread_creations()
    except Exception as e:
        print("Exception when calling SystemApi->pprof_thread_creations: %s\n" % e)
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

# **query_token_accessor_capabilities**
> query_token_accessor_capabilities(query_token_accessor_capabilities_request)



### Example


```python
import ahvac
from ahvac.models.query_token_accessor_capabilities_request import QueryTokenAccessorCapabilitiesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    query_token_accessor_capabilities_request = ahvac.QueryTokenAccessorCapabilitiesRequest() # QueryTokenAccessorCapabilitiesRequest | 

    try:
        await api_instance.query_token_accessor_capabilities(query_token_accessor_capabilities_request)
    except Exception as e:
        print("Exception when calling SystemApi->query_token_accessor_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_token_accessor_capabilities_request** | [**QueryTokenAccessorCapabilitiesRequest**](QueryTokenAccessorCapabilitiesRequest.md)|  | 

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

# **query_token_capabilities**
> query_token_capabilities(query_token_capabilities_request)



### Example


```python
import ahvac
from ahvac.models.query_token_capabilities_request import QueryTokenCapabilitiesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    query_token_capabilities_request = ahvac.QueryTokenCapabilitiesRequest() # QueryTokenCapabilitiesRequest | 

    try:
        await api_instance.query_token_capabilities(query_token_capabilities_request)
    except Exception as e:
        print("Exception when calling SystemApi->query_token_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_token_capabilities_request** | [**QueryTokenCapabilitiesRequest**](QueryTokenCapabilitiesRequest.md)|  | 

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

# **query_token_self_capabilities**
> query_token_self_capabilities(query_token_self_capabilities_request)



### Example


```python
import ahvac
from ahvac.models.query_token_self_capabilities_request import QueryTokenSelfCapabilitiesRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    query_token_self_capabilities_request = ahvac.QueryTokenSelfCapabilitiesRequest() # QueryTokenSelfCapabilitiesRequest | 

    try:
        await api_instance.query_token_self_capabilities(query_token_self_capabilities_request)
    except Exception as e:
        print("Exception when calling SystemApi->query_token_self_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_token_self_capabilities_request** | [**QueryTokenSelfCapabilitiesRequest**](QueryTokenSelfCapabilitiesRequest.md)|  | 

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

# **rate_limit_quotas_configure**
> rate_limit_quotas_configure(rate_limit_quotas_configure_request)



### Example


```python
import ahvac
from ahvac.models.rate_limit_quotas_configure_request import RateLimitQuotasConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    rate_limit_quotas_configure_request = ahvac.RateLimitQuotasConfigureRequest() # RateLimitQuotasConfigureRequest | 

    try:
        await api_instance.rate_limit_quotas_configure(rate_limit_quotas_configure_request)
    except Exception as e:
        print("Exception when calling SystemApi->rate_limit_quotas_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_limit_quotas_configure_request** | [**RateLimitQuotasConfigureRequest**](RateLimitQuotasConfigureRequest.md)|  | 

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_limit_quotas_delete**
> rate_limit_quotas_delete(name)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | Name of the quota rule.

    try:
        await api_instance.rate_limit_quotas_delete(name)
    except Exception as e:
        print("Exception when calling SystemApi->rate_limit_quotas_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the quota rule. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_limit_quotas_list**
> StandardListResponse rate_limit_quotas_list(list)



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
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        api_response = await api_instance.rate_limit_quotas_list(list)
        print("The response of SystemApi->rate_limit_quotas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rate_limit_quotas_list: %s\n" % e)
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

# **rate_limit_quotas_read**
> RateLimitQuotasReadResponse rate_limit_quotas_read(name)



### Example


```python
import ahvac
from ahvac.models.rate_limit_quotas_read_response import RateLimitQuotasReadResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | Name of the quota rule.

    try:
        api_response = await api_instance.rate_limit_quotas_read(name)
        print("The response of SystemApi->rate_limit_quotas_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rate_limit_quotas_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the quota rule. | 

### Return type

[**RateLimitQuotasReadResponse**](RateLimitQuotasReadResponse.md)

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

# **rate_limit_quotas_read_configuration**
> RateLimitQuotasReadConfigurationResponse rate_limit_quotas_read_configuration()



### Example


```python
import ahvac
from ahvac.models.rate_limit_quotas_read_configuration_response import RateLimitQuotasReadConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        api_response = await api_instance.rate_limit_quotas_read_configuration()
        print("The response of SystemApi->rate_limit_quotas_read_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rate_limit_quotas_read_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RateLimitQuotasReadConfigurationResponse**](RateLimitQuotasReadConfigurationResponse.md)

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

# **rate_limit_quotas_write**
> rate_limit_quotas_write(name, rate_limit_quotas_write_request)



### Example


```python
import ahvac
from ahvac.models.rate_limit_quotas_write_request import RateLimitQuotasWriteRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    name = 'name_example' # str | Name of the quota rule.
    rate_limit_quotas_write_request = ahvac.RateLimitQuotasWriteRequest() # RateLimitQuotasWriteRequest | 

    try:
        await api_instance.rate_limit_quotas_write(name, rate_limit_quotas_write_request)
    except Exception as e:
        print("Exception when calling SystemApi->rate_limit_quotas_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the quota rule. | 
 **rate_limit_quotas_write_request** | [**RateLimitQuotasWriteRequest**](RateLimitQuotasWriteRequest.md)|  | 

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

# **raw_delete**
> raw_delete(path)

Delete the key with given path.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 

    try:
        # Delete the key with given path.
        await api_instance.raw_delete(path)
    except Exception as e:
        print("Exception when calling SystemApi->raw_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **raw_list**
> StandardListResponse raw_list(path, list)

Return a list keys for a given path prefix.

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
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 
    list = 'list_example' # str | Must be set to `true`

    try:
        # Return a list keys for a given path prefix.
        api_response = await api_instance.raw_list(path, list)
        print("The response of SystemApi->raw_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->raw_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
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

# **raw_read**
> RawReadResponse raw_read(path)

Read the value of the key at the given path.

### Example


```python
import ahvac
from ahvac.models.raw_read_response import RawReadResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 

    try:
        # Read the value of the key at the given path.
        api_response = await api_instance.raw_read(path)
        print("The response of SystemApi->raw_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->raw_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

[**RawReadResponse**](RawReadResponse.md)

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

# **raw_write**
> raw_write(path, raw_write_request)

Update the value of the key at the given path.

### Example


```python
import ahvac
from ahvac.models.raw_write_request import RawWriteRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    path = 'path_example' # str | 
    raw_write_request = ahvac.RawWriteRequest() # RawWriteRequest | 

    try:
        # Update the value of the key at the given path.
        await api_instance.raw_write(path, raw_write_request)
    except Exception as e:
        print("Exception when calling SystemApi->raw_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **raw_write_request** | [**RawWriteRequest**](RawWriteRequest.md)|  | 

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

# **read_health_status**
> read_health_status()

Returns the health status of Vault.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns the health status of Vault.
        await api_instance.read_health_status()
    except Exception as e:
        print("Exception when calling SystemApi->read_health_status: %s\n" % e)
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
**200** | initialized, unsealed, and active |  -  |
**429** | unsealed and standby |  -  |
**472** | data recovery mode replication secondary and active |  -  |
**501** | not initialized |  -  |
**503** | sealed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_initialization_status**
> read_initialization_status()

Returns the initialization status of Vault.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Returns the initialization status of Vault.
        await api_instance.read_initialization_status()
    except Exception as e:
        print("Exception when calling SystemApi->read_initialization_status: %s\n" % e)
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

# **read_replication_status**
> read_replication_status()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.read_replication_status()
    except Exception as e:
        print("Exception when calling SystemApi->read_replication_status: %s\n" % e)
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

# **read_sanitized_configuration_state**
> read_sanitized_configuration_state()

Return a sanitized version of the Vault server configuration.

The sanitized output strips configuration values in the storage, HA storage, and seals stanzas, which may contain sensitive values such as API tokens. It also removes any token or secret fields in other stanzas, such as the circonus_api_token from telemetry.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Return a sanitized version of the Vault server configuration.
        await api_instance.read_sanitized_configuration_state()
    except Exception as e:
        print("Exception when calling SystemApi->read_sanitized_configuration_state: %s\n" % e)
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

# **read_wrapping_properties**
> ReadWrappingPropertiesResponse read_wrapping_properties(read_wrapping_properties_request)

Look up wrapping properties for the given token.

### Example


```python
import ahvac
from ahvac.models.read_wrapping_properties_request import ReadWrappingPropertiesRequest
from ahvac.models.read_wrapping_properties_response import ReadWrappingPropertiesResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    read_wrapping_properties_request = ahvac.ReadWrappingPropertiesRequest() # ReadWrappingPropertiesRequest | 

    try:
        # Look up wrapping properties for the given token.
        api_response = await api_instance.read_wrapping_properties(read_wrapping_properties_request)
        print("The response of SystemApi->read_wrapping_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->read_wrapping_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_wrapping_properties_request** | [**ReadWrappingPropertiesRequest**](ReadWrappingPropertiesRequest.md)|  | 

### Return type

[**ReadWrappingPropertiesResponse**](ReadWrappingPropertiesResponse.md)

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

# **read_wrapping_properties2**
> ReadWrappingProperties2Response read_wrapping_properties2(token=token)

Look up wrapping properties for the requester's token.

### Example


```python
import ahvac
from ahvac.models.read_wrapping_properties2_response import ReadWrappingProperties2Response
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    token = 'token_example' # str |  (optional)

    try:
        # Look up wrapping properties for the requester's token.
        api_response = await api_instance.read_wrapping_properties2(token=token)
        print("The response of SystemApi->read_wrapping_properties2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->read_wrapping_properties2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 

### Return type

[**ReadWrappingProperties2Response**](ReadWrappingProperties2Response.md)

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

# **rekey_attempt_cancel**
> rekey_attempt_cancel()

Cancels any in-progress rekey.

This clears the rekey settings as well as any progress made. This must be called to change the parameters of the rekey. Note: verification is still a part of a rekey. If rekeying is canceled during the verification flow, the current unseal keys remain valid.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Cancels any in-progress rekey.
        await api_instance.rekey_attempt_cancel()
    except Exception as e:
        print("Exception when calling SystemApi->rekey_attempt_cancel: %s\n" % e)
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

# **rekey_attempt_initialize**
> RekeyAttemptInitializeResponse rekey_attempt_initialize(rekey_attempt_initialize_request)

Initializes a new rekey attempt.

Only a single rekey attempt can take place at a time, and changing the parameters of a rekey requires canceling and starting a new rekey, which will also provide a new nonce.

### Example


```python
import ahvac
from ahvac.models.rekey_attempt_initialize_request import RekeyAttemptInitializeRequest
from ahvac.models.rekey_attempt_initialize_response import RekeyAttemptInitializeResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    rekey_attempt_initialize_request = ahvac.RekeyAttemptInitializeRequest() # RekeyAttemptInitializeRequest | 

    try:
        # Initializes a new rekey attempt.
        api_response = await api_instance.rekey_attempt_initialize(rekey_attempt_initialize_request)
        print("The response of SystemApi->rekey_attempt_initialize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_attempt_initialize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rekey_attempt_initialize_request** | [**RekeyAttemptInitializeRequest**](RekeyAttemptInitializeRequest.md)|  | 

### Return type

[**RekeyAttemptInitializeResponse**](RekeyAttemptInitializeResponse.md)

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

# **rekey_attempt_read_progress**
> RekeyAttemptReadProgressResponse rekey_attempt_read_progress()

Reads the configuration and progress of the current rekey attempt.

### Example


```python
import ahvac
from ahvac.models.rekey_attempt_read_progress_response import RekeyAttemptReadProgressResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Reads the configuration and progress of the current rekey attempt.
        api_response = await api_instance.rekey_attempt_read_progress()
        print("The response of SystemApi->rekey_attempt_read_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_attempt_read_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RekeyAttemptReadProgressResponse**](RekeyAttemptReadProgressResponse.md)

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

# **rekey_attempt_update**
> RekeyAttemptUpdateResponse rekey_attempt_update(rekey_attempt_update_request)

Enter a single unseal key share to progress the rekey of the Vault.

### Example


```python
import ahvac
from ahvac.models.rekey_attempt_update_request import RekeyAttemptUpdateRequest
from ahvac.models.rekey_attempt_update_response import RekeyAttemptUpdateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    rekey_attempt_update_request = ahvac.RekeyAttemptUpdateRequest() # RekeyAttemptUpdateRequest | 

    try:
        # Enter a single unseal key share to progress the rekey of the Vault.
        api_response = await api_instance.rekey_attempt_update(rekey_attempt_update_request)
        print("The response of SystemApi->rekey_attempt_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_attempt_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rekey_attempt_update_request** | [**RekeyAttemptUpdateRequest**](RekeyAttemptUpdateRequest.md)|  | 

### Return type

[**RekeyAttemptUpdateResponse**](RekeyAttemptUpdateResponse.md)

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

# **rekey_delete_backup_key**
> rekey_delete_backup_key()

Delete the backup copy of PGP-encrypted unseal keys.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Delete the backup copy of PGP-encrypted unseal keys.
        await api_instance.rekey_delete_backup_key()
    except Exception as e:
        print("Exception when calling SystemApi->rekey_delete_backup_key: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rekey_delete_backup_recovery_key**
> rekey_delete_backup_recovery_key()



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        await api_instance.rekey_delete_backup_recovery_key()
    except Exception as e:
        print("Exception when calling SystemApi->rekey_delete_backup_recovery_key: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rekey_read_backup_key**
> RekeyReadBackupKeyResponse rekey_read_backup_key()

Return the backup copy of PGP-encrypted unseal keys.

### Example


```python
import ahvac
from ahvac.models.rekey_read_backup_key_response import RekeyReadBackupKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Return the backup copy of PGP-encrypted unseal keys.
        api_response = await api_instance.rekey_read_backup_key()
        print("The response of SystemApi->rekey_read_backup_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_read_backup_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RekeyReadBackupKeyResponse**](RekeyReadBackupKeyResponse.md)

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

# **rekey_read_backup_recovery_key**
> RekeyReadBackupRecoveryKeyResponse rekey_read_backup_recovery_key()



### Example


```python
import ahvac
from ahvac.models.rekey_read_backup_recovery_key_response import RekeyReadBackupRecoveryKeyResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        api_response = await api_instance.rekey_read_backup_recovery_key()
        print("The response of SystemApi->rekey_read_backup_recovery_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_read_backup_recovery_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RekeyReadBackupRecoveryKeyResponse**](RekeyReadBackupRecoveryKeyResponse.md)

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

# **rekey_verification_cancel**
> RekeyVerificationCancelResponse rekey_verification_cancel()

Cancel any in-progress rekey verification operation.

This clears any progress made and resets the nonce. Unlike a `DELETE` against `sys/rekey/init`, this only resets the current verification operation, not the entire rekey atttempt.

### Example


```python
import ahvac
from ahvac.models.rekey_verification_cancel_response import RekeyVerificationCancelResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Cancel any in-progress rekey verification operation.
        api_response = await api_instance.rekey_verification_cancel()
        print("The response of SystemApi->rekey_verification_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_verification_cancel: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RekeyVerificationCancelResponse**](RekeyVerificationCancelResponse.md)

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

# **rekey_verification_read_progress**
> RekeyVerificationReadProgressResponse rekey_verification_read_progress()

Read the configuration and progress of the current rekey verification attempt.

### Example


```python
import ahvac
from ahvac.models.rekey_verification_read_progress_response import RekeyVerificationReadProgressResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Read the configuration and progress of the current rekey verification attempt.
        api_response = await api_instance.rekey_verification_read_progress()
        print("The response of SystemApi->rekey_verification_read_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_verification_read_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RekeyVerificationReadProgressResponse**](RekeyVerificationReadProgressResponse.md)

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

# **rekey_verification_update**
> RekeyVerificationUpdateResponse rekey_verification_update(rekey_verification_update_request)

Enter a single new key share to progress the rekey verification operation.

### Example


```python
import ahvac
from ahvac.models.rekey_verification_update_request import RekeyVerificationUpdateRequest
from ahvac.models.rekey_verification_update_response import RekeyVerificationUpdateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    rekey_verification_update_request = ahvac.RekeyVerificationUpdateRequest() # RekeyVerificationUpdateRequest | 

    try:
        # Enter a single new key share to progress the rekey verification operation.
        api_response = await api_instance.rekey_verification_update(rekey_verification_update_request)
        print("The response of SystemApi->rekey_verification_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->rekey_verification_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rekey_verification_update_request** | [**RekeyVerificationUpdateRequest**](RekeyVerificationUpdateRequest.md)|  | 

### Return type

[**RekeyVerificationUpdateResponse**](RekeyVerificationUpdateResponse.md)

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

# **reload_subsystem**
> reload_subsystem(subsystem)

Reload the given subsystem

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    subsystem = 'subsystem_example' # str | 

    try:
        # Reload the given subsystem
        await api_instance.reload_subsystem(subsystem)
    except Exception as e:
        print("Exception when calling SystemApi->reload_subsystem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsystem** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remount**
> RemountResponse remount(remount_request)

Initiate a mount migration

### Example


```python
import ahvac
from ahvac.models.remount_request import RemountRequest
from ahvac.models.remount_response import RemountResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    remount_request = ahvac.RemountRequest() # RemountRequest | 

    try:
        # Initiate a mount migration
        api_response = await api_instance.remount(remount_request)
        print("The response of SystemApi->remount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->remount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remount_request** | [**RemountRequest**](RemountRequest.md)|  | 

### Return type

[**RemountResponse**](RemountResponse.md)

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

# **remount_status**
> RemountStatusResponse remount_status(migration_id)

Check status of a mount migration

### Example


```python
import ahvac
from ahvac.models.remount_status_response import RemountStatusResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    migration_id = 'migration_id_example' # str | The ID of the migration operation

    try:
        # Check status of a mount migration
        api_response = await api_instance.remount_status(migration_id)
        print("The response of SystemApi->remount_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->remount_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **str**| The ID of the migration operation | 

### Return type

[**RemountStatusResponse**](RemountStatusResponse.md)

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

# **rewrap**
> rewrap(rewrap_request)



### Example


```python
import ahvac
from ahvac.models.rewrap_request import RewrapRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    rewrap_request = ahvac.RewrapRequest() # RewrapRequest | 

    try:
        await api_instance.rewrap(rewrap_request)
    except Exception as e:
        print("Exception when calling SystemApi->rewrap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rewrap_request** | [**RewrapRequest**](RewrapRequest.md)|  | 

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

# **root_token_generation_cancel**
> root_token_generation_cancel()

Cancels any in-progress root generation attempt.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Cancels any in-progress root generation attempt.
        await api_instance.root_token_generation_cancel()
    except Exception as e:
        print("Exception when calling SystemApi->root_token_generation_cancel: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_token_generation_cancel2**
> root_token_generation_cancel2()

Cancels any in-progress root generation attempt.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Cancels any in-progress root generation attempt.
        await api_instance.root_token_generation_cancel2()
    except Exception as e:
        print("Exception when calling SystemApi->root_token_generation_cancel2: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_token_generation_initialize**
> RootTokenGenerationInitializeResponse root_token_generation_initialize(root_token_generation_initialize_request)

Initializes a new root generation attempt.

Only a single root generation attempt can take place at a time. One (and only one) of otp or pgp_key are required.

### Example


```python
import ahvac
from ahvac.models.root_token_generation_initialize_request import RootTokenGenerationInitializeRequest
from ahvac.models.root_token_generation_initialize_response import RootTokenGenerationInitializeResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    root_token_generation_initialize_request = ahvac.RootTokenGenerationInitializeRequest() # RootTokenGenerationInitializeRequest | 

    try:
        # Initializes a new root generation attempt.
        api_response = await api_instance.root_token_generation_initialize(root_token_generation_initialize_request)
        print("The response of SystemApi->root_token_generation_initialize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->root_token_generation_initialize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_token_generation_initialize_request** | [**RootTokenGenerationInitializeRequest**](RootTokenGenerationInitializeRequest.md)|  | 

### Return type

[**RootTokenGenerationInitializeResponse**](RootTokenGenerationInitializeResponse.md)

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

# **root_token_generation_initialize2**
> RootTokenGenerationInitialize2Response root_token_generation_initialize2(root_token_generation_initialize2_request)

Initializes a new root generation attempt.

Only a single root generation attempt can take place at a time. One (and only one) of otp or pgp_key are required.

### Example


```python
import ahvac
from ahvac.models.root_token_generation_initialize2_request import RootTokenGenerationInitialize2Request
from ahvac.models.root_token_generation_initialize2_response import RootTokenGenerationInitialize2Response
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    root_token_generation_initialize2_request = ahvac.RootTokenGenerationInitialize2Request() # RootTokenGenerationInitialize2Request | 

    try:
        # Initializes a new root generation attempt.
        api_response = await api_instance.root_token_generation_initialize2(root_token_generation_initialize2_request)
        print("The response of SystemApi->root_token_generation_initialize2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->root_token_generation_initialize2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_token_generation_initialize2_request** | [**RootTokenGenerationInitialize2Request**](RootTokenGenerationInitialize2Request.md)|  | 

### Return type

[**RootTokenGenerationInitialize2Response**](RootTokenGenerationInitialize2Response.md)

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

# **root_token_generation_read_progress**
> RootTokenGenerationReadProgressResponse root_token_generation_read_progress()

Read the configuration and progress of the current root generation attempt.

### Example


```python
import ahvac
from ahvac.models.root_token_generation_read_progress_response import RootTokenGenerationReadProgressResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Read the configuration and progress of the current root generation attempt.
        api_response = await api_instance.root_token_generation_read_progress()
        print("The response of SystemApi->root_token_generation_read_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->root_token_generation_read_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RootTokenGenerationReadProgressResponse**](RootTokenGenerationReadProgressResponse.md)

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

# **root_token_generation_read_progress2**
> RootTokenGenerationReadProgress2Response root_token_generation_read_progress2()

Read the configuration and progress of the current root generation attempt.

### Example


```python
import ahvac
from ahvac.models.root_token_generation_read_progress2_response import RootTokenGenerationReadProgress2Response
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Read the configuration and progress of the current root generation attempt.
        api_response = await api_instance.root_token_generation_read_progress2()
        print("The response of SystemApi->root_token_generation_read_progress2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->root_token_generation_read_progress2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RootTokenGenerationReadProgress2Response**](RootTokenGenerationReadProgress2Response.md)

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

# **root_token_generation_update**
> RootTokenGenerationUpdateResponse root_token_generation_update(root_token_generation_update_request)

Enter a single unseal key share to progress the root generation attempt.

If the threshold number of unseal key shares is reached, Vault will complete the root generation and issue the new token. Otherwise, this API must be called multiple times until that threshold is met. The attempt nonce must be provided with each call.

### Example


```python
import ahvac
from ahvac.models.root_token_generation_update_request import RootTokenGenerationUpdateRequest
from ahvac.models.root_token_generation_update_response import RootTokenGenerationUpdateResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    root_token_generation_update_request = ahvac.RootTokenGenerationUpdateRequest() # RootTokenGenerationUpdateRequest | 

    try:
        # Enter a single unseal key share to progress the root generation attempt.
        api_response = await api_instance.root_token_generation_update(root_token_generation_update_request)
        print("The response of SystemApi->root_token_generation_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->root_token_generation_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_token_generation_update_request** | [**RootTokenGenerationUpdateRequest**](RootTokenGenerationUpdateRequest.md)|  | 

### Return type

[**RootTokenGenerationUpdateResponse**](RootTokenGenerationUpdateResponse.md)

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

# **seal**
> seal()

Seal the Vault.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Seal the Vault.
        await api_instance.seal()
    except Exception as e:
        print("Exception when calling SystemApi->seal: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seal_status**
> SealStatusResponse seal_status()

Check the seal status of a Vault.

### Example


```python
import ahvac
from ahvac.models.seal_status_response import SealStatusResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Check the seal status of a Vault.
        api_response = await api_instance.seal_status()
        print("The response of SystemApi->seal_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->seal_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SealStatusResponse**](SealStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **step_down_leader**
> step_down_leader()

Cause the node to give up active status.

This endpoint forces the node to give up active status. If the node does not have active status, this endpoint does nothing. Note that the node will sleep for ten seconds before attempting to grab the active lock again, but if no standby nodes grab the active lock in the interim, the same node may become the active node again.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)

    try:
        # Cause the node to give up active status.
        await api_instance.step_down_leader()
    except Exception as e:
        print("Exception when calling SystemApi->step_down_leader: %s\n" % e)
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
**204** | empty body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_headers_configure**
> ui_headers_configure(header, ui_headers_configure_request)

Configure the values to be returned for the UI header.

### Example


```python
import ahvac
from ahvac.models.ui_headers_configure_request import UiHeadersConfigureRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    header = 'header_example' # str | The name of the header.
    ui_headers_configure_request = ahvac.UiHeadersConfigureRequest() # UiHeadersConfigureRequest | 

    try:
        # Configure the values to be returned for the UI header.
        await api_instance.ui_headers_configure(header, ui_headers_configure_request)
    except Exception as e:
        print("Exception when calling SystemApi->ui_headers_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**| The name of the header. | 
 **ui_headers_configure_request** | [**UiHeadersConfigureRequest**](UiHeadersConfigureRequest.md)|  | 

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

# **ui_headers_delete_configuration**
> ui_headers_delete_configuration(header)

Remove a UI header.

### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    header = 'header_example' # str | The name of the header.

    try:
        # Remove a UI header.
        await api_instance.ui_headers_delete_configuration(header)
    except Exception as e:
        print("Exception when calling SystemApi->ui_headers_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**| The name of the header. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_headers_list**
> UiHeadersListResponse ui_headers_list(list)

Return a list of configured UI headers.

### Example


```python
import ahvac
from ahvac.models.ui_headers_list_response import UiHeadersListResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # Return a list of configured UI headers.
        api_response = await api_instance.ui_headers_list(list)
        print("The response of SystemApi->ui_headers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->ui_headers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**UiHeadersListResponse**](UiHeadersListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_headers_read_configuration**
> UiHeadersReadConfigurationResponse ui_headers_read_configuration(header)

Return the given UI header's configuration

### Example


```python
import ahvac
from ahvac.models.ui_headers_read_configuration_response import UiHeadersReadConfigurationResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    header = 'header_example' # str | The name of the header.

    try:
        # Return the given UI header's configuration
        api_response = await api_instance.ui_headers_read_configuration(header)
        print("The response of SystemApi->ui_headers_read_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->ui_headers_read_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **header** | **str**| The name of the header. | 

### Return type

[**UiHeadersReadConfigurationResponse**](UiHeadersReadConfigurationResponse.md)

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

# **unseal**
> UnsealResponse unseal(unseal_request)

Unseal the Vault.

### Example


```python
import ahvac
from ahvac.models.unseal_request import UnsealRequest
from ahvac.models.unseal_response import UnsealResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    unseal_request = ahvac.UnsealRequest() # UnsealRequest | 

    try:
        # Unseal the Vault.
        api_response = await api_instance.unseal(unseal_request)
        print("The response of SystemApi->unseal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->unseal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unseal_request** | [**UnsealRequest**](UnsealRequest.md)|  | 

### Return type

[**UnsealResponse**](UnsealResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unwrap**
> unwrap(unwrap_request)



### Example


```python
import ahvac
from ahvac.models.unwrap_request import UnwrapRequest
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    unwrap_request = ahvac.UnwrapRequest() # UnwrapRequest | 

    try:
        await api_instance.unwrap(unwrap_request)
    except Exception as e:
        print("Exception when calling SystemApi->unwrap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unwrap_request** | [**UnwrapRequest**](UnwrapRequest.md)|  | 

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
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_history**
> VersionHistoryResponse version_history(list)

Returns map of historical version change entries

### Example


```python
import ahvac
from ahvac.models.version_history_response import VersionHistoryResponse
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    list = 'list_example' # str | Must be set to `true`

    try:
        # Returns map of historical version change entries
        api_response = await api_instance.version_history(list)
        print("The response of SystemApi->version_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->version_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Must be set to &#x60;true&#x60; | 

### Return type

[**VersionHistoryResponse**](VersionHistoryResponse.md)

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

# **wrap**
> wrap(request_body)



### Example


```python
import ahvac
from ahvac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ahvac.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ahvac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ahvac.SystemApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        await api_instance.wrap(request_body)
    except Exception as e:
        print("Exception when calling SystemApi->wrap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

