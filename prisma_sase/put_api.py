#!/usr/bin/env python
"""
PRISMA SASE Python SDK - PUT

**Author:** Palo Alto Networks

**Copyright:** (c) 2024 Palo Alto Networks, Inc

**License:** MIT
"""
import logging

__author__ = "Prisma SASE Developer Support <prisma-sase-developers@paloaltonetworks.com>"
__email__ = "prisma-sase-developers@paloaltonetworks.com"
__copyright__ = "Copyright (c) 2024 Palo Alto Networks, Inc"
__license__ = """
    MIT License

    Copyright (c) 2024 Palo Alto Networks, Inc

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


class Put(object):
    """
    Prisma SASE API - PUT requests

    Object to handle making Put requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def apnprofiles(self, apnprofile_id, data, api_version="v2.0"):
        """
        Update an APN Profile (v2.0)

          **Parameters:**:

          - **apnprofile_id**: APN Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/apnprofiles/{}".format(api_version,
                                                                    apnprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs(self, appdef_id, data, api_version="v2.6"):
        """
        Update a application definition (v2.4)

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}".format(api_version,
                                                                appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs_overrides(self, appdef_id, override_id, data, api_version="v2.3"):
        """
        Update a application definition overrides for system appdef (v2.3)

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: AppDef Override ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}/overrides/{}".format(api_version,
                                                                             appdef_id,
                                                                             override_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs_version(self, appdefs_version_id, data, api_version="v2.1"):
        """
        Change standard apps version (v2.0)

          **Parameters:**:

          - **appdefs_version_id**: Application Definition Version ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/appdefs_version/{}".format(api_version,
                                                                        appdefs_version_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def application_probe(self, site_id, element_id, data, api_version="v2.0"):
        """
        Update application probe configuration (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/application_probe".format(api_version,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def bgpconfigs(self, site_id, element_id, bgpconfig_id, data, api_version="v2.4"):
        """
        Updates BGP config (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgpconfig_id**: BGP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgpconfigs/{}".format(api_version,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        bgpconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def bgppeers(self, site_id, element_id, bgppeer_id, data, api_version="v2.5"):
        """
        Updates BGP Peer config (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}".format(api_version,
                                                                                      site_id,
                                                                                      element_id,
                                                                                      bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def bulkconfigurations_sitetemplates(self, sitetemplate_id, data, api_version="v2.0"):
        """
        PUT Bulkconfigurations_Sitetemplates API Function

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}".format(api_version,
                                                                                         sitetemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def cellular_modules_sim_security(self, element_id, cellular_module_id, sim_security_id, data, api_version="v2.0"):
        """
        Update cellular module (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **sim_security_id**: SIM Security ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}/sim_security/{}".format(api_version,
                                                                                                     element_id,
                                                                                                     cellular_module_id,
                                                                                                     sim_security_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def demsiteconfigs(self, site_id, demsiteconfig_id, data, api_version="v2.0"):
        """
        PUT Demsiteconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **demsiteconfig_id**: DEM Site Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/demsiteconfigs/{}".format(api_version,
                                                                                site_id,
                                                                                demsiteconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def deviceidconfigs(self, site_id, deviceidconfig_id, data, api_version="v2.1"):
        """
        PUT Deviceidconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: Device Id Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}".format(api_version,
                                                                                 site_id,
                                                                                 deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def deviceidconfigs_snmpdiscoverystartnodes(self, site_id, deviceidconfig_id, snmpdiscoverystartnode_id, data, api_version="v2.0"):
        """
        PUT Deviceidconfigs_Snmpdiscoverystartnodes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: Device Id Config ID
          - **snmpdiscoverystartnode_id**: SNMP Discovery Start Node ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}/snmpdiscoverystartnodes/{}".format(api_version,
                                                                                                            site_id,
                                                                                                            deviceidconfig_id,
                                                                                                            snmpdiscoverystartnode_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def deviceidprofiles(self, deviceidprofile_id, data, api_version="v2.0"):
        """
        PUT Deviceidprofiles API Function

          **Parameters:**:

          - **deviceidprofile_id**: Device Id Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/deviceidprofiles/{}".format(api_version,
                                                                         deviceidprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dhcpservers(self, site_id, dhcpserver_id, data, api_version="v2.3"):
        """
        Update an existing dhcp server configuration for a subnet (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: DHCP Server ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/dhcpservers/{}".format(api_version,
                                                                             site_id,
                                                                             dhcpserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def directoryservices(self, directoryservice_id, data, api_version="v2.0"):
        """
        PUT Directoryservices API Function

          **Parameters:**:

          - **directoryservice_id**: Directory Service ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices/{}".format(api_version,
                                                                          directoryservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dnsserviceprofiles(self, dnsserviceprofile_id, data, api_version="v2.1"):
        """
        Update a DNS service profile (v2.0)

          **Parameters:**:

          - **dnsserviceprofile_id**: DNS Service Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceprofiles/{}".format(api_version,
                                                                           dnsserviceprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dnsserviceroles(self, dnsservicerole_id, data, api_version="v2.0"):
        """
        Update a DNS service role (v2.0)

          **Parameters:**:

          - **dnsservicerole_id**: DNS Service Role ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceroles/{}".format(api_version,
                                                                        dnsservicerole_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dnsservices(self, site_id, element_id, dnsservice_id, data, api_version="v2.0"):
        """
        Update a DNS service config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **dnsservice_id**: DNS Service ID 
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/dnsservices/{}".format(api_version,
                                                                                         site_id,
                                                                                         element_id,
                                                                                         dnsservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_admin_state(self, site_id, element_id, data, api_version="v2.0"):
        """
        Update admin state Northbound (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/admin_state".format(api_version,
                                                                                      site_id,
                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_cellular_modules(self, element_id, cellular_module_id, data, api_version="v2.0"):
        """
        Update cellular module (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}".format(api_version,
                                                                                     element_id,
                                                                                     cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_cellular_modules_firmware(self, element_id, cellular_module_id, data, api_version="v2.0"):
        """
        Update cellular module firmware configuration (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}/firmware".format(api_version,
                                                                                              element_id,
                                                                                              cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_deviceidconfigs(self, site_id, element_id, deviceidconfig_id, data, api_version="v2.0"):
        """
        PUT Element_Deviceidconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **deviceidconfig_id**: Device Id Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/deviceidconfigs/{}".format(api_version,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_extensions(self, site_id, element_id, extension_id, data, api_version="v2.0"):
        """
        Update element level extension configuration (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/extensions/{}".format(api_version,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_state(self, element_id, data, api_version="v2.0"):
        """
        PUT Element_State API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/state".format(api_version,
                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementaccessconfigs(self, element_id, elementaccessconfig_id, data, api_version="v2.2"):
        """
        Update an Access Config on particular element. (v2.2)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementaccessconfig_id**: Element Access Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/elementaccessconfigs/{}".format(api_version,
                                                                                         element_id,
                                                                                         elementaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elements(self, element_id, data, api_version="v3.1"):
        """
        Used for associations and element updates (v3.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}".format(api_version,
                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementsecurityzones(self, site_id, element_id, securityzone_id, data, api_version="v2.0"):
        """
        Update an existing element security zone (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **securityzone_id**: Security Zone (ZBFW) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/securityzones/{}".format(api_version,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementshells(self, site_id, elementshell_id, data, api_version="v2.0"):
        """
        PUT Elementshells API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}".format(api_version,
                                                                               site_id,
                                                                               elementshell_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementusers(self, elementuser_id, data, api_version="v2.1"):
        """
        Update an existing element user. (v2.1)

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}".format(api_version,
                                                                     elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementusers_access(self, elementuser_id, access_id, data, api_version="v2.1"):
        """
        PUT Elementusers_Access API Function

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: Access ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}/access/{}".format(api_version,
                                                                               elementuser_id,
                                                                               access_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def enterpriseprefixset(self, data, api_version="v2.1"):
        """
        PUT Enterpriseprefixset API Function

          **Parameters:**:

          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/enterpriseprefixset".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def esp_operator_permissions_client(self, operator_id, client_id, data, api_version="v2.1"):
        """
        Create or update esp operator permissions assigned under a client (v2.1)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/clients/{}/permissions".format(api_version,
                                                                                         operator_id,
                                                                                         client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, eventcorrelationpolicyrule_id, data, api_version="v2.1"):
        """
        Update event correlation policyrule configuration (v2.0)

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **eventcorrelationpolicyrule_id**: Event Correlation Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules/{}".format(api_version,
                                                                                                                  eventcorrelationpolicyset_id,
                                                                                                                  eventcorrelationpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def eventcorrelationpolicysets(self, eventcorrelationpolicyset_id, data, api_version="v2.0"):
        """
        Update event correlation policyset configuration (v2.0)

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}".format(api_version,
                                                                                   eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def events(self, event_id, data, api_version="v2.3"):
        """
        PUT Events API Function

          **Parameters:**:

          - **event_id**: Event ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/events/{}".format(api_version,
                                                               event_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def externalcaconfigs(self, externalcaconfig_id, data, api_version="v2.0"):
        """
        PUT Externalcaconfigs API Function

          **Parameters:**:

          - **externalcaconfig_id**: External CA Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/externalcaconfigs/{}".format(api_version,
                                                                          externalcaconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def globalprefixfilters(self, globalprefixfilter_id, data, api_version="v2.0"):
        """
        Update a new global prefix filter. (v2.0)

          **Parameters:**:

          - **globalprefixfilter_id**: Global Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters/{}".format(api_version,
                                                                            globalprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id, data, api_version="v3.0"):
        """
        Update specific hub cluster member. (v3.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: Hub Cluster Member ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/hubclustermembers/{}".format(api_version,
                                                                                                  site_id,
                                                                                                  hubcluster_id,
                                                                                                  hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def hubclusters(self, site_id, hubcluster_id, data, api_version="v4.0"):
        """
        Update hub cluster (v4.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v4.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}".format(api_version,
                                                                             site_id,
                                                                             hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def idps(self, idp_id, data, api_version="v3.3"):
        """
        Update sso (v3.3)

          **Parameters:**:

          - **idp_id**: SAML IDentity provider configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/idps/{}".format(api_version,
                                                             idp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def interfaces(self, site_id, element_id, interface_id, data, api_version="v4.18"):
        """
        Update a Cellular Interface (v4.14)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v4.18)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}".format(api_version,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementshells_interfaces(self, site_id, elementshell_id, interface_id, data, api_version="v2.1"):
        """
        PUT elementshells_interfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **interface_id**: Interface ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}/interfaces/{}".format(api_version,
                                                                                             site_id,
                                                                                             elementshell_id,
                                                                                             interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfix(self, site_id, element_id, ipfix_id, data, api_version="v2.0"):
        """
        Update a IPFix Config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ipfix_id**: IPFix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ipfix/{}".format(api_version,
                                                                                   site_id,
                                                                                   element_id,
                                                                                   ipfix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixcollectorcontexts(self, ipfixcollectorcontext_id, data, api_version="v2.0"):
        """
        Update a IPFix Collector context (v2.0)

          **Parameters:**:

          - **ipfixcollectorcontext_id**: IPFix Collector Context ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixcollectorcontexts/{}".format(api_version,
                                                                               ipfixcollectorcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixfiltercontexts(self, ipfixfiltercontext_id, data, api_version="v2.0"):
        """
        Update a IPFix Filter context (v2.0)

          **Parameters:**:

          - **ipfixfiltercontext_id**: IPFix Filter Context ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixfiltercontexts/{}".format(api_version,
                                                                            ipfixfiltercontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixglobalprefixes(self, ipfixglobalprefix_id, data, api_version="v2.0"):
        """
        Update a IPFix Global prefix (v2.0)

          **Parameters:**:

          - **ipfixglobalprefix_id**: IPFix Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixglobalprefixes/{}".format(api_version,
                                                                            ipfixglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixprofiles(self, ipfixprofile_id, data, api_version="v2.0"):
        """
        Update a IPFix Profile (v2.0)

          **Parameters:**:

          - **ipfixprofile_id**: IPFix Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixprofiles/{}".format(api_version,
                                                                      ipfixprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipfixtemplates(self, ipfixtemplate_id, data, api_version="v2.0"):
        """
        Update a IPFix template (v2.0)

          **Parameters:**:

          - **ipfixtemplate_id**: IPFix Template ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixtemplates/{}".format(api_version,
                                                                       ipfixtemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ipsecprofiles(self, ipsecprofile_id, data, api_version="v2.1"):
        """
        Update a IPSECProfile (v2.1)

          **Parameters:**:

          - **ipsecprofile_id**: IPSEC Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles/{}".format(api_version,
                                                                      ipsecprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def lannetworks(self, site_id, lannetwork_id, data, api_version="v3.3"):
        """
        Update an existing LAN (v3.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: LAN Network ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/lannetworks/{}".format(api_version,
                                                                             site_id,
                                                                             lannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def localprefixfilters(self, localprefixfilter_id, data, api_version="v2.0"):
        """
        Update a new local prefix filter. (v2.0)

          **Parameters:**:

          - **localprefixfilter_id**: Local Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/localprefixfilters/{}".format(api_version,
                                                                           localprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def machine_cellular_modules_firmware(self, machine_id, cellular_module_id, data, api_version="v2.0"):
        """
        Update cellular module firmware configuration (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: Cellular Module ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/cellular_modules/{}/firmware".format(api_version,
                                                                                              machine_id,
                                                                                              cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def mstp_instances(self, site_id, element_id, mstp_instance_id, data, api_version="v2.0"):
        """
        PUT Mstp_Instances API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **mstp_instance_id**: MSTP Instance ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/mstp_instances/{}".format(api_version,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            mstp_instance_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def multicastglobalconfigs(self, site_id, element_id, multicastglobalconfig_id, data, api_version="v2.1"):
        """
        Update Multicast config (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastglobalconfig_id**: Multicast Global Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastglobalconfigs/{}".format(api_version,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    multicastglobalconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def multicastpeergroups(self, multicastpeergroup_id, data, api_version="v2.1"):
        """
        PUT Multicastpeergroups API Function

          **Parameters:**:

          - **multicastpeergroup_id**: Multicast Peer Group ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/multicastpeergroups/{}".format(api_version,
                                                                            multicastpeergroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def multicastrps(self, site_id, element_id, multicastrp_id, data, api_version="v2.0"):
        """
        Updates Multicast RP config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastrp_id**: Multicast RP ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastrps/{}".format(api_version,
                                                                                          site_id,
                                                                                          element_id,
                                                                                          multicastrp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def multicastsourcesiteconfigs(self, site_id, multicastsourcesiteconfig_id, data, api_version="v2.0"):
        """
        PUT Multicastsourcesiteconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **multicastsourcesiteconfig_id**: Multicast Source Site Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiteconfigs/{}".format(api_version,
                                                                                            site_id,
                                                                                            multicastsourcesiteconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natglobalprefixes(self, natglobalprefix_id, data, api_version="v2.0"):
        """
        Update an existing NAT prefix. (v2.0)

          **Parameters:**:

          - **natglobalprefix_id**: NAT Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natglobalprefixes/{}".format(api_version,
                                                                          natglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natlocalprefixes(self, natlocalprefix_id, data, api_version="v2.0"):
        """
        Update a  NAT local prefix. (v2.0)

          **Parameters:**:

          - **natlocalprefix_id**: NAT Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natlocalprefixes/{}".format(api_version,
                                                                         natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicypools(self, natpolicypool_id, data, api_version="v2.0"):
        """
        Update a  NAT Policy Pool. (v2.0)

          **Parameters:**:

          - **natpolicypool_id**: NAT Policy Pool ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicypools/{}".format(api_version,
                                                                       natpolicypool_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicyrules(self, natpolicyset_id, natpolicyrule_id, data, api_version="v2.0"):
        """
        Update policy rule of tenant. (v2.0)

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **natpolicyrule_id**: NAT Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}/natpolicyrules/{}".format(api_version,
                                                                                        natpolicyset_id,
                                                                                        natpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicysets(self, natpolicyset_id, data, api_version="v2.0"):
        """
        Update NAT policy set. (v2.0)

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}".format(api_version,
                                                                      natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natpolicysetstacks(self, natpolicysetstack_id, data, api_version="v2.0"):
        """
        Update NAT Policy Set Stack. (v2.0)

          **Parameters:**:

          - **natpolicysetstack_id**: NAT Policy Set Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysetstacks/{}".format(api_version,
                                                                           natpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def natzones(self, natzone_id, data, api_version="v2.0"):
        """
        Update a Nat Policy Zone. (v2.0)

          **Parameters:**:

          - **natzone_id**: NAT Zone ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natzones/{}".format(api_version,
                                                                 natzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkcontexts(self, networkcontext_id, data, api_version="v2.0"):
        """
        Update LAN segment (v2.0)

          **Parameters:**:

          - **networkcontext_id**: Network Context ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkcontexts/{}".format(api_version,
                                                                        networkcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id, data, api_version="v2.1"):
        """
        Update a Network global prefix. (v2.0)

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: Network Policy Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyglobalprefixes/{}".format(api_version,
                                                                                    networkpolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id, data, api_version="v2.2"):
        """
        Update network policy rule of tenant. (v2.1)

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: Network Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}/networkpolicyrules/{}".format(api_version,
                                                                                                networkpolicyset_id,
                                                                                                networkpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicysets(self, networkpolicyset_id, data, api_version="v2.0"):
        """
        Update Network Policy Set. (v2.0)

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}".format(api_version,
                                                                          networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicysetstacks(self, networkpolicysetstack_id, data, api_version="v2.0"):
        """
        Update a NetworkPolicySetStack (v2.0)

          **Parameters:**:

          - **networkpolicysetstack_id**: Network Policy Set Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysetstacks/{}".format(api_version,
                                                                               networkpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ngfwsecuritypolicyglobalprefixes(self, ngfwsecuritypolicyglobalprefix_id, data, api_version="v2.1"):
        """
        Update an existing Security Policy V2 Global Prefix (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicyglobalprefix_id**: NGFW Security Policy Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyglobalprefixes/{}".format(api_version,
                                                                                         ngfwsecuritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ngfwsecuritypolicylocalprefixes(self, ngfwsecuritypolicylocalprefix_id, data, api_version="v2.0"):
        """
        Update an existing Security Policy V2 Local Prefix (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicylocalprefix_id**: NGFW Security Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                        ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ngfwsecuritypolicyrules(self, ngfwsecuritypolicyset_id, ngfwsecuritypolicyrule_id, data, api_version="v2.1"):
        """
        Update an existing Security Policy V2 Rule under a policy set (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **ngfwsecuritypolicyrule_id**: NGFW Security Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules/{}".format(api_version,
                                                                                                          ngfwsecuritypolicyset_id,
                                                                                                          ngfwsecuritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ngfwsecuritypolicysets(self, ngfwsecuritypolicyset_id, data, api_version="v2.0"):
        """
        Update an existing Security Policy V2 Set (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}".format(api_version,
                                                                               ngfwsecuritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ngfwsecuritypolicysetstacks(self, ngfwsecuritypolicysetstack_id, data, api_version="v2.0"):
        """
        Update an existing Security Policy V2 Set Stack (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicysetstack_id**: NGFW Security Policy Set Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysetstacks/{}".format(api_version,
                                                                                    ngfwsecuritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ntp(self, element_id, ntp_id, data, api_version="v2.0"):
        """
        Update an existing element NTP. (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **ntp_id**: NTP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/ntp/{}".format(api_version,
                                                                        element_id,
                                                                        ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ospfconfigs(self, site_id, element_id, ospfconfig_id, data, api_version="v2.0"):
        """
        PUT Ospfconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ospfconfig_id**: OSPF Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfconfigs/{}".format(api_version,
                                                                                         site_id,
                                                                                         element_id,
                                                                                         ospfconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ospfglobalconfigs(self, site_id, element_id, ospfglobalconfig_id, data, api_version="v2.0"):
        """
        PUT Ospfglobalconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ospfglobalconfig_id**: OSPF Global Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfglobalconfigs/{}".format(api_version,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               ospfglobalconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def otpaccessconfigs(self, otpaccessconfig_id, data, api_version="v2.0"):
        """
        Update an OTP Access for all elements under an Tenant. (v2.0)

          **Parameters:**:

          - **otpaccessconfig_id**: OTP Access configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/otpaccessconfigs/{}".format(api_version,
                                                                         otpaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def pathgroups(self, pathgroup_id, data, api_version="v2.1"):
        """
        Update A Path Group of a tenant. (v2.1)

          **Parameters:**:

          - **pathgroup_id**: Path Group ID (for network service/DC routing)
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/pathgroups/{}".format(api_version,
                                                                   pathgroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def perfmgmtpolicysets(self, perfmgmtpolicyset_id, data, api_version="v2.0"):
        """
        PUT Perfmgmtpolicysets API Function

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}".format(api_version,
                                                                           perfmgmtpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def perfmgmtpolicysets_perfmgmtpolicyrules(self, perfmgmtpolicyset_id, perfmgmtpolicyrule_id, data, api_version="v2.1"):
        """
        PUT Perfmgmtpolicysets_Perfmgmtpolicyrules API Function

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **perfmgmtpolicyrule_id**: Performance Management Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}/perfmgmtpolicyrules/{}".format(api_version,
                                                                                                  perfmgmtpolicyset_id,
                                                                                                  perfmgmtpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def perfmgmtpolicysetstacks(self, perfmgmtpolicysetstack_id, data, api_version="v2.0"):
        """
        PUT Perfmgmtpolicysetstacks API Function

          **Parameters:**:

          - **perfmgmtpolicysetstack_id**: Performance Management Policy Set Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysetstacks/{}".format(api_version,
                                                                                perfmgmtpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def perfmgmtthresholdprofiles(self, perfmgmtthresholdprofile_id, data, api_version="v2.1"):
        """
        PUT Perfmgmtthresholdprofiles API Function

          **Parameters:**:

          - **perfmgmtthresholdprofile_id**: Performance Management Threshold Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtthresholdprofiles/{}".format(api_version,
                                                                                  perfmgmtthresholdprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def policyrules(self, policyset_id, policyrule_id, data, api_version="v3.1"):
        """
        Update policy rule of tenant. (v3.1)

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **policyrule_id**: Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}/policyrules/{}".format(api_version,
                                                                                  policyset_id,
                                                                                  policyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def policysets(self, policyset_id, data, api_version="v3.0"):
        """
        Update policy set. (v3.0)

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}".format(api_version,
                                                                   policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prefixfilters(self, site_id, prefixfilter_id, data, api_version="v2.0"):
        """
        Update an existing security prefix filter (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixfilter_id**: Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters/{}".format(api_version,
                                                                               site_id,
                                                                               prefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id, data, api_version="v2.1"):
        """
        Update a  Priority global prefix. (v2.0)

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: Priority Policy Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyglobalprefixes/{}".format(api_version,
                                                                                     prioritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id, data, api_version="v2.1"):
        """
        Update priority policy rule of tenant. (v2.0)

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: Priority Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}/prioritypolicyrules/{}".format(api_version,
                                                                                                  prioritypolicyset_id,
                                                                                                  prioritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicysets(self, prioritypolicyset_id, data, api_version="v2.0"):
        """
        Update Priority Policy Set. (v2.0)

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}".format(api_version,
                                                                           prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicysetstacks(self, prioritypolicysetstack_id, data, api_version="v2.0"):
        """
        Update a PriorityPolicySetStack (v2.0)

          **Parameters:**:

          - **prioritypolicysetstack_id**: Priority Policy Stack ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysetstacks/{}".format(api_version,
                                                                                prioritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prismaaccess_configs(self, site_id, prismaaccess_config_id, data, api_version="v2.0"):
        """
        Update a Prisma Access Config with remote networks and security processing node (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prismaaccess_config_id**: Prisma Acceess Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismaaccess_configs/{}".format(api_version,
                                                                                      site_id,
                                                                                      prismaaccess_config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prismasase_connections(self, site_id, prismasase_connection_id, data, api_version="v2.1"):
        """
        PUT Prismasase_Connections API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **prismasase_connection_id**: Prisma SASE Connection ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismasase_connections/{}".format(api_version,
                                                                                        site_id,
                                                                                        prismasase_connection_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prismasase_connections_configs(self, data, api_version="v2.1"):
        """
        PUT Prismasase_Connections_Configs API Function

          **Parameters:**:

          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismasase_connections/configs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def probeconfigs(self, probeconfig_id, data, api_version="v2.0"):
        """
        PUT Probeconfigs API Function

          **Parameters:**:

          - **probeconfig_id**: Probe Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeconfigs/{}".format(api_version,
                                                                     probeconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def probeprofiles(self, probeprofile_id, data, api_version="v2.0"):
        """
        PUT Probeprofiles API Function

          **Parameters:**:

          - **probeprofile_id**: Probe Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/probeprofiles/{}".format(api_version,
                                                                      probeprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def radii(self, element_id, radii_id, data, api_version="v2.0"):
        """
        PUT Radii API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **radii_id**: Radii ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/radii/{}".format(api_version,
                                                                          element_id,
                                                                          radii_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def recovery_tokens(self, machine_id, recovery_token_id, data, api_version="v2.1"):
        """
        Update Recovery Token for Fips change mode (v2.1)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **recovery_token_id**: Recovery Token ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/recovery_tokens/{}".format(api_version,
                                                                                    machine_id,
                                                                                    recovery_token_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def roles(self, role_id, data, api_version="v2.1"):
        """
        Update a custom role (v2.1)

          **Parameters:**:

          - **role_id**: Role ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/roles/{}".format(api_version,
                                                              role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_aspathaccesslists(self, site_id, element_id, routing_aspathaccesslist_id, data, api_version="v2.1"):
        """
        Updates Access List (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_aspathaccesslist_id**: Routing AS-PATH Access List ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_aspathaccesslists/{}".format(api_version,
                                                                                                       site_id,
                                                                                                       element_id,
                                                                                                       routing_aspathaccesslist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_ipcommunitylists(self, site_id, element_id, routing_ipcommunitylist_id, data, api_version="v2.0"):
        """
        Updates Community List (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_ipcommunitylist_id**: Routing IP Community List ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_ipcommunitylists/{}".format(api_version,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      routing_ipcommunitylist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_prefixlists(self, site_id, element_id, routing_prefixlist_id, data, api_version="v2.1"):
        """
        Updates Prefix List (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_prefixlist_id**: Routing IP Prefix List ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_prefixlists/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 routing_prefixlist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_routemaps(self, site_id, element_id, routing_routemap_id, data, api_version="v2.3"):
        """
        Updates Route Map (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_routemap_id**: Routing Route Map ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_routemaps/{}".format(api_version,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               routing_routemap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def sdwanapps_configs(self, sdwanapp_id, config_id, data, api_version="v2.0"):
        """
        PUT Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **config_id**: SDWAN App Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/configs/{}".format(api_version,
                                                                             sdwanapp_id,
                                                                             config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def securitypolicyrules(self, securitypolicyset_id, securitypolicyrule_id, data, api_version="v2.0"):
        """
        Update a tenant security policy rule. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **securitypolicyrule_id**: Security Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}/securitypolicyrules/{}".format(api_version,
                                                                                                  securitypolicyset_id,
                                                                                                  securitypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def securitypolicysets(self, securitypolicyset_id, data, api_version="v2.0"):
        """
        Update a tenant security policy set. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}".format(api_version,
                                                                           securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def securityzones(self, securityzone_id, data, api_version="v2.0"):
        """
        Update an existing security zone (v2.0)

          **Parameters:**:

          - **securityzone_id**: Security Zone (ZBFW) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/securityzones/{}".format(api_version,
                                                                      securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def servicebindingmaps(self, servicebindingmap_id, data, api_version="v2.1"):
        """
        Update a ServiceBindingMap (v2.1)

          **Parameters:**:

          - **servicebindingmap_id**: Service Binding Map ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicebindingmaps/{}".format(api_version,
                                                                           servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def serviceendpoints(self, serviceendpoint_id, data, api_version="v2.4"):
        """
        Update a ServiceEndpoint (v2.3)

          **Parameters:**:

          - **serviceendpoint_id**: Service Endpoint ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/serviceendpoints/{}".format(api_version,
                                                                         serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def servicelabels(self, servicelabel_id, data, api_version="v2.1"):
        """
        Update a ServiceLabel (v2.1)

          **Parameters:**:

          - **servicelabel_id**: Service Label ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/servicelabels/{}".format(api_version,
                                                                      servicelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_admin_state(self, site_id, data, api_version="v3.0"):
        """
        Update an existing site (v3.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/admin_state".format(api_version,
                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_extensions(self, site_id, extension_id, data, api_version="v2.0"):
        """
        Update site level extension configuration (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/extensions/{}".format(api_version,
                                                                            site_id,
                                                                            extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_ipfixlocalprefixes(self, site_id, ipfixlocalprefix_id, data, api_version="v2.0"):
        """
        Update a IPFix site prefix association (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                    site_id,
                                                                                    ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_natlocalprefixes(self, site_id, natlocalprefix_id, data, api_version="v2.0"):
        """
        Update an existing Site NAT Local prefix Association (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **natlocalprefix_id**: NAT Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/natlocalprefixes/{}".format(api_version,
                                                                                  site_id,
                                                                                  natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id, data, api_version="v2.1"):
        """
        Update an existing Site Network policy local prefix (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                            site_id,
                                                                                            networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_ngfwsecuritypolicylocalprefixes(self, site_id, ngfwsecuritypolicylocalprefix_id, data, api_version="v2.1"):
        """
        Update an existing security policy V2 local prefix site association (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **ngfwsecuritypolicylocalprefix_id**: NGFW Security Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id, data, api_version="v2.1"):
        """
        Update an existing Site Priority policy local prefix (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                             site_id,
                                                                                             prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def siteciphers(self, site_id, data, api_version="v2.0"):
        """
        Update site cipher (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/siteciphers".format(api_version,
                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def sites(self, site_id, data, api_version="v4.10"):
        """
        Update an existing site (v4.7)

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v4.10)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}".format(api_version,
                                                              site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def sitesecurityzones(self, site_id, sitesecurityzone_id, data, api_version="v2.0"):
        """
        Update an existing security zone (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **sitesecurityzone_id**: Site Security Zone ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/sitesecurityzones/{}".format(api_version,
                                                                                   site_id,
                                                                                   sitesecurityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def snmpagents(self, site_id, element_id, snmpagent_id, data, api_version="v2.1"):
        """
        Update SNMP Agent (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: SNMP Agent ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmpagents/{}".format(api_version,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        snmpagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def snmptraps(self, site_id, element_id, snmptrap_id, data, api_version="v2.0"):
        """
        Update SNMP Trap (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmptrap_id**: SNMP Trap ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmptraps/{}".format(api_version,
                                                                                       site_id,
                                                                                       element_id,
                                                                                       snmptrap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def software(self, machine_id, software_id, data, api_version="v2.0"):
        """
        Update Machine Software (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **software_id**: Software ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/software/{}".format(api_version,
                                                                             machine_id,
                                                                             software_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def software_state(self, element_id, data, api_version="v2.0"):
        """
        Upgrade an element (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/software/state".format(api_version,
                                                                                element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def spokeclusters(self, site_id, spokecluster_id, data, api_version="v2.0"):
        """
        Update Spoke Cluster (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/{}".format(api_version,
                                                                               site_id,
                                                                               spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def staticroutes(self, site_id, element_id, staticroute_id, data, api_version="v2.3"):
        """
        Update static route (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/staticroutes/{}".format(api_version,
                                                                                          site_id,
                                                                                          element_id,
                                                                                          staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def syslogserverprofiles(self, syslogserverprofile_id, data, api_version="v2.0"):
        """
        Update Syslog Server Profile (v2.0)

          **Parameters:**:

          - **syslogserverprofile_id**: Sys Log Server Profile ID 
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/syslogserverprofiles/{}".format(api_version,
                                                                             syslogserverprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def syslogservers(self, site_id, element_id, syslogserver_id, data, api_version="v2.2"):
        """
        Update Syslog Server (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: SYSLOG server ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/syslogservers/{}".format(api_version,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           syslogserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def templates_ntp(self, ntp_id, data, api_version="v2.0"):
        """
        Update an existing NTP Template (v2.0)

          **Parameters:**:

          - **ntp_id**: NTP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/templates/ntp/{}".format(api_version,
                                                                      ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_anynetlinks(self, anynetlink_id, data, api_version="v3.4"):
        """
        PUT Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v3.4)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks/{}".format(api_version,
                                                                    anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_ipfixlocalprefixes(self, ipfixlocalprefix_id, data, api_version="v2.0"):
        """
        Update a IPFix local prefix (v2.0)

          **Parameters:**:

          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ipfixlocalprefixes/{}".format(api_version,
                                                                           ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_networkpolicylocalprefixes(self, networkpolicylocalprefix_id, data, api_version="v2.0"):
        """
        Update a  Network Policy local prefix. (v2.0)

          **Parameters:**:

          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicylocalprefixes/{}".format(api_version,
                                                                                   networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_operators(self, operator_id, data, api_version="v2.2"):
        """
        Update a tenant operator (v2.1)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}".format(api_version,
                                                                  operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_permissions(self, permission_id, data, api_version="v2.0"):
        """
        Update a custom permission (v2.0)

          **Parameters:**:

          - **permission_id**: Permission ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/permissions/{}".format(api_version,
                                                                    permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_prioritypolicylocalprefixes(self, prioritypolicylocalprefix_id, data, api_version="v2.0"):
        """
        Update a  Priority Policy local prefix. (v2.0)

          **Parameters:**:

          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                    prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenants(self, data, api_version="v2.9"):
        """
        Update tenant (v2.3)

          **Parameters:**:

          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.9)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def useridagents(self, useridagent_id, data, api_version="v2.0"):
        """
        PUT Useridagents API Function

          **Parameters:**:

          - **useridagent_id**: User Id Agent ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/useridagents/{}".format(api_version,
                                                                     useridagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def users(self, user_id, data, api_version="v2.0"):
        """
        Put an user identity. (v2.0)

          **Parameters:**:

          - **user_id**: User ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/users/{}".format(api_version,
                                                              user_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def vfflicense_tokens(self, vfflicense_id, token_id, data, api_version="v2.0"):
        """
        Update Tenant Vff License Token (v2.0)

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **token_id**: Token ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}/tokens/{}".format(api_version,
                                                                              vfflicense_id,
                                                                              token_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def vpnlinks_state(self, vpnlink_id, data, api_version="v2.0"):
        """
        Change the VPNLink admin state (v2.0)

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vpnlinks/{}/state".format(api_version,
                                                                       vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def vrfcontextprofiles(self, vrfcontextprofile_id, data, api_version="v2.0"):
        """
        PUT Vrfcontextprofiles API Function

          **Parameters:**:

          - **vrfcontextprofile_id**: VRF Context Profile ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontextprofiles/{}".format(api_version,
                                                                           vrfcontextprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def vrfcontexts(self, vrfcontext_id, data, api_version="v2.0"):
        """
        PUT Vrfcontexts API Function

          **Parameters:**:

          - **vrfcontext_id**: VRF Context ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontexts/{}".format(api_version,
                                                                    vrfcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def waninterfacelabels(self, waninterfacelabel_id, data, api_version="v2.5"):
        """
        Update specific WAN interface label (v2.4)

          **Parameters:**:

          - **waninterfacelabel_id**: WAN Interface Label ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/waninterfacelabels/{}".format(api_version,
                                                                           waninterfacelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def waninterfaces(self, site_id, waninterface_id, data, api_version="v2.8"):
        """
        Update the Site WAN interface (v2.7)

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.8)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces/{}".format(api_version,
                                                                               site_id,
                                                                               waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def wannetworks(self, wannetwork_id, data, api_version="v2.1"):
        """
        Update an existing WAN (v2.1)

          **Parameters:**:

          - **wannetwork_id**: WAN Network ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wannetworks/{}".format(api_version,
                                                                    wannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def wanoverlays(self, wanoverlay_id, data, api_version="v2.0"):
        """
        Update app/wan context (v2.0)

          **Parameters:**:

          - **wanoverlay_id**: WAN Overlay ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/wanoverlays/{}".format(api_version,
                                                                    wanoverlay_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ws_extensions(self, extension_id, data, api_version="v2.0"):
        """
        PUT Ws_Extensions API Function

          **Parameters:**:

          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/ws/extensions/{}".format(api_version,
                                                                      extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    access_elementusers = elementusers_access
    """ Backwards-compatibility alias of `access_elementusers` to `elementusers_access`"""

    admin_state_i = element_admin_state
    """ Backwards-compatibility alias of `admin_state_i` to `element_admin_state`"""

    admin_state_s = site_admin_state
    """ Backwards-compatibility alias of `admin_state_s` to `site_admin_state`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    cellular_modules_e = element_cellular_modules
    """ Backwards-compatibility alias of `cellular_modules_e` to `element_cellular_modules`"""

    configs_prismasase_connections = prismasase_connections_configs
    """ Backwards-compatibility alias of `configs_prismasase_connections` to `prismasase_connections_configs`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    deviceidconfigs_i = element_deviceidconfigs
    """ Backwards-compatibility alias of `deviceidconfigs_i` to `element_deviceidconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    firmware_cellular_modules_e = element_cellular_modules_firmware
    """ Backwards-compatibility alias of `firmware_cellular_modules_e` to `element_cellular_modules_firmware`"""

    firmware_cellular_modules_m = machine_cellular_modules_firmware
    """ Backwards-compatibility alias of `firmware_cellular_modules_m` to `machine_cellular_modules_firmware`"""

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

    sim_security_cellular_modules = cellular_modules_sim_security
    """ Backwards-compatibility alias of `sim_security_cellular_modules` to `cellular_modules_sim_security`"""

    sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates
    """ Backwards-compatibility alias of `sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates`"""

    snmpdiscoverystartnodes_deviceidconfigs = deviceidconfigs_snmpdiscoverystartnodes
    """ Backwards-compatibility alias of `snmpdiscoverystartnodes_deviceidconfigs` to `deviceidconfigs_snmpdiscoverystartnodes`"""

    state = element_state
    """ Backwards-compatibility alias of `state` to `element_state`"""

    state_software = software_state
    """ Backwards-compatibility alias of `state_software` to `software_state`"""

    state_vpnlinks = vpnlinks_state
    """ Backwards-compatibility alias of `state_vpnlinks` to `vpnlinks_state`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

