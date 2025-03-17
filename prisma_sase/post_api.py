#!/usr/bin/env python
"""
PRISMA SASE Python SDK - POST

**Author:** Palo Alto Networks

**Copyright:** (c) 2025 Palo Alto Networks, Inc

**License:** MIT
"""
import logging

__author__ = "Prisma SASE Developer Support <prisma-sase-developers@paloaltonetworks.com>"
__email__ = "prisma-sase-developers@paloaltonetworks.com"
__copyright__ = "Copyright (c) 2025 Palo Alto Networks, Inc"
__license__ = """
    MIT License

    Copyright (c) 2025 Palo Alto Networks, Inc

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

    def activeuserips_query(self, data, api_version="v2.0"):
        """
        Query active user mappings of tenant (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **add:**  Type: boolean 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **ip:**  Type: string 
           - **last_login_time:**  Type: integer 
           - **region:**  Type: string 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 
           - **user_id:**  Type: string 
           - **username:**  Type: string 
           - **valid_until:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/activeuserips/query".format(api_version)

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

    def anynetlinks_correlationevents_query(self, data, api_version="v2.1"):
        """
        POST Anynetlinks_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks/correlationevents/query".format(api_version)

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

    def apnprofiles_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of apn profiles that match query params. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/apnprofiles/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appacceleration_query(self, data, api_version="v2.0"):
        """
        POST Appacceleration_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


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

    def appdefs_query(self, data, api_version="v2.6"):
        """
        Queries db for limit number of app defs that match query params. (v2.6)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def auditlog_query(self, data, api_version="v2.1"):
        """
        POST Auditlog_Query API Function

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

    def bgppeers(self, site_id, element_id, data, api_version="v2.6"):
        """
        Create BGP peer config (v2.6)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

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

    def bgppeers_operations(self, site_id, element_id, bgppeer_id, data, api_version="v2.0"):
        """
        Reset BGP peer config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}/operations".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bgppeers_query(self, site_id, element_id, data, api_version="v2.6"):
        """
        Queries db for limit number of BGP peers that match query params. (v2.6)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/query".format(api_version,
                                                                                         site_id,
                                                                                         element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bgppeers_status_query(self, data, api_version="v2.0"):
        """
        POST Bgppeers_Status_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bgppeers/status/query".format(api_version)

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

    def bulkconfigurations_sitetemplates_clone(self, sitetemplate_id, data, api_version="v2.0"):
        """
        POST Bulkconfigurations_Sitetemplates_Clone API Function

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

    def bulkconfigurations_sitetemplates_deployments(self, sitetemplate_id, data, api_version="v2.0"):
        """
        Deploy site (v2.0)

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **deployment_id:**  Type: string 
           - **site_id:**  Type: string 
           - **template_id:**  Type: string 
           - **variable_map:**  Type: object 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}/deployments".format(api_version,
                                                                                                     sitetemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulkconfigurations_sitetemplates_deployments_query(self, data, api_version="v2.0"):
        """
        Get all site profile (v2.0)

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

    def bulkconfigurations_sitetemplates_query(self, data, api_version="v2.0"):
        """
        Get all site profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **data:**  Type: string 
           - **deployment_count:**  Type: integer 
           - **site_id:**  Type: string 
           - **site_type:**  Type: string 
           - **status:**  Type: string 
           - **status_description:**  Type: string 
           - **template_description:**  Type: string 
           - **template_id:**  Type: string 
           - **template_name:**  Type: string 
           - **tenant_id:**  Type: string 
           - **variable_map:**  Type: object 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulkoperations(self, data, api_version="v2.0"):
        """
        Bulk site update API (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **site_ids:**  [Type: string] 
           - **type:**  Type: string 
           - **vrf_context_profile_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/bulkoperations".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_module_firmware_status_query(self, data, api_version="v2.0"):
        """
        Query the cellular module firmware upgrade status of all tenant elements (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **active_image_id:**  Type: string 
           - **active_version:**  Type: string 
           - **download_interval:**  Type: integer 
           - **download_percent:**  Type: integer 
           - **element_id:**  Type: string 
           - **failure_info:**  Type: string 
           - **previous_image_id:**  Type: string 
           - **rollback_version:**  Type: string 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 
           - **upgrade_image_id:**  Type: string 
           - **upgrade_interval:**  Type: integer 
           - **upgrade_state:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cellular_module_firmware/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_module_revoked_images(self, data, api_version="v2.0"):
        """
        POST Cellular_Module_Revoked_Images API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cellular_module_revoked_images".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_modules_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of cellular modules that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **element_id:**  Type: string 
           - **gps_enable:**  Type: boolean 
           - **name:**  Type: string 
           - **primary_sim:**  Type: integer 
           - **radio_on:**  Type: boolean 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cellular_modules/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_modules_status_query(self, data, api_version="v2.1"):
        """
        POST Cellular_Modules_Status_Query API Function

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

    def clients_login(self, client_id, data, api_version="v2.0"):
        """
        Login api for esp client (v2.0)

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **email:**  Type: string 
           - **logout_others:**  Type: boolean 
           - **password:**  Type: string 
           - **requestId:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/login".format(api_version,
                                                                      client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def clients_logout(self, data, api_version="v2.0"):
        """
        Logout api for esp client. Reverts back to esp session (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **disallowed_permissions:**  Type: object 
           - **operator_id:**  Type: string 
           - **permissions:**  Type: object 
           - **redirect_region:**  Type: string 
           - **redirect_urlpath:**  Type: string 
           - **redirect_x_auth_token:**  Type: string 
           - **resource_role_map:**  [Type: object] 
           - **resource_uri_map:**  Type: object 
           - **resource_version_map:**  Type: object 
           - **tenant_id:**  Type: string 
           - **version_exceptions_map:**  [Type: object] 
           - **x_auth_token:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/logout".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def clients_machines_query(self, client_id, data, api_version="v2.5"):
        """
        Query and get all machines allocated by ESP to a client tenant (v2.5)

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 

           - **count:**  Type: integer 
           - **deleted_count:**  Type: integer 
           - **deleted_ids:**  [Type: string] 
           - **next_query:**  Type: object 
           - **tenant_id:**  Type: string 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/machines/query".format(api_version,
                                                                               client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def clients_query(self, data, api_version="v2.0"):
        """
        Get esp tenant clients details for tenant id (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **canonical_name:**  Type: string 
           - **clients:**  [Type: string] 
           - **is_esp:**  Type: boolean 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **telemetry_region:**  Type: string 
           - **tenant_id:**  Type: string 
           - **tsg_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def clients_reallocate(self, client_id, machine_id, data, api_version="v2.5"):
        """
        Reallocate a specific machine from one client tenant to another, both client tenants are clients of the same ESP. (v2.5)

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 

           - **connected:**  Type: boolean 
           - **console_conf_passphrase:**  Type: string 
           - **element_shell_id:**  Type: string 
           - **em_element_id:**  Type: string 
           - **esp_tenant_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **image_version:**  Type: string 
           - **inventory_op:**  Type: string 
           - **is_eval:**  Type: string 
           - **machine_state:**  Type: string 
           - **manufacture_id:**  Type: string 
           - **model_name:**  Type: string 
           - **ordering_info:**  Type: string 
           - **owner_tenant_id:**  Type: string 
           - **pki_op:**           
               - **ca_list:**  [Type: string] 
               - **operation:**  Type: string 
           - **renew_state:**  Type: string 
           - **sales_order_number:**  Type: string 
           - **ship_state:**  Type: string 
           - **sl_no:**  Type: string 
           - **suspend_state:**  Type: string 
           - **tenant_id:**  Type: string 
           - **token:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/machines/{}/reallocate".format(api_version,
                                                                                       client_id,
                                                                                       machine_id)

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

    def demstatus_query(self, data, api_version="v2.0"):
        """
        Query ADEM status (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **dem_enabled:**  Type: boolean 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/demstatus/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def deviceidconfigs_bulkdelete_snmpdiscoverystartnodes(self, site_id, deviceidconfig_id, data, api_version="v2.0"):
        """
        Bulk delete Start Network Node config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: Device Id Config ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **error_message:**  Type: string 
           - **ipv4_address:**  Type: string 
           - **name:**  Type: string 
           - **scope:**           
               - **ipv4_prefix:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}/bulkdelete_snmpdiscoverystartnodes".format(api_version,
                                                                                                                    site_id,
                                                                                                                    deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def deviceidconfigs_query(self, data, api_version="v2.0"):
        """
        Get device id profiles (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **cfg_device_id_enabled:**  Type: boolean 
           - **deviceid_profile_id:**  Type: string 
           - **site_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/deviceidconfigs/query".format(api_version)

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

    def deviceidprofiles_operations(self, deviceidprofile_id, data, api_version="v2.0"):
        """
        Associate device id profile in bulk (v2.0)

          **Parameters:**:

          - **deviceidprofile_id**: Device Id Profile ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **sites:**           
               - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 
           - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/deviceidprofiles/{}/operations".format(api_version,
                                                                                    deviceidprofile_id)

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

    def directoryservices(self, data, api_version="v2.0"):
        """
        Create Directory Service (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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

    def directoryservices_deltasync(self, data, api_version="v2.0"):
        """
        Force delta sync. (v2.0)

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

    def directoryservices_sync(self, data, api_version="v2.0"):
        """
        Force full sync. (v2.0)

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

    def directoryusergroups_query(self, data, api_version="v2.0"):
        """
        Query users or groups. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **stale:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryusergroups/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def directoryusers_query(self, data, api_version="v2.0"):
        """
        Query users. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **stale:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **user_group_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryusers/query".format(api_version)

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

    def dnsserviceprofiles_query(self, data, api_version="v2.1"):
        """
        Query DNS service profile based on parameters (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceprofiles/query".format(api_version)

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

    def dnsserviceroles_query(self, data, api_version="v2.0"):
        """
        Query DNS service role based on parameters (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceroles/query".format(api_version)

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

    def dnsservices_query(self, data, api_version="v2.0"):
        """
        Query DNS service config based on parameters (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsservices/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_bulk_config_state_query(self, data, api_version="v2.0"):
        """
        Get element config/state info for queried elements from NB (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **count:**  Type: integer 
           - **items:**  [Type: object] 
           - **tenant_id:**  Type: string 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/bulk_config_state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_correlationevents_query(self, data, api_version="v2.0"):
        """
        POST Element_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_deviceidconfigs(self, site_id, element_id, data, api_version="v2.0"):
        """
        Create device id element level (source interface) config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **snmp_discovery_source_interface_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/deviceidconfigs".format(api_version,
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

    def element_extensions_query(self, site_id, element_id, data, api_version="v2.0"):
        """
        Query element level extensions that match query params (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/extensions/query".format(api_version,
                                                                                           site_id,
                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_query(self, data, api_version="v3.2"):
        """
        Queries db for limit number of elements that match query params. (v3.2)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.2)

          **Payload Attributes:** 

           - **admin_action:**  Type: string 
           - **admin_renew_state:**  Type: string 
           - **admin_suspend_state:**  Type: string 
           - **allowed_roles:**  [Type: string] 
           - **cluster_id:**  Type: string 
           - **connected:**  Type: boolean 
           - **deployment_op:**  Type: string 
           - **description:**  Type: string 
           - **device_change_mode_start_time:**  Type: integer 
           - **device_change_mode_state:**  Type: string 
           - **device_mode:**  Type: string 
           - **device_profile_id:**  Type: string 
           - **fips_mode:**  Type: string 
           - **fips_mode_change_start_time:**  Type: integer 
           - **hub_cluster_config:**           
               - **intra_cluster_tunnel:**           
                   - **destination_ip:**  Type: string 
                   - **source_ip:**  Type: string 
                   - **status:**  Type: string 
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
           - **override_indicator:**  [Type: string] 
           - **priority_policysetstack_id:**  Type: string 
           - **role:**  Type: string 
           - **serial_number:**  Type: string 
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

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/query".format(api_version)

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

    def elements_rquery(self, data, api_version="v3.0"):
        """
        Query and get client elements across regions (v3.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 

           - **admin_action:**  Type: string 
           - **admin_renew_state:**  Type: string 
           - **admin_suspend_state:**  Type: string 
           - **allowed_roles:**  [Type: string] 
           - **cluster_id:**  Type: string 
           - **connected:**  Type: boolean 
           - **deployment_op:**  Type: string 
           - **description:**  Type: string 
           - **device_change_mode_start_time:**  Type: integer 
           - **device_change_mode_state:**  Type: string 
           - **device_mode:**  Type: string 
           - **device_profile_id:**  Type: string 
           - **fips_mode:**  Type: string 
           - **fips_mode_change_start_time:**  Type: integer 
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
           - **override_indicator:**  [Type: string] 
           - **priority_policysetstack_id:**  Type: string 
           - **role:**  Type: string 
           - **serial_number:**  Type: string 
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

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/rquery".format(api_version)

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

    def elementsecurityzones_query(self, data, api_version="v2.0"):
        """
        Query element security zones. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
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

        url = str(cur_ctlr) + "/sdwan/{}/api/elementsecurityzones/query".format(api_version)

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
                   - **destination_ip:**  Type: string 
                   - **source_ip:**  Type: string 
                   - **status:**  Type: string 
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

    def elementshells_copy_element_configurations(self, site_id, elementshell_id, data, api_version="v2.0"):
        """
        Asynchronization call to Copy Interface Configurations from element to element shell (v2.0)

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

    def elementshells_interfaces(self, site_id, elementshell_id, data, api_version="v2.4"):
        """
        Create a Interface (v2.4)

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
                   - **destination_ip:**  Type: string 
                   - **source_ip:**  Type: string 
                   - **status:**  Type: string 
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

    def eventcorrelationpolicyrules_query(self, data, api_version="v2.1"):
        """
        Queries db for limit number of event correlation policyrules that match query params. (v2.1)

          **Parameters:**:

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
           - **policyset_id:**  Type: string 
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

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicyrules/query".format(api_version)

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

    def eventcorrelationpolicysets_query(self, data, api_version="v2.0"):
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

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/query".format(api_version)

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

    def events_query(self, data, api_version="v3.6"):
        """
        POST Events_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/events/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def events_summary(self, data, api_version="v2.1"):
        """
        POST Events_Summary API Function

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

    def globalprefixfilters(self, data, api_version="v2.0"):
        """
        Create a new global prefix filter. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **filters:**           
               - **type:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def globalprefixfilters_query(self, data, api_version="v2.0"):
        """
        Query DB for the list of params. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters/query".format(api_version)

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

    def hubclusters_operations(self, site_id, hubcluster_id, data, api_version="v4.0"):
        """
        Operations hub cluster api (v4.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 

           - **cluster_state:**  Type: string 
           - **elements:**           
               - **hubClusterElementNumber:**  Type: string 
               - **hub_element_id:**  Type: string 
               - **locked:**  Type: boolean 
               - **peer_sites:**  [Type: string] 
           - **vpns_added:**  Type: integer 
           - **vpns_deleted:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/operations".format(api_version,
                                                                                        site_id,
                                                                                        hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def hubclusters_query(self, data, api_version="v4.0"):
        """
        Query hub clusters (v4.0)

          **Parameters:**:

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
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/hubclusters/query".format(api_version)

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

    def interfaces_correlationevents_query(self, data, api_version="v2.0"):
        """
        POST Interfaces_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/interfaces/correlationevents/query".format(api_version)

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

    def interfaces_query(self, data, api_version="v4.21"):
        """
        Queries db for limit number of interfaces that match query params. (v4.21)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.21)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/interfaces/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def interfaces_status_query(self, data, api_version="v2.0"):
        """
        POST Interfaces_Status_Query API Function

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

    def iotdevicemappings_query(self, data, api_version="v2.0"):
        """
        POST Iotdevicemappings_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/iotdevicemappings/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def iotdictionary_query(self, data, api_version="v2.0"):
        """
        POST Iotdictionary_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/iotdictionary/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def iotservices(self, data, api_version="v2.0"):
        """
        POST Iotservices API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


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

    def ipfix_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of ipfix configs that match query params. (v2.0)

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
           - **element_id:**  Type: string 
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
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfix/query".format(api_version)

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

    def ipfixcollectorcontexts_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of ipfix collector context that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixcollectorcontexts/query".format(api_version)

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

    def ipfixfiltercontexts_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of ipfix filter context that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixfiltercontexts/query".format(api_version)

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

    def ipfixglobalprefixes_query(self, data, api_version="v2.0"):
        """
        POST Ipfixglobalprefixes_Query API Function

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

    def ipfixlocalprefixes_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of ipfix site prefix association that match query (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixlocalprefixes/query".format(api_version)

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

    def ipfixprofiles_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of ipfix profiles that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixprofiles/query".format(api_version)

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

    def ipfixtemplates_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of ipfix templates that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixtemplates/query".format(api_version)

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
               - **force_encapsulation:**  Type: boolean
               - **lifesize:**
                   - **units:**  Type: string
                   - **value:**  Type: integer
               - **lifetime:**  Type: integer
               - **lifetime_units:**  Type: string
               - **mode:**  Type: string
               - **proposals:**
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
                   - **prf:**  Type: string
               - **responder_sase_proposals:**
                   - **dh_group:**  [Type: string]
                   - **encryption:**  [Type: string]
                   - **hash:**  [Type: string]
           - **ike_group:**
               - **aggressive:**  Type: boolean
               - **authentication_multiple:**  Type: integer
               - **key_exchange:**  Type: string
               - **lifetime:**  Type: integer
               - **lifetime_units:**  Type: string
               - **port:**  Type: integer
               - **proposals:**
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
                   - **prf:**  Type: string
               - **reauth:**  Type: boolean
           - **name:**  Type: string
           - **tags:**  [Type: string] 
           - **used_for:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipsecprofiles_query(self, data, api_version="v2.2"):
        """
        Queries db for limit number of tenant level ipsec profiles that match query params. (v2.2)

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
               - **force_encapsulation:**  Type: boolean
               - **lifesize:**
                   - **units:**  Type: string
                   - **value:**  Type: integer
               - **lifetime:**  Type: integer
               - **lifetime_units:**  Type: string
               - **mode:**  Type: string
               - **proposals:**
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
                   - **prf:**  Type: string
               - **responder_sase_proposals:**
                   - **dh_group:**  [Type: string]
                   - **encryption:**  [Type: string]
                   - **hash:**  [Type: string]
           - **ike_group:**
               - **aggressive:**  Type: boolean
               - **authentication_multiple:**  Type: integer
               - **key_exchange:**  Type: string
               - **lifetime:**  Type: integer
               - **lifetime_units:**  Type: string
               - **port:**  Type: integer
               - **proposals:**
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
                   - **prf:**  Type: string
               - **reauth:**  Type: boolean
           - **name:**  Type: string
           - **tags:**  [Type: string] 
           - **used_for:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles/query".format(api_version)

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

    def lannetworks_query(self, data, api_version="v3.3"):
        """
        Query db for Site LAN networks that match query parameters (v3.3)

          **Parameters:**:

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
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **scope:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/lannetworks/query".format(api_version)

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

    def localprefixfilters_query(self, data, api_version="v2.0"):
        """
        Query DB for the list of params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/localprefixfilters/query".format(api_version)

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

    def machine_upgrade_query(self, data, api_version="v2.0"):
        """
        Query Machine Upgrade Config (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machine_upgrade/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def machines_allocate_to_shell(self, machine_id, data, api_version="v2.0"):
        """
        Allocate Element Shell to Machine (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **connected:**  Type: boolean 
           - **console_conf_passphrase:**  Type: string 
           - **element_shell_id:**  Type: string 
           - **em_element_id:**  Type: string 
           - **esp_tenant_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **image_version:**  Type: string 
           - **inventory_op:**  Type: string 
           - **is_eval:**  Type: string 
           - **machine_state:**  Type: string 
           - **manufacture_id:**  Type: string 
           - **model_name:**  Type: string 
           - **ordering_info:**  Type: string 
           - **owner_tenant_id:**  Type: string 
           - **pki_op:**           
               - **ca_list:**  [Type: string] 
               - **operation:**  Type: string 
           - **renew_state:**  Type: string 
           - **sales_order_number:**  Type: string 
           - **ship_state:**  Type: string 
           - **sl_no:**  Type: string 
           - **suspend_state:**  Type: string 
           - **tenant_id:**  Type: string 
           - **token:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/allocate_to_shell".format(api_version,
                                                                                   machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def machines_query(self, data, api_version="v2.5"):
        """
        Query and get machines of a tenant (v2.5)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 

           - **connected:**  Type: boolean 
           - **console_conf_passphrase:**  Type: string 
           - **element_shell_id:**  Type: string 
           - **em_element_id:**  Type: string 
           - **esp_tenant_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **image_version:**  Type: string 
           - **inventory_op:**  Type: string 
           - **is_eval:**  Type: string 
           - **machine_state:**  Type: string 
           - **manufacture_id:**  Type: string 
           - **model_name:**  Type: string 
           - **ordering_info:**  Type: string 
           - **owner_tenant_id:**  Type: string 
           - **pki_op:**           
               - **ca_list:**  [Type: string] 
               - **operation:**  Type: string 
           - **renew_state:**  Type: string 
           - **sales_order_number:**  Type: string 
           - **ship_state:**  Type: string 
           - **sl_no:**  Type: string 
           - **suspend_state:**  Type: string 
           - **tenant_id:**  Type: string 
           - **token:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_aaa_client_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Aaa_Client_Metrics API Function

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

    def monitor_aaa_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Aaa_Metrics API Function

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

    def monitor_aaa_metrics_topn(self, data, api_version="v2.0"):
        """
        POST Monitor_Aaa_Metrics_Topn API Function

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

    def monitor_aggregates(self, data, api_version="v3.0"):
        """
        POST Monitor_Aggregates API Function

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

    def monitor_aggregates_application_qos(self, data, api_version="v2.0"):
        """
        POST Monitor_Aggregates_Application_Qos API Function

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

    def monitor_aggregates_healthscore(self, data, api_version="v2.1"):
        """
        POST Monitor_Aggregates_Healthscore API Function

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

    def monitor_aggregates_multicast_mroute(self, data, api_version="v2.0"):
        """
        POST Monitor_Aggregates_Multicast_Mroute API Function

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

    def monitor_aggregates_multicast_wan_neighbor(self, data, api_version="v2.0"):
        """
        POST Monitor_Aggregates_Multicast_Wan_Neighbor API Function

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

    def monitor_aiops_aggregates(self, data, api_version="v2.1"):
        """
        POST Monitor_Aiops_Aggregates API Function

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

    def monitor_aiops_anomaly(self, data, api_version="v2.0"):
        """
        POST Monitor_Aiops_Anomaly API Function

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

    def monitor_aiops_forecast(self, data, api_version="v2.1"):
        """
        POST Monitor_Aiops_Forecast API Function

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

    def monitor_aiops_health(self, data, api_version="v2.0"):
        """
        POST Monitor_Aiops_Health API Function

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

    def monitor_aiops_object_stats(self, data, api_version="v2.1"):
        """
        POST Monitor_Aiops_Object_Stats API Function

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

    def monitor_aiops_topn(self, data, api_version="v2.0"):
        """
        POST Monitor_Aiops_Topn API Function

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

    def monitor_application_qos_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Application_Qos_Metrics API Function

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

    def monitor_application_users(self, data, api_version="v2.0"):
        """
        POST Monitor_Application_Users API Function

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

    def monitor_bulk_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Bulk_Metrics API Function

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

    def monitor_cellular_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Cellular_Metrics API Function

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

    def monitor_cellular_metrics_topn(self, data, api_version="v2.0"):
        """
        POST Monitor_Cellular_Metrics_Topn API Function

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

    def monitor_flows(self, data, api_version="v3.10"):
        """
        POST Monitor_Flows API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.10)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/flows".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_insights(self, data, api_version="v2.0"):
        """
        POST Monitor_Insights API Function

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

    def monitor_insightslist(self, data, api_version="v2.0"):
        """
        POST Monitor_Insightslist API Function

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

    def monitor_lqm_point_metrics(self, data, api_version="v2.0"):
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

    def monitor_metrics(self, data, api_version="v2.6"):
        """
        POST Monitor_Metrics API Function

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

    def monitor_network_point_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Network_Point_Metrics API Function

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

    def monitor_network_point_metrics_bw(self, data, api_version="v2.0"):
        """
        POST Monitor_Network_Point_Metrics_Bw API Function

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

    def monitor_network_point_metrics_hs(self, data, api_version="v2.0"):
        """
        POST Monitor_Network_Point_Metrics_Hs API Function

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

    def monitor_object_stats(self, data, api_version="v2.7"):
        """
        POST Monitor_Object_Stats API Function

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

    def monitor_qos_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Qos_Metrics API Function

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

    def monitor_sys_metrics(self, data, api_version="v2.3"):
        """
        POST Monitor_Sys_Metrics API Function

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

    def monitor_sys_metrics_topn(self, data, api_version="v2.1"):
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

    def monitor_sys_point_metrics(self, data, api_version="v2.0"):
        """
        POST Monitor_Sys_Point_Metrics API Function

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

    def monitor_topn(self, data, api_version="v3.1"):
        """
        POST Monitor_Topn API Function

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

    def mstp_instances_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of MSTP Instances that match query params. (v2.0)

          **Parameters:**:

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

        url = str(cur_ctlr) + "/sdwan/{}/api/mstp_instances/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastdynamicrps_query(self, data, api_version="v2.0"):
        """
        Query Multicast Dynamic RPs (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **dynamic_rps:**           
               - **groups:**           
                   - **ipv4_prefix:**  Type: string 
                   - **is_active_rp:**  Type: boolean 
               - **ipv4_address:**  Type: string 
               - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastdynamicrps/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastigmpmemberships_query(self, data, api_version="v2.0"):
        """
        Query Multicast IGMP group membership information (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
           - **igmp_group_members:**           
               - **fwd:**  Type: string 
               - **group:**  Type: string 
               - **source:**  Type: string 
               - **timeout:**  Type: string 
               - **uptime:**  Type: string 
           - **interface_id:**  Type: string 
           - **name:**  Type: string 
           - **site_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastigmpmemberships/query".format(api_version)

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

    def multicastroutes_query(self, data, api_version="v2.0"):
        """
        Query Multicast route table (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
           - **mroutes:**           
               - **element_rp:**  Type: boolean 
               - **flags:**  Type: string 
               - **group:**  Type: string 
               - **incoming_interface:**  Type: string 
               - **outgoing_interfaces:**  [Type: string] 
               - **rp_address:**  Type: string 
               - **source:**  Type: string 
           - **site_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastroutes/query".format(api_version)

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

    def multicastrps_query(self, data, api_version="v2.0"):
        """
        Query Multicast RP config (v2.0)

          **Parameters:**:

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

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastrps/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastsourcesiderps_query(self, site_id, data, api_version="v2.0"):
        """
        Query multicast source side RPs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **source_side_rps:**           
               - **groups:**           
                   - **ipv4_prefix:**  Type: string 
                   - **source_ipv4_address:**  Type: string 
               - **ipv4_address:**  Type: string 
           - **source_site_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiderps/query".format(api_version,
                                                                                           site_id)

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

    def multicaststatus_query(self, data, api_version="v2.0"):
        """
        Query Multicast status information (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **address:**  Type: string 
           - **element_id:**  Type: string 
           - **interface_id:**  Type: string 
           - **name:**  Type: string 
           - **pim_neighbors:**           
               - **address:**  Type: string 
               - **dr:**  Type: boolean 
               - **dr_prio:**  Type: string 
               - **expires:**  Type: string 
               - **uptime:**  Type: string 
           - **site_id:**  Type: string 
           - **state:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicaststatus/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastwanstatus_query(self, data, api_version="v2.0"):
        """
        Query Multicast WAN status (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **pim_neighbors:**           
               - **remote_site_id:**  Type: string 
               - **state:**  Type: string 
               - **uptime:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastwanstatus/query".format(api_version)

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

    def natglobalprefixes_query(self, data, api_version="v2.0"):
        """
        Query Global Prefixes. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/natglobalprefixes/query".format(api_version)

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

    def natlocalprefixes_query(self, data, api_version="v2.0"):
        """
        Query site local prefixes. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natlocalprefixes/query".format(api_version)

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

    def natpolicypools_query(self, data, api_version="v2.0"):
        """
        Query NAT policy pools. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicypools/query".format(api_version)

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

    def natpolicyrules_query(self, data, api_version="v2.0"):
        """
        Query NAT policy rules. (v2.0)

          **Parameters:**:

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
           - **destination_prefixes_id:**  Type: string 
           - **destination_zone_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **policyset_id:**  Type: string 
           - **protocol:**  Type: integer 
           - **source_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **source_prefixes_id:**  Type: string 
           - **source_zone_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicyrules/query".format(api_version)

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

    def natpolicysets_query(self, data, api_version="v2.0"):
        """
        Query policy sets. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **destination_zone_policyrule_order:**  [Type: string] 
           - **name:**  Type: string 
           - **source_zone_policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/query".format(api_version)

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

    def natpolicysetstacks_query(self, data, api_version="v2.0"):
        """
        Query policyset stacks. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysetstacks/query".format(api_version)

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

    def natzones_query(self, data, api_version="v2.0"):
        """
        Query NAT policy zones. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_for_public_interfaces:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natzones/query".format(api_version)

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

    def networkcontexts_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of network contexts that match query params. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkcontexts/query".format(api_version)

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

    def networkpolicyglobalprefixes_query(self, data, api_version="v2.1"):
        """
        Query Network Global Prefixes. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyglobalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicylocalprefixes_query(self, data, api_version="v2.1"):
        """
        Query site network prefix association. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicylocalprefixes/query".format(api_version)

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

    def networkpolicyrules_query(self, data, api_version="v2.4"):
        """
        Query Network policy rules. (v2.4)

          **Parameters:**:

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

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyrules/query".format(api_version)

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

    def networkpolicysets_query(self, data, api_version="v2.0"):
        """
        Query Network policy sets. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/query".format(api_version)

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

    def networkpolicysetstacks_query(self, data, api_version="v2.0"):
        """
        Query network policyset stacks. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysetstacks/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networks_bulk_config_state_query(self, data, api_version="v2.0"):
        """
        Get all config/state info for given network from NB (v2.0)

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

    def ngfwsecuritypolicyglobalprefixes_query(self, data, api_version="v2.1"):
        """
        Query Security Policy V2 Global Prefixes of a tenant (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyglobalprefixes/query".format(api_version)

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

    def ngfwsecuritypolicylocalprefixes_query(self, data, api_version="v2.1"):
        """
        Query security policy v2 local prefix site associations of a tenant (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **ipv6_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicylocalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicyrules(self, ngfwsecuritypolicyset_id, data, api_version="v2.2"):
        """
        Create a Security Policy V2 Rule under a policy set (v2.2)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **dest_device_ids:**  [Type: string] 
           - **destination_prefix_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
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

    def ngfwsecuritypolicyrules_query(self, data, api_version="v2.2"):
        """
        Query security policy v2 rules of a tenant (v2.2)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefix_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **policyset_id:**  Type: string 
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
           - **tags:**  [Type: string] 
           - **user_or_group:**           
               - **user_group_ids:**  [Type: string] 
               - **user_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyrules/query".format(api_version)

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

    def ngfwsecuritypolicysets_query(self, data, api_version="v2.0"):
        """
        Query security policy v2 sets of a tenant (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/query".format(api_version)

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

    def ngfwsecuritypolicysetstacks_query(self, data, api_version="v2.0"):
        """
        Query Security Policy V2 Set stacks of a tenant (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysetstacks/query".format(api_version)

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

    def ospfconfigs_query (self, data, api_version="v2.0"):
        """
        Query OSPF config (v2.0)

          **Parameters:**:

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

    def password_change(self, data, api_version="v2.0"):
        """
        Allows one to change password (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **oldPassword:**  Type: string 
           - **password:**  Type: string 
           - **repeatPassword:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/accounts/password/change".format(api_version)

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

    def pathgroups_query(self, data, api_version="v2.1"):
        """
        Queries db for limit number of network contexts that match query params. (v2.1)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/pathgroups/query".format(api_version)

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

    def perfmgmtpolicysets_perfmgmtpolicyrules(self, perfmgmtpolicyset_id, data, api_version="v2.2"):
        """
        Create a new PERFMGMT Policy Rule V2.2 (v2.2)

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

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
           - **name:**  Type: string 
           - **network_context_ids:**  [Type: string] 
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

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}/perfmgmtpolicyrules".format(api_version,
                                                                                               perfmgmtpolicyset_id)

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

    def policyrules_query(self, data, api_version="v3.1"):
        """
        Queries db for policyrules that match query params. (v3.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **app_def_id:**  Type: string 
           - **description:**  Type: string 
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
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policyrules/query".format(api_version)

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

    def policysets_bulk_config_state_query(self, data, api_version="v2.0"):
        """
        Get all config/state info across all policysets from NB (v2.0)

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

    def policysets_query(self, data, api_version="v3.0"):
        """
        Queries db for policysets that match query params. (v3.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/query".format(api_version)

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

    def prefixes_query(self, data, api_version="v3.1"):
        """
        POST Prefixes_Query API Function

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

    def prefixfilters(self, site_id, data, api_version="v2.0"):
        """
        Create an association between site and security prefix filter. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **filters:**           
               - **type:**  Type: string 
           - **prefix_filter_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters".format(api_version,
                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prefixfilters_query(self, site_id, data, api_version="v2.0"):
        """
        Query security prefix filter for NB API. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **query_params:**           
               - **zone_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters/query".format(api_version,
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

    def prioritypolicyglobalprefixes_query(self, data, api_version="v2.1"):
        """
        Query Priority Global Prefixes. (v2.1)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyglobalprefixes/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicylocalprefixes_query(self, data, api_version="v2.1"):
        """
        Query site priority prefix association. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicylocalprefixes/query".format(api_version)

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

    def prioritypolicyrules_query(self, data, api_version="v2.2"):
        """
        Query Priority policy rules. (v2.2)

          **Parameters:**:

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
           - **policyset_id:**  Type: string 
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

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyrules/query".format(api_version)

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

    def prioritypolicysets_query(self, data, api_version="v2.0"):
        """
        Query Priority policy sets. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/query".format(api_version)

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

    def prioritypolicysetstacks_query(self, data, api_version="v2.0"):
        """
        Query priority policyset stacks. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysetstacks/query".format(api_version)

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

    def prismaaccess_configs_query(self, data, api_version="v2.0"):
        """
        Query Prisma Access config (v2.0)

          **Parameters:**:

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

        url = str(cur_ctlr) + "/sdwan/{}/api/prismaaccess_configs/query".format(api_version)

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

    def prismasase_connections_status_query(self, data, api_version="v2.0"):
        """
        Get a list of SASE connection statuses (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **common_messages:**  Type: string 
           - **connection_status:**           
               - **value:**  Type: string 
           - **ipsec_tunnel_status:**           
               - **attempts:**  Type: integer 
               - **branch_tunnel_connection_status:**  Type: string 
               - **branch_tunnel_provisioning_status:**  Type: string 
               - **completed_steps:**  [Type: string] 
               - **element_id:**  Type: string 
               - **error_messages:**  Type: object 
               - **info_messages:**  Type: object 
               - **interface_id:**  Type: string 
               - **name:**  Type: string 
               - **prismaaccess_tunnel_connection_status:**  Type: string 
               - **prismaaccess_tunnel_provisioning_status:**  Type: string 
               - **remoteNetworkGroupName:**  Type: string 
               - **uncompleted_steps:**  [Type: string] 
           - **is_active:**  Type: boolean 
           - **prismasase_connection_id:**  Type: string 
           - **site_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismasase_connections/status/query".format(api_version)

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

    def reports_query(self, data, api_version="v2.0"):
        """
        POST Reports_Query API Function

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

    def reportsdir_query(self, data, api_version="v2.0"):
        """
        POST Reportsdir_Query API Function

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

    def routing_aspathaccesslists_query(self, site_id, element_id, data, api_version="v2.1"):
        """
        Queries db for limit number of access lists that match query params. (v2.1)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_aspathaccesslists/query".format(api_version,
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

    def routing_ipcommunitylists_query(self, site_id, element_id, data, api_version="v2.0"):
        """
        Queries db for limit number of community lists that match query params. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_ipcommunitylists/query".format(api_version,
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

    def routing_prefixlists_query(self, site_id, element_id, data, api_version="v2.1"):
        """
        Queries db for limit number of prefix lists that match query params. (v2.1)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_prefixlists/query".format(api_version,
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

    def routing_routemaps_query(self, site_id, element_id, data, api_version="v2.3"):
        """
        Queries db for limit number of route maps that match query params. (v2.3)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_routemaps/query".format(api_version,
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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/rquery".format(api_version)

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

    def securitypolicyrules_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of LAN networks that match query params. (v2.0)

          **Parameters:**:

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
           - **security_policyset_id:**  Type: string 
           - **source_filter_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicyrules/query".format(api_version)

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

    def securitypolicysets_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of security policysets that match query params. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/query".format(api_version)

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

    def securityzones_query(self, data, api_version="v2.1"):
        """
        query (v2.1)

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

    def servicebindingmaps_query(self, data, api_version="v2.1"):
        """
        Queries db for limit number of service bindings that match query params. (v2.1)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/servicebindingmaps/query".format(api_version)

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

    def serviceendpoints_query(self, data, api_version="v3.1"):
        """
        Queries db for limit number of service bindings that match query params. (v3.1)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/serviceendpoints/query".format(api_version)

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

    def servicelabels_query(self, data, api_version="v2.1"):
        """
        Queries db for limit number of service labels that match query params. (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicelabels/query".format(api_version)

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

    def site_bulk_config_state_query(self, data, api_version="v2.0"):
        """
        Get site config/state info for queried site from NB (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **count:**  Type: integer 
           - **items:**  [Type: object] 
           - **tenant_id:**  Type: string 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/bulk_config_state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_correlationevents_query(self, data, api_version="v2.0"):
        """
        POST Site_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_deviceidconfigs(self, site_id, data, api_version="v2.1"):
        """
        POST Deviceidconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs".format(api_version,
                                                                              site_id)

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

    def site_extensions_query(self, site_id, data, api_version="v2.0"):
        """
        Query site level extensions that match query params (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/extensions/query".format(api_version,
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

    def site_lannetworks_query(self, site_id, data, api_version="v3.3"):
        """
        Query LAN networks that match query params (v3.3)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/lannetworks/query".format(api_version,
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

    def site_operations(self, site_id, data, api_version="v2.0"):
        """
        POST Site_Operations API Function

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

    def site_query(self, data, api_version="v4.12"):
        """
        Queries db for limit number of sites that match query params. (v4.12)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.12)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_sitesecurityzones_query(self, site_id, data, api_version="v2.0"):
        """
        Query security zone for NB API. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/sitesecurityzones/query".format(api_version,
                                                                                      site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_spokeclusters_query(self, site_id, data, api_version="v2.0"):
        """
        Query Spoke Clusters. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/query".format(api_version,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sites(self, data, api_version="v4.12"):
        """
        Create a site (v4.12)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v4.12)

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

    def sitesecurityzones_query(self, data, api_version="v2.0"):
        """
        Query security zone. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **networks:**           
               - **network_id:**  Type: string 
               - **network_type:**  Type: string 
           - **site_id:**  Type: string 
           - **zone_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sitesecurityzones/query".format(api_version)

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

    def snmpdiscoverystartnodes_query(self, data, api_version="v2.0"):
        """
        Query Start Network Node based on parameters (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/snmpdiscoverystartnodes/query".format(api_version)

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

    def software_current_status_query(self, data, api_version="v2.1"):
        """
        Get the current image status of all the element (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **active_image_id:**  Type: string 
           - **active_version:**  Type: string 
           - **download_interval:**  Type: integer 
           - **download_percent:**  Type: integer 
           - **element_id:**  Type: string 
           - **failure_info:**  Type: string 
           - **previous_image_id:**  Type: string 
           - **rollback_version:**  Type: string 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 
           - **upgrade_image_id:**  Type: string 
           - **upgrade_interval:**  Type: integer 
           - **upgrade_state:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/software/current_status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def software_state_query(self, data, api_version="v2.0"):
        """
        Query software state for all tenants elements (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **image_id:**  Type: string 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/software/state/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def software_status_query(self, data, api_version="v2.1"):
        """
        Query the software upgrade status of all tenant elements (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **active_image_id:**  Type: string 
           - **active_version:**  Type: string 
           - **download_interval:**  Type: integer 
           - **download_percent:**  Type: integer 
           - **element_id:**  Type: string 
           - **failure_info:**  Type: string 
           - **previous_image_id:**  Type: string 
           - **rollback_version:**  Type: string 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 
           - **upgrade_image_id:**  Type: string 
           - **upgrade_interval:**  Type: integer 
           - **upgrade_state:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/software/status/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def softwarehistory_query(self, data, api_version="v2.0"):
        """
        Queries db for all software download done by a tenant (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/softwarehistory/query".format(api_version)

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

    def spokeclusters_operations(self, site_id, spokecluster_id, data, api_version="v2.0"):
        """
        Handle operations on spokecluster. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/{}/operations".format(api_version,
                                                                                          site_id,
                                                                                          spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def spokeclusters_query(self, data, api_version="v2.0"):
        """
        Query Spoke Clusters. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **advertisement_interval:**  Type: number 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **preempt:**  Type: boolean 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/spokeclusters/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def spokeclusters_status_query(self, data, api_version="v2.0"):
        """
        POST Spokeclusters_Status_Query API Function

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

    def status_query(self, data, api_version="v2.5"):
        """
        Query and get element status objects for a tenant (v2.5)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/status/query".format(api_version)

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

    def syslogserverprofiles(self, data, api_version="v2.0"):
        """
        Create Syslog Server Profile (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_flow_logging:**  Type: boolean 
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

    def syslogservers(self, site_id, element_id, data, api_version="v2.2"):
        """
        Create Syslog Server (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_flow_logging:**  Type: boolean 
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
        POST Tacacs_Plus_Profiles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/tacacs_plus_profiles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tacacs_plus_servers(self, site_id, element_id, data, api_version="v2.0"):
        """
        POST Tacacs_Plus_Servers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


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

    def tenant_bgppeers_query(self, data, api_version="v2.6"):
        """
        Queries db for BGP peers that match query params. (v2.6)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/bgppeers/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_element_operations(self, element_id, data, api_version="v2.0"):
        """
        Handle operations on element. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/operations".format(api_version,
                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_extensions_query(self, data, api_version="v2.0"):
        """
        Queries db for limit number of tenant extensions that match the query params. (v2.0)

          **Parameters:**:

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

        url = str(cur_ctlr) + "/sdwan/{}/api/extensions/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_forgot_password_login(self, data, api_version="v2.0"):
        """
        Forgot password API (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **email:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/login/password/forgot".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

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

    def tenant_machine_operations(self, machine_id, data, api_version="v2.5"):
        """
        Update a specific machine of a tenant using operations (v2.5)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 

           - **connected:**  Type: boolean 
           - **console_conf_passphrase:**  Type: string 
           - **element_shell_id:**  Type: string 
           - **em_element_id:**  Type: string 
           - **esp_tenant_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **image_version:**  Type: string 
           - **inventory_op:**  Type: string 
           - **is_eval:**  Type: string 
           - **machine_state:**  Type: string 
           - **manufacture_id:**  Type: string 
           - **model_name:**  Type: string 
           - **ordering_info:**  Type: string 
           - **owner_tenant_id:**  Type: string 
           - **pki_op:**           
               - **ca_list:**  [Type: string] 
               - **operation:**  Type: string 
           - **renew_state:**  Type: string 
           - **sales_order_number:**  Type: string 
           - **ship_state:**  Type: string 
           - **sl_no:**  Type: string 
           - **suspend_state:**  Type: string 
           - **tenant_id:**  Type: string 
           - **token:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/operations".format(api_version,
                                                                            machine_id)

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

    def tenant_prefixfilters_query(self, data, api_version="v2.0"):
        """
        Query security prefix filter for NB API. (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **filters:**           
               - **type:**  Type: string 
           - **prefix_filter_id:**  Type: string 
           - **site_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prefixfilters/query".format(api_version)

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

    def tenant_waninterfaces_query(self, data, api_version="v2.10"):
        """
        Query db for Site WAN interfaces that match query parameters (v2.10)

          **Parameters:**:

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
           - **site_id:**  Type: string 
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

        url = str(cur_ctlr) + "/sdwan/{}/api/waninterfaces/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenants_certificates(self, data, api_version="v2.0"):
        """
        POST Tenants_Certificates API Function

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

    def toolkitsessions_query(self, data, api_version="v2.0"):
        """
        POST Toolkitsessions_Query API Function

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

    def upgrade_status_query(self, data, api_version="v2.0"):
        """
        Query Machine Upgrade Status (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/upgrade_status/query".format(api_version)

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

    def useridagents_query(self, data, api_version="v2.0"):
        """
        Query User ID Agents. (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/useridagents/query".format(api_version)

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

    def vff_token_query(self, data, api_version="v2.0"):
        """
        Query Tenant Vff License Tokens (v2.0)

          **Parameters:**:

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

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/tokens/query".format(api_version)

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

    def vfflicenses_operations(self, vfflicense_id, data, api_version="v2.0"):
        """
        Vff operation (v2.0)

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **allocated_ions:**  Type: integer 
           - **allowed_ions:**  Type: integer 
           - **model:**  Type: string 
           - **source_license_id:**  Type: string 
           - **source_tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}/operations".format(api_version,
                                                                               vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vfflicenses_rquery(self, data, api_version="v2.0"):
        """
        Query and get Vff License (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/rquery".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vfflicensesstatus_rquery(self, data, api_version="v2.0"):
        """
        Query and get Vff License State (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicensesstatus/rquery".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vpnlinks_operations(self, vpnlink_id, data, api_version="v2.0"):
        """
        Perform an operation on a VPN link (v2.0)

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vpnlinks/{}/operations".format(api_version,
                                                                            vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vpnlinks_query(self, data, api_version="v2.0"):
        """
        Query db for VPNLinks that match query parameters (v2.0)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vpnlinks/query".format(api_version)

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

    def vrfcontextprofiles_query(self, data, api_version="v2.0"):
        """
        Query VRF Context Profiles (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontextprofiles/query".format(api_version)

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

    def vrfcontexts_query(self, data, api_version="v2.0"):
        """
        Query VRF Contexts (v2.0)

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

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontexts/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def waninterfacelabels_query(self, data, api_version="v2.6"):
        """
        Query db for site WAN interfaces that match query parameters (v2.6)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 

           - **app_acceleration_enabled:**  Type: boolean 
           - **bwc_enabled:**  Type: boolean 
           - **description:**  Type: string 
           - **l3_reachability:**           
               - **probe_config_ids:**  [Type: string] 
               - **use_element_default:**  Type: boolean 
           - **label:**  Type: string 
           - **lqm_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **probe_profile_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **use_for_application_reachability_probes:**  Type: boolean 
           - **use_for_controller_connections:**  Type: boolean 
           - **use_lqm_for_non_hub_paths:**  Type: boolean 
           - **vpnlink_configuration:**           
               - **keep_alive_failure_count:**  Type: integer 
               - **keep_alive_interval:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/waninterfacelabels/query".format(api_version)

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

    def waninterfaces_correlationevents_query(self, data, api_version="v2.0"):
        """
        POST Waninterfaces_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/waninterfaces/correlationevents/query".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def waninterfaces_query(self, site_id, data, api_version="v2.5"):
        """
        Query db for Site WAN interfaces that match query parameters (v2.5)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.5)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces/query".format(api_version,
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

    def wannetworks_query(self, data, api_version="v2.1"):
        """
        Query db for WAN networks that match query parameters (v2.1)

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.1)

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
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wannetworks/query".format(api_version)

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

    def ws_extensions_query(self, data, api_version="v2.0"):
        """
        POST Ws_Extensions_Query API Function

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

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    aaa_client_metrics_monitor = monitor_aaa_client_metrics
    """ Backwards-compatibility alias of `aaa_client_metrics_monitor` to `monitor_aaa_client_metrics`"""

    aaa_metrics_monitor = monitor_aaa_metrics
    """ Backwards-compatibility alias of `aaa_metrics_monitor` to `monitor_aaa_metrics`"""

    access_elementusers = elementusers_access
    """ Backwards-compatibility alias of `access_elementusers` to `elementusers_access`"""

    agg_bw_stats_monitor = monitor_agg_bw_stats
    """ Backwards-compatibility alias of `agg_bw_stats_monitor` to `monitor_agg_bw_stats`"""

    aggregates_aiops_monitor = monitor_aiops_aggregates
    """ Backwards-compatibility alias of `aggregates_aiops_monitor` to `monitor_aiops_aggregates`"""

    aggregates_monitor = monitor_aggregates
    """ Backwards-compatibility alias of `aggregates_monitor` to `monitor_aggregates`"""

    allocate_to_shell = machines_allocate_to_shell
    """ Backwards-compatibility alias of `allocate_to_shell` to `machines_allocate_to_shell`"""

    anomaly_aiops_monitor = monitor_aiops_anomaly
    """ Backwards-compatibility alias of `anomaly_aiops_monitor` to `monitor_aiops_anomaly`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    app_acceleration_monitor = monitor_app_acceleration
    """ Backwards-compatibility alias of `app_acceleration_monitor` to `monitor_app_acceleration`"""

    bulk_metrics_monitor = monitor_bulk_metrics
    """ Backwards-compatibility alias of `bulk_metrics_monitor` to `monitor_bulk_metrics`"""

    bulkdelete_snmpdiscoverystartnodes_deviceidconfigs = deviceidconfigs_bulkdelete_snmpdiscoverystartnodes
    """ Backwards-compatibility alias of `bulkdelete_snmpdiscoverystartnodes_deviceidconfigs` to `deviceidconfigs_bulkdelete_snmpdiscoverystartnodes`"""

    bulkoperations_anynetlinks = anynetlinks_bulkoperations
    """ Backwards-compatibility alias of `bulkoperations_anynetlinks` to `anynetlinks_bulkoperations`"""

    cellular_metrics_monitor = monitor_cellular_metrics
    """ Backwards-compatibility alias of `cellular_metrics_monitor` to `monitor_cellular_metrics`"""

    certificates_tenants = tenants_certificates
    """ Backwards-compatibility alias of `certificates_tenants` to `tenants_certificates`"""

    change_password = password_change
    """ Backwards-compatibility alias of `change_password` to `password_change`"""

    clone_sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates_clone
    """ Backwards-compatibility alias of `clone_sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates_clone`"""

    configs_prismasase_connections = prismasase_connections_configs
    """ Backwards-compatibility alias of `configs_prismasase_connections` to `prismasase_connections_configs`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    copy_element_configurations_elementshells = elementshells_copy_element_configurations
    """ Backwards-compatibility alias of `copy_element_configurations_elementshells` to `elementshells_copy_element_configurations`"""

    deltasync_directoryservices = directoryservices_deltasync
    """ Backwards-compatibility alias of `deltasync_directoryservices` to `directoryservices_deltasync`"""

    deployments_sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates_deployments
    """ Backwards-compatibility alias of `deployments_sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates_deployments`"""

    deviceidconfigs = site_deviceidconfigs
    """ Backwards-compatibility alias of `deviceidconfigs` to `site_deviceidconfigs`"""

    deviceidconfigs_i = element_deviceidconfigs
    """ Backwards-compatibility alias of `deviceidconfigs_i` to `element_deviceidconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    flows_monitor = monitor_flows
    """ Backwards-compatibility alias of `flows_monitor` to `monitor_flows`"""

    forecast_aiops_monitor = monitor_aiops_forecast
    """ Backwards-compatibility alias of `forecast_aiops_monitor` to `monitor_aiops_forecast`"""

    forgot_password_login_t = tenant_forgot_password_login
    """ Backwards-compatibility alias of `forgot_password_login_t` to `tenant_forgot_password_login`"""

    health_aiops_monitor = monitor_aiops_health
    """ Backwards-compatibility alias of `health_aiops_monitor` to `monitor_aiops_health`"""

    healthscore_aggregates_monitor = monitor_aggregates_healthscore
    """ Backwards-compatibility alias of `healthscore_aggregates_monitor` to `monitor_aggregates_healthscore`"""

    insights_monitor = monitor_insights
    """ Backwards-compatibility alias of `insights_monitor` to `monitor_insights`"""

    insightslist_monitor = monitor_insightslist
    """ Backwards-compatibility alias of `insightslist_monitor` to `monitor_insightslist`"""

    interfaces_elementshells = elementshells_interfaces
    """ Backwards-compatibility alias of `interfaces_elementshells` to `elementshells_interfaces`"""

    ipfixlocalprefixes_s = site_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_s` to `site_ipfixlocalprefixes`"""

    ipfixlocalprefixes_t = tenant_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_t` to `tenant_ipfixlocalprefixes`"""

    login_clients = clients_login
    """ Backwards-compatibility alias of `login_clients` to `clients_login`"""

    logout_clients = clients_logout
    """ Backwards-compatibility alias of `logout_clients` to `clients_logout`"""

    lqm_point_metrics_monitor = monitor_lqm_point_metrics
    """ Backwards-compatibility alias of `lqm_point_metrics_monitor` to `monitor_lqm_point_metrics`"""

    metrics_monitor = monitor_metrics
    """ Backwards-compatibility alias of `metrics_monitor` to `monitor_metrics`"""

    mroute_multicast_aggregates_monitor = monitor_aggregates_multicast_mroute
    """ Backwards-compatibility alias of `mroute_multicast_aggregates_monitor` to `monitor_aggregates_multicast_mroute`"""

    natlocalprefixes_s = site_natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_s` to `site_natlocalprefixes`"""

    natlocalprefixes_t = natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_t` to `natlocalprefixes`"""

    network_point_metrics_bw_monitor = monitor_network_point_metrics_bw
    """ Backwards-compatibility alias of `network_point_metrics_bw_monitor` to `monitor_network_point_metrics_bw`"""

    network_point_metrics_hs_monitor = monitor_network_point_metrics_hs
    """ Backwards-compatibility alias of `network_point_metrics_hs_monitor` to `monitor_network_point_metrics_hs`"""

    network_point_metrics_monitor = monitor_network_point_metrics
    """ Backwards-compatibility alias of `network_point_metrics_monitor` to `monitor_network_point_metrics`"""

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

    object_stats_aiops_monitor = monitor_aiops_object_stats
    """ Backwards-compatibility alias of `object_stats_aiops_monitor` to `monitor_aiops_object_stats`"""

    object_stats_monitor = monitor_object_stats
    """ Backwards-compatibility alias of `object_stats_monitor` to `monitor_object_stats`"""

    operations_e = tenant_element_operations
    """ Backwards-compatibility alias of `operations_e` to `tenant_element_operations`"""

    operations_h = hubclusters_operations
    """ Backwards-compatibility alias of `operations_h` to `hubclusters_operations`"""

    operations_s = site_operations
    """ Backwards-compatibility alias of `operations_s` to `site_operations`"""

    operations_t = tenant_machine_operations
    """ Backwards-compatibility alias of `operations_t` to `tenant_machine_operations`"""

    ops_bgppeers = bgppeers_operations
    """ Backwards-compatibility alias of `ops_bgppeers` to `bgppeers_operations`"""

    ops_deviceidprofiles = deviceidprofiles_operations
    """ Backwards-compatibility alias of `ops_deviceidprofiles` to `deviceidprofiles_operations`"""

    ops_events = events_operations
    """ Backwards-compatibility alias of `ops_events` to `events_operations`"""

    ops_interfaces = interfaces_operations
    """ Backwards-compatibility alias of `ops_interfaces` to `interfaces_operations`"""

    ops_spokeclusters = spokeclusters_operations
    """ Backwards-compatibility alias of `ops_spokeclusters` to `spokeclusters_operations`"""

    ops_vfflicenses = vfflicenses_operations
    """ Backwards-compatibility alias of `ops_vfflicenses` to `vfflicenses_operations`"""

    ops_vpnlinks = vpnlinks_operations
    """ Backwards-compatibility alias of `ops_vpnlinks` to `vpnlinks_operations`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    perfmgmtpolicyrules_perfmgmtpolicysets = perfmgmtpolicysets_perfmgmtpolicyrules
    """ Backwards-compatibility alias of `perfmgmtpolicyrules_perfmgmtpolicysets` to `perfmgmtpolicysets_perfmgmtpolicyrules`"""

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

    qos_application_aggregates_monitor = monitor_aggregates_application_qos
    """ Backwards-compatibility alias of `qos_application_aggregates_monitor` to `monitor_aggregates_application_qos`"""

    qos_metrics_application_monitor = monitor_application_qos_metrics
    """ Backwards-compatibility alias of `qos_metrics_application_monitor` to `monitor_application_qos_metrics`"""

    qos_metrics_monitor = monitor_qos_metrics
    """ Backwards-compatibility alias of `qos_metrics_monitor` to `monitor_qos_metrics`"""

    query_activeuserips = activeuserips_query
    """ Backwards-compatibility alias of `query_activeuserips` to `activeuserips_query`"""

    query_aggregatebandwidth_monitor = monitor_aggregatebandwidth_query
    """ Backwards-compatibility alias of `query_aggregatebandwidth_monitor` to `monitor_aggregatebandwidth_query`"""

    query_anynetlinks = anynetlinks_query
    """ Backwards-compatibility alias of `query_anynetlinks` to `anynetlinks_query`"""

    query_apnprofiles = apnprofiles_query
    """ Backwards-compatibility alias of `query_apnprofiles` to `apnprofiles_query`"""

    query_appacceleration = appacceleration_query
    """ Backwards-compatibility alias of `query_appacceleration` to `appacceleration_query`"""

    query_appdefs = appdefs_query
    """ Backwards-compatibility alias of `query_appdefs` to `appdefs_query`"""

    query_applicationstats_monitor = monitor_applicationstats_query
    """ Backwards-compatibility alias of `query_applicationstats_monitor` to `monitor_applicationstats_query`"""

    query_applicationsummary_monitor = monitor_applicationsummary_query
    """ Backwards-compatibility alias of `query_applicationsummary_monitor` to `monitor_applicationsummary_query`"""

    query_auditlog = auditlog_query
    """ Backwards-compatibility alias of `query_auditlog` to `auditlog_query`"""

    query_bgppeers = bgppeers_query
    """ Backwards-compatibility alias of `query_bgppeers` to `bgppeers_query`"""

    query_bgppeers_t = tenant_bgppeers_query
    """ Backwards-compatibility alias of `query_bgppeers_t` to `tenant_bgppeers_query`"""

    query_bulk_config_state_e = element_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_e` to `element_bulk_config_state_query`"""

    query_bulk_config_state_networks = networks_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_networks` to `networks_bulk_config_state_query`"""

    query_bulk_config_state_policysets = policysets_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_policysets` to `policysets_bulk_config_state_query`"""

    query_bulk_config_state_s = site_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_s` to `site_bulk_config_state_query`"""

    query_cellular_modules = cellular_modules_query
    """ Backwards-compatibility alias of `query_cellular_modules` to `cellular_modules_query`"""

    query_clients = clients_query
    """ Backwards-compatibility alias of `query_clients` to `clients_query`"""

    query_correlationevents_anynetlinks = anynetlinks_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_anynetlinks` to `anynetlinks_correlationevents_query`"""

    query_correlationevents_e = element_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_e` to `element_correlationevents_query`"""

    query_correlationevents_interfaces = interfaces_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_interfaces` to `interfaces_correlationevents_query`"""

    query_correlationevents_s = site_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_s` to `site_correlationevents_query`"""

    query_correlationevents_waninterfaces = waninterfaces_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_waninterfaces` to `waninterfaces_correlationevents_query`"""

    query_current_status_software = software_current_status_query
    """ Backwards-compatibility alias of `query_current_status_software` to `software_current_status_query`"""

    query_demsiteconfigs = demsiteconfigs_query
    """ Backwards-compatibility alias of `query_demsiteconfigs` to `demsiteconfigs_query`"""

    query_demstatus = demstatus_query
    """ Backwards-compatibility alias of `query_demstatus` to `demstatus_query`"""

    query_deployments_sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates_deployments_query
    """ Backwards-compatibility alias of `query_deployments_sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates_deployments_query`"""

    query_deviceidconfigs = deviceidconfigs_query
    """ Backwards-compatibility alias of `query_deviceidconfigs` to `deviceidconfigs_query`"""

    query_directoryusergroups = directoryusergroups_query
    """ Backwards-compatibility alias of `query_directoryusergroups` to `directoryusergroups_query`"""

    query_directoryusers = directoryusers_query
    """ Backwards-compatibility alias of `query_directoryusers` to `directoryusers_query`"""

    query_dnsserviceprofiles = dnsserviceprofiles_query
    """ Backwards-compatibility alias of `query_dnsserviceprofiles` to `dnsserviceprofiles_query`"""

    query_dnsserviceroles = dnsserviceroles_query
    """ Backwards-compatibility alias of `query_dnsserviceroles` to `dnsserviceroles_query`"""

    query_dnsservices = dnsservices_query
    """ Backwards-compatibility alias of `query_dnsservices` to `dnsservices_query`"""

    query_e = element_query
    """ Backwards-compatibility alias of `query_e` to `element_query`"""

    query_elementsecurityzones = elementsecurityzones_query
    """ Backwards-compatibility alias of `query_elementsecurityzones` to `elementsecurityzones_query`"""

    query_elementshells = elementshells_query
    """ Backwards-compatibility alias of `query_elementshells` to `elementshells_query`"""

    query_eventcorrelationpolicyrules = eventcorrelationpolicyrules_query
    """ Backwards-compatibility alias of `query_eventcorrelationpolicyrules` to `eventcorrelationpolicyrules_query`"""

    query_eventcorrelationpolicysets = eventcorrelationpolicysets_query
    """ Backwards-compatibility alias of `query_eventcorrelationpolicysets` to `eventcorrelationpolicysets_query`"""

    query_events = events_query
    """ Backwards-compatibility alias of `query_events` to `events_query`"""

    query_extensions_i = element_extensions_query
    """ Backwards-compatibility alias of `query_extensions_i` to `element_extensions_query`"""

    query_extensions_s = site_extensions_query
    """ Backwards-compatibility alias of `query_extensions_s` to `site_extensions_query`"""

    query_extensions_t = tenant_extensions_query
    """ Backwards-compatibility alias of `query_extensions_t` to `tenant_extensions_query`"""

    query_extensions_ws = ws_extensions_query
    """ Backwards-compatibility alias of `query_extensions_ws` to `ws_extensions_query`"""

    query_globalprefixfilters = globalprefixfilters_query
    """ Backwards-compatibility alias of `query_globalprefixfilters` to `globalprefixfilters_query`"""

    query_h = hubclusters_query
    """ Backwards-compatibility alias of `query_h` to `hubclusters_query`"""

    query_interfaces = interfaces_query
    """ Backwards-compatibility alias of `query_interfaces` to `interfaces_query`"""

    query_iotdevicemappings = iotdevicemappings_query
    """ Backwards-compatibility alias of `query_iotdevicemappings` to `iotdevicemappings_query`"""

    query_iotdictionary = iotdictionary_query
    """ Backwards-compatibility alias of `query_iotdictionary` to `iotdictionary_query`"""

    query_ipfix = ipfix_query
    """ Backwards-compatibility alias of `query_ipfix` to `ipfix_query`"""

    query_ipfixcollectorcontexts = ipfixcollectorcontexts_query
    """ Backwards-compatibility alias of `query_ipfixcollectorcontexts` to `ipfixcollectorcontexts_query`"""

    query_ipfixfiltercontexts = ipfixfiltercontexts_query
    """ Backwards-compatibility alias of `query_ipfixfiltercontexts` to `ipfixfiltercontexts_query`"""

    query_ipfixglobalprefixes = ipfixglobalprefixes_query
    """ Backwards-compatibility alias of `query_ipfixglobalprefixes` to `ipfixglobalprefixes_query`"""

    query_ipfixlocalprefixes = ipfixlocalprefixes_query
    """ Backwards-compatibility alias of `query_ipfixlocalprefixes` to `ipfixlocalprefixes_query`"""

    query_ipfixprofiles = ipfixprofiles_query
    """ Backwards-compatibility alias of `query_ipfixprofiles` to `ipfixprofiles_query`"""

    query_ipfixtemplates = ipfixtemplates_query
    """ Backwards-compatibility alias of `query_ipfixtemplates` to `ipfixtemplates_query`"""

    query_ipsecprofiles = ipsecprofiles_query
    """ Backwards-compatibility alias of `query_ipsecprofiles` to `ipsecprofiles_query`"""

    query_lannetworks = site_lannetworks_query
    """ Backwards-compatibility alias of `query_lannetworks` to `site_lannetworks_query`"""

    query_lannetworks_t = lannetworks_query
    """ Backwards-compatibility alias of `query_lannetworks_t` to `lannetworks_query`"""

    query_localprefixfilters = localprefixfilters_query
    """ Backwards-compatibility alias of `query_localprefixfilters` to `localprefixfilters_query`"""

    query_m = machines_query
    """ Backwards-compatibility alias of `query_m` to `machines_query`"""

    query_machine_upgrade = machine_upgrade_query
    """ Backwards-compatibility alias of `query_machine_upgrade` to `machine_upgrade_query`"""

    query_machines_c = clients_machines_query
    """ Backwards-compatibility alias of `query_machines_c` to `clients_machines_query`"""

    query_mstp_instances = mstp_instances_query
    """ Backwards-compatibility alias of `query_mstp_instances` to `mstp_instances_query`"""

    query_multicastdynamicrps = multicastdynamicrps_query
    """ Backwards-compatibility alias of `query_multicastdynamicrps` to `multicastdynamicrps_query`"""

    query_multicastigmpmemberships = multicastigmpmemberships_query
    """ Backwards-compatibility alias of `query_multicastigmpmemberships` to `multicastigmpmemberships_query`"""

    query_multicastroutes = multicastroutes_query
    """ Backwards-compatibility alias of `query_multicastroutes` to `multicastroutes_query`"""

    query_multicastrps = multicastrps_query
    """ Backwards-compatibility alias of `query_multicastrps` to `multicastrps_query`"""

    query_multicastsourcesiderps = multicastsourcesiderps_query
    """ Backwards-compatibility alias of `query_multicastsourcesiderps` to `multicastsourcesiderps_query`"""

    query_multicaststatus = multicaststatus_query
    """ Backwards-compatibility alias of `query_multicaststatus` to `multicaststatus_query`"""

    query_multicastwanstatus = multicastwanstatus_query
    """ Backwards-compatibility alias of `query_multicastwanstatus` to `multicastwanstatus_query`"""

    query_natglobalprefixes = natglobalprefixes_query
    """ Backwards-compatibility alias of `query_natglobalprefixes` to `natglobalprefixes_query`"""

    query_natlocalprefixes = natlocalprefixes_query
    """ Backwards-compatibility alias of `query_natlocalprefixes` to `natlocalprefixes_query`"""

    query_natpolicypools = natpolicypools_query
    """ Backwards-compatibility alias of `query_natpolicypools` to `natpolicypools_query`"""

    query_natpolicyrules = natpolicyrules_query
    """ Backwards-compatibility alias of `query_natpolicyrules` to `natpolicyrules_query`"""

    query_natpolicysets = natpolicysets_query
    """ Backwards-compatibility alias of `query_natpolicysets` to `natpolicysets_query`"""

    query_natpolicysetstacks = natpolicysetstacks_query
    """ Backwards-compatibility alias of `query_natpolicysetstacks` to `natpolicysetstacks_query`"""

    query_natzones = natzones_query
    """ Backwards-compatibility alias of `query_natzones` to `natzones_query`"""

    query_networkcontexts = networkcontexts_query
    """ Backwards-compatibility alias of `query_networkcontexts` to `networkcontexts_query`"""

    query_networkpolicyglobalprefixes = networkpolicyglobalprefixes_query
    """ Backwards-compatibility alias of `query_networkpolicyglobalprefixes` to `networkpolicyglobalprefixes_query`"""

    query_networkpolicylocalprefixes = networkpolicylocalprefixes_query
    """ Backwards-compatibility alias of `query_networkpolicylocalprefixes` to `networkpolicylocalprefixes_query`"""

    query_networkpolicyrules = networkpolicyrules_query
    """ Backwards-compatibility alias of `query_networkpolicyrules` to `networkpolicyrules_query`"""

    query_networkpolicysets = networkpolicysets_query
    """ Backwards-compatibility alias of `query_networkpolicysets` to `networkpolicysets_query`"""

    query_networkpolicysetstacks = networkpolicysetstacks_query
    """ Backwards-compatibility alias of `query_networkpolicysetstacks` to `networkpolicysetstacks_query`"""

    query_ngfwsecuritypolicyglobalprefixes = ngfwsecuritypolicyglobalprefixes_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicyglobalprefixes` to `ngfwsecuritypolicyglobalprefixes_query`"""

    query_ngfwsecuritypolicylocalprefixes = ngfwsecuritypolicylocalprefixes_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicylocalprefixes` to `ngfwsecuritypolicylocalprefixes_query`"""

    query_ngfwsecuritypolicyrules = ngfwsecuritypolicyrules_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicyrules` to `ngfwsecuritypolicyrules_query`"""

    query_ngfwsecuritypolicysets = ngfwsecuritypolicysets_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicysets` to `ngfwsecuritypolicysets_query`"""

    query_ngfwsecuritypolicysetstacks = ngfwsecuritypolicysetstacks_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicysetstacks` to `ngfwsecuritypolicysetstacks_query`"""

    query_ospfconfigs = ospfconfigs_query 
    """ Backwards-compatibility alias of `query_ospfconfigs` to `ospfconfigs_query `"""

    query_ospfdiscoveredneighbors = ospfdiscoveredneighbors_query
    """ Backwards-compatibility alias of `query_ospfdiscoveredneighbors` to `ospfdiscoveredneighbors_query`"""

    query_ospfreachableprefixes = ospfreachableprefixes_query
    """ Backwards-compatibility alias of `query_ospfreachableprefixes` to `ospfreachableprefixes_query`"""

    query_pathgroups = pathgroups_query
    """ Backwards-compatibility alias of `query_pathgroups` to `pathgroups_query`"""

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

    query_policyrules = policyrules_query
    """ Backwards-compatibility alias of `query_policyrules` to `policyrules_query`"""

    query_policysets = policysets_query
    """ Backwards-compatibility alias of `query_policysets` to `policysets_query`"""

    query_prefixes = prefixes_query
    """ Backwards-compatibility alias of `query_prefixes` to `prefixes_query`"""

    query_prefixfilters = prefixfilters_query
    """ Backwards-compatibility alias of `query_prefixfilters` to `prefixfilters_query`"""

    query_prefixfilters_t = tenant_prefixfilters_query
    """ Backwards-compatibility alias of `query_prefixfilters_t` to `tenant_prefixfilters_query`"""

    query_prioritypolicyglobalprefixes = prioritypolicyglobalprefixes_query
    """ Backwards-compatibility alias of `query_prioritypolicyglobalprefixes` to `prioritypolicyglobalprefixes_query`"""

    query_prioritypolicylocalprefixes = prioritypolicylocalprefixes_query
    """ Backwards-compatibility alias of `query_prioritypolicylocalprefixes` to `prioritypolicylocalprefixes_query`"""

    query_prioritypolicyrules = prioritypolicyrules_query
    """ Backwards-compatibility alias of `query_prioritypolicyrules` to `prioritypolicyrules_query`"""

    query_prioritypolicysets = prioritypolicysets_query
    """ Backwards-compatibility alias of `query_prioritypolicysets` to `prioritypolicysets_query`"""

    query_prioritypolicysetstacks = prioritypolicysetstacks_query
    """ Backwards-compatibility alias of `query_prioritypolicysetstacks` to `prioritypolicysetstacks_query`"""

    query_prismaaccess_configs = prismaaccess_configs_query
    """ Backwards-compatibility alias of `query_prismaaccess_configs` to `prismaaccess_configs_query`"""

    query_probeconfigs = probeconfigs_query
    """ Backwards-compatibility alias of `query_probeconfigs` to `probeconfigs_query`"""

    query_probeprofiles = probeprofiles_query
    """ Backwards-compatibility alias of `query_probeprofiles` to `probeprofiles_query`"""

    query_reports = reports_query
    """ Backwards-compatibility alias of `query_reports` to `reports_query`"""

    query_reportsdir = reportsdir_query
    """ Backwards-compatibility alias of `query_reportsdir` to `reportsdir_query`"""

    query_routing_aspathaccesslists = routing_aspathaccesslists_query
    """ Backwards-compatibility alias of `query_routing_aspathaccesslists` to `routing_aspathaccesslists_query`"""

    query_routing_ipcommunitylists = routing_ipcommunitylists_query
    """ Backwards-compatibility alias of `query_routing_ipcommunitylists` to `routing_ipcommunitylists_query`"""

    query_routing_prefixlists = routing_prefixlists_query
    """ Backwards-compatibility alias of `query_routing_prefixlists` to `routing_prefixlists_query`"""

    query_routing_routemaps = routing_routemaps_query
    """ Backwards-compatibility alias of `query_routing_routemaps` to `routing_routemaps_query`"""

    query_s = site_query
    """ Backwards-compatibility alias of `query_s` to `site_query`"""

    query_securitypolicyrules = securitypolicyrules_query
    """ Backwards-compatibility alias of `query_securitypolicyrules` to `securitypolicyrules_query`"""

    query_securitypolicysets = securitypolicysets_query
    """ Backwards-compatibility alias of `query_securitypolicysets` to `securitypolicysets_query`"""

    query_securityzones = securityzones_query
    """ Backwards-compatibility alias of `query_securityzones` to `securityzones_query`"""

    query_servicebindingmaps = servicebindingmaps_query
    """ Backwards-compatibility alias of `query_servicebindingmaps` to `servicebindingmaps_query`"""

    query_serviceendpoints = serviceendpoints_query
    """ Backwards-compatibility alias of `query_serviceendpoints` to `serviceendpoints_query`"""

    query_servicelabels = servicelabels_query
    """ Backwards-compatibility alias of `query_servicelabels` to `servicelabels_query`"""

    query_sitesecurityzones = site_sitesecurityzones_query
    """ Backwards-compatibility alias of `query_sitesecurityzones` to `site_sitesecurityzones_query`"""

    query_sitesecurityzones_t = sitesecurityzones_query
    """ Backwards-compatibility alias of `query_sitesecurityzones_t` to `sitesecurityzones_query`"""

    query_sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates_query
    """ Backwards-compatibility alias of `query_sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates_query`"""

    query_snmpdiscoverystartnodes = snmpdiscoverystartnodes_query
    """ Backwards-compatibility alias of `query_snmpdiscoverystartnodes` to `snmpdiscoverystartnodes_query`"""

    query_softwarehistory = softwarehistory_query
    """ Backwards-compatibility alias of `query_softwarehistory` to `softwarehistory_query`"""

    query_spokeclusters = site_spokeclusters_query
    """ Backwards-compatibility alias of `query_spokeclusters` to `site_spokeclusters_query`"""

    query_spokeclusters_t = spokeclusters_query
    """ Backwards-compatibility alias of `query_spokeclusters_t` to `spokeclusters_query`"""

    query_state_software = software_state_query
    """ Backwards-compatibility alias of `query_state_software` to `software_state_query`"""

    query_status = status_query
    """ Backwards-compatibility alias of `query_status` to `status_query`"""

    query_status_bgppeers = bgppeers_status_query
    """ Backwards-compatibility alias of `query_status_bgppeers` to `bgppeers_status_query`"""

    query_status_cellular_module_firmware = cellular_module_firmware_status_query
    """ Backwards-compatibility alias of `query_status_cellular_module_firmware` to `cellular_module_firmware_status_query`"""

    query_status_cellular_modules = cellular_modules_status_query
    """ Backwards-compatibility alias of `query_status_cellular_modules` to `cellular_modules_status_query`"""

    query_status_interfaces = interfaces_status_query
    """ Backwards-compatibility alias of `query_status_interfaces` to `interfaces_status_query`"""

    query_status_prismasase_connections = prismasase_connections_status_query
    """ Backwards-compatibility alias of `query_status_prismasase_connections` to `prismasase_connections_status_query`"""

    query_status_software = software_status_query
    """ Backwards-compatibility alias of `query_status_software` to `software_status_query`"""

    query_status_spokeclusters = spokeclusters_status_query
    """ Backwards-compatibility alias of `query_status_spokeclusters` to `spokeclusters_status_query`"""

    query_tokens_vfflicenses = vff_token_query
    """ Backwards-compatibility alias of `query_tokens_vfflicenses` to `vff_token_query`"""

    query_toolkitsessions = toolkitsessions_query
    """ Backwards-compatibility alias of `query_toolkitsessions` to `toolkitsessions_query`"""

    query_topn_traffic_vol_monitor = monitor_topn_traffic_vol_query
    """ Backwards-compatibility alias of `query_topn_traffic_vol_monitor` to `monitor_topn_traffic_vol_query`"""

    query_upgrade_status = upgrade_status_query
    """ Backwards-compatibility alias of `query_upgrade_status` to `upgrade_status_query`"""

    query_useridagents = useridagents_query
    """ Backwards-compatibility alias of `query_useridagents` to `useridagents_query`"""

    query_vpnlinks = vpnlinks_query
    """ Backwards-compatibility alias of `query_vpnlinks` to `vpnlinks_query`"""

    query_vrfcontextprofiles = vrfcontextprofiles_query
    """ Backwards-compatibility alias of `query_vrfcontextprofiles` to `vrfcontextprofiles_query`"""

    query_vrfcontexts = vrfcontexts_query
    """ Backwards-compatibility alias of `query_vrfcontexts` to `vrfcontexts_query`"""

    query_waninterfacelabels = waninterfacelabels_query
    """ Backwards-compatibility alias of `query_waninterfacelabels` to `waninterfacelabels_query`"""

    query_waninterfaces = waninterfaces_query
    """ Backwards-compatibility alias of `query_waninterfaces` to `waninterfaces_query`"""

    query_waninterfaces_t = tenant_waninterfaces_query
    """ Backwards-compatibility alias of `query_waninterfaces_t` to `tenant_waninterfaces_query`"""

    query_wannetworks = wannetworks_query
    """ Backwards-compatibility alias of `query_wannetworks` to `wannetworks_query`"""

    reallocate_clients = clients_reallocate
    """ Backwards-compatibility alias of `reallocate_clients` to `clients_reallocate`"""

    rquery_e = elements_rquery
    """ Backwards-compatibility alias of `rquery_e` to `elements_rquery`"""

    rquery_vfflicenses = vfflicenses_rquery
    """ Backwards-compatibility alias of `rquery_vfflicenses` to `vfflicenses_rquery`"""

    rquery_vfflicensesstatus = vfflicensesstatus_rquery
    """ Backwards-compatibility alias of `rquery_vfflicensesstatus` to `vfflicensesstatus_rquery`"""

    sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates
    """ Backwards-compatibility alias of `sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates`"""

    snmpdiscoverystartnodes_deviceidconfigs = deviceidconfigs_snmpdiscoverystartnodes
    """ Backwards-compatibility alias of `snmpdiscoverystartnodes_deviceidconfigs` to `deviceidconfigs_snmpdiscoverystartnodes`"""

    summary_events = events_summary
    """ Backwards-compatibility alias of `summary_events` to `events_summary`"""

    sync_directoryservices = directoryservices_sync
    """ Backwards-compatibility alias of `sync_directoryservices` to `directoryservices_sync`"""

    sys_metrics_monitor = monitor_sys_metrics
    """ Backwards-compatibility alias of `sys_metrics_monitor` to `monitor_sys_metrics`"""

    sys_point_metrics_monitor = monitor_sys_point_metrics
    """ Backwards-compatibility alias of `sys_point_metrics_monitor` to `monitor_sys_point_metrics`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

    topn_aaa_metrics_monitor = monitor_aaa_metrics_topn
    """ Backwards-compatibility alias of `topn_aaa_metrics_monitor` to `monitor_aaa_metrics_topn`"""

    topn_aiops_monitor = monitor_aiops_topn
    """ Backwards-compatibility alias of `topn_aiops_monitor` to `monitor_aiops_topn`"""

    topn_cellular_metrics_monitor = monitor_cellular_metrics_topn
    """ Backwards-compatibility alias of `topn_cellular_metrics_monitor` to `monitor_cellular_metrics_topn`"""

    topn_monitor = monitor_topn
    """ Backwards-compatibility alias of `topn_monitor` to `monitor_topn`"""

    topn_sys_metrics_monitor = monitor_sys_metrics_topn
    """ Backwards-compatibility alias of `topn_sys_metrics_monitor` to `monitor_sys_metrics_topn`"""

    users_application_monitor = monitor_application_users
    """ Backwards-compatibility alias of `users_application_monitor` to `monitor_application_users`"""

    wan_neighbor_multicast_aggregates_monitor = monitor_aggregates_multicast_wan_neighbor
    """ Backwards-compatibility alias of `wan_neighbor_multicast_aggregates_monitor` to `monitor_aggregates_multicast_wan_neighbor`"""

    elements_bulk_config_state_query = element_bulk_config_state_query
    """ Backwards-compatibility alias of `elements_bulk_config_state_query` to `element_bulk_config_state_query`"""

    elements_query = element_query
    """ Backwards-compatibility alias of `elements_query` to `element_query`"""

    sites_bulk_config_state_query = site_bulk_config_state_query
    """ Backwards-compatibility alias of `sites_bulk_config_state_query` to `site_bulk_config_state_query`"""

    sites_query = site_query
    """ Backwards-compatibility alias of `sites_query` to `site_query`"""

