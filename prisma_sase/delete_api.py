#!/usr/bin/env python
"""
PRISMA SASE Python SDK - DELETE

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


class Delete(object):
    """
    Prisma SASE API - DELETE requests

    Object to handle making Delete requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def apnprofiles(self, apnprofile_id, api_version="v2.0"):
        """
        Delete an APN Profile (v2.0)

          **Parameters:**:

          - **apnprofile_id**: APN Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/apnprofiles/{}".format(api_version,
                                                                    apnprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def appdefs(self, appdef_id, api_version="v2.6"):
        """
        Delete an application definition (v2.6)

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **api_version**: API version to use (default v2.6)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}".format(api_version,
                                                                appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def appdefs_overrides(self, appdef_id, override_id, api_version="v2.3"):
        """
        Delete application definition overrides for system appdef (v2.3)

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: AppDef Override ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}/overrides/{}".format(api_version,
                                                                             appdef_id,
                                                                             override_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def authtokens(self, operator_id, authtoken_id, api_version="v2.1"):
        """
        Delete an auth token (v2.1)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **authtoken_id**: Static AUTH_TOKEN ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/authtokens/{}".format(api_version,
                                                                                operator_id,
                                                                                authtoken_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def bgppeers(self, site_id, element_id, bgppeer_id, api_version="v2.6"):
        """
        Delete BGP Peer config (v2.6)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **api_version**: API version to use (default v2.6)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}".format(api_version,
                                                                                      site_id,
                                                                                      element_id,
                                                                                      bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def bulkconfigurations_sitetemplates(self, sitetemplate_id, api_version="v2.0"):
        """
        delete site profile (v2.0)

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}".format(api_version,
                                                                                         sitetemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def bulkconfigurations_sitetemplates_deployments(self, sitetemplate_id, deployment_id, api_version="v2.0"):
        """
        Delete a deployment (v2.0)

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **deployment_id**: Deployment ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}/deployments/{}".format(api_version,
                                                                                                        sitetemplate_id,
                                                                                                        deployment_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def demsiteconfigs(self, site_id, demsiteconfig_id, api_version="v2.0"):
        """
        Delete Start Network Node config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **demsiteconfig_id**: DEM Site Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/demsiteconfigs/{}".format(api_version,
                                                                                site_id,
                                                                                demsiteconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def deviceidconfigs_snmpdiscoverystartnodes(self, site_id, deviceidconfig_id, snmpdiscoverystartnode_id, api_version="v2.0"):
        """
        Delete Start Network Node config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: Device Id Config ID
          - **snmpdiscoverystartnode_id**: SNMP Discovery Start Node ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}/snmpdiscoverystartnodes/{}".format(api_version,
                                                                                                            site_id,
                                                                                                            deviceidconfig_id,
                                                                                                            snmpdiscoverystartnode_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def deviceidprofiles(self, deviceidprofile_id, api_version="v2.0"):
        """
        Delete device Id profile configuration (v2.0)

          **Parameters:**:

          - **deviceidprofile_id**: Device Id Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/deviceidprofiles/{}".format(api_version,
                                                                         deviceidprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dhcpservers(self, site_id, dhcpserver_id, api_version="v2.3"):
        """
        Delete DHCPServer for a Tenant on a site (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: DHCP Server ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/dhcpservers/{}".format(api_version,
                                                                             site_id,
                                                                             dhcpserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def directoryservices(self, directoryservice_id, api_version="v2.0"):
        """
        Delete Directory Service (v2.0)

          **Parameters:**:

          - **directoryservice_id**: Directory Service ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices/{}".format(api_version,
                                                                          directoryservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dnsserviceprofiles(self, dnsserviceprofile_id, api_version="v2.1"):
        """
        Delete a DNS service profile (v2.1)

          **Parameters:**:

          - **dnsserviceprofile_id**: DNS Service Profile ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceprofiles/{}".format(api_version,
                                                                           dnsserviceprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dnsserviceroles(self, dnsservicerole_id, api_version="v2.0"):
        """
        Delete a DNS service role (v2.0)

          **Parameters:**:

          - **dnsservicerole_id**: DNS Service Role ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceroles/{}".format(api_version,
                                                                        dnsservicerole_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dnsservices(self, site_id, element_id, dnsservice_id, api_version="v2.0"):
        """
        Delete a DNS service config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **dnsservice_id**: DNS Service ID 
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/dnsservices/{}".format(api_version,
                                                                                         site_id,
                                                                                         element_id,
                                                                                         dnsservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def element_deviceidconfigs(self, site_id, element_id, deviceidconfig_id, api_version="v2.0"):
        """
        Delete device id element level (source interface) config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **deviceidconfig_id**: Device Id Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/deviceidconfigs/{}".format(api_version,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def element_extensions(self, site_id, element_id, extension_id, api_version="v2.0"):
        """
        Delete a specific extension associated with an element (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **extension_id**: Extension ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/extensions/{}".format(api_version,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def element_passages(self, element_id, passage_id, api_version="v2.0"):
        """
        DELETE Element_Passages API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **passage_id**: Passage Configuration ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/passages/{}".format(api_version,
                                                                             element_id,
                                                                             passage_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def element_toolkitsessions(self, element_id, toolkitsession_id, api_version="v2.0"):
        """
        DELETE Element_Toolkitsessions API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **toolkitsession_id**: Toolkit Session ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/toolkitsessions/{}".format(api_version,
                                                                                    element_id,
                                                                                    toolkitsession_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementpassageconfigs(self, element_id, elementpassageconfig_id, api_version="v2.0"):
        """
        DELETE Elementpassageconfigs API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementpassageconfig_id**: Element Passage Configuration ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/elementpassageconfigs/{}".format(api_version,
                                                                                          element_id,
                                                                                          elementpassageconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementsecurityzones(self, site_id, element_id, securityzone_id, api_version="v2.0"):
        """
        Delete an existing security zone (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **securityzone_id**: Security Zone (ZBFW) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/securityzones/{}".format(api_version,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementshells(self, site_id, elementshell_id, api_version="v2.1"):
        """
        Delete an element shell (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}".format(api_version,
                                                                               site_id,
                                                                               elementshell_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementshells_interfaces(self, site_id, elementshell_id, interface_id, api_version="v2.4"):
        """
        Delete an element shell interface (v2.4)

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **interface_id**: Interface ID
          - **api_version**: API version to use (default v2.4)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}/interfaces/{}".format(api_version,
                                                                                             site_id,
                                                                                             elementshell_id,
                                                                                             interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementusers(self, elementuser_id, api_version="v2.1"):
        """
        Delete element user (v2.1)

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}".format(api_version,
                                                                     elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementusers_access(self, elementuser_id, access_id, api_version="v2.1"):
        """
        Delete element user Access (v2.1)

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: Access ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}/access/{}".format(api_version,
                                                                               elementuser_id,
                                                                               access_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def esp_operator_permissions_client(self, operator_id, client_id, api_version="v2.1"):
        """
        Delete esp operator permissions assigned under a client (v2.1)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/clients/{}/permissions".format(api_version,
                                                                                         operator_id,
                                                                                         client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, eventcorrelationpolicyrule_id, api_version="v2.1"):
        """
        Delete specific event correlation policy rule (v2.1)

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **eventcorrelationpolicyrule_id**: Event Correlation Policy Rule ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules/{}".format(api_version,
                                                                                                                  eventcorrelationpolicyset_id,
                                                                                                                  eventcorrelationpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def eventcorrelationpolicysets(self, eventcorrelationpolicyset_id, api_version="v2.0"):
        """
        Delete specific event correlation policyset (v2.0)

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}".format(api_version,
                                                                                   eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def externalcaconfigs(self, externalcaconfig_id, api_version="v2.0"):
        """
        DELETE Externalcaconfigs API Function

          **Parameters:**:

          - **externalcaconfig_id**: External CA Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/externalcaconfigs/{}".format(api_version,
                                                                          externalcaconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def globalprefixfilters(self, globalprefixfilter_id, api_version="v2.0"):
        """
        Delete a global prefix filter. (v2.0)

          **Parameters:**:

          - **globalprefixfilter_id**: Global Prefix Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters/{}".format(api_version,
                                                                            globalprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id, api_version="v3.0"):
        """
        Deletes specific hub cluster member. (v3.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: Hub Cluster Member ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/hubclustermembers/{}".format(api_version,
                                                                                                  site_id,
                                                                                                  hubcluster_id,
                                                                                                  hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def hubclusters(self, site_id, hubcluster_id, api_version="v4.0"):
        """
        Delete hub cluster (v4.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **api_version**: API version to use (default v4.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}".format(api_version,
                                                                             site_id,
                                                                             hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def idps(self, idp_id, api_version="v3.3"):
        """
        Delete idp (v3.3)

          **Parameters:**:

          - **idp_id**: SAML IDentity provider configuration ID
          - **api_version**: API version to use (default v3.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/idps/{}".format(api_version,
                                                             idp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def interfaces(self, site_id, element_id, interface_id, api_version="v4.21"):
        """
        Delete a Interface (v4.21)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **api_version**: API version to use (default v4.21)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}".format(api_version,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfix(self, site_id, element_id, ipfix_id, api_version="v2.0"):
        """
        Delete IPFix config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ipfix_id**: IPFix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ipfix/{}".format(api_version,
                                                                                   site_id,
                                                                                   element_id,
                                                                                   ipfix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixcollectorcontexts(self, ipfixcollectorcontext_id, api_version="v2.0"):
        """
        Delete a IPFix collector context (v2.0)

          **Parameters:**:

          - **ipfixcollectorcontext_id**: IPFix Collector Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixcollectorcontexts/{}".format(api_version,
                                                                               ipfixcollectorcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixfiltercontexts(self, ipfixfiltercontext_id, api_version="v2.0"):
        """
        Delete a IPFix filter context (v2.0)

          **Parameters:**:

          - **ipfixfiltercontext_id**: IPFix Filter Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixfiltercontexts/{}".format(api_version,
                                                                            ipfixfiltercontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixglobalprefixes(self, ipfixglobalprefix_id, api_version="v2.0"):
        """
        Delete a IPFix global prefix (v2.0)

          **Parameters:**:

          - **ipfixglobalprefix_id**: IPFix Global Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixglobalprefixes/{}".format(api_version,
                                                                            ipfixglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixprofiles(self, ipfixprofile_id, api_version="v2.0"):
        """
        Delete IPFix Profile (v2.0)

          **Parameters:**:

          - **ipfixprofile_id**: IPFix Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixprofiles/{}".format(api_version,
                                                                      ipfixprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixtemplates(self, ipfixtemplate_id, api_version="v2.0"):
        """
        Delete a IPFix template (v2.0)

          **Parameters:**:

          - **ipfixtemplate_id**: IPFix Template ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixtemplates/{}".format(api_version,
                                                                       ipfixtemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipsecprofiles(self, ipsecprofile_id, api_version="v2.2"):
        """
        Delete a IPSEC Profile (v2.2)

          **Parameters:**:

          - **ipsecprofile_id**: IPSEC Profile ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles/{}".format(api_version,
                                                                      ipsecprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def lannetworks(self, site_id, lannetwork_id, api_version="v3.3"):
        """
        Delete an existing LAN (v3.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: LAN Network ID
          - **api_version**: API version to use (default v3.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/lannetworks/{}".format(api_version,
                                                                             site_id,
                                                                             lannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def localprefixfilters(self, localprefixfilter_id, api_version="v2.0"):
        """
        Delete a local prefix filter. (v2.0)

          **Parameters:**:

          - **localprefixfilter_id**: Local Prefix Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/localprefixfilters/{}".format(api_version,
                                                                           localprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def mstp_instances(self, site_id, element_id, mstp_instance_id, api_version="v2.0"):
        """
        Delete MSTP instance for an element (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **mstp_instance_id**: MSTP Instance ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/mstp_instances/{}".format(api_version,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            mstp_instance_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def multicastpeergroups(self, multicastpeergroup_id, api_version="v2.1"):
        """
        Delete multicast peer group (v2.1)

          **Parameters:**:

          - **multicastpeergroup_id**: Multicast Peer Group ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastpeergroups/{}".format(api_version,
                                                                            multicastpeergroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def multicastrps(self, site_id, element_id, multicastrp_id, api_version="v2.0"):
        """
        Deletes Multicast RP config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastrp_id**: Multicast RP ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastrps/{}".format(api_version,
                                                                                          site_id,
                                                                                          element_id,
                                                                                          multicastrp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def multicastsourcesiteconfigs(self, site_id, multicastsourcesiteconfig_id, api_version="v2.0"):
        """
        Delete multicast source site config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **multicastsourcesiteconfig_id**: Multicast Source Site Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiteconfigs/{}".format(api_version,
                                                                                            site_id,
                                                                                            multicastsourcesiteconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natglobalprefixes(self, natglobalprefix_id, api_version="v2.0"):
        """
        Delete a NAT Global Prefix. (v2.0)

          **Parameters:**:

          - **natglobalprefix_id**: NAT Global Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natglobalprefixes/{}".format(api_version,
                                                                          natglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natlocalprefixes(self, natlocalprefix_id, api_version="v2.0"):
        """
        Delete a NAT local prefix. (v2.0)

          **Parameters:**:

          - **natlocalprefix_id**: NAT Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natlocalprefixes/{}".format(api_version,
                                                                         natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicypools(self, natpolicypool_id, api_version="v2.0"):
        """
        Delete a NAT Policy Pool. (v2.0)

          **Parameters:**:

          - **natpolicypool_id**: NAT Policy Pool ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicypools/{}".format(api_version,
                                                                       natpolicypool_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicyrules(self, natpolicyset_id, natpolicyrule_id, api_version="v2.0"):
        """
        Delete NAT policy rule of tenant. (v2.0)

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **natpolicyrule_id**: NAT Policy Rule ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}/natpolicyrules/{}".format(api_version,
                                                                                        natpolicyset_id,
                                                                                        natpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicysets(self, natpolicyset_id, api_version="v2.0"):
        """
        Delete NAT policy set. (v2.0)

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}".format(api_version,
                                                                      natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicysetstacks(self, natpolicysetstack_id, api_version="v2.0"):
        """
        Delete NAT Policy Set Stack. (v2.0)

          **Parameters:**:

          - **natpolicysetstack_id**: NAT Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysetstacks/{}".format(api_version,
                                                                           natpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natzones(self, natzone_id, api_version="v2.0"):
        """
        Delete a Nat Policy Zone. (v2.0)

          **Parameters:**:

          - **natzone_id**: NAT Zone ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natzones/{}".format(api_version,
                                                                 natzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def networkcontexts(self, networkcontext_id, api_version="v2.0"):
        """
        Delete LAN segment (v2.0)

          **Parameters:**:

          - **networkcontext_id**: Network Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkcontexts/{}".format(api_version,
                                                                        networkcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id, api_version="v2.1"):
        """
        Delete a Network Policy Global Prefix. (v2.1)

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: Network Policy Global Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyglobalprefixes/{}".format(api_version,
                                                                                    networkpolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id, api_version="v2.4"):
        """
        Delete network policy rule of tenant. (v2.4)

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: Network Policy Rule ID
          - **api_version**: API version to use (default v2.4)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}/networkpolicyrules/{}".format(api_version,
                                                                                                networkpolicyset_id,
                                                                                                networkpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def networkpolicysets(self, networkpolicyset_id, api_version="v2.0"):
        """
        Delete Network Policy Set. (v2.0)

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}".format(api_version,
                                                                          networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def networkpolicysetstacks(self, networkpolicysetstack_id, api_version="v2.0"):
        """
        Delete a NetworkPolicySetStack (v2.0)

          **Parameters:**:

          - **networkpolicysetstack_id**: Network Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysetstacks/{}".format(api_version,
                                                                               networkpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ngfwsecuritypolicyglobalprefixes(self, ngfwsecuritypolicyglobalprefix_id, api_version="v2.1"):
        """
        Delete a Security Policy V2 Local Prefix by tenant ID and its ID (v2.1)

          **Parameters:**:

          - **ngfwsecuritypolicyglobalprefix_id**: NGFW Security Policy Global Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyglobalprefixes/{}".format(api_version,
                                                                                         ngfwsecuritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ngfwsecuritypolicylocalprefixes(self, ngfwsecuritypolicylocalprefix_id, api_version="v2.0"):
        """
        Delete a Security Policy V2 Local Prefix by tenant ID and its ID (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicylocalprefix_id**: NGFW Security Policy Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                        ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ngfwsecuritypolicyrules(self, ngfwsecuritypolicyset_id, ngfwsecuritypolicyrule_id, api_version="v2.2"):
        """
        Delete an existing Security Policy V2 Rule under a policy set (v2.2)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **ngfwsecuritypolicyrule_id**: NGFW Security Policy Rule ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules/{}".format(api_version,
                                                                                                          ngfwsecuritypolicyset_id,
                                                                                                          ngfwsecuritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ngfwsecuritypolicysets(self, ngfwsecuritypolicyset_id, api_version="v2.0"):
        """
        Delete an existing Security Policy V2 Set by tenant ID and its ID (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}".format(api_version,
                                                                               ngfwsecuritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ngfwsecuritypolicysetstacks(self, ngfwsecuritypolicysetstack_id, api_version="v2.0"):
        """
        Delete an existing Security Policy V2 Set Stack by tenant ID and its ID (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicysetstack_id**: NGFW Security Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysetstacks/{}".format(api_version,
                                                                                    ngfwsecuritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def operator_sessions(self, operator_id, session_id, api_version="v2.0"):
        """
        Delete session for tenant_id, operator id, and session id (v2.0)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **session_id**: User Session ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/sessions/{}".format(api_version,
                                                                              operator_id,
                                                                              session_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ospfconfigs(self, site_id, element_id, ospfconfig_id, api_version="v2.0"):
        """
        Deletes OSPF config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ospfconfig_id**: OSPF Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfconfigs/{}".format(api_version,
                                                                                         site_id,
                                                                                         element_id,
                                                                                         ospfconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def pathgroups(self, pathgroup_id, api_version="v2.1"):
        """
        Delete A Path Group of a tenant. (v2.1)

          **Parameters:**:

          - **pathgroup_id**: Path Group ID (for network service/DC routing)
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/pathgroups/{}".format(api_version,
                                                                   pathgroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def pathprefixdistributionfilterassociation(self, site_id, pathprefixdistributionfilterassociation_id, api_version="v2.0"):
        """
        DELETE Pathprefixdistributionfilterassociation API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **pathprefixdistributionfilterassociation_id**: Path Prefix Distribution Filter Association ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilterassociation/{}".format(api_version,
                                                                                                         site_id,
                                                                                                         pathprefixdistributionfilterassociation_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def pathprefixdistributionfilters(self, site_id, pathprefixdistributionfilter_id, api_version="v2.0"):
        """
        DELETE Pathprefixdistributionfilters API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **pathprefixdistributionfilter_id**: Path Prefix Distribution Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilters/{}".format(api_version,
                                                                                               site_id,
                                                                                               pathprefixdistributionfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def perfmgmtpolicysets(self, perfmgmtpolicyset_id, api_version="v2.0"):
        """
        Delete a PERFMGMT Policy Set (v2.0)

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}".format(api_version,
                                                                           perfmgmtpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def perfmgmtpolicysets_perfmgmtpolicyrules(self, perfmgmtpolicyset_id, perfmgmtpolicyrule_id, api_version="v2.2"):
        """
        Delete PERFMGMT policy rule of tenant V2.2 (v2.2)

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **perfmgmtpolicyrule_id**: Performance Management Policy Rule ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}/perfmgmtpolicyrules/{}".format(api_version,
                                                                                                  perfmgmtpolicyset_id,
                                                                                                  perfmgmtpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def perfmgmtpolicysetstacks(self, perfmgmtpolicysetstack_id, api_version="v2.0"):
        """
        Delete a PERFMGMT Policy Set Stack (v2.0)

          **Parameters:**:

          - **perfmgmtpolicysetstack_id**: Performance Management Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysetstacks/{}".format(api_version,
                                                                                perfmgmtpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def perfmgmtthresholdprofiles(self, perfmgmtthresholdprofile_id, api_version="v2.1"):
        """
        Delete a Threshold Profile (v2.1)

          **Parameters:**:

          - **perfmgmtthresholdprofile_id**: Performance Management Threshold Profile ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtthresholdprofiles/{}".format(api_version,
                                                                                  perfmgmtthresholdprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def policyrules(self, policyset_id, policyrule_id, api_version="v3.1"):
        """
        Delete policy rule of tenant. (v3.1)

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **policyrule_id**: Policy Rule ID
          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}/policyrules/{}".format(api_version,
                                                                                  policyset_id,
                                                                                  policyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def policysets(self, policyset_id, api_version="v3.0"):
        """
        Delete policy set. (v3.0)

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}".format(api_version,
                                                                   policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prefixdistributionspokelists(self, site_id, prefixdistributionspokelist_id, api_version="v2.0"):
        """
        DELETE Prefixdistributionspokelists API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixdistributionspokelist_id**: Prefix Distribution Spoke List ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixdistributionspokelists/{}".format(api_version,
                                                                                              site_id,
                                                                                              prefixdistributionspokelist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prefixfilters(self, site_id, prefixfilter_id, api_version="v2.0"):
        """
        Delete an existing security prefix filter (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixfilter_id**: Prefix Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters/{}".format(api_version,
                                                                               site_id,
                                                                               prefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id, api_version="v2.1"):
        """
        Delete a Priority Policy Global Prefix. (v2.1)

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: Priority Policy Global Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyglobalprefixes/{}".format(api_version,
                                                                                     prioritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id, api_version="v2.2"):
        """
        Delete priority policy rule of tenant. (v2.2)

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: Priority Policy Rule ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}/prioritypolicyrules/{}".format(api_version,
                                                                                                  prioritypolicyset_id,
                                                                                                  prioritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prioritypolicysets(self, prioritypolicyset_id, api_version="v2.0"):
        """
        Delete Priority Policy Set. (v2.0)

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}".format(api_version,
                                                                           prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prioritypolicysetstacks(self, prioritypolicysetstack_id, api_version="v2.0"):
        """
        Delete a PriorityPolicySetStack (v2.0)

          **Parameters:**:

          - **prioritypolicysetstack_id**: Priority Policy Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysetstacks/{}".format(api_version,
                                                                                prioritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prismaaccess_configs(self, site_id, prismaaccess_config_id, api_version="v2.0"):
        """
        Delete a Prisma Access Config with remote networks and security processing node (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prismaaccess_config_id**: Prisma Acceess Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismaaccess_configs/{}".format(api_version,
                                                                                      site_id,
                                                                                      prismaaccess_config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prismasase_connections(self, site_id, prismasase_connection_id, api_version="v2.1"):
        """
        DELETE Prismasase_Connections API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **prismasase_connection_id**: Prisma SASE Connection ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismasase_connections/{}".format(api_version,
                                                                                        site_id,
                                                                                        prismasase_connection_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prismasase_connections_configs(self, api_version="v3.1"):
        """
        Delete existing SASE connection config (v3.1)

          **Parameters:**:

          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismasase_connections/configs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def probeconfigs(self, probeconfig_id, api_version="v2.0"):
        """
        Delete a Probe Config (v2.0)

          **Parameters:**:

          - **probeconfig_id**: Probe Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeconfigs/{}".format(api_version,
                                                                     probeconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def probeprofiles(self, probeprofile_id, api_version="v2.0"):
        """
        Delete a PROBE Profile (v2.0)

          **Parameters:**:

          - **probeprofile_id**: Probe Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeprofiles/{}".format(api_version,
                                                                      probeprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def radii(self, element_id, radii_id, api_version="v2.0"):
        """
        Delete radius configuration in an element (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **radii_id**: Radii ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/radii/{}".format(api_version,
                                                                          element_id,
                                                                          radii_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def roles(self, role_id, api_version="v2.1"):
        """
        Delete a custom role (v2.1)

          **Parameters:**:

          - **role_id**: Role ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/roles/{}".format(api_version,
                                                              role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def routing_aspathaccesslists(self, site_id, element_id, routing_aspathaccesslist_id, api_version="v2.1"):
        """
        Delete Access List (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_aspathaccesslist_id**: Routing AS-PATH Access List ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_aspathaccesslists/{}".format(api_version,
                                                                                                       site_id,
                                                                                                       element_id,
                                                                                                       routing_aspathaccesslist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def routing_ipcommunitylists(self, site_id, element_id, routing_ipcommunitylist_id, api_version="v2.0"):
        """
        Delete Community List (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_ipcommunitylist_id**: Routing IP Community List ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_ipcommunitylists/{}".format(api_version,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      routing_ipcommunitylist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def routing_prefixlists(self, site_id, element_id, routing_prefixlist_id, api_version="v2.1"):
        """
        Delete Prefix List (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_prefixlist_id**: Routing IP Prefix List ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_prefixlists/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 routing_prefixlist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def routing_routemaps(self, site_id, element_id, routing_routemap_id, api_version="v2.3"):
        """
        Delete Route Map (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_routemap_id**: Routing Route Map ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_routemaps/{}".format(api_version,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               routing_routemap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def sdwanapps_configs(self, sdwanapp_id, config_id, api_version="v2.0"):
        """
        DELETE Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **config_id**: SDWAN App Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/configs/{}".format(api_version,
                                                                             sdwanapp_id,
                                                                             config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def securitypolicyrules(self, securitypolicyset_id, securitypolicyrule_id, api_version="v2.0"):
        """
        Delete a security policyrule. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **securitypolicyrule_id**: Security Policy Rule ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}/securitypolicyrules/{}".format(api_version,
                                                                                                  securitypolicyset_id,
                                                                                                  securitypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def securitypolicysets(self, securitypolicyset_id, api_version="v2.0"):
        """
        Delete a security policyset. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}".format(api_version,
                                                                           securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def securityzones(self, securityzone_id, api_version="v2.1"):
        """
        Delete an existing security zone (v2.1)

          **Parameters:**:

          - **securityzone_id**: Security Zone (ZBFW) ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securityzones/{}".format(api_version,
                                                                      securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def servicebindingmaps(self, servicebindingmap_id, api_version="v2.1"):
        """
        Delete a Service Binding Map (v2.1)

          **Parameters:**:

          - **servicebindingmap_id**: Service Binding Map ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicebindingmaps/{}".format(api_version,
                                                                           servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def serviceendpoints(self, serviceendpoint_id, api_version="v3.1"):
        """
        Delete a Service Endpoint (v3.1)

          **Parameters:**:

          - **serviceendpoint_id**: Service Endpoint ID
          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/serviceendpoints/{}".format(api_version,
                                                                         serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def servicelabels(self, servicelabel_id, api_version="v2.1"):
        """
        Delete a Service Label (v2.1)

          **Parameters:**:

          - **servicelabel_id**: Service Label ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicelabels/{}".format(api_version,
                                                                      servicelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_extensions(self, site_id, extension_id, api_version="v2.0"):
        """
        Delete a specific extension associated with a site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **extension_id**: Extension ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/extensions/{}".format(api_version,
                                                                            site_id,
                                                                            extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_ipfixlocalprefixes(self, site_id, ipfixlocalprefix_id, api_version="v2.0"):
        """
        Delete a IPFix site prefix association (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                    site_id,
                                                                                    ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_natlocalprefixes(self, site_id, natlocalprefix_id, api_version="v2.0"):
        """
        Delete an existing Site NAT prefix (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **natlocalprefix_id**: NAT Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/natlocalprefixes/{}".format(api_version,
                                                                                  site_id,
                                                                                  natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id, api_version="v2.1"):
        """
        Delete an existing Site Network Policy local prefix association (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                            site_id,
                                                                                            networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_ngfwsecuritypolicylocalprefixes(self, site_id, ngfwsecuritypolicylocalprefix_id, api_version="v2.1"):
        """
        Delete an existing security policy v2 local prefix site association (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **ngfwsecuritypolicylocalprefix_id**: NGFW Security Policy Local Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id, api_version="v2.1"):
        """
        Delete an existing Site Priority Policy local prefix association (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                             site_id,
                                                                                             prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def sites(self, site_id, api_version="v4.12"):
        """
        Delete a site (v4.12)

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v4.12)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}".format(api_version,
                                                              site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def sitesecurityzones(self, site_id, sitesecurityzone_id, api_version="v2.0"):
        """
        Delete an existing security zone (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **sitesecurityzone_id**: Site Security Zone ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/sitesecurityzones/{}".format(api_version,
                                                                                   site_id,
                                                                                   sitesecurityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def snmpagents(self, site_id, element_id, snmpagent_id, api_version="v2.1"):
        """
        delete SNMP Agent (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: SNMP Agent ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmpagents/{}".format(api_version,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        snmpagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def snmptraps(self, site_id, element_id, snmptrap_id, api_version="v2.0"):
        """
        delete SNMP Trap (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmptrap_id**: SNMP Trap ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmptraps/{}".format(api_version,
                                                                                       site_id,
                                                                                       element_id,
                                                                                       snmptrap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def spokeclusters(self, site_id, spokecluster_id, api_version="v2.0"):
        """
        Delete spoke cluster. (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/{}".format(api_version,
                                                                               site_id,
                                                                               spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def staticroutes(self, site_id, element_id, staticroute_id, api_version="v2.3"):
        """
        Delete static route (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/staticroutes/{}".format(api_version,
                                                                                          site_id,
                                                                                          element_id,
                                                                                          staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def syslogserverprofiles(self, syslogserverprofile_id, api_version="v2.0"):
        """
        Delete Syslog Server Profile (v2.0)

          **Parameters:**:

          - **syslogserverprofile_id**: Sys Log Server Profile ID 
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/syslogserverprofiles/{}".format(api_version,
                                                                             syslogserverprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def syslogservers(self, site_id, element_id, syslogserver_id, api_version="v2.2"):
        """
        Delete Syslog Server (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: SYSLOG server ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/syslogservers/{}".format(api_version,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           syslogserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tacacs_plus_profiles(self, tacacs_plus_profile_id, api_version="v2.0"):
        """
        DELETE Tacacs_Plus_Profiles API Function

          **Parameters:**:

          - **tacacs_plus_profile_id**: Tacacs Plus Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/tacacs_plus_profiles/{}".format(api_version,
                                                                             tacacs_plus_profile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tacacs_plus_servers(self, site_id, element_id, tacacs_plus_server_id, api_version="v2.0"):
        """
        DELETE Tacacs_Plus_Servers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **tacacs_plus_server_id**: Tacacs Plus Server ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/tacacs_plus_servers/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 tacacs_plus_server_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def templates_ntp(self, ntp_id, api_version="v2.0"):
        """
        Delete an existing NTP Template (v2.0)

          **Parameters:**:

          - **ntp_id**: NTP Configuration ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/templates/ntp/{}".format(api_version,
                                                                      ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_anynetlinks(self, anynetlink_id, api_version="v4.0"):
        """
        DELETE Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **api_version**: API version to use (default v4.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks/{}".format(api_version,
                                                                    anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_ipfixlocalprefixes(self, ipfixlocalprefix_id, api_version="v2.0"):
        """
        Delete a IPFix local prefix (v2.0)

          **Parameters:**:

          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixlocalprefixes/{}".format(api_version,
                                                                           ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_networkpolicylocalprefixes(self, networkpolicylocalprefix_id, api_version="v2.0"):
        """
        Delete a Network Policy local prefix. (v2.0)

          **Parameters:**:

          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicylocalprefixes/{}".format(api_version,
                                                                                   networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_operators(self, operator_id, api_version="v2.2"):
        """
        Delete a tenant operator (v2.2)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}".format(api_version,
                                                                  operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_permissions(self, permission_id, api_version="v2.0"):
        """
        Delete a tenant custom permission (v2.0)

          **Parameters:**:

          - **permission_id**: Permission ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/permissions/{}".format(api_version,
                                                                    permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_prioritypolicylocalprefixes(self, prioritypolicylocalprefix_id, api_version="v2.0"):
        """
        Delete a Priority Policy local prefix. (v2.0)

          **Parameters:**:

          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                    prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenantpassageconfigs(self, tenantpassageconfig_id, api_version="v2.0"):
        """
        DELETE Tenantpassageconfigs API Function

          **Parameters:**:

          - **tenantpassageconfig_id**: Tenant Passage Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/tenantpassageconfigs/{}".format(api_version,
                                                                             tenantpassageconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenants_certificates(self, certificate_id, api_version="v2.0"):
        """
        DELETE Tenants_Certificates API Function

          **Parameters:**:

          - **certificate_id**: Certificate ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/certificates/{}".format(api_version,
                                                                     certificate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def useridagents(self, useridagent_id, api_version="v2.0"):
        """
        Delete User ID Agent (v2.0)

          **Parameters:**:

          - **useridagent_id**: User Id Agent ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/useridagents/{}".format(api_version,
                                                                     useridagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def users(self, user_id, api_version="v2.0"):
        """
        Delete an user identity. (v2.0)

          **Parameters:**:

          - **user_id**: User ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/users/{}".format(api_version,
                                                              user_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def vrfcontextprofiles(self, vrfcontextprofile_id, api_version="v2.0"):
        """
        Delete VRF Context Profile (v2.0)

          **Parameters:**:

          - **vrfcontextprofile_id**: VRF Context Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontextprofiles/{}".format(api_version,
                                                                           vrfcontextprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def vrfcontexts(self, vrfcontext_id, api_version="v2.0"):
        """
        Delete VRF segment (v2.0)

          **Parameters:**:

          - **vrfcontext_id**: VRF Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontexts/{}".format(api_version,
                                                                    vrfcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def waninterfaces(self, site_id, waninterface_id, api_version="v2.10"):
        """
        Delete existing WAN interface (v2.10)

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **api_version**: API version to use (default v2.10)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces/{}".format(api_version,
                                                                               site_id,
                                                                               waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def wannetworks(self, wannetwork_id, api_version="v2.1"):
        """
        Delete an existing WAN (v2.1)

          **Parameters:**:

          - **wannetwork_id**: WAN Network ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wannetworks/{}".format(api_version,
                                                                    wannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def wanoverlays(self, wanoverlay_id, api_version="v2.0"):
        """
        Delete app/wan context (v2.0)

          **Parameters:**:

          - **wanoverlay_id**: WAN Overlay ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wanoverlays/{}".format(api_version,
                                                                    wanoverlay_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ws_extensions(self, extension_id, api_version="v2.0"):
        """
        DELETE Ws_Extensions API Function

          **Parameters:**:

          - **extension_id**: Extension ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ws/extensions/{}".format(api_version,
                                                                      extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    access_elementusers = elementusers_access
    """ Backwards-compatibility alias of `access_elementusers` to `elementusers_access`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    certificates_tenants = tenants_certificates
    """ Backwards-compatibility alias of `certificates_tenants` to `tenants_certificates`"""

    configs_prismasase_connections = prismasase_connections_configs
    """ Backwards-compatibility alias of `configs_prismasase_connections` to `prismasase_connections_configs`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    deployments_sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates_deployments
    """ Backwards-compatibility alias of `deployments_sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates_deployments`"""

    deviceidconfigs_i = element_deviceidconfigs
    """ Backwards-compatibility alias of `deviceidconfigs_i` to `element_deviceidconfigs`"""

    elementpassageconfigs_e = elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_e` to `elementpassageconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    interfaces_elementshells = elementshells_interfaces
    """ Backwards-compatibility alias of `interfaces_elementshells` to `elementshells_interfaces`"""

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

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    passages_e = element_passages
    """ Backwards-compatibility alias of `passages_e` to `element_passages`"""

    perfmgmtpolicyrules_perfmgmtpolicysets = perfmgmtpolicysets_perfmgmtpolicyrules
    """ Backwards-compatibility alias of `perfmgmtpolicyrules_perfmgmtpolicysets` to `perfmgmtpolicysets_perfmgmtpolicyrules`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    sessions_t = operator_sessions
    """ Backwards-compatibility alias of `sessions_t` to `operator_sessions`"""

    sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates
    """ Backwards-compatibility alias of `sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates`"""

    snmpdiscoverystartnodes_deviceidconfigs = deviceidconfigs_snmpdiscoverystartnodes
    """ Backwards-compatibility alias of `snmpdiscoverystartnodes_deviceidconfigs` to `deviceidconfigs_snmpdiscoverystartnodes`"""

    toolkitsessions_e = element_toolkitsessions
    """ Backwards-compatibility alias of `toolkitsessions_e` to `element_toolkitsessions`"""

