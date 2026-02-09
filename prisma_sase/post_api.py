#!/usr/bin/env python
"""
PRISMA SASE Python SDK - POST

**Author:** Palo Alto Networks

**Copyright:** (c) 2026 Palo Alto Networks, Inc

**License:** MIT
"""
import logging

__author__ = "Prisma SASE Developer Support <prisma-sase-developers@paloaltonetworks.com>"
__email__ = "prisma-sase-developers@paloaltonetworks.com"
__copyright__ = "Copyright (c) 2026 Palo Alto Networks, Inc"
__license__ = """
    MIT License

    Copyright (c) 2026 Palo Alto Networks, Inc

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

# Set logging to function name
api_logger = logging.getLogger(__name__)
"""logging.getlogger object to enable debug printing via `prisma_sase.API.set_debug`"""


class Post(object):
    """
    Prisma SASE API - POST requests

    Object to handle making Post requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def aaa_client_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Aaa_Client_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aaa_client_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def aaa_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Aaa_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aaa_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def aggregates_aiops_monitor(self, data, api_version="v2.1"):
        """
        POST Aggregates_Aiops_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/aggregates".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def aggregates_monitor(self, data, api_version="v3.0"):
        """
        POST Aggregates_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aggregates".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def anomaly_aiops_monitor(self, data, api_version="v2.0"):
        """
        POST Anomaly_Aiops_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/anomaly".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def anynetlinks_bulkoperations(self, site_id, data, api_version="v4.0"):
        """
        POST Anynetlinks_Bulkoperations API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/anynetlinks/bulkoperations".format(api_version,
                                                                                         site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def anynetlinks_query(self, data, api_version="v4.0"):
        """
        POST Anynetlinks_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def apnprofiles(self, data, api_version="v2.0"):
        """
        Create an APN Profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **apn:**  Type: string 
           - **authentication:**  Type: string 
           - **clear_password:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **password:**  Type: string 
           - **tags:**  [Type: string] 
           - **user_name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/apnprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appacceleration_query(self, data, api_version="v2.0"):
        """
        Query App Acceleration status V2.0. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **enabled:**  Type: boolean 
           - **primary_pa_compute_region_oid:**  Type: string 
           - **secondary_pa_compute_region_oid:**  Type: string 
           - **secondary_state:**  Type: string 
           - **site_id:**  Type: string 
           - **state:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/appacceleration/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appdefs(self, data, api_version="v2.6"):
        """
        Create an application definition (v2.6)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 

           - **abbreviation:**  Type: string 
           - **aggregate_flows:**  Type: boolean 
           - **app_type:**  Type: string 
           - **app_unreachability_detection:**  Type: boolean 
           - **category:**  Type: string 
           - **conn_idle_timeout:**  Type: integer 
           - **description:**  Type: string 
           - **display_name:**  Type: string 
           - **domains:**  [Type: string] 
           - **ingress_traffic_pct:**  Type: integer 
           - **ip_rules:**  [Type: object] 
           - **is_deprecated:**  Type: boolean 
           - **network_scan_application:**  Type: boolean 
           - **order_number:**  Type: integer 
           - **overrides_allowed:**  Type: boolean 
           - **p_category:**  Type: string 
           - **p_parent_id:**  Type: string 
           - **p_sub_category:**  Type: string 
           - **parent_id:**  Type: string 
           - **path_affinity:**  Type: string 
           - **session_timeout:**  Type: integer 
           - **supported_base_software_version:**  Type: string 
           - **supported_engines:**  Type: string 
           - **system_app_overridden:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tcp_rules:**  [Type: string] 
           - **transfer_type:**  Type: string 
           - **udp_rules:**  [Type: object] 
           - **use_parentapp_network_policy:**  Type: boolean 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appdefs_overrides(self, appdef_id, data, api_version="v2.3"):
        """
        Create a application definition overrides for system appdef (v2.3)

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **aggregate_flows:**  Type: boolean 
           - **app_unreachability_detection:**  Type: boolean 
           - **category:**  Type: string 
           - **conn_idle_timeout:**  Type: integer 
           - **description:**  Type: string 
           - **domains:**  [Type: string] 
           - **ingress_traffic_pct:**  Type: integer 
           - **ip_rules:**           
               - **dest_filters:**  [Type: string] 
               - **dest_prefixes:**  [Type: string] 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **protocol:**  Type: string 
               - **src_filters:**  [Type: string] 
           - **override_default_ip_rules:**  Type: boolean 
           - **override_default_tcp_rules:**  Type: boolean 
           - **override_default_udp_rules:**  Type: boolean 
           - **override_domains:**  Type: boolean 
           - **overrides_disable:**  Type: boolean 
           - **p_category:**  Type: string 
           - **path_affinity:**  Type: string 
           - **session_timeout:**  Type: integer 
           - **tags:**  [Type: string] 
           - **tcp_rules:**           
               - **client_filters:**  [Type: string] 
               - **client_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **server_filters:**  [Type: string] 
               - **server_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **server_prefixes:**  [Type: string] 
           - **transfer_type:**  Type: string 
           - **udp_rules:**           
               - **dest_prefixes:**  [Type: string] 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **udp_filters:**  [Type: string] 
               - **udp_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
           - **use_parentapp_network_policy:**  Type: boolean 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}/overrides".format(api_version,
                                                                          appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def authtokens(self, operator_id, data, api_version="v2.1"):
        """
        Create an auth token (v2.1)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **custom_roles:**           
               - **custom_permissions:**           
                   - **allowed_after_ms:**  Type: integer 
                   - **allowed_before_ms:**  Type: integer 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **disallow_permission:**  Type: boolean 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **value:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **name:**  Type: string 
               - **permissions:**           
                   - **value:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
           - **expires_utc_ms:**  Type: integer 
           - **is_system_owned:**  Type: boolean 
           - **roles:**           
               - **name:**  Type: string 
           - **session_key_c:**  Type: string 
           - **x_auth_token:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/authtokens".format(api_version,
                                                                             operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bgppeers(self, site_id, element_id, data, api_version="v3.0"):
        """
        Create BGP peer config (v3.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 

           - **advertise_default_route:**  Type: boolean 
           - **allow_v4_prefixes:**  Type: boolean 
           - **allow_v6_prefixes:**  Type: boolean 
           - **bgp_config:**           
               - **adv_interval:**  Type: integer 
               - **hold_time:**  Type: integer 
               - **keepalive_time:**  Type: integer 
               - **local_as_num:**  Type: string 
               - **md5_secret:**  Type: string 
               - **multi_hop_limit:**  Type: integer 
               - **peer_auth_type:**  Type: string 
               - **peer_retry_time:**  Type: integer 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **peer_ip:**  Type: string 
           - **peer_ip_v6:**  Type: string 
           - **peer_type:**  Type: string 
           - **remote_as_num:**  Type: string 
           - **route_aggregation:**           
               - **aggregate_prefixes:**           
                   - **ip_prefixes:**  [Type: string] 
                   - **type:**  Type: string 
               - **aggregate_type:**  Type: string 
               - **ipv4_prefix_list_id:**  Type: string 
               - **ipv6_prefix_list_id:**  Type: string 
           - **route_map_in_id:**  Type: string 
           - **route_map_out_id:**  Type: string 
           - **router_id:**  Type: string 
           - **scope:**  Type: string 
           - **shutdown:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **update_source:**  Type: string 
           - **update_source_v6:**  Type: string 
           - **vrf_context_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers".format(api_version,
                                                                                   site_id,
                                                                                   element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulk_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Bulk_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/bulk_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulkconfigurations_clone_sitetemplates(self, sitetemplate_id, data, api_version="v2.0"):
        """
        POST Bulkconfigurations_Clone_Sitetemplates API Function

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}/clone".format(api_version,
                                                                                               sitetemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulkconfigurations_deployments_sitetemplates(self, sitetemplate_id, data, api_version="v2.0"):
        """
        POST Bulkconfigurations_Deployments_Sitetemplates API Function

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}/deployments".format(api_version,
                                                                                                     sitetemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulkconfigurations_sitetemplates(self, data, api_version="v2.0"):
        """
        Create site profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **data:**  Type: string 
           - **site_id:**  Type: string 
           - **site_type:**  Type: string 
           - **template_description:**  Type: string 
           - **template_id:**  Type: string 
           - **template_name:**  Type: string 
           - **tenant_id:**  Type: string 
           - **variable_map:**  Type: object 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulkdelete_snmpdiscoverystartnodes_deviceidconfigs(self, site_id, deviceidconfig_id, data, api_version="v2.0"):
        """
        POST Bulkdelete_Snmpdiscoverystartnodes_Deviceidconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: Device Id Config ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}/bulkdelete_snmpdiscoverystartnodes".format(api_version,
                                                                                                                    site_id,
                                                                                                                    deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulkoperations(self, data, api_version="v2.1"):
        """
        Bulk site update API (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **element_system_limit_profile_id:**  Type: string 
           - **site_ids:**  [Type: string] 
           - **type:**  Type: string 
           - **vrf_context_profile_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/bulkoperations".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Cellular_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/cellular_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_module_revoked_images(self, data, api_version="v2.0"):
        """
        Create a Revoked Cellular Image (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **carrier:**  Type: string 
           - **fw_version:**  Type: string 
           - **pri_version:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cellular_module_revoked_images".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def certificate_operations(self, element_id, data, api_version="v2.0"):
        """
        Start CIC renewal process for an element device (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **parameters:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/certificate_operations".format(api_version,
                                                                                        element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def certificates_tenants(self, data, api_version="v2.0"):
        """
        POST Certificates_Tenants API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/certificates".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def change_password(self, data, api_version="v2.0"):
        """
        POST Change_Password API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/accounts/password/change".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def copy_element_configurations_elementshells(self, site_id, elementshell_id, data, api_version="v2.0"):
        """
        POST Copy_Element_Configurations_Elementshells API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}/copy_element_configurations".format(api_version,
                                                                                                           site_id,
                                                                                                           elementshell_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def deltasync_directoryservices(self, data, api_version="v2.0"):
        """
        POST Deltasync_Directoryservices API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices/deltasync".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def demsiteconfigs(self, site_id, data, api_version="v2.0"):
        """
        Create dem site config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **adem_enabled:**  Type: boolean 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/demsiteconfigs".format(api_version,
                                                                             site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def demsiteconfigs_query(self, data, api_version="v2.0"):
        """
        Queries db for Dem site config that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **adem_enabled:**  Type: boolean 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/demsiteconfigs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def deployments_sitetemplates_bulkconfigurations_query(self, data, api_version="v2.0"):
        """
        POST Deployments_Sitetemplates_Bulkconfigurations_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/deployments/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def deviceidconfigs(self, site_id, element_id, data, api_version="v2.0"):
        """
        POST Deviceidconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/deviceidconfigs".format(api_version,
                                                                                          site_id,
                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def deviceidconfigs_snmpdiscoverystartnodes(self, site_id, deviceidconfig_id, data, api_version="v2.0"):
        """
        Create Start Network Node config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: Device Id Config ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_address:**  Type: string 
           - **name:**  Type: string 
           - **scope:**           
               - **ipv4_prefix:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}/snmpdiscoverystartnodes".format(api_version,
                                                                                                         site_id,
                                                                                                         deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def deviceidprofiles(self, data, api_version="v2.0"):
        """
        Create device id profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **num_associated_sites:**  Type: integer 
           - **region:**  Type: string 
           - **snmp_discovery_device_refresh_frequency:**  Type: integer 
           - **snmp_discovery_enabled:**  Type: boolean 
           - **snmp_discovery_network_refresh_frequency:**  Type: integer 
           - **snmp_discovery_use_local_neighbours:**  Type: boolean 
           - **snmp_version:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **v2_config:**           
               - **snmp_community_string:**  Type: string 
           - **v3_config:**           
               - **snmp_auth_password:**  Type: string 
               - **snmp_auth_password_encrypted:**  Type: string 
               - **snmp_auth_protocol:**  Type: string 
               - **snmp_privacy_password:**  Type: string 
               - **snmp_privacy_password_encrypted:**  Type: string 
               - **snmp_privacy_protocol:**  Type: string 
               - **snmp_security_level:**  Type: string 
               - **snmp_username:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/deviceidprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dhcpservers(self, site_id, data, api_version="v2.3"):
        """
        Create a new dhcp server configuration for a subnet (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **address_family:**  Type: string 
           - **broadcast_address:**  Type: string 
           - **custom_options:**           
               - **option_definition:**  Type: string 
               - **option_value:**  Type: string 
               - **vendor_class_identifier:**  Type: string 
           - **default_lease_time:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **dns_servers:**  [Type: string] 
           - **domain_name:**  Type: string 
           - **gateway:**  Type: string 
           - **ip_ranges:**           
               - **end_ip:**  Type: string 
               - **start_ip:**  Type: string 
           - **max_lease_time:**  Type: integer 
           - **network_context_id:**  Type: string 
           - **static_mappings:**           
               - **client_duid:**  Type: string 
               - **ip_address:**  Type: string 
               - **mac:**  Type: string 
               - **name:**  Type: string 
           - **subnet:**  Type: string 
           - **tags:**  [Type: string] 
           - **vrf_context_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/dhcpservers".format(api_version,
                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def directoryservices(self, data, api_version="v2.1"):
        """
        Create Directory Service (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **directory_tenant_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **group_attributes:**           
               - **email:**  Type: string 
               - **primary_name:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **user_attributes:**           
               - **alternate_username_1:**  Type: string 
               - **alternate_username_2:**  Type: string 
               - **alternate_username_3:**  Type: string 
               - **email:**  Type: string 
               - **primary_name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsserviceprofiles(self, data, api_version="v2.1"):
        """
        Create a new DNS service profile (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **authoritative_config:**           
               - **caa_records:**           
                   - **flags:**  Type: string 
                   - **name:**  Type: string 
                   - **tag:**  Type: string 
                   - **value:**  Type: string 
               - **cname_records:**           
                   - **name:**  [Type: string] 
                   - **target:**  Type: string 
                   - **ttl:**  Type: integer 
               - **dns_resource_records:**           
                   - **hex_data:**  Type: string 
                   - **name:**  Type: string 
                   - **rr_number:**  Type: integer 
               - **host_records:**           
                   - **domain_names:**  [Type: string] 
                   - **ipv4_address:**  Type: string 
                   - **ipv6_address:**  Type: string 
                   - **ttl:**  Type: integer 
               - **mx_host_records:**           
                   - **hostname:**  Type: string 
                   - **mx_name:**  Type: string 
                   - **preference:**  Type: integer 
               - **naptr_records:**           
                   - **flags:**  Type: string 
                   - **name:**  Type: string 
                   - **order:**  Type: integer 
                   - **preference:**  Type: integer 
                   - **regexp:**  Type: string 
                   - **replacement:**  Type: string 
                   - **service:**  Type: string 
               - **peers:**  [Type: string] 
               - **ptr_records:**           
                   - **name:**  Type: string 
                   - **target:**  Type: string 
               - **secondary_servers:**  [Type: string] 
               - **servers:**           
                   - **dnsservicerole_id:**  Type: string 
                   - **domain_name:**  Type: string 
               - **soa:**           
                   - **expiry:**  Type: integer 
                   - **host_master:**  Type: string 
                   - **refresh:**  Type: integer 
                   - **retry:**  Type: integer 
                   - **serial_number:**  Type: integer 
               - **srv_hosts:**           
                   - **domain_name:**  Type: string 
                   - **port:**  Type: integer 
                   - **priority:**  Type: integer 
                   - **protocol:**  Type: string 
                   - **service:**  Type: string 
                   - **target:**  Type: integer 
                   - **weight:**  Type: integer 
               - **synth_domains:**           
                   - **domain:**  Type: string 
                   - **end_ipaddress:**  Type: string 
                   - **ipaddress_prefix:**  Type: string 
                   - **prefix:**  Type: string 
                   - **start_ipaddress:**  Type: string 
               - **ttl:**  Type: integer 
               - **txt_records:**           
                   - **domain_name:**  Type: string 
                   - **texts:**  [Type: string] 
               - **zones:**           
                   - **domain_name:**  Type: string 
                   - **exclude_prefix:**  [Type: string] 
                   - **include_prefix:**  [Type: string] 
           - **cache_config:**           
               - **cache_size:**  Type: integer 
               - **disable_negative_caching:**  Type: boolean 
               - **max_cache_ttl:**  Type: integer 
               - **min_cache_ttl:**  Type: integer 
               - **negative_cache_ttl:**  Type: integer 
           - **description:**  Type: string 
           - **dns_forward_config:**           
               - **dns_servers:**           
                   - **address_family:**  Type: string 
                   - **dnsserver_ip:**  Type: string 
                   - **dnsserver_port:**  Type: integer 
                   - **domain_names:**  [Type: string] 
                   - **forward_dnsservicerole_id:**  Type: string 
                   - **ip_prefix:**  Type: string 
                   - **source_port:**  Type: integer 
               - **max_source_port:**  Type: integer 
               - **min_source_port:**  Type: integer 
               - **send_to_all_dns_servers:**  Type: boolean 
           - **dns_queries_metadata:**           
               - **add_client_mac:**           
                   - **mac_encoding_format:**  Type: string 
               - **add_customer_premises_equipment:**           
                   - **identifier_text:**  Type: string 
                   - **type:**  Type: string 
               - **add_subnets:**           
                   - **ipv4_address:**  Type: string 
                   - **ipv4_prefix_length:**  Type: integer 
                   - **ipv6_address:**  Type: string 
                   - **ipv6_prefix_length:**  Type: integer 
           - **dns_rebind_config:**           
               - **enable_localhost_rebind:**  Type: boolean 
               - **rebind_domains:**  [Type: string] 
               - **stop_dns_rebind_privateip:**  Type: boolean 
           - **dns_response_overrides:**           
               - **aliases:**           
                   - **mask:**  Type: integer 
                   - **original_end_ip:**  Type: string 
                   - **original_ip:**  Type: string 
                   - **original_start_ip:**  Type: string 
                   - **replace_ip:**  Type: string 
               - **bogus_nx_domains:**  [Type: string] 
               - **disable_private_ip_lookups:**  Type: boolean 
               - **ignore_ip_addresses:**  [Type: string] 
               - **local_ttl:**  Type: integer 
               - **max_ttl:**  Type: integer 
           - **dnssec_config:**           
               - **disable_dnssec_timecheck:**  Type: boolean 
               - **dns_check_unsigned:**  Type: boolean 
               - **enabled:**  Type: boolean 
               - **trust_anchors:**           
                   - **class:**  Type: string 
                   - **domain:**  Type: string 
                   - **key_digest:**           
                       - **algorithm:**  Type: integer 
                       - **digest:**  Type: string 
                       - **digest_type:**  Type: integer 
                       - **key_tag:**  Type: integer 
           - **domains_to_addresses:**           
               - **domain_names:**  [Type: string] 
               - **ipv4_address:**  Type: string 
               - **ipv6_address:**  Type: string 
           - **edns_packet_max:**  Type: integer 
           - **enable_dns_loop_detection:**  Type: boolean 
           - **enable_dnssec_proxy:**  Type: boolean 
           - **enable_strict_domain_name:**  Type: boolean 
           - **listen_dnsservicerole_id:**  Type: string 
           - **listen_port:**  Type: integer 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsserviceroles(self, data, api_version="v2.0"):
        """
        Create a new DNS service role (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceroles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsservices(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create a new DNS service config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **cache_config:**           
               - **cache_size:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **dns_queries_metadata:**           
               - **add_customer_premises_equipment:**           
                   - **identifier_text:**  Type: string 
                   - **type:**  Type: string 
               - **add_subnets:**           
                   - **ipv4_address:**  Type: string 
                   - **ipv4_prefix_length:**  Type: integer 
                   - **ipv6_address:**  Type: string 
                   - **ipv6_prefix_length:**  Type: integer 
           - **dnsservice_profile_id:**  Type: string 
           - **dnsservicerole_bindings:**           
               - **dnsservicerole_id:**  Type: string 
               - **interfaces:**           
                   - **interface_id:**  Type: string 
                   - **interface_ip:**  Type: string 
           - **domains_to_addresses:**           
               - **domain_names:**  [Type: string] 
               - **ipv4_address:**  Type: string 
               - **ipv6_address:**  Type: string 
           - **domains_to_interfaces:**           
               - **domain_names:**  [Type: string] 
               - **interface_id:**  Type: string 
           - **element_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **max_concurrent_dns_queries:**  Type: integer 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **upperCaseName:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/dnsservices".format(api_version,
                                                                                      site_id,
                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_extensions(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create element level extension configuration (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **conf:**  Type: object 
           - **disabled:**  Type: boolean 
           - **name:**  Type: string 
           - **namespace:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/extensions".format(api_version,
                                                                                     site_id,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_rquery(self, data, api_version="v3.0"):
        """
        POST Element_Rquery API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/rquery".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementaccessconfigs(self, element_id, data, api_version="v2.2"):
        """
        POST Elementaccessconfigs API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/elementaccessconfigs".format(api_version,
                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementaccessconfigs_query(self, data, api_version="v2.2"):
        """
        Query Element Access Config based on parameters (v2.2)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementaccessconfigs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementsecurityzones(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create an association between element and security zone. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **interface_ids:**  [Type: string] 
           - **lannetwork_ids:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 
           - **waninterface_ids:**  [Type: string] 
           - **wanoverlay_ids:**  [Type: string] 
           - **zone_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/securityzones".format(api_version,
                                                                                        site_id,
                                                                                        element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementshells(self, site_id, data, api_version="v2.1"):
        """
        Create an element shell (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **allowed_roles:**  [Type: string] 
           - **cluster_id:**  Type: string 
           - **cluster_insertion_mode:**  Type: string 
           - **cluster_member_id:**  Type: string 
           - **description:**  Type: string 
           - **device_mode:**  Type: string 
           - **device_profile_id:**  Type: string 
           - **element_id:**  Type: string 
           - **hub_cluster_config:**           
               - **intra_cluster_tunnel:**           
                   - **disabled:**  Type: boolean 
                   - **source_interfaces:**  [Type: string] 
               - **track:**           
                   - **hosts:**           
                       - **address_v4:**  Type: string 
                       - **address_v6:**  Type: string 
                       - **vrf_context_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **l3_direct_private_wan_forwarding:**  Type: boolean 
           - **l3_lan_forwarding:**  Type: boolean 
           - **led_config:**           
               - **service_led_on:**  Type: boolean 
           - **main_power_usage_threshold:**  Type: integer 
           - **model_name:**  Type: string 
           - **name:**  Type: string 
           - **nat_policysetstack_id:**  Type: string 
           - **network_policysetstack_id:**  Type: string 
           - **priority_policysetstack_id:**  Type: string 
           - **role:**  Type: string 
           - **site_id:**  Type: string 
           - **software_version:**  Type: string 
           - **spoke_ha_config:**           
               - **cluster_id:**  Type: string 
               - **enable:**  Type: boolean 
               - **priority:**  Type: integer 
               - **source_interface:**  Type: string 
               - **track:**           
                   - **interfaces:**           
                       - **interface_id:**  Type: string 
                       - **reduce_priority:**  Type: integer 
                   - **waninterfaces:**           
                       - **reduce_priority:**  Type: integer 
                       - **wan_interface_id:**  Type: string 
           - **state:**  Type: string 
           - **switch_config:**           
               - **default_vlan_id:**  Type: integer 
               - **mstp_enabled:**  Type: boolean 
               - **stp_aging_timer:**  Type: integer 
               - **stp_forward_delay:**  Type: integer 
               - **stp_hello_time:**  Type: integer 
               - **stp_max_age:**  Type: integer 
               - **stp_mode:**  Type: string 
               - **stp_priority:**  Type: integer 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **vpn_to_vpn_forwarding:**  Type: boolean 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells".format(api_version,
                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementshells_query(self, data, api_version="v2.1"):
        """
        Queries db for limit number of element shells that match query params. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **allowed_roles:**  [Type: string] 
           - **cluster_id:**  Type: string 
           - **cluster_insertion_mode:**  Type: string 
           - **cluster_member_id:**  Type: string 
           - **description:**  Type: string 
           - **device_mode:**  Type: string 
           - **device_profile_id:**  Type: string 
           - **element_id:**  Type: string 
           - **hub_cluster_config:**           
               - **intra_cluster_tunnel:**           
                   - **disabled:**  Type: boolean 
                   - **source_interfaces:**  [Type: string] 
               - **track:**           
                   - **hosts:**           
                       - **address_v4:**  Type: string 
                       - **address_v6:**  Type: string 
                       - **vrf_context_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **l3_direct_private_wan_forwarding:**  Type: boolean 
           - **l3_lan_forwarding:**  Type: boolean 
           - **led_config:**           
               - **service_led_on:**  Type: boolean 
           - **main_power_usage_threshold:**  Type: integer 
           - **model_name:**  Type: string 
           - **name:**  Type: string 
           - **nat_policysetstack_id:**  Type: string 
           - **network_policysetstack_id:**  Type: string 
           - **priority_policysetstack_id:**  Type: string 
           - **role:**  Type: string 
           - **site_id:**  Type: string 
           - **software_version:**  Type: string 
           - **spoke_ha_config:**           
               - **cluster_id:**  Type: string 
               - **enable:**  Type: boolean 
               - **priority:**  Type: integer 
               - **source_interface:**  Type: string 
               - **track:**           
                   - **interfaces:**           
                       - **interface_id:**  Type: string 
                       - **reduce_priority:**  Type: integer 
                   - **waninterfaces:**           
                       - **reduce_priority:**  Type: integer 
                       - **wan_interface_id:**  Type: string 
           - **state:**  Type: string 
           - **switch_config:**           
               - **default_vlan_id:**  Type: integer 
               - **mstp_enabled:**  Type: boolean 
               - **stp_aging_timer:**  Type: integer 
               - **stp_forward_delay:**  Type: integer 
               - **stp_hello_time:**  Type: integer 
               - **stp_max_age:**  Type: integer 
               - **stp_mode:**  Type: string 
               - **stp_priority:**  Type: integer 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **vpn_to_vpn_forwarding:**  Type: boolean 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementshells/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementsystemlimitprofiles(self, data, api_version="v2.0"):
        """
        Create a new Element System Limit Profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **flow_acceptance_criteria:**           
               - **flow_limit_percentage_per_source:**  Type: integer 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementsystemlimitprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementsystemlimitprofiles_query(self, data, api_version="v2.0"):
        """
        Query Element System Limit Profiles (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementsystemlimitprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementusers(self, data, api_version="v2.1"):
        """
        Create Element User (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **is_tenant_level:**  Type: boolean 
           - **login_id:**  Type: string 
           - **role:**  Type: string 
           - **tenant_id:**  Type: string 
           - **username:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementusers".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementusers_access(self, elementuser_id, data, api_version="v2.1"):
        """
        Grant Specific role to Element user on specific element (v2.1)

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
           - **role:**  Type: string 
           - **tenant_id:**  Type: string 
           - **user_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}/access".format(api_version,
                                                                            elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def entitlements(self, operator_id, session_id, data, api_version="v2.0"):
        """
        POST Entitlements API Function

          **Parameters:**:

          - **operator_id**: Operator ID
          - **session_id**: User Session ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/sessions/{}/actionservice/appportal/api/v1/entitlements".format(api_version,
                                                                                                                          operator_id,
                                                                                                                          session_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, data, api_version="v2.1"):
        """
        Create event correlation policyrule configuration (v2.1)

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **dampening_duration:**  Type: integer 
           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **end_time:**  Type: integer 
           - **escalation_rules:**           
               - **flap_rule:**           
                   - **flap_duration:**  Type: integer 
                   - **flap_rate:**  Type: integer 
               - **standing_rule:**           
                   - **priority:**  Type: string 
                   - **standing_for:**  Type: integer 
           - **event_codes:**  [Type: string] 
           - **name:**  Type: string 
           - **priority:**  Type: string 
           - **resource_ids:**  [Type: string] 
           - **resource_type:**  Type: string 
           - **start_time:**  Type: integer 
           - **sub_resource_type:**  Type: string 
           - **suppress:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules".format(api_version,
                                                                                                               eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def eventcorrelationpolicysets(self, data, api_version="v2.0"):
        """
        Queries db for limit number of event correlation policysets that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **active_policyset:**  Type: boolean 
           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 
           - **severity_priority_mapping:**           
               - **priority:**  Type: string 
               - **severity:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def events_operations(self, data, api_version="v2.0"):
        """
        POST Events_Operations API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/events/operations".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def extensions_ws_query(self, data, api_version="v2.0"):
        """
        POST Extensions_Ws_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ws/extensions/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def externalcaconfigs(self, data, api_version="v2.0"):
        """
        POST Externalcaconfigs API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/externalcaconfigs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def fips_mode_change_operations(self, element_id, data, api_version="v2.1"):
        """
        Change Mode of an element from FIPS to Non-FIPS or vice-versa. (v2.1)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **parameters:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/fips_mode_change_operations".format(api_version,
                                                                                             element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def flows_monitor(self, data, api_version="v3.11"):
        """
        POST Flows_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.11)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/flows".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def forecast_aiops_monitor(self, data, api_version="v2.1"):
        """
        POST Forecast_Aiops_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/forecast".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def forgot_password_login_t(self, data, api_version="v2.0"):
        """
        POST Forgot_Password_Login_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/login/password/forgot".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def globalprefixfilters(self, data, api_version="v2.0"):
        """
        Create a new global prefix filter. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **filters:**           
               - **ip_prefixes:**  [Type: string] 
               - **type:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def health_aiops_monitor(self, data, api_version="v2.0"):
        """
        POST Health_Aiops_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/health".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def healthscore_aggregates_monitor(self, data, api_version="v2.1"):
        """
        POST Healthscore_Aggregates_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aggregates/healthscore".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def hubclustermembers(self, site_id, hubcluster_id, data, api_version="v3.0"):
        """
        Creates a new hub cluster member. (v3.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 

           - **headend1_site_ids:**  [Type: string] 
           - **headend2_site_ids:**  [Type: string] 
           - **hub_element_id:**  Type: string 
           - **load_factors:**           
               - **alarm_threshold:**  Type: integer 
               - **allocated:**  Type: integer 
               - **subscription_factor:**  Type: number 
               - **threshold:**           
                   - **critical_alarm:**  Type: integer 
                   - **major_alarm:**  Type: integer 
                   - **subscription_factor:**  Type: number 
               - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/hubclustermembers".format(api_version,
                                                                                               site_id,
                                                                                               hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def hubclusters(self, site_id, data, api_version="v4.0"):
        """
        Creates a new hub cluster (v4.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 

           - **default_cluster:**  Type: boolean 
           - **description:**  Type: string 
           - **elements:**           
               - **hubClusterElementNumber:**  Type: string 
               - **hub_element_id:**  Type: string 
               - **locked:**  Type: boolean 
           - **name:**  Type: string 
           - **peer_sites:**  [Type: string] 
           - **site_count_alarm_threshold:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters".format(api_version,
                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def insights_monitor(self, data, api_version="v2.0"):
        """
        POST Insights_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/monitor/insights".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def insightslist_monitor(self, data, api_version="v2.0"):
        """
        POST Insightslist_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/monitor/insightslist".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def interfaces(self, site_id, element_id, data, api_version="v4.21"):
        """
        Create a Interface (v4.21)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.21)

          **Payload Attributes:** 

           - **admin_up:**  Type: boolean 
           - **attached_lan_networks:**           
               - **lan_network_id:**  Type: string 
               - **vlan_id:**  Type: integer 
           - **authentication_config:**           
               - **fallback_retry_count:**  Type: integer 
               - **mode:**  Type: string 
               - **reauthentication_timeout:**  Type: integer 
           - **bound_interfaces:**  [Type: string] 
           - **bypass_pair:**           
               - **lan:**  Type: string 
               - **lan_state_propagation:**  Type: boolean 
               - **use_relay:**  Type: boolean 
               - **wan:**  Type: string 
           - **cellular_config:**           
               - **apn_config:**           
                   - **apn:**  Type: string 
                   - **authentication:**  Type: string 
                   - **clear_password:**  Type: boolean 
                   - **password:**  Type: string 
                   - **password_encrypted:**  Type: string 
                   - **user_name:**  Type: string 
               - **apnprofile_id:**  Type: string 
               - **auto_apn:**  Type: boolean 
               - **parent_module_id:**  Type: string 
               - **parent_sim_slot_number:**  Type: integer 
           - **description:**  Type: string 
           - **devicemgmt_policysetstack_id:**  Type: string 
           - **dhcp_relay:**           
               - **enabled:**  Type: boolean 
               - **option_82:**           
                   - **circuit_id:**  Type: string 
                   - **enabled:**  Type: boolean 
                   - **reforwarding_policy:**  Type: string 
                   - **remote_id:**  Type: string 
               - **server_ips:**  [Type: string] 
               - **source_interface:**  Type: string 
           - **directed_broadcast:**  Type: boolean 
           - **ethernet_port:**           
               - **full_duplex:**  Type: boolean 
               - **port_id:**           
                   - **connector:**  Type: string 
                   - **device:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **element_id:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **max_mtu:**  Type: integer 
                   - **max_speed:**  Type: integer 
                   - **name:**  Type: string 
                   - **original_mac_address:**  Type: string 
                   - **region:**  Type: string 
                   - **site_id:**  Type: string 
                   - **tenant_id:**  Type: string 
               - **port_name:**  Type: string 
               - **speed:**  Type: integer 
           - **fec_mode:**  Type: string 
           - **interface_profile_id:**  Type: string 
           - **ipfixcollectorcontext_id:**  Type: string 
           - **ipfixfiltercontext_id:**  Type: string 
           - **ipv4_config:**           
               - **dhcp_config:**           
                   - **client_id:**  Type: string 
                   - **hostname:**  Type: string 
               - **dns_v4_config:**           
                   - **name_servers:**  [Type: string] 
                   - **search:**  [Type: string] 
               - **pppoe_config:**           
                   - **chap_passwd:**  Type: string 
                   - **chap_user:**  Type: string 
                   - **set_route:**  Type: boolean 
               - **routes:**           
                   - **destination:**  Type: string 
                   - **via:**  Type: string 
               - **static_config:**           
                   - **address:**  Type: string 
               - **type:**  Type: string 
           - **ipv6_config:**           
               - **dhcp_config:**           
                   - **client_id:**  Type: string 
                   - **hostname:**  Type: string 
               - **dns_v6_config:**           
                   - **name_servers:**  [Type: string] 
                   - **search:**  [Type: string] 
               - **routes:**           
                   - **destination:**  Type: string 
                   - **via:**  Type: string 
               - **static_config:**           
                   - **address:**  Type: string 
                   - **enable_prefix_distribution:**  Type: boolean 
               - **type:**  Type: string 
           - **lldp_enabled:**  Type: boolean 
           - **loopback_config:**           
               - **binding_interface_id:**  Type: string 
           - **mac_address:**  Type: string 
           - **mtu:**  Type: integer 
           - **multicast_config:**           
               - **igmp_version:**  Type: string 
               - **multicast_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **nat_address:**  Type: string 
           - **nat_address_v6:**  Type: string 
           - **nat_pools:**           
               - **ipv4_ranges:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **nat_pool_id:**  Type: string 
           - **nat_port:**  Type: integer 
           - **nat_port_v6:**  Type: integer 
           - **nat_zone_id:**  Type: string 
           - **network_context_id:**  Type: string 
           - **parent:**  Type: string 
           - **peer_bypasspair_wan_port_type:**  Type: string 
           - **poe_enabled:**  Type: boolean 
           - **port_channel_config:**           
               - **lacp_enabled:**  Type: boolean 
               - **transmission_mode:**  Type: string 
           - **power_usage_threshold:**  Type: integer 
           - **pppoe_config:**           
               - **host_uniq:**  Type: string 
               - **ip_address_type:**  Type: string 
               - **password:**  Type: string 
               - **reconnection_delay:**  Type: integer 
               - **service_name:**  Type: string 
               - **username:**  Type: string 
           - **scope:**  Type: string 
           - **secondary_ip_configs:**           
               - **ipv4_address:**  Type: string 
               - **scope:**  Type: string 
           - **service_link_config:**           
               - **gre_config:**           
                   - **csum:**  Type: boolean 
                   - **keepalive_enable:**  Type: boolean 
                   - **keepalive_fail_count:**  Type: integer 
                   - **keepalive_interval:**  Type: integer 
               - **ipsec_config:**           
                   - **authentication:**           
                       - **certificate:**  Type: string 
                       - **certificate_profile_id:**  Type: string 
                       - **comment:**  Type: string 
                       - **ikev1_params:**           
                           - **xauth_id:**  Type: string 
                           - **xauth_secret:**  Type: string 
                           - **xauth_secret_encrypted:**  Type: string 
                           - **xauth_secret_hash:**  Type: string 
                           - **xauth_type:**  Type: string 
                       - **local_ca_certificate:**  Type: string 
                       - **local_id:**  Type: string 
                       - **local_id_custom:**  Type: string 
                       - **local_pa_certificate_id:**  Type: string 
                       - **pa_master_key_id:**  Type: string 
                       - **passphrase:**  Type: string 
                       - **passphrase_encrypted:**  Type: string 
                       - **peer_id_check:**  Type: string 
                       - **permit_peer_id_mismatch:**  Type: boolean 
                       - **private_key:**  Type: string 
                       - **private_key_encrypted:**  Type: string 
                       - **remote_ca_certificate:**  Type: string 
                       - **remote_id:**  Type: string 
                       - **secret:**  Type: string 
                       - **secret_encrypted:**  Type: string 
                       - **secret_hash:**  Type: string 
                       - **strict_validation_peer_extended_key_use:**  Type: boolean 
                       - **type:**  Type: string 
                       - **x509Objects:**           
                           - **certHolder:**  Type: object 
                           - **certificate:**  Type: string 
                           - **is_local_ca_cert_set:**  Type: boolean 
                           - **is_remote_ca_cert_set:**  Type: boolean 
                           - **keyPair:**  Type: object 
                           - **local_ca_certificate:**  Type: string 
                           - **local_ca_certs_set:**  [Type: object] 
                           - **passphrase:**  Type: string 
                           - **pkcs12_certificate:**  Type: string 
                           - **privateKey:**  Type: java.security.privatekey 
                           - **private_key:**  Type: string 
                           - **remote_ca_certificate:**  Type: string 
                           - **remote_ca_certs_set:**  [Type: object] 
                   - **ipsec_profile_id:**  Type: string 
               - **last_parent:**  Type: string 
               - **parent:**  Type: string 
               - **passive_mode:**           
                   - **enable:**  Type: boolean 
                   - **peer_ip_dynamic:**  Type: boolean 
               - **peer:**           
                   - **hostname:**  Type: string 
                   - **ip_addresses:**  [Type: string] 
               - **service_endpoint_id:**  Type: string 
               - **type:**  Type: string 
           - **sgi_apply_static_tag:**  Type: boolean 
           - **site_wan_interface_ids:**  [Type: string] 
           - **static_arp_configs:**           
               - **ipv4_address:**  Type: string 
               - **mac_address:**  Type: string 
           - **sub_interface:**           
               - **vlan_id:**  Type: integer 
           - **switch_port_config:**           
               - **access_vlan_id:**  Type: integer 
               - **bpdu_guard_enabled:**  Type: boolean 
               - **forward_fast_enabled:**  Type: boolean 
               - **native_vlan_id:**  Type: integer 
               - **root_guard_enabled:**  Type: boolean 
               - **storm_control_config:**           
                   - **broadcast_threshold:**  Type: integer 
                   - **multicast_threshold:**  Type: integer 
                   - **unicast_threshold:**  Type: integer 
               - **stp_port_cost:**  Type: integer 
               - **stp_port_enabled:**  Type: boolean 
               - **stp_port_priority:**  Type: integer 
               - **trunk_vlans:**  [Type: string] 
               - **vlan_mode:**  Type: string 
               - **voice_vlan_id:**  Type: integer 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 
           - **used_for:**  Type: string 
           - **vlan_config:**           
               - **mstp_instance:**  Type: integer 
               - **vlan_id:**  Type: integer 
               - **voice_enabled:**  Type: boolean 
           - **vrf_context_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces".format(api_version,
                                                                                     site_id,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def interfaces_elementshells(self, site_id, elementshell_id, data, api_version="v2.4"):
        """
        POST Interfaces_Elementshells API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}/interfaces".format(api_version,
                                                                                          site_id,
                                                                                          elementshell_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def interfaces_operations(self, site_id, element_id, interface_id, data, api_version="v2.0"):
        """
        Reset action on interface (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}/operations".format(api_version,
                                                                                                   site_id,
                                                                                                   element_id,
                                                                                                   interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def iotdevicemappings_query(self, data, api_version="v2.0"):
        """
        Query the Active Device Profiles (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **category:**  Type: string 
           - **confidence_score:**  Type: integer 
           - **firewallids:**  [Type: string] 
           - **first_seen_date:**  Type: string 
           - **hostname:**  Type: string 
           - **ip_address:**  Type: string 
           - **mac_address:**  Type: string 
           - **model:**  Type: string 
           - **os_combined:**  Type: string 
           - **os_group:**  Type: string 
           - **primaryDeviceid:**  Type: string 
           - **profile:**  Type: string 
           - **profile_type:**  Type: string 
           - **risk_level:**  Type: string 
           - **risk_score:**  Type: integer 
           - **secondaryDevicesList:**  [Type: string] 
           - **trafficRestricted:**  Type: string 
           - **vendor:**  Type: string 
           - **verdictUpdateTime:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/iotdevicemappings/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def iotdictionary_query(self, data, api_version="v2.0"):
        """
        Query the Device Dictionary (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **add:**  Type: boolean 
           - **name:**  Type: string 
           - **stale:**  Type: boolean 
           - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/iotdictionary/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def iotservices(self, data, api_version="v2.0"):
        """
        POST the confidence score of the mappings stored in the IOT portal (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **device_confidence_score:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/iotservices".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfix(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create a IPFix Config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **collector_config:**           
               - **host:**  Type: string 
               - **host_port:**  Type: integer 
               - **ipfixcollectorcontext_id:**  Type: string 
               - **max_message_size:**  Type: integer 
               - **protocol:**  Type: string 
           - **description:**  Type: string 
           - **export_cache_timeout:**  Type: integer 
           - **filters:**           
               - **app_def_ids:**  [Type: string] 
               - **dst_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dst_prefixes_id:**  Type: string 
               - **ipfixfiltercontext_ids:**  [Type: string] 
               - **priority_traffic_types:**  [Type: string] 
               - **protocols:**  [Type: string] 
               - **rtp_transport_type:**  Type: string 
               - **src_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **src_prefixes_id:**  Type: string 
               - **wan_path_direction:**  Type: string 
           - **ipfixprofile_id:**  Type: string 
           - **ipfixtemplate_id:**  Type: string 
           - **name:**  Type: string 
           - **sampler:**           
               - **algorithm:**  Type: string 
               - **time_interval:**  Type: integer 
               - **time_spacing:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ipfix".format(api_version,
                                                                                site_id,
                                                                                element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixcollectorcontexts(self, data, api_version="v2.0"):
        """
        Create a IPFix Collector context (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixcollectorcontexts".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixfiltercontexts(self, data, api_version="v2.0"):
        """
        Create a IPFix Filter context (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixfiltercontexts".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixglobalprefixes(self, data, api_version="v2.0"):
        """
        Create a IPFix Global prefix (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixglobalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixprofiles(self, data, api_version="v2.0"):
        """
        Create a IPFix Profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **collector_config:**           
               - **host:**  Type: string 
               - **host_port:**  Type: integer 
               - **ipfixcollectorcontext_id:**  Type: string 
               - **max_message_size:**  Type: integer 
               - **protocol:**  Type: string 
           - **description:**  Type: string 
           - **export_cache_timeout:**  Type: integer 
           - **filters:**           
               - **app_def_ids:**  [Type: string] 
               - **dst_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dst_prefixes_id:**  Type: string 
               - **ipfixfiltercontext_ids:**  [Type: string] 
               - **priority_traffic_types:**  [Type: string] 
               - **protocols:**  [Type: string] 
               - **rtp_transport_type:**  Type: string 
               - **src_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **src_prefixes_id:**  Type: string 
               - **wan_path_direction:**  Type: string 
           - **ipfixtemplate_id:**  Type: string 
           - **name:**  Type: string 
           - **sampler:**           
               - **algorithm:**  Type: string 
               - **time_interval:**  Type: integer 
               - **time_spacing:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixtemplates(self, data, api_version="v2.0"):
        """
        Create a IPFix template (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **flow_fields:**  [Type: string] 
           - **generate_biflow:**  Type: boolean 
           - **name:**  Type: string 
           - **option_export_timeout:**  Type: integer 
           - **options:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **template_export_timeout:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixtemplates".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipsecprofiles(self, data, api_version="v2.2"):
        """
        Create a new IPSEC Profile (v2.2)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **authentication:**           
               - **certificate:**  Type: string 
               - **certificate_profile_id:**  Type: string 
               - **comment:**  Type: string 
               - **ikev1_params:**           
                   - **xauth_id:**  Type: string 
                   - **xauth_secret:**  Type: string 
                   - **xauth_secret_encrypted:**  Type: string 
                   - **xauth_secret_hash:**  Type: string 
                   - **xauth_type:**  Type: string 
               - **local_ca_certificate:**  Type: string 
               - **local_id:**  Type: string 
               - **local_id_custom:**  Type: string 
               - **local_pa_certificate_id:**  Type: string 
               - **pa_master_key_id:**  Type: string 
               - **passphrase:**  Type: string 
               - **passphrase_encrypted:**  Type: string 
               - **peer_id_check:**  Type: string 
               - **permit_peer_id_mismatch:**  Type: boolean 
               - **private_key:**  Type: string 
               - **private_key_encrypted:**  Type: string 
               - **remote_ca_certificate:**  Type: string 
               - **remote_id:**  Type: string 
               - **secret:**  Type: string 
               - **secret_encrypted:**  Type: string 
               - **secret_hash:**  Type: string 
               - **strict_validation_peer_extended_key_use:**  Type: boolean 
               - **type:**  Type: string 
               - **x509Objects:**           
                   - **certHolder:**  Type: object 
                   - **certificate:**  Type: string 
                   - **is_local_ca_cert_set:**  Type: boolean 
                   - **is_remote_ca_cert_set:**  Type: boolean 
                   - **keyPair:**  Type: object 
                   - **local_ca_certificate:**  Type: string 
                   - **local_ca_certs_set:**  [Type: object] 
                   - **passphrase:**  Type: string 
                   - **pkcs12_certificate:**  Type: string 
                   - **privateKey:**  Type: java.security.privatekey 
                   - **private_key:**  Type: string 
                   - **remote_ca_certificate:**  Type: string 
                   - **remote_ca_certs_set:**  [Type: object] 
           - **description:**  Type: string 
           - **dpd_delay:**  Type: integer 
           - **dpd_enable:**  Type: boolean 
           - **dpd_timeout:**  Type: integer 
           - **esp_group:**           
               - **lifetime:**  Type: integer 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
           - **ike_group:**           
               - **lifetime:**  Type: integer 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **used_for:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def lannetworks(self, site_id, data, api_version="v3.3"):
        """
        Create a new LAN (v3.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.3)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_config:**           
               - **default_routers:**  [Type: string] 
               - **dhcp_relay:**           
                   - **enabled:**  Type: boolean 
                   - **option_82:**           
                       - **circuit_id:**  Type: string 
                       - **enabled:**  Type: boolean 
                       - **reforwarding_policy:**  Type: string 
                       - **remote_id:**  Type: string 
                   - **server_ips:**  [Type: string] 
                   - **source_interface:**  Type: string 
               - **dhcp_server:**           
                   - **broadcast_address:**  Type: string 
                   - **custom_options:**           
                       - **option_definition:**  Type: string 
                       - **option_value:**  Type: string 
                   - **default_lease_time:**  Type: integer 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **dns_servers:**  [Type: string] 
                   - **domain_name:**  Type: string 
                   - **gateway:**  Type: string 
                   - **id:**  Type: string 
                   - **ip_ranges:**           
                       - **end_ip:**  Type: string 
                       - **start_ip:**  Type: string 
                   - **max_lease_time:**  Type: integer 
                   - **network_context_id:**  Type: string 
                   - **static_mappings:**           
                       - **ip_address:**  Type: string 
                       - **mac:**  Type: string 
                       - **name:**  Type: string 
                   - **subnet:**  Type: string 
                   - **tags:**  [Type: string] 
               - **prefixes:**  [Type: string] 
           - **ipv6_config:**           
               - **default_routers:**  [Type: string] 
               - **prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **scope:**  Type: string 
           - **tags:**  [Type: string] 
           - **vrf_context_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/lannetworks".format(api_version,
                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def localprefixfilters(self, data, api_version="v2.0"):
        """
        Create a new local prefix filter. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/localprefixfilters".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def login(self, data, api_version="v2.0"):
        """
        Login api

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/login".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def login_clients(self, client_id, data, api_version="v2.0"):
        """
        POST Login_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/login".format(api_version,
                                                                      client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def logout_clients(self, data, api_version="v2.0"):
        """
        POST Logout_Clients API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/logout".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def lqm_point_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Lqm_Point_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/lqm_point_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def metrics_monitor(self, data, api_version="v2.6"):
        """
        POST Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def migratecbtoezb(self, data, api_version="v2.0"):
        """
        Trigger migration API (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **compatible_sites:**           
               - **site_id:**  Type: string 
               - **site_name:**  Type: string 
           - **current_step:**  Type: string 
           - **failed_sites:**           
               - **site_id:**  Type: string 
               - **site_name:**  Type: string 
           - **incompatible_sites:**           
               - **errors:**           
                   - **error:**  Type: string 
                   - **error_message:**  Type: string 
               - **site_id:**  Type: string 
               - **site_name:**  Type: string 
               - **tunnels:**           
                   - **errors:**           
                       - **error:**  Type: string 
                       - **error_message:**  Type: string 
                   - **ipsec_tunnel_id:**  Type: string 
                   - **ipsec_tunnel_name:**  Type: string 
                   - **servicelinks:**           
                       - **bgppeer_id:**  Type: string 
                       - **element_id:**  Type: string 
                       - **error:**           
                           - **error:**  Type: string 
                           - **error_message:**  Type: string 
                       - **ike_gateway_id:**  Type: string 
                       - **ipsec_tunnel_id:**  Type: string 
                       - **remote_network_id:**  Type: string 
                       - **servicelink_id:**  Type: string 
                       - **servicelink_name:**  Type: string 
                       - **waninterface_id:**  Type: string 
                   - **waninterface_id:**  Type: string 
           - **is_fawkes:**  Type: boolean 
           - **job_id:**  Type: string 
           - **migrated_sites:**           
               - **site_id:**  Type: string 
               - **site_name:**  Type: string 
           - **status:**  Type: string 
           - **steps:**           
               - **attempts:**  Type: integer 
               - **error:**  Type: string 
               - **name:**  Type: string 
               - **started_at:**  Type: integer 
               - **status:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/migratecbtoezb".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_agg_bw_stats(self, data, api_version="v2.0"):
        """
        POST Monitor_Agg_Bw_Stats API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/agg_bw_stats".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_aggregatebandwidth_query(self, data, api_version="v2.0"):
        """
        POST Monitor_Aggregatebandwidth_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aggregatebandwidth/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_app_acceleration(self, data, api_version="v2.0"):
        """
        POST Monitor_App_Acceleration API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/app_acceleration".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_applicationstats_query(self, data, api_version="v2.0"):
        """
        POST Monitor_Applicationstats_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/applicationstats/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_applicationsummary_query(self, data, api_version="v2.0"):
        """
        POST Monitor_Applicationsummary_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/applicationsummary/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_metrics_probes(self, data, api_version="v2.0"):
        """
        POST Monitor_Metrics_Probes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/metrics/probes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_probe_point_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Probe_Point_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/probe_point_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_topn_traffic_vol_query(self, data, api_version="v2.0"):
        """
        POST Monitor_Topn_Traffic_Vol_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/topn_traffic_vol/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def mroute_multicast_aggregates_monitor(self, data, api_version="v2.0"):
        """
        POST Mroute_Multicast_Aggregates_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aggregates/multicast/mroute".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def mstp_instances(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create a MSTP Instance (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **instance_number:**  Type: integer 
           - **instance_priority:**  Type: integer 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/mstp_instances".format(api_version,
                                                                                         site_id,
                                                                                         element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastpeergroups(self, data, api_version="v2.1"):
        """
        Create multicast peer group (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **is_source_site_receiver:**  Type: boolean 
           - **name:**  Type: string 
           - **peer_sites:**           
               - **peer_site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastpeergroups".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastrps(self, site_id, element_id, data, api_version="v2.0"):
        """
        Creates Multicast RP config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **groups:**           
               - **ipv4_prefix:**  Type: string 
               - **is_active_rp:**  Type: boolean 
           - **ipv4_address:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastrps".format(api_version,
                                                                                       site_id,
                                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastsourcesiteconfigs(self, site_id, data, api_version="v2.0"):
        """
        Create multicast source site config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **site_configs:**           
               - **group_ipv4_prefix:**  Type: string 
               - **source_ipv4_address:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiteconfigs".format(api_version,
                                                                                         site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natglobalprefixes(self, data, api_version="v2.0"):
        """
        Create a new NAT global prefix. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natglobalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natlocalprefixes(self, data, api_version="v2.0"):
        """
        Create a new NAT local prefix. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natlocalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicypools(self, data, api_version="v2.0"):
        """
        Create a new NATPolicy Pool. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicypools".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicyrules(self, natpolicyset_id, data, api_version="v2.0"):
        """
        Create a new NAT Policy Rule (v2.0)

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **actions:**           
               - **nat_pool_id:**  Type: string 
               - **port:**  Type: integer 
               - **protocols:**  [Type: string] 
               - **type:**  Type: string 
           - **description:**  Type: string 
           - **destination_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **destination_prefixes:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **ipv4_prefixes:**  [Type: string] 
               - **ipv6_prefixes:**  [Type: string] 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **destination_prefixes_id:**  Type: string 
           - **destination_zone:**           
               - **default_for_public_interfaces:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **destination_zone_id:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **enabled:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **natpolicypools:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **policyset_id:**  Type: string 
           - **protocol:**  Type: integer 
           - **region:**  Type: string 
           - **source_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **source_prefixes:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **ipv4_prefixes:**  [Type: string] 
               - **ipv6_prefixes:**  [Type: string] 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **source_prefixes_id:**  Type: string 
           - **source_zone:**           
               - **default_for_public_interfaces:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **source_zone_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}/natpolicyrules".format(api_version,
                                                                                     natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicysets(self, data, api_version="v2.0"):
        """
        Create a new NAT Policy Set (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **destination_zone_policyrule_order:**  [Type: string] 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **policy_req_version:**  Type: string 
           - **policy_rules:**           
               - **actions:**           
                   - **nat_pool_id:**  Type: string 
                   - **port:**  Type: integer 
                   - **protocols:**  [Type: string] 
                   - **type:**  Type: string 
               - **description:**  Type: string 
               - **destination_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **destination_prefixes:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **ipv4_prefixes:**  [Type: string] 
                   - **ipv6_prefixes:**  [Type: string] 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **destination_prefixes_id:**  Type: string 
               - **destination_zone:**           
                   - **default_for_public_interfaces:**  Type: boolean 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **destination_zone_id:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **enabled:**  Type: boolean 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **natpolicypools:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **policyset_id:**  Type: string 
               - **protocol:**  Type: integer 
               - **region:**  Type: string 
               - **source_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **source_prefixes:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **ipv4_prefixes:**  [Type: string] 
                   - **ipv6_prefixes:**  [Type: string] 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **source_prefixes_id:**  Type: string 
               - **source_zone:**           
                   - **default_for_public_interfaces:**  Type: boolean 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **source_zone_id:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **send_to_element:**  Type: boolean 
           - **source_zone_policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **update_order:**  Type: boolean 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicysetstacks(self, data, api_version="v2.0"):
        """
        Create a new NATPolicySet Stack (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysetstacks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natzones(self, data, api_version="v2.0"):
        """
        Create a Nat Policy Zone. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_for_public_interfaces:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natzones".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def network_point_metrics_bw_monitor(self, data, api_version="v2.0"):
        """
        POST Network_Point_Metrics_Bw_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/network_point_metrics_bw".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def network_point_metrics_hs_monitor(self, data, api_version="v2.0"):
        """
        POST Network_Point_Metrics_Hs_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/network_point_metrics_hs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def network_point_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Network_Point_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/network_point_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkcontexts(self, data, api_version="v2.0"):
        """
        Create a new LAN segment (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkcontexts".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicyglobalprefixes(self, data, api_version="v2.1"):
        """
        Create a new global prefix. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyglobalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicyrules(self, networkpolicyset_id, data, api_version="v2.4"):
        """
        Create a new NetworkPolicyRule (v2.4)

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **best_path_config:**           
               - **metric:**  Type: string 
               - **metric_type:**  Type: string 
               - **probe_config_id:**  Type: string 
           - **description:**  Type: string 
           - **dest_device_ids:**  [Type: string] 
           - **destination_prefixes_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 
           - **source_prefixes_id:**  Type: string 
           - **src_device_ids:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **user_or_group:**           
               - **user_group_ids:**  [Type: string] 
               - **user_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}/networkpolicyrules".format(api_version,
                                                                                             networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicysets(self, data, api_version="v2.0"):
        """
        Create a new NetworkPolicySet (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **policy_req_version:**  Type: string 
           - **policy_rules:**           
               - **app_def_ids:**  [Type: string] 
               - **description:**  Type: string 
               - **destination_prefixes_id:**  Type: string 
               - **enabled:**  Type: boolean 
               - **id:**  Type: string 
               - **name:**  Type: string 
               - **network_context_id:**  Type: string 
               - **order_number:**  Type: integer 
               - **paths_allowed:**           
                   - **active_paths:**           
                       - **label:**  Type: string 
                       - **path_type:**  Type: string 
                   - **backup_paths:**           
                       - **label:**  Type: string 
                       - **path_type:**  Type: string 
                   - **l3_failure_paths:**           
                       - **label:**  Type: string 
                       - **path_type:**  Type: string 
               - **service_context:**           
                   - **active_service_label_id:**  Type: string 
                   - **active_service_label_type:**  Type: string 
                   - **backup_service_label_id:**  Type: string 
                   - **backup_service_label_type:**  Type: string 
                   - **type:**  Type: string 
               - **source_prefixes_id:**  Type: string 
               - **tags:**  [Type: string] 
           - **region:**  Type: string 
           - **send_to_element:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicysetstacks(self, data, api_version="v2.0"):
        """
        Create a new NetworkPolicySetStack (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset:**           
               - **clone_from:**  Type: string 
               - **defaultrule_policyset:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policy_req_version:**  Type: string 
               - **policy_rules:**           
                   - **app_def_ids:**  [Type: string] 
                   - **description:**  Type: string 
                   - **destination_prefixes_id:**  Type: string 
                   - **enabled:**  Type: boolean 
                   - **id:**  Type: string 
                   - **name:**  Type: string 
                   - **network_context_id:**  Type: string 
                   - **order_number:**  Type: integer 
                   - **paths_allowed:**           
                       - **active_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                       - **backup_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                       - **l3_failure_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                   - **service_context:**           
                       - **active_service_label_id:**  Type: string 
                       - **active_service_label_type:**  Type: string 
                       - **backup_service_label_id:**  Type: string 
                       - **backup_service_label_type:**  Type: string 
                       - **type:**  Type: string 
                   - **source_prefixes_id:**  Type: string 
                   - **tags:**  [Type: string] 
               - **region:**  Type: string 
               - **send_to_element:**  Type: boolean 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **legacy_policystack:**  Type: boolean 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **policyset_ids_update:**  Type: boolean 
           - **policysets:**           
               - **clone_from:**  Type: string 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policy_rules:**           
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **policyset_id:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **region:**  Type: string 
               - **send_to_element:**  Type: boolean 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysetstacks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicyglobalprefixes(self, data, api_version="v2.1"):
        """
        Create an Security Policy V2 Global Prefix (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyglobalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicylocalprefixes(self, data, api_version="v2.0"):
        """
        Create an Security Policy V2 Local Prefix (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicylocalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicyrules(self, ngfwsecuritypolicyset_id, data, api_version="v2.3"):
        """
        Create a Security Policy V2 Rule under a policy set (v2.3)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **dest_device_ids:**  [Type: string] 
           - **destination_prefix_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **security_profile_group_id:**  Type: string 
           - **services:**           
               - **destination_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **protocol:**  Type: integer 
               - **source_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
           - **source_prefix_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 
           - **src_device_ids:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **user_or_group:**           
               - **user_group_ids:**  [Type: string] 
               - **user_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules".format(api_version,
                                                                                                       ngfwsecuritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicysets(self, data, api_version="v2.0"):
        """
        Create a Security Policy V2 Set (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicysetstacks(self, data, api_version="v2.0"):
        """
        Create a Security Policy V2 Set Stack (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysetstacks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def object_stats_aiops_monitor(self, data, api_version="v2.1"):
        """
        POST Object_Stats_Aiops_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/object_stats".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def object_stats_monitor(self, data, api_version="v2.7"):
        """
        POST Object_Stats_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.7)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/object_stats".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def operations_e(self, element_id, data, api_version="v2.0"):
        """
        POST Operations_E API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/operations".format(api_version,
                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def operations_h(self, site_id, hubcluster_id, data, api_version="v4.0"):
        """
        POST Operations_H API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/operations".format(api_version,
                                                                                        site_id,
                                                                                        hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def operations_s(self, site_id, data, api_version="v2.0"):
        """
        POST Operations_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/operations".format(api_version,
                                                                         site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def operations_t(self, machine_id, data, api_version="v2.5"):
        """
        POST Operations_T API Function

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/operations".format(api_version,
                                                                            machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ops_bgppeers(self, site_id, element_id, bgppeer_id, data, api_version="v2.0"):
        """
        POST Ops_Bgppeers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}/operations".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ops_deviceidprofiles(self, deviceidprofile_id, data, api_version="v2.0"):
        """
        POST Ops_Deviceidprofiles API Function

          **Parameters:**:

          - **deviceidprofile_id**: Device Id Profile ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/deviceidprofiles/{}/operations".format(api_version,
                                                                                    deviceidprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ops_spokeclusters(self, site_id, spokecluster_id, data, api_version="v2.0"):
        """
        POST Ops_Spokeclusters API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/{}/operations".format(api_version,
                                                                                          site_id,
                                                                                          spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ops_vfflicenses(self, vfflicense_id, data, api_version="v2.0"):
        """
        POST Ops_Vfflicenses API Function

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}/operations".format(api_version,
                                                                               vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ops_vpnlinks(self, vpnlink_id, data, api_version="v2.0"):
        """
        POST Ops_Vpnlinks API Function

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vpnlinks/{}/operations".format(api_version,
                                                                            vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ospfconfigs(self, site_id, element_id, data, api_version="v2.0"):
        """
        Creates OSPF config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **areas:**           
               - **area_id:**  Type: integer 
               - **area_type:**  Type: string 
           - **description:**  Type: string 
           - **interfaces:**           
               - **area_id:**  Type: integer 
               - **interface_id:**  Type: string 
               - **ospf_config_override:**           
                   - **cost:**  Type: integer 
                   - **dead_interval:**  Type: integer 
                   - **hello_interval:**  Type: integer 
                   - **md5_key_id:**  Type: integer 
                   - **md5_secret:**  Type: string 
                   - **retransmit_interval:**  Type: integer 
                   - **transmit_delay:**  Type: integer 
           - **name:**  Type: string 
           - **prefix_adv_route_map_id:**  Type: string 
           - **prefix_adv_type_to_lan:**  Type: string 
           - **redistribute_bgp:**  Type: boolean 
           - **redistribute_route_map_id:**  Type: string 
           - **router_id:**  Type: string 
           - **scope:**  Type: string 
           - **shutdown:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **vrf_context_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfconfigs".format(api_version,
                                                                                      site_id,
                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ospfconfigs_query(self, data, api_version="v2.0"):
        """
        POST Ospfconfigs_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ospfconfigs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ospfdiscoveredneighbors_query(self, data, api_version="v2.0"):
        """
        POST Ospfdiscoveredneighbors_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ospfdiscoveredneighbors/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ospfreachableprefixes_query(self, data, api_version="v2.0"):
        """
        POST Ospfreachableprefixes_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ospfreachableprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def otpaccess(self, element_id, data, api_version="v2.0"):
        """
        Verify Challenge phrase and generate response phrase (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **challenge_phrase:**  Type: string 
           - **response_phrase:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/otpaccess".format(api_version,
                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def pathgroups(self, data, api_version="v2.1"):
        """
        Create a Path Group for a tenant. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **paths:**           
               - **label:**  Type: string 
               - **path_type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/pathgroups".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def pathprefixdistributionfilterassociation(self, site_id, data, api_version="v2.0"):
        """
        POST Pathprefixdistributionfilterassociation API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilterassociation".format(api_version,
                                                                                                      site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def pathprefixdistributionfilterassociation_query(self, data, api_version="v2.0"):
        """
        POST Pathprefixdistributionfilterassociation_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/pathprefixdistributionfilterassociation/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def pathprefixdistributionfilters(self, site_id, data, api_version="v2.0"):
        """
        POST Pathprefixdistributionfilters API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilters".format(api_version,
                                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def pathprefixdistributionfilters_query(self, data, api_version="v2.0"):
        """
        POST Pathprefixdistributionfilters_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/pathprefixdistributionfilters/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtpolicyrules_perfmgmtpolicysets(self, perfmgmtpolicyset_id, data, api_version="v2.2"):
        """
        POST Perfmgmtpolicyrules_Perfmgmtpolicysets API Function

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}/perfmgmtpolicyrules".format(api_version,
                                                                                               perfmgmtpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtpolicyrules_query(self, data, api_version="v2.2"):
        """
        Query PERFMGMT policy rules V2.2. (v2.2)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **actions:**           
               - **action_type:**  Type: string 
               - **app_perf:**           
                   - **bad_health_thresholds:**           
                       - **clear_below:**  Type: integer 
                       - **raise_above:**  Type: integer 
                   - **monitoring_approach:**  Type: string 
               - **circuit_utilization_perf:**           
                   - **bad_health_thresholds:**           
                       - **clear_below:**  Type: integer 
                       - **raise_above:**  Type: integer 
                   - **monitoring_approach:**  Type: string 
               - **lqm_perf:**           
                   - **bad_health_thresholds:**           
                       - **clear_below:**  Type: integer 
                       - **raise_above:**  Type: integer 
                   - **monitoring_approach:**  Type: string 
               - **probe_perf:**           
                   - **bad_health_thresholds:**           
                       - **clear_below:**  Type: integer 
                       - **raise_above:**  Type: integer 
                   - **monitoring_approach:**  Type: string 
               - **sys_perf:**           
                   - **bad_health_thresholds:**           
                       - **clear_below:**  Type: integer 
                       - **raise_above:**  Type: integer 
                   - **monitoring_approach:**  Type: string 
           - **app_filters:**           
               - **app_transfer_types:**  [Type: string] 
               - **application_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **path_filters:**           
               - **label:**  Type: string 
               - **path_type:**  Type: string 
           - **service_label_ids:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **thresholdprofile_id:**  Type: string 
           - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtpolicysets(self, data, api_version="v2.0"):
        """
        Create a new PERFMGMT Policy Set (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **link_health_policyrule_order:**  [Type: string] 
           - **link_health_rules:**           
               - **actions:**           
                   - **action_type:**  Type: string 
                   - **always_on:**  Type: boolean 
                   - **app_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **circuit_utilization_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **lqm_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **probe_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **sys_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
               - **app_filters:**           
                   - **app_transfer_types:**  [Type: string] 
                   - **application_ids:**  [Type: string] 
               - **description:**  Type: string 
               - **enabled:**  Type: boolean 
               - **id:**  Type: string 
               - **name:**  Type: string 
               - **path_filters:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **service_label_ids:**  [Type: string] 
               - **tags:**  [Type: string] 
               - **thresholdprofile_id:**  Type: string 
               - **type:**  Type: string 
           - **name:**  Type: string 
           - **policy_rules:**           
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policyset_id:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **send_to_element:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtpolicysets_query(self, data, api_version="v2.0"):
        """
        Query PERFMGMT Policy Set (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **link_health_policyrule_order:**  [Type: string] 
           - **link_health_rules:**           
               - **actions:**           
                   - **action_type:**  Type: string 
                   - **always_on:**  Type: boolean 
                   - **app_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **circuit_utilization_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **lqm_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **probe_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
                   - **sys_perf:**           
                       - **bad_health_thresholds:**           
                           - **clear_below:**  Type: integer 
                           - **raise_above:**  Type: integer 
                       - **monitoring_approach:**  Type: string 
               - **app_filters:**           
                   - **app_transfer_types:**  [Type: string] 
                   - **application_ids:**  [Type: string] 
               - **description:**  Type: string 
               - **enabled:**  Type: boolean 
               - **id:**  Type: string 
               - **name:**  Type: string 
               - **path_filters:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **service_label_ids:**  [Type: string] 
               - **tags:**  [Type: string] 
               - **thresholdprofile_id:**  Type: string 
               - **type:**  Type: string 
           - **name:**  Type: string 
           - **policy_rules:**           
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policyset_id:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **send_to_element:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtpolicysetstacks(self, data, api_version="v2.0"):
        """
        Create a new PERFMGMT Policy Set Stack (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysetstacks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtpolicysetstacks_query(self, data, api_version="v2.0"):
        """
        Query PERFMGMT Policy Set Stack (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysetstacks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtthresholdprofiles(self, data, api_version="v2.1"):
        """
        Create a new Threshold Profile (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **circuit_utilization_metrics_thresholds:**           
               - **percentage_circuit_utilization:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **flow_metrics_thresholds:**           
               - **percentage_flow_utilization:**  Type: integer 
           - **hard_limit_app_metrics:**           
               - **max_init_failure_rate:**  Type: integer 
               - **max_rtt:**  Type: integer 
               - **udp_trt:**  Type: integer 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **is_default:**  Type: boolean 
           - **lqm_thresholds:**           
               - **max_jitter:**  Type: integer 
               - **max_latency:**  Type: integer 
               - **max_packet_loss:**  Type: integer 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **soft_limit_app_metrics:**           
               - **max_init_failure_rate:**  Type: integer 
               - **max_rtt:**  Type: integer 
               - **udp_trt:**  Type: integer 
           - **synthetic_probe_thresholds:**           
               - **dns_txn_failure_pct:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **init_failure_pct:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **jitter:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **latency:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **packet_loss:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
           - **system_health_metrics_thresholds:**           
               - **cpu_utilization:**  Type: integer 
               - **disk_utilization:**  Type: integer 
               - **memory_utilization:**  Type: integer 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtthresholdprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def perfmgmtthresholdprofiles_query(self, data, api_version="v2.1"):
        """
        Queries db for limit number of tenant level threshold profiles that match query params. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **circuit_utilization_metrics_thresholds:**           
               - **percentage_circuit_utilization:**  Type: integer 
           - **description:**  Type: string 
           - **flow_metrics_thresholds:**           
               - **percentage_flow_utilization:**  Type: integer 
           - **hard_limit_app_metrics:**           
               - **max_init_failure_rate:**  Type: integer 
               - **max_rtt:**  Type: integer 
               - **udp_trt:**  Type: integer 
           - **lqm_thresholds:**           
               - **max_jitter:**  Type: integer 
               - **max_latency:**  Type: integer 
               - **max_packet_loss:**  Type: integer 
               - **min_mos:**  Type: integer 
           - **name:**  Type: string 
           - **soft_limit_app_metrics:**           
               - **max_init_failure_rate:**  Type: integer 
               - **max_rtt:**  Type: integer 
               - **udp_trt:**  Type: integer 
           - **synthetic_probe_thresholds:**           
               - **dns_txn_failure_pct:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **init_failure_pct:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **jitter:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **latency:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
               - **packet_loss:**           
                   - **probe_config_id:**  Type: string 
                   - **value:**  Type: integer 
           - **system_health_metrics_thresholds:**           
               - **cpu_utilization:**  Type: integer 
               - **disk_utilization:**  Type: integer 
               - **memory_utilization:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtthresholdprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policyrules(self, policyset_id, data, api_version="v3.1"):
        """
        Create a new Policy (v3.1)

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **app_def_id:**  Type: string 
           - **app_def_name:**  Type: string 
           - **default_rule:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **lan_network_ids:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **priority_num:**  Type: integer 
           - **region:**  Type: string 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 
           - **site_paths_allowed:**           
               - **wn_name:**  Type: string 
               - **wp_type:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}/policyrules".format(api_version,
                                                                               policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policysets(self, data, api_version="v3.0"):
        """
        Create a new Policy Set (v3.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 

           - **bandwidth_allocation_schemes:**           
               - **bandwidth_range:**           
                   - **high:**  Type: number 
                   - **low:**  Type: number 
               - **business_priorities:**           
                   - **bandwidth_allocation:**  Type: number 
                   - **bandwidth_split_per_type:**           
                       - **bulk:**  Type: number 
                       - **rt_audio:**  Type: number 
                       - **rt_video:**  Type: number 
                       - **transactional:**  Type: number 
                   - **priority_num:**  Type: integer 
           - **business_priority_names:**           
               - **priority_name:**  Type: string 
               - **priority_num:**  Type: integer 
           - **default_policy:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prefixdistributionspokelists(self, site_id, data, api_version="v2.0"):
        """
        POST Prefixdistributionspokelists API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixdistributionspokelists".format(api_version,
                                                                                           site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prefixfilters(self, site_id, data, api_version="v2.0"):
        """
        Create an association between site and security prefix filter. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **filters:**           
               - **ip_prefixes:**  [Type: string] 
               - **type:**  Type: string 
           - **prefix_filter_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters".format(api_version,
                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicyglobalprefixes(self, data, api_version="v2.1"):
        """
        Create a new global prefix. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyglobalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicyrules(self, prioritypolicyset_id, data, api_version="v2.2"):
        """
        Create a new PriorityPolicyRule (v2.2)

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **dest_device_ids:**  [Type: string] 
           - **destination_prefixes_id:**  Type: string 
           - **dscp:**           
               - **value:**  Type: integer 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **priority_number:**  Type: integer 
           - **source_prefixes_id:**  Type: string 
           - **src_device_ids:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **user_or_group:**           
               - **user_group_ids:**  [Type: string] 
               - **user_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}/prioritypolicyrules".format(api_version,
                                                                                               prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicysets(self, data, api_version="v2.0"):
        """
        Create a new PriorityPolicySet (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **bandwidth_allocation_schemes:**           
               - **bandwidth_range:**           
                   - **high:**  Type: number 
                   - **low:**  Type: number 
               - **business_priorities:**           
                   - **bandwidth_allocation:**  Type: number 
                   - **bandwidth_split_per_type:**           
                       - **bulk:**  Type: number 
                       - **rt_audio:**  Type: number 
                       - **rt_video:**  Type: number 
                       - **transactional:**  Type: number 
                   - **priority_number:**  Type: integer 
           - **business_priority_names:**           
               - **priority_name:**  Type: string 
               - **priority_num:**  Type: integer 
           - **clone_from:**  Type: string 
           - **default_rule_dscp_mappings:**           
               - **dscp:**  [Type: integer] 
               - **priority_number:**  Type: integer 
               - **transfer_type:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **template:**  Type: boolean 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicysetstacks(self, data, api_version="v2.0"):
        """
        Create a new PriorityPolicySetStack (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysetstacks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prismaaccess_configs(self, site_id, data, api_version="v2.0"):
        """
        Create a Prisma Access Config with remote networks and security processing node (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **remote_networks:**           
               - **edge_location_display:**  Type: string 
               - **edge_location_value:**  Type: string 
               - **remote_network_names:**  [Type: string] 
               - **service_link_ids:**  [Type: string] 
               - **spn_name:**  Type: string 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismaaccess_configs".format(api_version,
                                                                                   site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prismasase_connections(self, site_id, data, api_version="v2.1"):
        """
        Create a new SASE connection (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **enabled_wan_interface_ids:**  [Type: string] 
           - **ipsec_tunnel_configs:**           
               - **anti_replay:**  Type: boolean 
               - **copy_tos:**  Type: boolean 
               - **enable_gre_encapsulation:**  Type: boolean 
               - **ike_key_exchange:**  Type: string 
               - **prismaaccess_ike_crypto_profile_id:**  Type: string 
               - **prismaaccess_ipsec_profile_id:**  Type: string 
               - **tunnel_monitoring:**  Type: boolean 
           - **is_active:**  Type: boolean 
           - **is_enabled:**  Type: boolean 
           - **license_type:**  Type: string 
           - **prismaaccess_edge_location:**  [Type: string] 
           - **prismaaccess_qos_cir_mbps:**  Type: integer 
           - **prismaaccess_qos_profile_id:**  Type: string 
           - **remote_network_groups:**           
               - **ipsec_tunnels:**           
                   - **authentication:**           
                       - **branch_ike_identification:**  Type: string 
                       - **prismaaccess_ike_identification:**  Type: string 
                       - **psk:**  Type: string 
                   - **name:**  Type: string 
                   - **routing:**           
                       - **branch_as_number:**  Type: string 
                       - **branch_ip_address:**  Type: string 
                       - **prismaaccess_ip_address:**  Type: string 
                   - **routing_configs:**           
                       - **advertise_default_route:**  Type: boolean 
                       - **bgp_secret:**  Type: string 
                       - **export_routes:**  Type: boolean 
                       - **summarize_mobile_routes_before_advertise:**  Type: boolean 
                   - **wan_interface_id:**  Type: string 
               - **name:**  Type: string 
               - **spn_name:**  [Type: string] 
           - **routing_configs:**           
               - **advertise_default_route:**  Type: boolean 
               - **bgp_secret:**  Type: string 
               - **export_routes:**  Type: boolean 
               - **summarize_mobile_routes_before_advertise:**  Type: boolean 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismasase_connections".format(api_version,
                                                                                     site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prismasase_connections_configs(self, data, api_version="v3.1"):
        """
        Create a new SASE connection config (v3.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **deployment_mode:**  Type: string 
           - **extended_tunnel_cidrs:**           
               - **extended_tunnel_cidr:**  Type: string 
               - **priority:**  Type: integer 
           - **ipsec_profile:**           
               - **dpd_delay:**  Type: integer 
               - **dpd_enable:**  Type: boolean 
               - **esp_group:**           
                   - **lifetime:**  Type: integer 
                   - **proposals:**           
                       - **dh_groups:**  Type: string 
                       - **encryption:**  Type: string 
                       - **hash:**  Type: string 
               - **ike_group:**           
                   - **lifetime:**  Type: integer 
                   - **proposals:**           
                       - **dh_groups:**  Type: string 
                       - **encryption:**  Type: string 
                       - **hash:**  Type: string 
           - **panorama_sub_tenant_name:**  Type: string 
           - **prisma_sdwan_bgp_as_number:**  Type: string 
           - **security_zone_id:**  Type: string 
           - **tunnel_cidr:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismasase_connections/configs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prismasase_connections_query(self, data, api_version="v2.0"):
        """
        Get a list of SASE connections (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismasase_connections/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def probeconfigs(self, data, api_version="v2.0"):
        """
        Create a new Probe Config (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **endpoints:**           
               - **allow_insecure_https_connection:**  Type: boolean 
               - **dns_server_ip:**  Type: string 
               - **fqdn:**  Type: string 
               - **http_response_codes:**  [Type: integer] 
               - **http_response_string:**  Type: string 
               - **ipv4_address:**  Type: string 
               - **path_types:**  [Type: string] 
               - **probe_count:**  Type: integer 
               - **probe_cycle_duration:**  Type: integer 
               - **protocol:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeconfigs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def probeconfigs_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of tenant level probe profiles that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **endpoints:**           
               - **allow_insecure_https_connection:**  Type: boolean 
               - **dns_server_ip:**  Type: string 
               - **fqdn:**  Type: string 
               - **http_response_codes:**  [Type: integer] 
               - **http_response_string:**  Type: string 
               - **ipv4_address:**  Type: string 
               - **path_types:**  [Type: string] 
               - **probe_count:**  Type: integer 
               - **probe_cycle_duration:**  Type: integer 
               - **protocol:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeconfigs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def probeprofiles(self, data, api_version="v2.0"):
        """
        Create a new PROBE Profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **probe_config_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def probeprofiles_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of tenant level probe profiles that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **probe_config_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def qos_application_aggregates_monitor(self, data, api_version="v2.0"):
        """
        POST Qos_Application_Aggregates_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aggregates/application/qos".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def qos_metrics_application_monitor(self, data, api_version="v2.0"):
        """
        POST Qos_Metrics_Application_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/application/qos_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def qos_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Qos_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/qos_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_activeuserips(self, data, api_version="v2.1"):
        """
        POST Query_Activeuserips API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/activeuserips/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_apnprofiles(self, data, api_version="v2.0"):
        """
        POST Query_Apnprofiles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/apnprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_appdefs(self, data, api_version="v2.6"):
        """
        POST Query_Appdefs API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_auditlog(self, data, api_version="v2.1"):
        """
        POST Query_Auditlog API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/auditlog/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_bgppeers(self, site_id, element_id, data, api_version="v3.0"):
        """
        POST Query_Bgppeers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/query".format(api_version,
                                                                                         site_id,
                                                                                         element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_bgppeers_t(self, data, api_version="v3.0"):
        """
        POST Query_Bgppeers_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bgppeers/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_bulk_config_state_e(self, data, api_version="v2.0"):
        """
        POST Query_Bulk_Config_State_E API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/bulk_config_state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_bulk_config_state_networks(self, data, api_version="v2.0"):
        """
        POST Query_Bulk_Config_State_Networks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networks/bulk_config_state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_bulk_config_state_policysets(self, data, api_version="v2.0"):
        """
        POST Query_Bulk_Config_State_Policysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/bulk_config_state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_bulk_config_state_s(self, data, api_version="v2.0"):
        """
        POST Query_Bulk_Config_State_S API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/bulk_config_state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_cellular_modules(self, data, api_version="v2.0"):
        """
        POST Query_Cellular_Modules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cellular_modules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_clients(self, data, api_version="v2.0"):
        """
        POST Query_Clients API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_correlationevents_anynetlinks(self, data, api_version="v2.2"):
        """
        POST Query_Correlationevents_Anynetlinks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_correlationevents_e(self, data, api_version="v2.1"):
        """
        POST Query_Correlationevents_E API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_correlationevents_interfaces(self, data, api_version="v2.1"):
        """
        POST Query_Correlationevents_Interfaces API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/interfaces/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_correlationevents_s(self, data, api_version="v2.1"):
        """
        POST Query_Correlationevents_S API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_correlationevents_waninterfaces(self, data, api_version="v2.1"):
        """
        POST Query_Correlationevents_Waninterfaces API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/waninterfaces/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_current_status_software(self, data, api_version="v2.1"):
        """
        POST Query_Current_Status_Software API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/software/current_status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_demstatus(self, data, api_version="v2.0"):
        """
        POST Query_Demstatus API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/demstatus/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_deviceidconfigs(self, data, api_version="v2.0"):
        """
        POST Query_Deviceidconfigs API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/deviceidconfigs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_directoryusergroups(self, data, api_version="v2.0"):
        """
        POST Query_Directoryusergroups API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryusergroups/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_directoryusers(self, data, api_version="v2.1"):
        """
        POST Query_Directoryusers API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryusers/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_dnsserviceprofiles(self, data, api_version="v2.1"):
        """
        POST Query_Dnsserviceprofiles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_dnsserviceroles(self, data, api_version="v2.0"):
        """
        POST Query_Dnsserviceroles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceroles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_dnsservices(self, data, api_version="v2.0"):
        """
        POST Query_Dnsservices API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsservices/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_e(self, data, api_version="v3.2"):
        """
        POST Query_E API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_elementsecurityzones(self, data, api_version="v2.0"):
        """
        POST Query_Elementsecurityzones API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementsecurityzones/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_eventcorrelationpolicyrules(self, data, api_version="v2.1"):
        """
        POST Query_Eventcorrelationpolicyrules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_eventcorrelationpolicysets(self, data, api_version="v2.0"):
        """
        POST Query_Eventcorrelationpolicysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_events(self, data, api_version="v3.7"):
        """
        POST Query_Events API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.7)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/events/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_extensions_i(self, site_id, element_id, data, api_version="v2.0"):
        """
        POST Query_Extensions_I API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/extensions/query".format(api_version,
                                                                                           site_id,
                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_extensions_s(self, site_id, data, api_version="v2.0"):
        """
        POST Query_Extensions_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/extensions/query".format(api_version,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_extensions_t(self, data, api_version="v2.0"):
        """
        POST Query_Extensions_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/extensions/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_globalprefixfilters(self, data, api_version="v2.0"):
        """
        POST Query_Globalprefixfilters API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_h(self, data, api_version="v4.0"):
        """
        POST Query_H API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/hubclusters/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_interfaces(self, data, api_version="v4.21"):
        """
        POST Query_Interfaces API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.21)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/interfaces/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipfix(self, data, api_version="v2.0"):
        """
        POST Query_Ipfix API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfix/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipfixcollectorcontexts(self, data, api_version="v2.0"):
        """
        POST Query_Ipfixcollectorcontexts API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixcollectorcontexts/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipfixfiltercontexts(self, data, api_version="v2.0"):
        """
        POST Query_Ipfixfiltercontexts API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixfiltercontexts/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipfixglobalprefixes(self, data, api_version="v2.0"):
        """
        POST Query_Ipfixglobalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixglobalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipfixlocalprefixes(self, data, api_version="v2.0"):
        """
        POST Query_Ipfixlocalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixlocalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipfixprofiles(self, data, api_version="v2.0"):
        """
        POST Query_Ipfixprofiles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipfixtemplates(self, data, api_version="v2.0"):
        """
        POST Query_Ipfixtemplates API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixtemplates/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ipsecprofiles(self, data, api_version="v2.2"):
        """
        POST Query_Ipsecprofiles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_lannetworks(self, site_id, data, api_version="v3.3"):
        """
        POST Query_Lannetworks API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/lannetworks/query".format(api_version,
                                                                                site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_lannetworks_t(self, data, api_version="v3.3"):
        """
        POST Query_Lannetworks_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/lannetworks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_localprefixfilters(self, data, api_version="v2.0"):
        """
        POST Query_Localprefixfilters API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/localprefixfilters/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_m(self, data, api_version="v2.5"):
        """
        POST Query_M API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_machine_upgrade(self, data, api_version="v2.0"):
        """
        POST Query_Machine_Upgrade API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machine_upgrade/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_machines_c(self, client_id, data, api_version="v2.5"):
        """
        POST Query_Machines_C API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/machines/query".format(api_version,
                                                                               client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_mstp_instances(self, data, api_version="v2.0"):
        """
        POST Query_Mstp_Instances API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/mstp_instances/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_multicastdynamicrps(self, data, api_version="v2.0"):
        """
        POST Query_Multicastdynamicrps API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastdynamicrps/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_multicastigmpmemberships(self, data, api_version="v2.0"):
        """
        POST Query_Multicastigmpmemberships API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastigmpmemberships/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_multicastroutes(self, data, api_version="v2.0"):
        """
        POST Query_Multicastroutes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastroutes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_multicastrps(self, data, api_version="v2.0"):
        """
        POST Query_Multicastrps API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastrps/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_multicastsourcesiderps(self, site_id, data, api_version="v2.0"):
        """
        POST Query_Multicastsourcesiderps API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiderps/query".format(api_version,
                                                                                           site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_multicaststatus(self, data, api_version="v2.0"):
        """
        POST Query_Multicaststatus API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicaststatus/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_multicastwanstatus(self, data, api_version="v2.0"):
        """
        POST Query_Multicastwanstatus API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastwanstatus/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_natglobalprefixes(self, data, api_version="v2.0"):
        """
        POST Query_Natglobalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natglobalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_natlocalprefixes(self, data, api_version="v2.0"):
        """
        POST Query_Natlocalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natlocalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_natpolicypools(self, data, api_version="v2.0"):
        """
        POST Query_Natpolicypools API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicypools/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_natpolicyrules(self, data, api_version="v2.0"):
        """
        POST Query_Natpolicyrules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_natpolicysets(self, data, api_version="v2.0"):
        """
        POST Query_Natpolicysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_natpolicysetstacks(self, data, api_version="v2.0"):
        """
        POST Query_Natpolicysetstacks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysetstacks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_natzones(self, data, api_version="v2.0"):
        """
        POST Query_Natzones API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natzones/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_networkcontexts(self, data, api_version="v2.0"):
        """
        POST Query_Networkcontexts API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkcontexts/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_networkpolicyglobalprefixes(self, data, api_version="v2.1"):
        """
        POST Query_Networkpolicyglobalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyglobalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_networkpolicylocalprefixes(self, data, api_version="v2.1"):
        """
        POST Query_Networkpolicylocalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicylocalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_networkpolicyrules(self, data, api_version="v2.4"):
        """
        POST Query_Networkpolicyrules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_networkpolicysets(self, data, api_version="v2.0"):
        """
        POST Query_Networkpolicysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_networkpolicysetstacks(self, data, api_version="v2.0"):
        """
        POST Query_Networkpolicysetstacks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysetstacks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ngfwsecuritypolicyglobalprefixes(self, data, api_version="v2.1"):
        """
        POST Query_Ngfwsecuritypolicyglobalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyglobalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ngfwsecuritypolicylocalprefixes(self, data, api_version="v2.1"):
        """
        POST Query_Ngfwsecuritypolicylocalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicylocalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ngfwsecuritypolicyrules(self, data, api_version="v2.3"):
        """
        POST Query_Ngfwsecuritypolicyrules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ngfwsecuritypolicysets(self, data, api_version="v2.0"):
        """
        POST Query_Ngfwsecuritypolicysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_ngfwsecuritypolicysetstacks(self, data, api_version="v2.0"):
        """
        POST Query_Ngfwsecuritypolicysetstacks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysetstacks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_pathgroups(self, data, api_version="v2.1"):
        """
        POST Query_Pathgroups API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/pathgroups/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_policyrules(self, data, api_version="v3.1"):
        """
        POST Query_Policyrules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_policysets(self, data, api_version="v3.0"):
        """
        POST Query_Policysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prefixes(self, data, api_version="v3.1"):
        """
        POST Query_Prefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prefixfilters(self, site_id, data, api_version="v2.0"):
        """
        POST Query_Prefixfilters API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters/query".format(api_version,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prefixfilters_t(self, data, api_version="v2.0"):
        """
        POST Query_Prefixfilters_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prefixfilters/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prioritypolicyglobalprefixes(self, data, api_version="v2.1"):
        """
        POST Query_Prioritypolicyglobalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyglobalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prioritypolicylocalprefixes(self, data, api_version="v2.1"):
        """
        POST Query_Prioritypolicylocalprefixes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicylocalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prioritypolicyrules(self, data, api_version="v2.2"):
        """
        POST Query_Prioritypolicyrules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prioritypolicysets(self, data, api_version="v2.0"):
        """
        POST Query_Prioritypolicysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prioritypolicysetstacks(self, data, api_version="v2.0"):
        """
        POST Query_Prioritypolicysetstacks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysetstacks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_prismaaccess_configs(self, data, api_version="v2.0"):
        """
        POST Query_Prismaaccess_Configs API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismaaccess_configs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_reports(self, data, api_version="v2.0"):
        """
        POST Query_Reports API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/reports/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_reportsdir(self, data, api_version="v2.0"):
        """
        POST Query_Reportsdir API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/reportsdir/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_routing_aspathaccesslists(self, site_id, element_id, data, api_version="v2.1"):
        """
        POST Query_Routing_Aspathaccesslists API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_aspathaccesslists/query".format(api_version,
                                                                                                          site_id,
                                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_routing_ipcommunitylists(self, site_id, element_id, data, api_version="v2.0"):
        """
        POST Query_Routing_Ipcommunitylists API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_ipcommunitylists/query".format(api_version,
                                                                                                         site_id,
                                                                                                         element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_routing_prefixlists(self, site_id, element_id, data, api_version="v2.1"):
        """
        POST Query_Routing_Prefixlists API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_prefixlists/query".format(api_version,
                                                                                                    site_id,
                                                                                                    element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_routing_routemaps(self, site_id, element_id, data, api_version="v2.3"):
        """
        POST Query_Routing_Routemaps API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_routemaps/query".format(api_version,
                                                                                                  site_id,
                                                                                                  element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_s(self, data, api_version="v4.13"):
        """
        POST Query_S API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.13)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_securitypolicyrules(self, data, api_version="v2.0"):
        """
        POST Query_Securitypolicyrules API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicyrules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_securitypolicysets(self, data, api_version="v2.0"):
        """
        POST Query_Securitypolicysets API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_securityzones(self, data, api_version="v2.1"):
        """
        POST Query_Securityzones API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securityzones/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_servicebindingmaps(self, data, api_version="v2.1"):
        """
        POST Query_Servicebindingmaps API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicebindingmaps/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_serviceendpoints(self, data, api_version="v3.1"):
        """
        POST Query_Serviceendpoints API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/serviceendpoints/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_servicelabels(self, data, api_version="v2.1"):
        """
        POST Query_Servicelabels API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicelabels/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_sitesecurityzones(self, site_id, data, api_version="v2.0"):
        """
        POST Query_Sitesecurityzones API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/sitesecurityzones/query".format(api_version,
                                                                                      site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_sitesecurityzones_t(self, data, api_version="v2.0"):
        """
        POST Query_Sitesecurityzones_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sitesecurityzones/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_snmpdiscoverystartnodes(self, data, api_version="v2.0"):
        """
        POST Query_Snmpdiscoverystartnodes API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/snmpdiscoverystartnodes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_softwarehistory(self, data, api_version="v2.0"):
        """
        POST Query_Softwarehistory API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/softwarehistory/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_spokeclusters(self, site_id, data, api_version="v2.0"):
        """
        POST Query_Spokeclusters API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/query".format(api_version,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_spokeclusters_t(self, data, api_version="v2.0"):
        """
        POST Query_Spokeclusters_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/spokeclusters/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_state_software(self, data, api_version="v2.0"):
        """
        POST Query_State_Software API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/software/state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_status(self, data, api_version="v2.6"):
        """
        Query and get element status objects for a tenant (v2.6)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_status_cellular_module_firmware(self, data, api_version="v2.0"):
        """
        POST Query_Status_Cellular_Module_Firmware API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cellular_module_firmware/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_status_prismasase_connections(self, data, api_version="v2.0"):
        """
        POST Query_Status_Prismasase_Connections API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismasase_connections/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_status_software(self, data, api_version="v2.1"):
        """
        POST Query_Status_Software API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/software/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_tokens_vfflicenses(self, data, api_version="v2.0"):
        """
        POST Query_Tokens_Vfflicenses API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/tokens/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_toolkitsessions(self, data, api_version="v2.0"):
        """
        POST Query_Toolkitsessions API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/toolkitsessions/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_upgrade_status(self, data, api_version="v2.0"):
        """
        POST Query_Upgrade_Status API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/upgrade_status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_useridagents(self, data, api_version="v2.0"):
        """
        POST Query_Useridagents API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/useridagents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_vpnlinks(self, data, api_version="v2.0"):
        """
        POST Query_Vpnlinks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vpnlinks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_vrfcontextprofiles(self, data, api_version="v2.0"):
        """
        POST Query_Vrfcontextprofiles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontextprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_vrfcontexts(self, data, api_version="v2.0"):
        """
        POST Query_Vrfcontexts API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontexts/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_waninterfacelabels(self, data, api_version="v2.6"):
        """
        POST Query_Waninterfacelabels API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/waninterfacelabels/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_waninterfaces(self, site_id, data, api_version="v2.5"):
        """
        POST Query_Waninterfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces/query".format(api_version,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_waninterfaces_t(self, data, api_version="v2.10"):
        """
        POST Query_Waninterfaces_T API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.10)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/waninterfaces/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_wannetworks(self, data, api_version="v2.1"):
        """
        POST Query_Wannetworks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wannetworks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def radii(self, element_id, data, api_version="v2.0"):
        """
        Used to create element radius (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **override_indicator:**  [Type: string] 
           - **radius_configuration:**           
               - **accounting_port:**  Type: integer 
               - **authentication_port:**  Type: integer 
               - **ip_version:**  Type: integer 
               - **priority:**  Type: integer 
               - **retain_shared_secret:**  Type: boolean 
               - **server_ip_address:**  Type: string 
               - **shared_secret:**  Type: string 
               - **shared_secret_encrypted:**  Type: string 
           - **radius_profile_id:**  Type: string 
           - **source_interface_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/radii".format(api_version,
                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def reallocate_clients(self, client_id, machine_id, data, api_version="v2.5"):
        """
        POST Reallocate_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/machines/{}/reallocate".format(api_version,
                                                                                       client_id,
                                                                                       machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def recovery_tokens(self, machine_id, data, api_version="v2.1"):
        """
        Create a Recovery Token for Fips change mode (v2.1)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **hardware_id:**  Type: string 
           - **ion_token:**  Type: string 
           - **is_used:**  Type: boolean 
           - **secret_token:**  Type: string 
           - **token_validity_in_hour:**  Type: integer 
           - **valid_till_secs:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/recovery_tokens".format(api_version,
                                                                                 machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def roles(self, data, api_version="v2.1"):
        """
        Add a custom role (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **custom_permissions:**           
               - **allowed_after_ms:**  Type: integer 
               - **allowed_before_ms:**  Type: integer 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **disallow_permission:**  Type: boolean 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **region:**  Type: string 
               - **tenant_id:**  Type: string 
               - **value:**  Type: string 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **disallow_permissions:**           
               - **value:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **is_system_owned:**  Type: boolean 
           - **name:**  Type: string 
           - **permissions:**           
               - **value:**  Type: string 
           - **region:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/roles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_aspathaccesslists(self, site_id, element_id, data, api_version="v2.1"):
        """
        Create AS-Path Access List (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **as_path_regex_list:**           
               - **as_path_regex:**  Type: string 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_aspathaccesslists".format(api_version,
                                                                                                    site_id,
                                                                                                    element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_ipcommunitylists(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create IP Community List (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **community_list:**           
               - **community_str:**  Type: string 
               - **permit:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_ipcommunitylists".format(api_version,
                                                                                                   site_id,
                                                                                                   element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_prefixlists(self, site_id, element_id, data, api_version="v2.1"):
        """
        Create IP Prefix List (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **prefix_filter_list:**           
               - **ge:**  Type: integer 
               - **ipv6_prefix:**  Type: string 
               - **le:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **prefix:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_prefixlists".format(api_version,
                                                                                              site_id,
                                                                                              element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_routemaps(self, site_id, element_id, data, api_version="v2.3"):
        """
        Create Route Map (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **route_map_entries:**           
               - **continue_entry:**  Type: string 
               - **match:**           
                   - **as_path_id:**  Type: string 
                   - **community_list_id:**  Type: string 
                   - **ip_next_hop_id:**  Type: string 
                   - **ip_prefix_list_id:**  Type: string 
                   - **metric:**  Type: integer 
                   - **tag:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **set:**           
                   - **additive_community:**  Type: boolean 
                   - **as_path_prepend:**  Type: string 
                   - **community:**  Type: string 
                   - **ip_next_hop:**  Type: string 
                   - **ip_v6_next_hop:**  Type: string 
                   - **local_preference:**  Type: integer 
                   - **metric:**  Type: integer 
                   - **tag:**  Type: integer 
                   - **type:**  Type: string 
                   - **weight:**  Type: integer 
           - **tags:**  [Type: string] 
           - **used_for:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_routemaps".format(api_version,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def rquery(self, data, api_version="v3.2"):
        """
        Query and get ESP machines across regions (v3.2)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.2)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **isReadPreferenceSecondary:**  Type: boolean 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_case_insensitive:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/rquery".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def rquery_vfflicenses(self, data, api_version="v2.0"):
        """
        POST Rquery_Vfflicenses API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/rquery".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def rquery_vfflicensesstatus(self, data, api_version="v2.0"):
        """
        POST Rquery_Vfflicensesstatus API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicensesstatus/rquery".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sdwanapps_configs(self, sdwanapp_id, data, api_version="v2.0"):
        """
        POST Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/configs".format(api_version,
                                                                          sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicyruleorder(self, securitypolicyset_id, data, api_version="v2.0"):
        """
        Update a tenant security policy set. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}/firewallpolicyruleorder".format(api_version,
                                                                                                   securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicyrules(self, securitypolicyset_id, data, api_version="v2.0"):
        """
        Create a new tenant security policy rule. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **application_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_filter_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **disabled_flag:**  Type: boolean 
           - **name:**  Type: string 
           - **source_filter_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}/securitypolicyrules".format(api_version,
                                                                                               securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicysets(self, data, api_version="v2.0"):
        """
        Create a new tenant security policy set. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securityprofilegroups(self, data, api_version="v2.0"):
        """
        Create a Security Profile Group (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **dns_security_profile:**           
               - **cm_version:**  Type: string 
               - **etag:**  Type: integer 
               - **name:**  Type: string 
               - **profile_id:**  Type: string 
           - **name:**  Type: string 
           - **predefined:**  Type: boolean 
           - **spyware_profile:**           
               - **cm_version:**  Type: string 
               - **etag:**  Type: integer 
               - **name:**  Type: string 
               - **profile_id:**  Type: string 
           - **url_filtering_profile:**           
               - **cm_version:**  Type: string 
               - **etag:**  Type: integer 
               - **name:**  Type: string 
               - **profile_id:**  Type: string 
           - **vulnerability_profile:**           
               - **cm_version:**  Type: string 
               - **etag:**  Type: integer 
               - **name:**  Type: string 
               - **profile_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securityprofilegroups".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securityprofilegroups_query(self, data, api_version="v2.0"):
        """
        Query Security profile groups of a tenant (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securityprofilegroups/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securityzones(self, data, api_version="v2.1"):
        """
        Create a new security zone (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tcp_allow_non_syn:**  Type: boolean 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securityzones".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def servicebindingmaps(self, data, api_version="v2.1"):
        """
        Create a new Service Binding Map (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **is_default:**  Type: boolean 
           - **name:**  Type: string 
           - **service_bindings:**           
               - **service_endpoint_ids:**  [Type: string] 
               - **service_label_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicebindingmaps".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def serviceendpoints(self, data, api_version="v3.1"):
        """
        Create a new Service Endpoint (v3.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_up:**  Type: boolean 
           - **allow_enterprise_traffic:**  Type: boolean 
           - **description:**  Type: string 
           - **disable_tunnel_reoptimization:**  Type: boolean 
           - **is_sase:**  Type: boolean 
           - **liveliness_probe:**           
               - **http:**           
                   - **failure_count:**  Type: integer 
                   - **http_status_codes:**  [Type: integer] 
                   - **interval:**  Type: integer 
                   - **url:**  Type: string 
               - **icmp_ping:**           
                   - **failure_count:**  Type: integer 
                   - **interval:**  Type: integer 
                   - **ip_addresses:**  [Type: string] 
               - **use_tunnel_for_url_dns_resolution:**  Type: boolean 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **name:**  Type: string 
           - **sase_properties:**           
               - **lqm_enabled:**  Type: boolean 
           - **service_link_peers:**           
               - **hostnames:**  [Type: string] 
               - **ip_addresses:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/serviceendpoints".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def servicelabels(self, data, api_version="v2.1"):
        """
        Create a new Service Label (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **sase_properties:**           
               - **active_sase_label:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicelabels".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def signup(self, data, api_version="v2.0"):
        """
        Signup new operators (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **addresses:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **custom_roles:**           
               - **custom_permissions:**           
                   - **allowed_after_ms:**  Type: integer 
                   - **allowed_before_ms:**  Type: integer 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **disallow_permission:**  Type: boolean 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **value:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **name:**  Type: string 
               - **permissions:**           
                   - **value:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
           - **email:**  Type: string 
           - **enable_session_ip_lock:**  Type: boolean 
           - **first_name:**  Type: string 
           - **ipv4_list:**           
               - **ipv4:**  Type: string 
           - **last_name:**  Type: string 
           - **logout_others:**  Type: boolean 
           - **name:**  Type: string 
           - **password:**  Type: string 
           - **phone_numbers:**           
               - **country_code:**  Type: integer 
               - **local_extension:**  Type: integer 
               - **number:**  Type: integer 
               - **types:**           
                   - **value:**  Type: string 
           - **repeatPassword:**  Type: string 
           - **requestId:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **secondary_emails:**           
               - **email:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/signup".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_extensions(self, site_id, data, api_version="v2.0"):
        """
        Create site level extension configuration (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **conf:**  Type: object 
           - **disabled:**  Type: boolean 
           - **name:**  Type: string 
           - **namespace:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/extensions".format(api_version,
                                                                         site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_ipfixlocalprefixes(self, site_id, data, api_version="v2.0"):
        """
        Create a IPFix site prefix association (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ipfixlocalprefixes".format(api_version,
                                                                                 site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_natlocalprefixes(self, site_id, data, api_version="v2.0"):
        """
        Create an association between site and NAT Prefix. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/natlocalprefixes".format(api_version,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_networkpolicylocalprefixes(self, site_id, data, api_version="v2.1"):
        """
        Create an association between site and Network local Prefix. (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/networkpolicylocalprefixes".format(api_version,
                                                                                         site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_ngfwsecuritypolicylocalprefixes(self, site_id, data, api_version="v2.1"):
        """
        Create a security policy V2 local prefix site association (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ngfwsecuritypolicylocalprefixes".format(api_version,
                                                                                              site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_prioritypolicylocalprefixes(self, site_id, data, api_version="v2.1"):
        """
        Create an association between site and Priority local Prefix. (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prioritypolicylocalprefixes".format(api_version,
                                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sites(self, data, api_version="v4.13"):
        """
        Create a site (v4.13)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.13)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_state:**  Type: string 
           - **app_acceleration_enabled:**  Type: boolean 
           - **branch_gateway:**  Type: boolean 
           - **description:**  Type: string 
           - **element_cluster_role:**  Type: string 
           - **element_system_limit_profile_id:**  Type: string 
           - **extended_tags:**           
               - **key:**  Type: string 
               - **value:**  Type: string 
               - **value_type:**  Type: string 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **multicast_peer_group_id:**  Type: string 
           - **name:**  Type: string 
           - **nat_policysetstack_id:**  Type: string 
           - **network_policysetstack_id:**  Type: string 
           - **perfmgmt_policysetstack_id:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **prefer_lan_default_over_wan_default_route:**  Type: boolean 
           - **priority_policysetstack_id:**  Type: string 
           - **security_policyset_id:**  Type: string 
           - **security_policysetstack_id:**  Type: string 
           - **service_binding:**  Type: string 
           - **sgi_config:**           
               - **sgi_tag:**  Type: integer 
               - **sgi_vendor_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **vrf_context_profile_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sitesecurityzones(self, site_id, data, api_version="v2.0"):
        """
        Create an association between site and security zone. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **networks:**           
               - **network_id:**  Type: string 
               - **network_type:**  Type: string 
           - **zone_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/sitesecurityzones".format(api_version,
                                                                                site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sitesnapshots(self, data, api_version="v2.0"):
        """
        Create or retry a site deployment (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **status:**  Type: string 
           - **status_description:**  Type: string 
           - **yaml_configuration:**  Type: string 
           - **yaml_name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sitesnapshots".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sitesnapshots_query(self, data, api_version="v2.0"):
        """
        Query import jobs with filters (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sitesnapshots/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sitetemplates_bulkconfigurations_query(self, data, api_version="v2.0"):
        """
        POST Sitetemplates_Bulkconfigurations_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def snapshots(self, site_id, data, api_version="v2.0"):
        """
        Generate a snapshot of a particular site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **site_id:**  Type: string 
           - **snapshot_name:**  Type: string 
           - **status:**  Type: string 
           - **status_description:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/snapshots".format(api_version,
                                                                        site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def snapshots_query(self, data, api_version="v2.0"):
        """
        Query export jobs (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/snapshots/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def snmpagents(self, site_id, element_id, data, api_version="v2.1"):
        """
        Create SNMP Agent (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **system_contact:**  Type: string 
           - **system_location:**  Type: string 
           - **tags:**  [Type: string] 
           - **v2_config:**           
               - **community:**  Type: string 
               - **enabled:**  Type: boolean 
           - **v3_config:**           
               - **enabled:**  Type: boolean 
               - **users_access:**           
                   - **auth_phrase:**  Type: string 
                   - **auth_type:**  Type: string 
                   - **enc_phrase:**  Type: string 
                   - **enc_type:**  Type: string 
                   - **engine_id:**  Type: string 
                   - **security_level:**  Type: string 
                   - **user_name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmpagents".format(api_version,
                                                                                     site_id,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def snmptraps(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create SNMP Trap (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **server_ip:**  Type: string 
           - **source_interface:**  Type: string 
           - **tags:**  [Type: string] 
           - **v2_config:**           
               - **community:**  Type: string 
           - **v3_config:**           
               - **user_access:**           
                   - **auth_phrase:**  Type: string 
                   - **auth_type:**  Type: string 
                   - **enc_phrase:**  Type: string 
                   - **enc_type:**  Type: string 
                   - **engine_id:**  Type: string 
                   - **security_level:**  Type: string 
                   - **user_name:**  Type: string 
           - **version:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmptraps".format(api_version,
                                                                                    site_id,
                                                                                    element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def spnnpnsitemigration_remotenetworks_query(self, data, api_version="v2.0"):
        """
        Get all easy onboarding created remote networks for a tenant (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/spnnpnsitemigration/remotenetworks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def spokeclusters(self, site_id, data, api_version="v2.0"):
        """
        Create Spoke Cluster (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **advertisement_interval:**  Type: number 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **preempt:**  Type: boolean 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters".format(api_version,
                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def staticroutes(self, site_id, element_id, data, api_version="v2.3"):
        """
        Create static route (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **address_family:**  Type: string 
           - **description:**  Type: string 
           - **destination_prefix:**  Type: string 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **nexthop_reachability_probe:**  Type: boolean 
           - **nexthops:**           
               - **admin_distance:**  Type: integer 
               - **nexthop_interface_id:**  Type: string 
               - **nexthop_ip:**  Type: string 
               - **self:**  Type: boolean 
           - **scope:**  Type: string 
           - **tags:**  [Type: string] 
           - **vrf_context_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/staticroutes".format(api_version,
                                                                                       site_id,
                                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def status_bgppeers_query(self, data, api_version="v2.1"):
        """
        POST Status_Bgppeers_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bgppeers/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def status_cellular_modules_query(self, data, api_version="v2.1"):
        """
        POST Status_Cellular_Modules_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cellular_modules/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def status_interfaces_query(self, data, api_version="v2.0"):
        """
        POST Status_Interfaces_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/interfaces/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def status_spokeclusters_query(self, data, api_version="v2.0"):
        """
        POST Status_Spokeclusters_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/spokeclusters/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def summary_events(self, data, api_version="v2.1"):
        """
        POST Summary_Events API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/events/summary".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def support_operations(self, element_id, data, api_version="v2.0"):
        """
        POST Support_Operations API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/support_operations".format(api_version,
                                                                                    element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sync_directoryservices(self, data, api_version="v2.0"):
        """
        POST Sync_Directoryservices API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices/sync".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sys_metrics_monitor(self, data, api_version="v2.3"):
        """
        POST Sys_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/sys_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sys_point_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Sys_Point_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/sys_point_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def syslogserverprofiles(self, data, api_version="v2.1"):
        """
        Create Syslog Server Profile (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_dns_logging:**  Type: boolean 
           - **enable_flow_logging:**  Type: boolean 
           - **enable_threat_logging:**  Type: boolean 
           - **enable_url_logging:**  Type: boolean 
           - **name:**  Type: string 
           - **protocol:**  Type: string 
           - **remote_ca_certificate:**  Type: string 
           - **server_fqdn:**  Type: string 
           - **server_ip:**  Type: string 
           - **server_port:**  Type: integer 
           - **severity_level:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/syslogserverprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def syslogservers(self, site_id, element_id, data, api_version="v2.3"):
        """
        Create Syslog Server (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_dns_logging:**  Type: boolean 
           - **enable_flow_logging:**  Type: boolean 
           - **enable_threat_logging:**  Type: boolean 
           - **enable_url_logging:**  Type: boolean 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **protocol:**  Type: string 
           - **remote_ca_certificate:**  Type: string 
           - **server_fqdn:**  Type: string 
           - **server_ip:**  Type: string 
           - **server_port:**  Type: integer 
           - **severity_level:**  Type: string 
           - **source_interface:**  Type: string 
           - **syslog_profile_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/syslogservers".format(api_version,
                                                                                        site_id,
                                                                                        element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tacacs_plus_profiles(self, data, api_version="v2.0"):
        """
        Create TACACS+ Profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **authentication_protocol:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tacacs_plus_servers:**           
               - **secret:**  Type: string 
               - **server_fqdn:**  Type: string 
               - **server_ip:**  Type: string 
               - **server_ipv6:**  Type: string 
               - **server_port:**  Type: integer 
               - **timeout:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/tacacs_plus_profiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tacacs_plus_servers(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create TACACS+ Servers (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **authentication_protocol:**  Type: string 
           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **source_interface_id:**  Type: string 
           - **tacacs_plus_profile_id:**  Type: string 
           - **tacacs_plus_servers:**           
               - **secret:**  Type: string 
               - **server_fqdn:**  Type: string 
               - **server_ip:**  Type: string 
               - **server_ipv6:**  Type: string 
               - **server_port:**  Type: integer 
               - **timeout:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/tacacs_plus_servers".format(api_version,
                                                                                              site_id,
                                                                                              element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def templates_ntp(self, data, api_version="v2.0"):
        """
        Create a new NTP Template (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_template:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **ntp_servers:**           
               - **algorithm:**  Type: string 
               - **authentication_key:**  Type: string 
               - **authentication_key_id:**  Type: integer 
               - **host:**  Type: string 
               - **max_poll:**  Type: integer 
               - **min_poll:**  Type: integer 
               - **version:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/templates/ntp".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_anynetlinks(self, data, api_version="v4.0"):
        """
        POST Tenant_Anynetlinks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_ipfixlocalprefixes(self, data, api_version="v2.0"):
        """
        Create a IPFix local prefix (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixlocalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_networkpolicylocalprefixes(self, data, api_version="v2.0"):
        """
        Create a new Network Policy local prefix. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicylocalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_permissions(self, data, api_version="v2.0"):
        """
        Add a custom permission (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **allowed_after_ms:**  Type: integer 
           - **allowed_before_ms:**  Type: integer 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **disallow_permission:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **region:**  Type: string 
           - **tenant_id:**  Type: string 
           - **value:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/permissions".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_prioritypolicylocalprefixes(self, data, api_version="v2.0"):
        """
        Create a new Priority Policy local prefix. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicylocalprefixes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def threatmetadata_query(self, data, api_version="v2.0"):
        """
        Query Threat Metadata. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/threatmetadata/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def to_shell_allocate(self, machine_id, data, api_version="v2.0"):
        """
        POST To_Shell_Allocate API Function

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/allocate_to_shell".format(api_version,
                                                                                   machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topn_aaa_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Topn_Aaa_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aaa_metrics/topn".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topn_aiops_monitor(self, data, api_version="v2.0"):
        """
        POST Topn_Aiops_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/topn".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topn_cellular_metrics_monitor(self, data, api_version="v2.0"):
        """
        POST Topn_Cellular_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/cellular_metrics/topn".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topn_monitor(self, data, api_version="v3.1"):
        """
        POST Topn_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/topn".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topn_sys_metrics_monitor(self, data, api_version="v2.1"):
        """
        POST Topn_Sys_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/sys_metrics/topn".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topology(self, data, api_version="v3.6"):
        """
        POST Topology API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/topology".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def urlcategories_query(self, data, api_version="v2.0"):
        """
        Query URL Categories. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/urlcategories/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def useridagents(self, data, api_version="v2.0"):
        """
        Create User ID Agent (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **authentication:**           
               - **collector_name:**  Type: string 
               - **collector_secret:**  Type: string 
               - **collector_secret_encrypted:**  Type: string 
               - **local_certificate:**  Type: string 
               - **local_private_key:**  Type: string 
               - **passphrase:**  Type: string 
               - **remote_ca_certificate:**  Type: string 
           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **port:**  Type: integer 
           - **server_fqdn:**  Type: string 
           - **server_ip:**  Type: string 
           - **site_id:**  Type: string 
           - **source_interface:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/useridagents".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def users(self, data, api_version="v2.0"):
        """
        Create an user identity. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **first_name:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **last_name:**  Type: string 
           - **middle_name:**  Type: string 
           - **region:**  Type: string 
           - **tenant_id:**  Type: string 
           - **user_dn:**  Type: string 
           - **user_fqn:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/users".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def users_application_monitor(self, data, api_version="v2.0"):
        """
        POST Users_Application_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/application/users".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vfflicense_tokens(self, vfflicense_id, data, api_version="v2.0"):
        """
        Create Tenant Vff License Token (v2.0)

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ion_key:**  Type: string 
           - **is_expired:**  Type: boolean 
           - **is_multiuse:**  Type: boolean 
           - **is_revoked:**  Type: boolean 
           - **is_used:**  Type: boolean 
           - **secret_key:**  Type: string 
           - **valid_till_secs:**  Type: integer 
           - **vfflicense_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}/tokens".format(api_version,
                                                                           vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vrfcontextprofiles(self, data, api_version="v2.0"):
        """
        Create a new VRF context profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_vrf_context_profile:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **vrf_context_ids:**  [Type: string] 
           - **vrf_context_route_leak_rules:**           
               - **description:**  Type: string 
               - **dest_vrf_context_id:**  Type: string 
               - **ipv4_prefixes:**  [Type: string] 
               - **name:**  Type: string 
               - **src_vrf_context_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontextprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vrfcontexts(self, data, api_version="v2.0"):
        """
        Create a new VRF context (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_vrf_context:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontexts".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def wan_neighbor_multicast_aggregates_monitor(self, data, api_version="v2.0"):
        """
        POST Wan_Neighbor_Multicast_Aggregates_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aggregates/multicast/wan_neighbor".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def waninterfaces(self, site_id, data, api_version="v2.10"):
        """
        Create a new Site WAN interface (v2.10)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.10)

          **Payload Attributes:** 

           - **app_acceleration_enabled:**  Type: boolean 
           - **bfd_mode:**  Type: string 
           - **bw_config_mode:**  Type: string 
           - **bwc_enabled:**  Type: boolean 
           - **cost:**  Type: integer 
           - **description:**  Type: string 
           - **l3_reachability:**           
               - **probe_config_ids:**  [Type: string] 
               - **use_element_default:**  Type: boolean 
           - **label_id:**  Type: string 
           - **link_bw_down:**  Type: number 
           - **link_bw_up:**  Type: number 
           - **lqm_config:**           
               - **hub_site_ids:**  [Type: string] 
               - **inter_packet_gap:**  Type: integer 
               - **statistic:**  Type: string 
           - **lqm_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_id:**  Type: string 
           - **probe_profile_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 
           - **use_for_application_reachability_probes:**  Type: boolean 
           - **use_for_controller_connections:**  Type: boolean 
           - **use_lqm_for_non_hub_paths:**  Type: boolean 
           - **vpnlink_configuration:**           
               - **keep_alive_failure_count:**  Type: integer 
               - **keep_alive_interval:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces".format(api_version,
                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def wannetworks(self, data, api_version="v2.1"):
        """
        Create a new WAN (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **provider_as_numbers:**  [Type: integer] 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wannetworks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def wanoverlays(self, data, api_version="v2.0"):
        """
        Create a new app/wan context (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **vni:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wanoverlays".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ws_extensions(self, data, api_version="v2.0"):
        """
        POST Ws_Extensions API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ws/extensions".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    access_elementusers = elementusers_access
    """ Backwards-compatibility alias of `access_elementusers` to `elementusers_access`"""

    agg_bw_stats_monitor = monitor_agg_bw_stats
    """ Backwards-compatibility alias of `agg_bw_stats_monitor` to `monitor_agg_bw_stats`"""

    allocate_to_shell = to_shell_allocate
    """ Backwards-compatibility alias of `allocate_to_shell` to `to_shell_allocate`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    app_acceleration_monitor = monitor_app_acceleration
    """ Backwards-compatibility alias of `app_acceleration_monitor` to `monitor_app_acceleration`"""

    bulkoperations_anynetlinks = anynetlinks_bulkoperations
    """ Backwards-compatibility alias of `bulkoperations_anynetlinks` to `anynetlinks_bulkoperations`"""

    clone_sitetemplates_bulkconfigurations = bulkconfigurations_clone_sitetemplates
    """ Backwards-compatibility alias of `clone_sitetemplates_bulkconfigurations` to `bulkconfigurations_clone_sitetemplates`"""

    configs_prismasase_connections = prismasase_connections_configs
    """ Backwards-compatibility alias of `configs_prismasase_connections` to `prismasase_connections_configs`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    deployments_sitetemplates_bulkconfigurations = bulkconfigurations_deployments_sitetemplates
    """ Backwards-compatibility alias of `deployments_sitetemplates_bulkconfigurations` to `bulkconfigurations_deployments_sitetemplates`"""

    deviceidconfigs_i = deviceidconfigs
    """ Backwards-compatibility alias of `deviceidconfigs_i` to `deviceidconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    ipfixlocalprefixes_s = site_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_s` to `site_ipfixlocalprefixes`"""

    ipfixlocalprefixes_t = tenant_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_t` to `tenant_ipfixlocalprefixes`"""

    natlocalprefixes_s = site_natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_s` to `site_natlocalprefixes`"""

    natlocalprefixes_t = natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_t` to `natlocalprefixes`"""

    networkpolicylocalprefixes_s = site_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_s` to `site_networkpolicylocalprefixes`"""

    networkpolicylocalprefixes_t = tenant_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_t` to `tenant_networkpolicylocalprefixes`"""

    ngfwsecuritypolicylocalprefixes_s = site_ngfwsecuritypolicylocalprefixes
    """ Backwards-compatibility alias of `ngfwsecuritypolicylocalprefixes_s` to `site_ngfwsecuritypolicylocalprefixes`"""

    ngfwsecuritypolicylocalprefixes_t = ngfwsecuritypolicylocalprefixes
    """ Backwards-compatibility alias of `ngfwsecuritypolicylocalprefixes_t` to `ngfwsecuritypolicylocalprefixes`"""

    ntp_templates = templates_ntp
    """ Backwards-compatibility alias of `ntp_templates` to `templates_ntp`"""

    ops_events = events_operations
    """ Backwards-compatibility alias of `ops_events` to `events_operations`"""

    ops_interfaces = interfaces_operations
    """ Backwards-compatibility alias of `ops_interfaces` to `interfaces_operations`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    probe_point_metrics_monitor = monitor_probe_point_metrics
    """ Backwards-compatibility alias of `probe_point_metrics_monitor` to `monitor_probe_point_metrics`"""

    probes_metrics_monitor = monitor_metrics_probes
    """ Backwards-compatibility alias of `probes_metrics_monitor` to `monitor_metrics_probes`"""

    query_aggregatebandwidth_monitor = monitor_aggregatebandwidth_query
    """ Backwards-compatibility alias of `query_aggregatebandwidth_monitor` to `monitor_aggregatebandwidth_query`"""

    query_anynetlinks = anynetlinks_query
    """ Backwards-compatibility alias of `query_anynetlinks` to `anynetlinks_query`"""

    query_appacceleration = appacceleration_query
    """ Backwards-compatibility alias of `query_appacceleration` to `appacceleration_query`"""

    query_applicationstats_monitor = monitor_applicationstats_query
    """ Backwards-compatibility alias of `query_applicationstats_monitor` to `monitor_applicationstats_query`"""

    query_applicationsummary_monitor = monitor_applicationsummary_query
    """ Backwards-compatibility alias of `query_applicationsummary_monitor` to `monitor_applicationsummary_query`"""

    query_demsiteconfigs = demsiteconfigs_query
    """ Backwards-compatibility alias of `query_demsiteconfigs` to `demsiteconfigs_query`"""

    query_deployments_sitetemplates_bulkconfigurations = deployments_sitetemplates_bulkconfigurations_query
    """ Backwards-compatibility alias of `query_deployments_sitetemplates_bulkconfigurations` to `deployments_sitetemplates_bulkconfigurations_query`"""

    query_elementaccessconfigs = elementaccessconfigs_query
    """ Backwards-compatibility alias of `query_elementaccessconfigs` to `elementaccessconfigs_query`"""

    query_elementshells = elementshells_query
    """ Backwards-compatibility alias of `query_elementshells` to `elementshells_query`"""

    query_elementsystemlimitprofiles = elementsystemlimitprofiles_query
    """ Backwards-compatibility alias of `query_elementsystemlimitprofiles` to `elementsystemlimitprofiles_query`"""

    query_extensions_ws = extensions_ws_query
    """ Backwards-compatibility alias of `query_extensions_ws` to `extensions_ws_query`"""

    query_iotdevicemappings = iotdevicemappings_query
    """ Backwards-compatibility alias of `query_iotdevicemappings` to `iotdevicemappings_query`"""

    query_iotdictionary = iotdictionary_query
    """ Backwards-compatibility alias of `query_iotdictionary` to `iotdictionary_query`"""

    query_ospfconfigs = ospfconfigs_query
    """ Backwards-compatibility alias of `query_ospfconfigs` to `ospfconfigs_query`"""

    query_ospfdiscoveredneighbors = ospfdiscoveredneighbors_query
    """ Backwards-compatibility alias of `query_ospfdiscoveredneighbors` to `ospfdiscoveredneighbors_query`"""

    query_ospfreachableprefixes = ospfreachableprefixes_query
    """ Backwards-compatibility alias of `query_ospfreachableprefixes` to `ospfreachableprefixes_query`"""

    query_pathprefixdistributionfilterassociation = pathprefixdistributionfilterassociation_query
    """ Backwards-compatibility alias of `query_pathprefixdistributionfilterassociation` to `pathprefixdistributionfilterassociation_query`"""

    query_pathprefixdistributionfilters = pathprefixdistributionfilters_query
    """ Backwards-compatibility alias of `query_pathprefixdistributionfilters` to `pathprefixdistributionfilters_query`"""

    query_perfmgmtpolicyrules = perfmgmtpolicyrules_query
    """ Backwards-compatibility alias of `query_perfmgmtpolicyrules` to `perfmgmtpolicyrules_query`"""

    query_perfmgmtpolicysets = perfmgmtpolicysets_query
    """ Backwards-compatibility alias of `query_perfmgmtpolicysets` to `perfmgmtpolicysets_query`"""

    query_perfmgmtpolicysetstacks = perfmgmtpolicysetstacks_query
    """ Backwards-compatibility alias of `query_perfmgmtpolicysetstacks` to `perfmgmtpolicysetstacks_query`"""

    query_perfmgmtthresholdprofiles = perfmgmtthresholdprofiles_query
    """ Backwards-compatibility alias of `query_perfmgmtthresholdprofiles` to `perfmgmtthresholdprofiles_query`"""

    query_prismasase_connections = prismasase_connections_query
    """ Backwards-compatibility alias of `query_prismasase_connections` to `prismasase_connections_query`"""

    query_probeconfigs = probeconfigs_query
    """ Backwards-compatibility alias of `query_probeconfigs` to `probeconfigs_query`"""

    query_probeprofiles = probeprofiles_query
    """ Backwards-compatibility alias of `query_probeprofiles` to `probeprofiles_query`"""

    query_remotenetworks_spnnpnsitemigration = spnnpnsitemigration_remotenetworks_query
    """ Backwards-compatibility alias of `query_remotenetworks_spnnpnsitemigration` to `spnnpnsitemigration_remotenetworks_query`"""

    query_securityprofilegroups = securityprofilegroups_query
    """ Backwards-compatibility alias of `query_securityprofilegroups` to `securityprofilegroups_query`"""

    query_sitesnapshots = sitesnapshots_query
    """ Backwards-compatibility alias of `query_sitesnapshots` to `sitesnapshots_query`"""

    query_sitetemplates_bulkconfigurations = sitetemplates_bulkconfigurations_query
    """ Backwards-compatibility alias of `query_sitetemplates_bulkconfigurations` to `sitetemplates_bulkconfigurations_query`"""

    query_snapshots = snapshots_query
    """ Backwards-compatibility alias of `query_snapshots` to `snapshots_query`"""

    query_status_bgppeers = status_bgppeers_query
    """ Backwards-compatibility alias of `query_status_bgppeers` to `status_bgppeers_query`"""

    query_status_cellular_modules = status_cellular_modules_query
    """ Backwards-compatibility alias of `query_status_cellular_modules` to `status_cellular_modules_query`"""

    query_status_interfaces = status_interfaces_query
    """ Backwards-compatibility alias of `query_status_interfaces` to `status_interfaces_query`"""

    query_status_spokeclusters = status_spokeclusters_query
    """ Backwards-compatibility alias of `query_status_spokeclusters` to `status_spokeclusters_query`"""

    query_threatmetadata = threatmetadata_query
    """ Backwards-compatibility alias of `query_threatmetadata` to `threatmetadata_query`"""

    query_topn_traffic_vol_monitor = monitor_topn_traffic_vol_query
    """ Backwards-compatibility alias of `query_topn_traffic_vol_monitor` to `monitor_topn_traffic_vol_query`"""

    query_urlcategories = urlcategories_query
    """ Backwards-compatibility alias of `query_urlcategories` to `urlcategories_query`"""

    rquery_e = element_rquery
    """ Backwards-compatibility alias of `rquery_e` to `element_rquery`"""

    sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates
    """ Backwards-compatibility alias of `sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates`"""

    snmpdiscoverystartnodes_deviceidconfigs = deviceidconfigs_snmpdiscoverystartnodes
    """ Backwards-compatibility alias of `snmpdiscoverystartnodes_deviceidconfigs` to `deviceidconfigs_snmpdiscoverystartnodes`"""

    status_query = query_status
    """ Backwards-compatibility alias of `status_query` to `query_status`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

