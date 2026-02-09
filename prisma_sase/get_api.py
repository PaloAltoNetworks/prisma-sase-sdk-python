#!/usr/bin/env python
"""
PRISMA SASE Python SDK - GET

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


class Get(object):
    """
    Prisma SASE API - GET requests

    Object to handle making Get requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def aaa_metrics_monitor(self, api_version="v2.0"):
        """
        GET Aaa_Metrics_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aaa_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def advertisedprefixes_bgppeers(self, site_id, element_id, bgppeer_id, api_version="v2.1"):
        """
        GET Advertisedprefixes_Bgppeers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}/advertisedprefixes".format(api_version,
                                                                                                         site_id,
                                                                                                         element_id,
                                                                                                         bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def aggregates_aiops_monitor(self, api_version="v2.1"):
        """
        GET Aggregates_Aiops_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/aggregates".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def aggregates_monitor(self, api_version="v3.0"):
        """
        GET Aggregates_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aggregates".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def anomaly_aiops_monitor(self, api_version="v2.0"):
        """
        GET Anomaly_Aiops_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/anomaly".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def anynetlinks_s(self, site_id, anynetlink_id, api_version="v2.0"):
        """
        GET Anynetlinks_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/anynetlinks/{}".format(api_version,
                                                                             site_id,
                                                                             anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def apnprofiles(self, apnprofile_id=None, api_version="v2.0"):
        """
        Get all APN Profiles (v2.0)

          **Parameters:**:

          - **apnprofile_id**: (optional) APN Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not apnprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/apnprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/apnprofiles/{}".format(api_version,
                                                                        apnprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appaccelerationstatus(self, site_id, api_version="v2.0"):
        """
        Get site App Acceleration status for a tenant (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/appaccelerationstatus".format(api_version,
                                                                                    site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs(self, appdef_id=None, api_version="v2.6"):
        """
        Get all application definitions (v2.6)

          **Parameters:**:

          - **appdef_id**: (optional) Application Definition ID
          - **api_version**: API version to use (default v2.6)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not appdef_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/appdefs".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}".format(api_version,
                                                                    appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs_overrides(self, appdef_id, override_id=None, api_version="v2.3"):
        """
        Get application definition overrides for system appdef (v2.3)

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: (optional) AppDef Override ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not override_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}/overrides".format(api_version,
                                                                              appdef_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/appdefs/{}/overrides/{}".format(api_version,
                                                                                 appdef_id,
                                                                                 override_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs_version(self, appdefs_version_id=None, api_version="v2.2"):
        """
        Get application version for a tenant (v2.2)

          **Parameters:**:

          - **appdefs_version_id**: (optional) Application Definition Version ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not appdefs_version_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/appdefs_version".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/appdefs_version/{}".format(api_version,
                                                                            appdefs_version_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def application_probe(self, site_id, element_id, api_version="v2.0"):
        """
        Get application probe configuration of element (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/application_probe".format(api_version,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appstatus_sdwanapps(self, sdwanapp_id, appstatus_id, api_version="v2.0"):
        """
        GET Appstatus_Sdwanapps API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **appstatus_id**: SDWAN App Status ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/appstatus/{}".format(api_version,
                                                                               sdwanapp_id,
                                                                               appstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def auditlog(self, auditlog_id=None, api_version="v2.1"):
        """
        GET Auditlog API Function

          **Parameters:**:

          - **auditlog_id**: (optional) Audit Log ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not auditlog_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/auditlog".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/auditlog/{}".format(api_version,
                                                                     auditlog_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def authtokens(self, operator_id, authtoken_id=None, api_version="v2.1"):
        """
        Get a list of auth tokens (v2.1)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **authtoken_id**: (optional) Static AUTH_TOKEN ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not authtoken_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/authtokens".format(api_version,
                                                                                 operator_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/authtokens/{}".format(api_version,
                                                                                    operator_id,
                                                                                    authtoken_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def base_permissions(self, api_version="v2.0"):
        """
        Get a list of tenant base permissions (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/base_permissions".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def base_roles(self, api_version="v2.0"):
        """
        Get a list of tenant base roles (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/base_roles".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def base_roles_clients(self, client_id, api_version="v2.0"):
        """
        GET Base_Roles_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/base_roles".format(api_version,
                                                                           client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bfdpeers(self, site_id, api_version="v3.0"):
        """
        GET Bfdpeers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/bfdpeers".format(api_version,
                                                                       site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgpconfigs(self, site_id, element_id, bgpconfig_id=None, api_version="v2.5"):
        """
        Get all BGP configs (v2.5)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgpconfig_id**: (optional) BGP Configuration ID
          - **api_version**: API version to use (default v2.5)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not bgpconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgpconfigs".format(api_version,
                                                                                         site_id,
                                                                                         element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgpconfigs/{}".format(api_version,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            bgpconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgppeers(self, site_id, element_id, bgppeer_id=None, api_version="v3.0"):
        """
        Get all BGP Peer configs (v3.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: (optional) BGP Peer ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not bgppeer_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers".format(api_version,
                                                                                       site_id,
                                                                                       element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}".format(api_version,
                                                                                          site_id,
                                                                                          element_id,
                                                                                          bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bulk_metrics_monitor(self, bulk_metric_id, api_version="v2.0"):
        """
        GET Bulk_Metrics_Monitor API Function

          **Parameters:**:

          - **bulk_metric_id**: Bulk Metric ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/bulk_metrics/{}".format(api_version,
                                                                                     bulk_metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bulkconfigurations_deployments_sitetemplates(self, sitetemplate_id, deployment_id, api_version="v2.0"):
        """
        GET Bulkconfigurations_Deployments_Sitetemplates API Function

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
        return self._parent_class.rest_call(url, "get")

    def bulkconfigurations_sitetemplates(self, sitetemplate_id, api_version="v2.0"):
        """
        Get site profile (v2.0)

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}".format(api_version,
                                                                                         sitetemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def cellular_metrics_monitor(self, api_version="v2.0"):
        """
        GET Cellular_Metrics_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/cellular_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def cellular_module_images(self, cellular_module_image_id=None, api_version="v2.1"):
        """
        Get existing element cellular module images (v2.1)

          **Parameters:**:

          - **cellular_module_image_id**: (optional) Cellular Module Image ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not cellular_module_image_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/cellular_module_images".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/cellular_module_images/{}".format(api_version,
                                                                                   cellular_module_image_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def cellular_modules_m(self, machine_id, cellular_module_id=None, api_version="v2.0"):
        """
        GET Cellular_Modules_M API Function

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: (optional) Cellular Module ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not cellular_module_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/cellular_modules".format(api_version,
                                                                                      machine_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/cellular_modules/{}".format(api_version,
                                                                                         machine_id,
                                                                                         cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def cellular_modules_sim_security(self, element_id, cellular_module_id, sim_security_id=None, api_version="v2.0"):
        """
        Get all cellular modules sim security info (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **sim_security_id**: (optional) SIM Security ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not sim_security_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}/sim_security".format(api_version,
                                                                                                      element_id,
                                                                                                      cellular_module_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}/sim_security/{}".format(api_version,
                                                                                                         element_id,
                                                                                                         cellular_module_id,
                                                                                                         sim_security_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def certificates(self, entitie_id, api_version="v2.0"):
        """
        GET Certificates API Function

          **Parameters:**:

          - **entitie_id**: Entitie ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/entities/{}/certificates".format(api_version,
                                                                              entitie_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def certificates_tenants(self, certificate_id=None, api_version="v2.0"):
        """
        GET Certificates_Tenants API Function

          **Parameters:**:

          - **certificate_id**: (optional) Certificate ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not certificate_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/certificates".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/certificates/{}".format(api_version,
                                                                         certificate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def clients_t(self, api_version="v2.1"):
        """
        GET Clients_T API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/clients".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def connectivity_appstatus_sdwanapps(self, sdwanapp_id, api_version="v2.0"):
        """
        GET Connectivity_Appstatus_Sdwanapps API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/appstatus/connectivity".format(api_version,
                                                                                         sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def copy_element_configurations_elementshells_status(self, site_id, elementshell_id, api_version="v2.0"):
        """
        GET Copy_Element_Configurations_Elementshells_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}/copy_element_configurations/status".format(api_version,
                                                                                                                  site_id,
                                                                                                                  elementshell_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def correlationevents_anynetlinks(self, anynetlink_id, api_version="v2.2"):
        """
        GET Correlationevents_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks/{}/correlationevents".format(api_version,
                                                                                      anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def correlationevents_e(self, site_id, element_id, api_version="v2.1"):
        """
        GET Correlationevents_E API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/correlationevents".format(api_version,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def correlationevents_interfaces(self, site_id, element_id, interface_id, api_version="v2.1"):
        """
        GET Correlationevents_Interfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}/correlationevents".format(api_version,
                                                                                                          site_id,
                                                                                                          element_id,
                                                                                                          interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def correlationevents_s(self, site_id, api_version="v2.1"):
        """
        GET Correlationevents_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/correlationevents".format(api_version,
                                                                                site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def correlationevents_waninterfaces(self, site_id, waninterface_id, api_version="v2.1"):
        """
        GET Correlationevents_Waninterfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces/{}/correlationevents".format(api_version,
                                                                                                 site_id,
                                                                                                 waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def cuid_status(self, api_version="v2.0"):
        """
        GET Status_Cuid API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/cuid/status".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def demsiteconfigs(self, site_id, demsiteconfig_id=None, api_version="v2.0"):
        """
        Get all ADEM status for a site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **demsiteconfig_id**: (optional) DEM Site Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not demsiteconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/demsiteconfigs".format(api_version,
                                                                                 site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/demsiteconfigs/{}".format(api_version,
                                                                                    site_id,
                                                                                    demsiteconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def demstatus(self, site_id, demstatus_id=None, api_version="v2.0"):
        """
        Get all ADEM status for a site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **demstatus_id**: (optional) DEM Status ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not demstatus_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/demstatus".format(api_version,
                                                                            site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/demstatus/{}".format(api_version,
                                                                               site_id,
                                                                               demstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def deployments_sitetemplates_bulkconfigurations_status(self, sitetemplate_id, deployment_id, api_version="v2.0"):
        """
        GET Deployments_Sitetemplates_Bulkconfigurations_Status API Function

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **deployment_id**: Deployment ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}/deployments/{}/status".format(api_version,
                                                                                                               sitetemplate_id,
                                                                                                               deployment_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def deviceidconfigs(self, site_id, element_id, deviceidconfig_id=None, api_version="v2.0"):
        """
        GET Deviceidconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **deviceidconfig_id**: (optional) Device Id Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not deviceidconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/deviceidconfigs".format(api_version,
                                                                                              site_id,
                                                                                              element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/deviceidconfigs/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def deviceidconfigs_snmpdiscoverystartnodes(self, site_id, deviceidconfig_id, snmpdiscoverystartnode_id=None, api_version="v2.0"):
        """
        Get all Start Network Node config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: Device Id Config ID
          - **snmpdiscoverystartnode_id**: (optional) SNMP Discovery Start Node ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not snmpdiscoverystartnode_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}/snmpdiscoverystartnodes".format(api_version,
                                                                                                             site_id,
                                                                                                             deviceidconfig_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/deviceidconfigs/{}/snmpdiscoverystartnodes/{}".format(api_version,
                                                                                                                site_id,
                                                                                                                deviceidconfig_id,
                                                                                                                snmpdiscoverystartnode_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def deviceidprofiles(self, deviceidprofile_id=None, api_version="v2.0"):
        """
        Get device id profiles (v2.0)

          **Parameters:**:

          - **deviceidprofile_id**: (optional) Device Id Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not deviceidprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/deviceidprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/deviceidprofiles/{}".format(api_version,
                                                                             deviceidprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dhcpservers(self, site_id, dhcpserver_id=None, api_version="v2.3"):
        """
        Get all DHCPServers for a Tenant on a site (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: (optional) DHCP Server ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not dhcpserver_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/dhcpservers".format(api_version,
                                                                              site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/dhcpservers/{}".format(api_version,
                                                                                 site_id,
                                                                                 dhcpserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def directoryservices(self, api_version="v2.1"):
        """
        Get directory service details of tenant (v2.1)

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def directoryusergroups(self, directoryusergroup_id=None, api_version="v2.0"):
        """
        Get users or groups of tenant (v2.0)

          **Parameters:**:

          - **directoryusergroup_id**: (optional) Directory User Group Id
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not directoryusergroup_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/directoryusergroups".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/directoryusergroups/{}".format(api_version,
                                                                                directoryusergroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def directoryusers(self, directoryuser_id=None, api_version="v2.1"):
        """
        Get users of tenant (v2.1)

          **Parameters:**:

          - **directoryuser_id**: (optional) Directory User ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not directoryuser_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/directoryusers".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/directoryusers/{}".format(api_version,
                                                                           directoryuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def discoveredprefixes_bgppeers(self, site_id, element_id, bgppeer_id, api_version="v2.2"):
        """
        GET Discoveredprefixes_Bgppeers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}/discoveredprefixes".format(api_version,
                                                                                                         site_id,
                                                                                                         element_id,
                                                                                                         bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnssecuritycategories(self, dnssecuritycategorie_id=None, api_version="v2.0"):
        """
        Get all the DNSCategories that are supported, this is a global resource (v2.0)

          **Parameters:**:

          - **dnssecuritycategorie_id**: (optional) DNS Security Categorie ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not dnssecuritycategorie_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnssecuritycategories".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnssecuritycategories/{}".format(api_version,
                                                                                  dnssecuritycategorie_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnssecurityprofiles(self, dnssecurityprofile_id=None, api_version="v2.0"):
        """
        Get all DNSSec profiles for a tenant (v2.0)

          **Parameters:**:

          - **dnssecurityprofile_id**: (optional) DNS Security Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not dnssecurityprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnssecurityprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnssecurityprofiles/{}".format(api_version,
                                                                                dnssecurityprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnsserviceprofiles(self, dnsserviceprofile_id=None, api_version="v2.1"):
        """
        Read all DNS service profiles (v2.1)

          **Parameters:**:

          - **dnsserviceprofile_id**: (optional) DNS Service Profile ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not dnsserviceprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceprofiles/{}".format(api_version,
                                                                               dnsserviceprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnsserviceroles(self, dnsservicerole_id=None, api_version="v2.0"):
        """
        Read all DNS service roles (v2.0)

          **Parameters:**:

          - **dnsservicerole_id**: (optional) DNS Service Role ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not dnsservicerole_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceroles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/dnsserviceroles/{}".format(api_version,
                                                                            dnsservicerole_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnsservices(self, site_id, element_id, dnsservice_id=None, api_version="v2.0"):
        """
        Read all DNS service configs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **dnsservice_id**: (optional) DNS Service ID 
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not dnsservice_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/dnsservices".format(api_version,
                                                                                          site_id,
                                                                                          element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/dnsservices/{}".format(api_version,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             dnsservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def domainstatus_directoryservices(self, directoryservice_id, domainstatus_id, api_version="v2.0"):
        """
        GET Domainstatus_Directoryservices API Function

          **Parameters:**:

          - **directoryservice_id**: Directory Service ID
          - **domainstatus_id**: Domain Status ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices/{}/domainstatus/{}".format(api_version,
                                                                                          directoryservice_id,
                                                                                          domainstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_cellular_modules(self, element_id, cellular_module_id=None, api_version="v2.0"):
        """
        Get all cellular modules (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: (optional) Cellular Module ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not cellular_module_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules".format(api_version,
                                                                                      element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}".format(api_version,
                                                                                         element_id,
                                                                                         cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_cellular_modules_firmware(self, element_id, cellular_module_id, api_version="v2.0"):
        """
        Get cellular module firmware configuration (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}/firmware".format(api_version,
                                                                                              element_id,
                                                                                              cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_extensions(self, site_id, element_id, extension_id=None, api_version="v2.0"):
        """
        Get all element level extensions (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **extension_id**: (optional) Extension ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not extension_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/extensions".format(api_version,
                                                                                         site_id,
                                                                                         element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/extensions/{}".format(api_version,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_images(self, element_image_id=None, api_version="v2.4"):
        """
        Get existing machine images (v2.4)

          **Parameters:**:

          - **element_image_id**: (optional) Element Code Image ID
          - **api_version**: API version to use (default v2.4)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not element_image_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/element_images".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/element_images/{}".format(api_version,
                                                                           element_image_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_passages(self, element_id, passage_id=None, api_version="v2.0"):
        """
        GET Element_Passages API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **passage_id**: (optional) Passage Configuration ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not passage_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/passages".format(api_version,
                                                                              element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/passages/{}".format(api_version,
                                                                                 element_id,
                                                                                 passage_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_state(self, element_id, api_version="v2.0"):
        """
        Get element state (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/state".format(api_version,
                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementaccessconfigs(self, element_id, elementaccessconfig_id=None, api_version="v2.2"):
        """
        Get all Element Access Configs (v2.2)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementaccessconfig_id**: (optional) Element Access Config ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not elementaccessconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/elementaccessconfigs".format(api_version,
                                                                                          element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/elementaccessconfigs/{}".format(api_version,
                                                                                             element_id,
                                                                                             elementaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementaccessstates(self, element_id, api_version="v2.0"):
        """
        Get specific element's Access State (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/elementaccessstates".format(api_version,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementmodels(self, api_version="v3.7"):
        """
        Get all element models (v3.7)

          **Parameters:**:

          - **api_version**: API version to use (default v3.7)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementmodels".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementpassageconfigs(self, element_id, api_version="v2.0"):
        """
        GET Elementpassageconfigs API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/elementpassageconfigs".format(api_version,
                                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementpassageconfigs_t(self, api_version="v2.0"):
        """
        GET Elementpassageconfigs_T API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementpassageconfigs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elements(self, element_id=None, api_version="v3.2"):
        """
        Get Elements of a tenant (v3.2)

          **Parameters:**:

          - **element_id**: (optional) Element (Device) ID
          - **api_version**: API version to use (default v3.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not element_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}".format(api_version,
                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementsecurityzones(self, site_id, element_id, securityzone_id=None, api_version="v2.0"):
        """
        Get element security zones (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **securityzone_id**: (optional) Security Zone (ZBFW) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not securityzone_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/securityzones".format(api_version,
                                                                                            site_id,
                                                                                            element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/securityzones/{}".format(api_version,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementshells(self, site_id, elementshell_id=None, api_version="v2.1"):
        """
        Get All Element Shells (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: (optional) Element Shell ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not elementshell_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells".format(api_version,
                                                                                site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}".format(api_version,
                                                                                   site_id,
                                                                                   elementshell_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementsystemlimitprofiles(self, elementsystemlimitprofile_id=None, api_version="v2.0"):
        """
        Get All Element System Limit Profiles (v2.0)

          **Parameters:**:

          - **elementsystemlimitprofile_id**: (optional) Element System Limit Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not elementsystemlimitprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elementsystemlimitprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elementsystemlimitprofiles/{}".format(api_version,
                                                                                       elementsystemlimitprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementusers(self, elementuser_id=None, api_version="v2.1"):
        """
        Get all element User (v2.1)

          **Parameters:**:

          - **elementuser_id**: (optional) Element User ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not elementuser_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elementusers".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}".format(api_version,
                                                                         elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementusers_access(self, elementuser_id, access_id=None, api_version="v2.1"):
        """
        Get all accesses for a particular user (v2.1)

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: (optional) Access ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not access_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}/access".format(api_version,
                                                                                elementuser_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}/access/{}".format(api_version,
                                                                                   elementuser_id,
                                                                                   access_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def enterpriseprefixset(self, api_version="v2.1"):
        """
        GET Enterpriseprefixset API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/enterpriseprefixset".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def esp(self, api_version="v2.0"):
        """
        Get esp tenant details for tenant id (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/esp".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def esp_operator_permissions_client(self, operator_id, client_id, api_version="v2.1"):
        """
        Get esp operator permissions assigned under a client (v2.1)

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
        return self._parent_class.rest_call(url, "get")

    def eventcodes(self, api_version="v2.0"):
        """
        GET Eventcodes API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/eventcodes".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, eventcorrelationpolicyrule_id=None, api_version="v2.1"):
        """
        Get all event correlation policyrules (v2.1)

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **eventcorrelationpolicyrule_id**: (optional) Event Correlation Policy Rule ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not eventcorrelationpolicyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules".format(api_version,
                                                                                                                   eventcorrelationpolicyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules/{}".format(api_version,
                                                                                                                      eventcorrelationpolicyset_id,
                                                                                                                      eventcorrelationpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def eventcorrelationpolicysets(self, eventcorrelationpolicyset_id=None, api_version="v2.0"):
        """
        Get all event correlation policysets (v2.0)

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: (optional) Event Correlation Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not eventcorrelationpolicyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/eventcorrelationpolicysets/{}".format(api_version,
                                                                                       eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def events(self, event_id, api_version="v2.4"):
        """
        GET Events API Function

          **Parameters:**:

          - **event_id**: Event ID
          - **api_version**: API version to use (default v2.4)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/events/{}".format(api_version,
                                                               event_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def extensions_t(self, extension_id=None, api_version="v2.0"):
        """
        GET Extensions_T API Function

          **Parameters:**:

          - **extension_id**: (optional) Extension ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not extension_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/extensions".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/extensions/{}".format(api_version,
                                                                       extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def externalcaconfigs(self, externalcaconfig_id=None, api_version="v2.0"):
        """
        GET Externalcaconfigs API Function

          **Parameters:**:

          - **externalcaconfig_id**: (optional) External CA Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not externalcaconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/externalcaconfigs".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/externalcaconfigs/{}".format(api_version,
                                                                              externalcaconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def flowexport_status(self, site_id, api_version="v2.0"):
        """
        Get flow logging status for a site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/flowexport_status".format(api_version,
                                                                                site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def forecast_aiops_monitor(self, api_version="v2.1"):
        """
        GET Forecast_Aiops_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/forecast".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def globalprefixfilters(self, globalprefixfilter_id=None, api_version="v2.0"):
        """
        Get global prefix filters. (v2.0)

          **Parameters:**:

          - **globalprefixfilter_id**: (optional) Global Prefix Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not globalprefixfilter_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/globalprefixfilters/{}".format(api_version,
                                                                                globalprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hardwarebypass(self, element_id, api_version="v2.0"):
        """
        Get a list of all the hardware bypasses in element (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/hardwarebypass".format(api_version,
                                                                                element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def health_aiops_monitor(self, api_version="v2.0"):
        """
        GET Health_Aiops_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/health".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id=None, api_version="v3.0"):
        """
        Get all hub cluster members (v3.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: (optional) Hub Cluster Member ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not hubclustermember_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/hubclustermembers".format(api_version,
                                                                                                   site_id,
                                                                                                   hubcluster_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/hubclustermembers/{}".format(api_version,
                                                                                                      site_id,
                                                                                                      hubcluster_id,
                                                                                                      hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubclusters(self, site_id, hubcluster_id=None, api_version="v4.0"):
        """
        Get all hub clusters (v4.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: (optional) Hub (DC) Cluster ID
          - **api_version**: API version to use (default v4.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not hubcluster_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters".format(api_version,
                                                                              site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}".format(api_version,
                                                                                 site_id,
                                                                                 hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubserviceendpoints_s(self, site_id, api_version="v2.0"):
        """
        GET Hubserviceendpoints_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubserviceendpoints".format(api_version,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubserviceendpoints_t(self, api_version="v2.0"):
        """
        GET Hubserviceendpoints_T API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/hubserviceendpoints".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def icon_appstatus_sdwanapps(self, sdwanapp_id, api_version="v2.0"):
        """
        GET Icon_Appstatus_Sdwanapps API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/appstatus/icon".format(api_version,
                                                                                 sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def idps(self, idp_id=None, api_version="v3.3"):
        """
        Get all idps (v3.3)

          **Parameters:**:

          - **idp_id**: (optional) SAML IDentity provider configuration ID
          - **api_version**: API version to use (default v3.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not idp_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/idps".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/idps/{}".format(api_version,
                                                                 idp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces(self, site_id, element_id, interface_id=None, api_version="v4.21"):
        """
        Get all Interfaces (v4.21)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: (optional) Interface ID
          - **api_version**: API version to use (default v4.21)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not interface_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces".format(api_version,
                                                                                         site_id,
                                                                                         element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}".format(api_version,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces_elementshells(self, site_id, elementshell_id, interface_id=None, api_version="v2.4"):
        """
        GET Interfaces_Elementshells API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **elementshell_id**: Element Shell ID
          - **interface_id**: (optional) Interface ID
          - **api_version**: API version to use (default v2.4)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not interface_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}/interfaces".format(api_version,
                                                                                              site_id,
                                                                                              elementshell_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elementshells/{}/interfaces/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 elementshell_id,
                                                                                                 interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def iotdevicemappings(self, iotdevicemapping_id, api_version="v2.0"):
        """
        Get the active ip mappings (v2.0)

          **Parameters:**:

          - **iotdevicemapping_id**: IOT Device Mapping ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/iotdevicemappings/{}".format(api_version,
                                                                          iotdevicemapping_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def iotdictionary(self, iotdictionary_id=None, api_version="v2.0"):
        """
        Get all the XML Ingested data (v2.0)

          **Parameters:**:

          - **iotdictionary_id**: (optional) IOT Dictionary ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not iotdictionary_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/iotdictionary".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/iotdictionary/{}".format(api_version,
                                                                          iotdictionary_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def iotservices(self, api_version="v2.0"):
        """
        Get the confidence score of the mappings stored in the IOT portal (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/iotservices".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfix(self, site_id, element_id, ipfix_id=None, api_version="v2.0"):
        """
        Get all IPFix config (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ipfix_id**: (optional) IPFix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ipfix".format(api_version,
                                                                                    site_id,
                                                                                    element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ipfix/{}".format(api_version,
                                                                                       site_id,
                                                                                       element_id,
                                                                                       ipfix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixcollectorcontexts(self, ipfixcollectorcontext_id=None, api_version="v2.0"):
        """
        Get all IPFix collector context (v2.0)

          **Parameters:**:

          - **ipfixcollectorcontext_id**: (optional) IPFix Collector Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfixcollectorcontext_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixcollectorcontexts".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixcollectorcontexts/{}".format(api_version,
                                                                                   ipfixcollectorcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixfiltercontexts(self, ipfixfiltercontext_id=None, api_version="v2.0"):
        """
        Get all IPFix filter context (v2.0)

          **Parameters:**:

          - **ipfixfiltercontext_id**: (optional) IPFix Filter Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfixfiltercontext_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixfiltercontexts".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixfiltercontexts/{}".format(api_version,
                                                                                ipfixfiltercontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixglobalprefixes(self, ipfixglobalprefix_id=None, api_version="v2.0"):
        """
        Get all IPFix global prefix (v2.0)

          **Parameters:**:

          - **ipfixglobalprefix_id**: (optional) IPFix Global Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfixglobalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixglobalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixglobalprefixes/{}".format(api_version,
                                                                                ipfixglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixprofiles(self, ipfixprofile_id=None, api_version="v2.0"):
        """
        Get all IPFix Profiles (v2.0)

          **Parameters:**:

          - **ipfixprofile_id**: (optional) IPFix Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfixprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixprofiles/{}".format(api_version,
                                                                          ipfixprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixtemplates(self, ipfixtemplate_id=None, api_version="v2.0"):
        """
        Get all IPFix templates (v2.0)

          **Parameters:**:

          - **ipfixtemplate_id**: (optional) IPFix Template ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfixtemplate_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixtemplates".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixtemplates/{}".format(api_version,
                                                                           ipfixtemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipsecprofiles(self, ipsecprofile_id=None, api_version="v2.2"):
        """
        Get IPSECProfileList (v2.2)

          **Parameters:**:

          - **ipsecprofile_id**: (optional) IPSEC Profile ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipsecprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipsecprofiles/{}".format(api_version,
                                                                          ipsecprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def lannetworks(self, site_id, lannetwork_id=None, api_version="v3.3"):
        """
        Get LAN networks (v3.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: (optional) LAN Network ID
          - **api_version**: API version to use (default v3.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not lannetwork_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/lannetworks".format(api_version,
                                                                              site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/lannetworks/{}".format(api_version,
                                                                                 site_id,
                                                                                 lannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def licenses(self, api_version="v2.0"):
        """
        Get all licenses for a tenant (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/licenses".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def localprefixfilters(self, localprefixfilter_id=None, api_version="v2.0"):
        """
        Get local prefix filters. (v2.0)

          **Parameters:**:

          - **localprefixfilter_id**: (optional) Local Prefix Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not localprefixfilter_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/localprefixfilters".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/localprefixfilters/{}".format(api_version,
                                                                               localprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def localprefixset(self, site_id, api_version="v2.0"):
        """
        GET Localprefixset API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/localprefixset".format(api_version,
                                                                             site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def login(self, api_version="v2.0"):
        """
        GET Login API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/login".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get", sensitive=True)

    def logout(self, api_version="v2.0"):
        """
        Logout current session

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/logout".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machine_cellular_modules_firmware(self, machine_id, cellular_module_id, api_version="v2.0"):
        """
        Get cellular module firmware configuration (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: Cellular Module ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/cellular_modules/{}/firmware".format(api_version,
                                                                                              machine_id,
                                                                                              cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machine_state(self, machine_id, api_version="v2.1"):
        """
        Get Machine state (v2.1)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/state".format(api_version,
                                                                       machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machines(self, machine_id=None, api_version="v2.5"):
        """
        Get machines of a tenant (v2.5)

          **Parameters:**:

          - **machine_id**: (optional) Machine ID
          - **api_version**: API version to use (default v2.5)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not machine_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}".format(api_version,
                                                                     machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machines_c(self, client_id, machine_id=None, api_version="v2.5"):
        """
        GET Machines_C API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **machine_id**: (optional) Machine ID
          - **api_version**: API version to use (default v2.5)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not machine_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/machines".format(api_version,
                                                                             client_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/machines/{}".format(api_version,
                                                                                client_id,
                                                                                machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machinesystemstatus(self, machine_id, api_version="v2.1"):
        """
        Get Machine system status for a tenant (v2.1)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/machinesystemstatus".format(api_version,
                                                                                     machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def metadata_appstatus_sdwanapps(self, sdwanapp_id, api_version="v2.0"):
        """
        GET Metadata_Appstatus_Sdwanapps API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/appstatus/metadata".format(api_version,
                                                                                     sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def metrics_monitor(self, metric_id, api_version="v2.6"):
        """
        GET Metrics_Monitor API Function

          **Parameters:**:

          - **metric_id**: Metric ID
          - **api_version**: API version to use (default v2.6)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/metrics/{}".format(api_version,
                                                                                metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def migratecbtoezb(self, api_version="v2.0"):
        """
        Get migration API status (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/migratecbtoezb".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_agg_bw_stats(self, api_version="v2.0"):
        """
        GET Monitor_Agg_Bw_Stats API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/agg_bw_stats".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_metrics_probes(self, probe_id, api_version="v2.0"):
        """
        GET Monitor_Metrics_Probes API Function

          **Parameters:**:

          - **probe_id**: Probe ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/metrics/probes/{}".format(api_version,
                                                                                       probe_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def mstp_instances(self, site_id, element_id, mstp_instance_id=None, api_version="v2.0"):
        """
        Get all MSTP Instances (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **mstp_instance_id**: (optional) MSTP Instance ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not mstp_instance_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/mstp_instances".format(api_version,
                                                                                             site_id,
                                                                                             element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/mstp_instances/{}".format(api_version,
                                                                                                site_id,
                                                                                                element_id,
                                                                                                mstp_instance_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastdynamicrps(self, site_id, element_id, multicastdynamicrp_id=None, api_version="v2.0"):
        """
        Get all Multicast dynamic RPs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastdynamicrp_id**: (optional) Multicast Dynamic RP ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastdynamicrp_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastdynamicrps".format(api_version,
                                                                                                  site_id,
                                                                                                  element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastdynamicrps/{}".format(api_version,
                                                                                                     site_id,
                                                                                                     element_id,
                                                                                                     multicastdynamicrp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastglobalconfigs(self, site_id, element_id, multicastglobalconfig_id=None, api_version="v2.1"):
        """
        Get all Multicast configs (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastglobalconfig_id**: (optional) Multicast Global Config ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastglobalconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastglobalconfigs".format(api_version,
                                                                                                     site_id,
                                                                                                     element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastglobalconfigs/{}".format(api_version,
                                                                                                        site_id,
                                                                                                        element_id,
                                                                                                        multicastglobalconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastigmpmemberships_interfaces(self, site_id, element_id, interface_id, multicastigmpmembership_id=None, api_version="v2.0"):
        """
        GET Multicastigmpmemberships_Interfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **multicastigmpmembership_id**: (optional) Multicast IGMP Membership ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastigmpmembership_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}/multicastigmpmemberships".format(api_version,
                                                                                                                     site_id,
                                                                                                                     element_id,
                                                                                                                     interface_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}/multicastigmpmemberships/{}".format(api_version,
                                                                                                                        site_id,
                                                                                                                        element_id,
                                                                                                                        interface_id,
                                                                                                                        multicastigmpmembership_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastpeergroups(self, multicastpeergroup_id=None, api_version="v2.1"):
        """
        Get multicast peer groups (v2.1)

          **Parameters:**:

          - **multicastpeergroup_id**: (optional) Multicast Peer Group ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastpeergroup_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/multicastpeergroups".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/multicastpeergroups/{}".format(api_version,
                                                                                multicastpeergroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastprotocolparameters(self, site_id, element_id, api_version="v2.0"):
        """
        Get all Multicast Protocol Parameters (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastprotocolparameters".format(api_version,
                                                                                                      site_id,
                                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastroutes(self, site_id, element_id, api_version="v2.0"):
        """
        Get all Multicast routes (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastroutes".format(api_version,
                                                                                          site_id,
                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastrps(self, site_id, element_id, multicastrp_id=None, api_version="v2.0"):
        """
        Get all Multicast RP configs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastrp_id**: (optional) Multicast RP ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastrp_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastrps".format(api_version,
                                                                                           site_id,
                                                                                           element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastrps/{}".format(api_version,
                                                                                              site_id,
                                                                                              element_id,
                                                                                              multicastrp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastsourcesiderps(self, site_id, multicastsourcesiderp_id=None, api_version="v2.0"):
        """
        Get multicast source side RPs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **multicastsourcesiderp_id**: (optional) Multicast Source Side RP ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastsourcesiderp_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiderps".format(api_version,
                                                                                         site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiderps/{}".format(api_version,
                                                                                            site_id,
                                                                                            multicastsourcesiderp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastsourcesiteconfigs(self, site_id, multicastsourcesiteconfig_id=None, api_version="v2.0"):
        """
        Get multicast source site configs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **multicastsourcesiteconfig_id**: (optional) Multicast Source Site Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastsourcesiteconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiteconfigs".format(api_version,
                                                                                             site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/multicastsourcesiteconfigs/{}".format(api_version,
                                                                                                site_id,
                                                                                                multicastsourcesiteconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicaststatus_interfaces(self, site_id, element_id, interface_id, api_version="v2.0"):
        """
        GET Multicaststatus_Interfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}/multicaststatus".format(api_version,
                                                                                                        site_id,
                                                                                                        element_id,
                                                                                                        interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastwanstatus(self, site_id, element_id, multicastwanstatus_id=None, api_version="v2.0"):
        """
        Get all Multicast WAN status (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastwanstatus_id**: (optional) Multicast WAN Status ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not multicastwanstatus_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastwanstatus".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/multicastwanstatus/{}".format(api_version,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    multicastwanstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natglobalprefixes(self, natglobalprefix_id=None, api_version="v2.0"):
        """
        Get all Global NAT prefixes. (v2.0)

          **Parameters:**:

          - **natglobalprefix_id**: (optional) NAT Global Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natglobalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/natglobalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/natglobalprefixes/{}".format(api_version,
                                                                              natglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natlocalprefixes(self, natlocalprefix_id=None, api_version="v2.0"):
        """
        Get NAT local prefixes. (v2.0)

          **Parameters:**:

          - **natlocalprefix_id**: (optional) NAT Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natlocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/natlocalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/natlocalprefixes/{}".format(api_version,
                                                                             natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicypools(self, natpolicypool_id=None, api_version="v2.0"):
        """
        Get NAT Policy Pools. (v2.0)

          **Parameters:**:

          - **natpolicypool_id**: (optional) NAT Policy Pool ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natpolicypool_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicypools".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicypools/{}".format(api_version,
                                                                           natpolicypool_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicyrules(self, natpolicyset_id, natpolicyrule_id=None, api_version="v2.0"):
        """
        Get policy rules of policy set (v2.0)

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **natpolicyrule_id**: (optional) NAT Policy Rule ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natpolicyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}/natpolicyrules".format(api_version,
                                                                                         natpolicyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}/natpolicyrules/{}".format(api_version,
                                                                                            natpolicyset_id,
                                                                                            natpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicysets(self, natpolicyset_id=None, api_version="v2.0"):
        """
        Get all NAT policy sets of tenant. (v2.0)

          **Parameters:**:

          - **natpolicyset_id**: (optional) NAT Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natpolicyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}".format(api_version,
                                                                          natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicysetstacks(self, natpolicysetstack_id=None, api_version="v2.0"):
        """
        Get all NAT policy Set stacks of tenant. (v2.0)

          **Parameters:**:

          - **natpolicysetstack_id**: (optional) NAT Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natpolicysetstack_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysetstacks".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysetstacks/{}".format(api_version,
                                                                               natpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natzones(self, natzone_id=None, api_version="v2.0"):
        """
        Get Nat Policy Zones. (v2.0)

          **Parameters:**:

          - **natzone_id**: (optional) NAT Zone ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natzone_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/natzones".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/natzones/{}".format(api_version,
                                                                     natzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkcontexts(self, networkcontext_id=None, api_version="v2.0"):
        """
        Get LAN segments (v2.0)

          **Parameters:**:

          - **networkcontext_id**: (optional) Network Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not networkcontext_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkcontexts".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkcontexts/{}".format(api_version,
                                                                            networkcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id=None, api_version="v2.1"):
        """
        Get all Network policy global prefixes. (v2.1)

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: (optional) Network Policy Global Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not networkpolicyglobalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyglobalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicyglobalprefixes/{}".format(api_version,
                                                                                        networkpolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id=None, api_version="v2.4"):
        """
        Get network policy rules of tenant (v2.4)

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: (optional) Network Policy Rule ID
          - **api_version**: API version to use (default v2.4)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not networkpolicyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}/networkpolicyrules".format(api_version,
                                                                                                 networkpolicyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}/networkpolicyrules/{}".format(api_version,
                                                                                                    networkpolicyset_id,
                                                                                                    networkpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicysets(self, networkpolicyset_id=None, api_version="v2.0"):
        """
        Get all network policy sets of tenant. (v2.0)

          **Parameters:**:

          - **networkpolicyset_id**: (optional) Network Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not networkpolicyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}".format(api_version,
                                                                              networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicysetstacks(self, networkpolicysetstack_id=None, api_version="v2.0"):
        """
        Get all network policy set stacks of tenant. (v2.0)

          **Parameters:**:

          - **networkpolicysetstack_id**: (optional) Network Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not networkpolicysetstack_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysetstacks".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysetstacks/{}".format(api_version,
                                                                                   networkpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicyglobalprefixes(self, ngfwsecuritypolicyglobalprefix_id=None, api_version="v2.1"):
        """
        Get all Security Policy V2 Global Prefixes for a tenant (v2.1)

          **Parameters:**:

          - **ngfwsecuritypolicyglobalprefix_id**: (optional) NGFW Security Policy Global Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicyglobalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyglobalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicyglobalprefixes/{}".format(api_version,
                                                                                             ngfwsecuritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicylocalprefixes(self, ngfwsecuritypolicylocalprefix_id=None, api_version="v2.0"):
        """
        Get all Security Policy V2 Local Prefixes for a tenant (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicylocalprefix_id**: (optional) NGFW Security Policy Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicylocalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                            ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicyrules(self, ngfwsecuritypolicyset_id, ngfwsecuritypolicyrule_id=None, api_version="v2.3"):
        """
        Get all Security Policy V2 Rules under a policy set (v2.3)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **ngfwsecuritypolicyrule_id**: (optional) NGFW Security Policy Rule ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules".format(api_version,
                                                                                                           ngfwsecuritypolicyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules/{}".format(api_version,
                                                                                                              ngfwsecuritypolicyset_id,
                                                                                                              ngfwsecuritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicysets(self, ngfwsecuritypolicyset_id=None, api_version="v2.0"):
        """
        Get all Security Policy V2 Sets by tenant ID (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: (optional) NGFW Security Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysets/{}".format(api_version,
                                                                                   ngfwsecuritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicysetstacks(self, ngfwsecuritypolicysetstack_id=None, api_version="v2.0"):
        """
        Get all Security Policy V2 Set Stacks by tenant ID (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicysetstack_id**: (optional) NGFW Security Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicysetstack_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysetstacks".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ngfwsecuritypolicysetstacks/{}".format(api_version,
                                                                                        ngfwsecuritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ntp(self, element_id, ntp_id=None, api_version="v2.1"):
        """
        Get all element NTP (v2.1)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **ntp_id**: (optional) NTP Configuration ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ntp_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/ntp".format(api_version,
                                                                         element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/ntp/{}".format(api_version,
                                                                            element_id,
                                                                            ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def object_stats_aiops_monitor(self, api_version="v2.1"):
        """
        GET Object_Stats_Aiops_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/aiops/object_stats".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def object_stats_monitor(self, api_version="v2.7"):
        """
        GET Object_Stats_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.7)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/object_stats".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def openapi(self, api_version="v2.0"):
        """
        GET Openapi API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/openapi".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def openapi_json(self, api_version="v2.0"):
        """
        GET Openapi_Json API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/openapi.json".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def operator_sessions(self, operator_id, session_id=None, api_version="v2.0"):
        """
        Get all sessions for operator id belonging to a tenant id (v2.0)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **session_id**: (optional) User Session ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not session_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/sessions".format(api_version,
                                                                               operator_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/sessions/{}".format(api_version,
                                                                                  operator_id,
                                                                                  session_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ospfconfigs(self, site_id, element_id, ospfconfig_id=None, api_version="v2.0"):
        """
        Get all OSPF configs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ospfconfig_id**: (optional) OSPF Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ospfconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfconfigs".format(api_version,
                                                                                          site_id,
                                                                                          element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfconfigs/{}".format(api_version,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             ospfconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ospfconfigs_ospfdiscoveredneighbors(self, site_id, element_id, ospfconfig_id, api_version="v2.0"):
        """
        GET Ospfconfigs_Ospfdiscoveredneighbors API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ospfconfig_id**: OSPF Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfconfigs/{}/ospfdiscoveredneighbors".format(api_version,
                                                                                                                 site_id,
                                                                                                                 element_id,
                                                                                                                 ospfconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ospfconfigs_ospfreachableprefixes(self, site_id, element_id, ospfconfig_id, api_version="v2.0"):
        """
        GET Ospfconfigs_Ospfreachableprefixes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ospfconfig_id**: OSPF Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfconfigs/{}/ospfreachableprefixes".format(api_version,
                                                                                                               site_id,
                                                                                                               element_id,
                                                                                                               ospfconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ospfglobalconfigs(self, site_id, element_id, ospfglobalconfig_id=None, api_version="v2.0"):
        """
        Get all OSPF configs from NB (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ospfglobalconfig_id**: (optional) OSPF Global Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ospfglobalconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfglobalconfigs".format(api_version,
                                                                                                site_id,
                                                                                                element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/ospfglobalconfigs/{}".format(api_version,
                                                                                                   site_id,
                                                                                                   element_id,
                                                                                                   ospfglobalconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def otpaccessconfigs(self, api_version="v2.0"):
        """
        Get all otp access configs. (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/otpaccessconfigs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def pasdwan_integration_status(self, api_version="v2.0"):
        """
        Get Native PA SDWAN Integration Tenant Provision Status (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/pasdwan_integration_status".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def passages_t(self, api_version="v2.0"):
        """
        GET Passages_T API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/passages".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def password_elementusers(self, elementuser_id, api_version="v2.1"):
        """
        GET Password_Elementusers API Function

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elementusers/{}/password".format(api_version,
                                                                              elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def pathgroups(self, pathgroup_id=None, api_version="v2.1"):
        """
        get all Path Groups for a tenant. (v2.1)

          **Parameters:**:

          - **pathgroup_id**: (optional) Path Group ID (for network service/DC routing)
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not pathgroup_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/pathgroups".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/pathgroups/{}".format(api_version,
                                                                       pathgroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def pathprefixdistributionfilterassociation(self, site_id, pathprefixdistributionfilterassociation_id=None, api_version="v2.0"):
        """
        GET Pathprefixdistributionfilterassociation API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **pathprefixdistributionfilterassociation_id**: (optional) Path Prefix Distribution Filter Association ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not pathprefixdistributionfilterassociation_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilterassociation".format(api_version,
                                                                                                          site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilterassociation/{}".format(api_version,
                                                                                                             site_id,
                                                                                                             pathprefixdistributionfilterassociation_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def pathprefixdistributionfilters(self, site_id, pathprefixdistributionfilter_id=None, api_version="v2.0"):
        """
        GET Pathprefixdistributionfilters API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **pathprefixdistributionfilter_id**: (optional) Path Prefix Distribution Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not pathprefixdistributionfilter_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilters".format(api_version,
                                                                                                site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/pathprefixdistributionfilters/{}".format(api_version,
                                                                                                   site_id,
                                                                                                   pathprefixdistributionfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def pathprefixes_peersites(self, site_id, peersite_id, api_version="v2.0"):
        """
        GET Pathprefixes_Peersites API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **peersite_id**: Peer Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/peersites/{}/pathprefixes".format(api_version,
                                                                                        site_id,
                                                                                        peersite_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def perfmgmtpolicyrules_perfmgmtpolicysets(self, perfmgmtpolicyset_id, perfmgmtpolicyrule_id=None, api_version="v2.2"):
        """
        GET Perfmgmtpolicyrules_Perfmgmtpolicysets API Function

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **perfmgmtpolicyrule_id**: (optional) Performance Management Policy Rule ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not perfmgmtpolicyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}/perfmgmtpolicyrules".format(api_version,
                                                                                                   perfmgmtpolicyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}/perfmgmtpolicyrules/{}".format(api_version,
                                                                                                      perfmgmtpolicyset_id,
                                                                                                      perfmgmtpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def perfmgmtpolicysets(self, perfmgmtpolicyset_id=None, api_version="v2.0"):
        """
        Get PERFMGMT Policy Sets (v2.0)

          **Parameters:**:

          - **perfmgmtpolicyset_id**: (optional) Performance Management Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not perfmgmtpolicyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}".format(api_version,
                                                                               perfmgmtpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def perfmgmtpolicysets_status(self, perfmgmtpolicyset_id, api_version="v2.0"):
        """
        Get PERFMGMT Policy Set status (v2.0)

          **Parameters:**:

          - **perfmgmtpolicyset_id**: Performance Management Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysets/{}/status".format(api_version,
                                                                                  perfmgmtpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def perfmgmtpolicysetstacks(self, perfmgmtpolicysetstack_id=None, api_version="v2.0"):
        """
        Get PERFMGMT Policy Set Stacks (v2.0)

          **Parameters:**:

          - **perfmgmtpolicysetstack_id**: (optional) Performance Management Policy Set Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not perfmgmtpolicysetstack_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysetstacks".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtpolicysetstacks/{}".format(api_version,
                                                                                    perfmgmtpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def perfmgmtthresholdprofiles(self, perfmgmtthresholdprofile_id=None, api_version="v2.1"):
        """
        Get ThreholdProfileList (v2.1)

          **Parameters:**:

          - **perfmgmtthresholdprofile_id**: (optional) Performance Management Threshold Profile ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not perfmgmtthresholdprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtthresholdprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/perfmgmtthresholdprofiles/{}".format(api_version,
                                                                                      perfmgmtthresholdprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def permissions(self, permission_id=None, api_version="v2.0"):
        """
        Get a list of custom permissions (v2.0)

          **Parameters:**:

          - **permission_id**: (optional) Permission ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not permission_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/permissions".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/permissions/{}".format(api_version,
                                                                        permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def permissions_clients_d(self, operator_id, api_version="v2.0"):
        """
        GET Permissions_Clients_D API Function

          **Parameters:**:

          - **operator_id**: Operator ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}/clients/permissions".format(api_version,
                                                                                      operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def policyrules(self, policyset_id, policyrule_id=None, api_version="v3.1"):
        """
        Get policy rules of tenant (v3.1)

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **policyrule_id**: (optional) Policy Rule ID
          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not policyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}/policyrules".format(api_version,
                                                                                   policyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}/policyrules/{}".format(api_version,
                                                                                      policyset_id,
                                                                                      policyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def policysets(self, policyset_id=None, api_version="v3.0"):
        """
        Get all policy sets of tenant. (v3.0)

          **Parameters:**:

          - **policyset_id**: (optional) Policy Set ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not policyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/policysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}".format(api_version,
                                                                       policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def port_vlan_members(self, site_id, element_id, api_version="v2.0"):
        """
        Get switch port to VLAN port mapping information for an element (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/port_vlan_members".format(api_version,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prefixdistributionspokelists(self, site_id, prefixdistributionspokelist_id=None, api_version="v2.0"):
        """
        GET Prefixdistributionspokelists API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixdistributionspokelist_id**: (optional) Prefix Distribution Spoke List ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prefixdistributionspokelist_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixdistributionspokelists".format(api_version,
                                                                                               site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixdistributionspokelists/{}".format(api_version,
                                                                                                  site_id,
                                                                                                  prefixdistributionspokelist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prefixfilters(self, site_id, prefixfilter_id=None, api_version="v2.0"):
        """
        Get site security filters (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixfilter_id**: (optional) Prefix Filter ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prefixfilter_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters".format(api_version,
                                                                                site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prefixfilters/{}".format(api_version,
                                                                                   site_id,
                                                                                   prefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id=None, api_version="v2.1"):
        """
        Get all Priority policy prefixes. (v2.1)

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: (optional) Priority Policy Global Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prioritypolicyglobalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyglobalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicyglobalprefixes/{}".format(api_version,
                                                                                         prioritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id=None, api_version="v2.2"):
        """
        Get priority policy rules of tenant (v2.2)

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: (optional) Priority Policy Rule ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prioritypolicyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}/prioritypolicyrules".format(api_version,
                                                                                                   prioritypolicyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}/prioritypolicyrules/{}".format(api_version,
                                                                                                      prioritypolicyset_id,
                                                                                                      prioritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicysets(self, prioritypolicyset_id=None, api_version="v2.0"):
        """
        Get all priority policy sets of tenant. (v2.0)

          **Parameters:**:

          - **prioritypolicyset_id**: (optional) Priority Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prioritypolicyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}".format(api_version,
                                                                               prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicysetstacks(self, prioritypolicysetstack_id=None, api_version="v2.0"):
        """
        Get all Priority policy set stacks of tenant. (v2.0)

          **Parameters:**:

          - **prioritypolicysetstack_id**: (optional) Priority Policy Stack ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prioritypolicysetstack_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysetstacks".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysetstacks/{}".format(api_version,
                                                                                    prioritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prismaaccess_configs(self, site_id, prismaaccess_config_id=None, api_version="v2.0"):
        """
        Get all Prisma Access Configs for a site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prismaaccess_config_id**: (optional) Prisma Acceess Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prismaaccess_config_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismaaccess_configs".format(api_version,
                                                                                       site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismaaccess_configs/{}".format(api_version,
                                                                                          site_id,
                                                                                          prismaaccess_config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prismasase_connections(self, site_id, prismasase_connection_id=None, api_version="v2.1"):
        """
        Get SASE connections for sites (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **prismasase_connection_id**: (optional) Prisma SASE Connection ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prismasase_connection_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismasase_connections".format(api_version,
                                                                                         site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismasase_connections/{}".format(api_version,
                                                                                            site_id,
                                                                                            prismasase_connection_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prismasase_connections_configs(self, api_version="v3.1"):
        """
        Get a specific SASE connection config (v3.1)

          **Parameters:**:

          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prismasase_connections/configs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def probeconfigs(self, probeconfig_id=None, api_version="v2.0"):
        """
        Get ProbeConfigList (v2.0)

          **Parameters:**:

          - **probeconfig_id**: (optional) Probe Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not probeconfig_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/probeconfigs".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/probeconfigs/{}".format(api_version,
                                                                         probeconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def probeprofiles(self, probeprofile_id=None, api_version="v2.0"):
        """
        Get ProbeProfileList (v2.0)

          **Parameters:**:

          - **probeprofile_id**: (optional) Probe Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not probeprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/probeprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/probeprofiles/{}".format(api_version,
                                                                          probeprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def profile(self, api_version="v2.1"):
        """
        Get current user profile (v2.1)

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/profile".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def qos_metrics_application_monitor(self, qos_metric_id, api_version="v2.0"):
        """
        GET Qos_Metrics_Application_Monitor API Function

          **Parameters:**:

          - **qos_metric_id**: QoS Metric ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/application/qos_metrics/{}".format(api_version,
                                                                                                qos_metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def qos_metrics_monitor(self, api_version="v2.0"):
        """
        GET Qos_Metrics_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/qos_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def radii(self, element_id, radii_id=None, api_version="v2.0"):
        """
        Get all radius configuration of an element in a tenant (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **radii_id**: (optional) Radii ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not radii_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/radii".format(api_version,
                                                                           element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/radii/{}".format(api_version,
                                                                              element_id,
                                                                              radii_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def reachableprefixes_bgppeers(self, site_id, element_id, bgppeer_id, api_version="v2.1"):
        """
        GET Reachableprefixes_Bgppeers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}/reachableprefixes".format(api_version,
                                                                                                        site_id,
                                                                                                        element_id,
                                                                                                        bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def recovery_tokens(self, machine_id, api_version="v2.1"):
        """
        Get recovery token for a machine (v2.1)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/recovery_tokens".format(api_version,
                                                                                 machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def reports(self, api_version="v2.0"):
        """
        GET Reports API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/reports".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def reportsdir(self, api_version="v2.0"):
        """
        GET Reportsdir API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/reportsdir".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def reportsurl(self, api_version="v2.0"):
        """
        GET Reportsurl API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/reportsurl".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def revoked_certificates(self, api_version="v2.0"):
        """
        GET Revoked_Certificates API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/certificates/revoked".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def roles(self, role_id=None, api_version="v2.1"):
        """
        Get a list of custom roles (v2.1)

          **Parameters:**:

          - **role_id**: (optional) Role ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not role_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/roles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/roles/{}".format(api_version,
                                                                  role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def roles_clients(self, client_id, role_id=None, api_version="v2.1"):
        """
        GET Roles_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **role_id**: (optional) Role ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not role_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/roles".format(api_version,
                                                                          client_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/clients/{}/roles/{}".format(api_version,
                                                                             client_id,
                                                                             role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_aspathaccesslists(self, site_id, element_id, routing_aspathaccesslist_id=None, api_version="v2.1"):
        """
        Get all Access List for Element (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_aspathaccesslist_id**: (optional) Routing AS-PATH Access List ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not routing_aspathaccesslist_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_aspathaccesslists".format(api_version,
                                                                                                        site_id,
                                                                                                        element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_aspathaccesslists/{}".format(api_version,
                                                                                                           site_id,
                                                                                                           element_id,
                                                                                                           routing_aspathaccesslist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_ipcommunitylists(self, site_id, element_id, routing_ipcommunitylist_id=None, api_version="v2.0"):
        """
        Get all Community List for Element (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_ipcommunitylist_id**: (optional) Routing IP Community List ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not routing_ipcommunitylist_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_ipcommunitylists".format(api_version,
                                                                                                       site_id,
                                                                                                       element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_ipcommunitylists/{}".format(api_version,
                                                                                                          site_id,
                                                                                                          element_id,
                                                                                                          routing_ipcommunitylist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_prefixlists(self, site_id, element_id, routing_prefixlist_id=None, api_version="v2.1"):
        """
        Get all Prefix List for Element (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_prefixlist_id**: (optional) Routing IP Prefix List ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not routing_prefixlist_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_prefixlists".format(api_version,
                                                                                                  site_id,
                                                                                                  element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_prefixlists/{}".format(api_version,
                                                                                                     site_id,
                                                                                                     element_id,
                                                                                                     routing_prefixlist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_routemaps(self, site_id, element_id, routing_routemap_id=None, api_version="v2.3"):
        """
        Get all Route Map for Element (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_routemap_id**: (optional) Routing Route Map ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not routing_routemap_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_routemaps".format(api_version,
                                                                                                site_id,
                                                                                                element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/routing_routemaps/{}".format(api_version,
                                                                                                   site_id,
                                                                                                   element_id,
                                                                                                   routing_routemap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps(self, sdwanapp_id=None, api_version="v2.2"):
        """
        GET Sdwanapps API Function

          **Parameters:**:

          - **sdwanapp_id**: (optional) SDWAN Application ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not sdwanapp_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}".format(api_version,
                                                                      sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps_configs(self, sdwanapp_id, config_id=None, api_version="v2.0"):
        """
        GET Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **config_id**: (optional) SDWAN App Config ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not config_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/configs".format(api_version,
                                                                              sdwanapp_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/configs/{}".format(api_version,
                                                                                 sdwanapp_id,
                                                                                 config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def securitypolicyrules(self, securitypolicyset_id, securitypolicyrule_id=None, api_version="v2.0"):
        """
        Get tenant security policy rules. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **securitypolicyrule_id**: (optional) Security Policy Rule ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not securitypolicyrule_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}/securitypolicyrules".format(api_version,
                                                                                                   securitypolicyset_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}/securitypolicyrules/{}".format(api_version,
                                                                                                      securitypolicyset_id,
                                                                                                      securitypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def securitypolicysets(self, securitypolicyset_id=None, api_version="v2.0"):
        """
        Get tenant security policy sets. (v2.0)

          **Parameters:**:

          - **securitypolicyset_id**: (optional) Security Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not securitypolicyset_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/securitypolicysets/{}".format(api_version,
                                                                               securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def securityprofilegroups(self, securityprofilegroup_id=None, api_version="v2.0"):
        """
        Get all Security Profile Groups by tenant ID (v2.0)

          **Parameters:**:

          - **securityprofilegroup_id**: (optional) Security Profile Group ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not securityprofilegroup_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/securityprofilegroups".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/securityprofilegroups/{}".format(api_version,
                                                                                  securityprofilegroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def securityzones(self, securityzone_id=None, api_version="v2.1"):
        """
        getSecurityZones (v2.1)

          **Parameters:**:

          - **securityzone_id**: (optional) Security Zone (ZBFW) ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not securityzone_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/securityzones".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/securityzones/{}".format(api_version,
                                                                          securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def servicebindingmaps(self, servicebindingmap_id=None, api_version="v2.1"):
        """
        Get getServiceBindingMapList (v2.1)

          **Parameters:**:

          - **servicebindingmap_id**: (optional) Service Binding Map ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not servicebindingmap_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/servicebindingmaps".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/servicebindingmaps/{}".format(api_version,
                                                                               servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def serviceconnections_s(self, site_id, api_version="v2.0"):
        """
        GET Serviceconnections_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/serviceconnections".format(api_version,
                                                                                 site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def serviceconnections_t(self, api_version="v2.0"):
        """
        GET Serviceconnections_T API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/serviceconnections".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def serviceendpoints(self, serviceendpoint_id=None, api_version="v3.1"):
        """
        Get ServiceEndpointList (v3.1)

          **Parameters:**:

          - **serviceendpoint_id**: (optional) Service Endpoint ID
          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not serviceendpoint_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/serviceendpoints".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/serviceendpoints/{}".format(api_version,
                                                                             serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def servicelabels(self, servicelabel_id=None, api_version="v2.1"):
        """
        Get getServiceLabelList (v2.1)

          **Parameters:**:

          - **servicelabel_id**: (optional) Service Label ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not servicelabel_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/servicelabels".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/servicelabels/{}".format(api_version,
                                                                          servicelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_extensions(self, site_id, extension_id=None, api_version="v2.0"):
        """
        Get all site level extensions (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **extension_id**: (optional) Extension ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not extension_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/extensions".format(api_version,
                                                                             site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/extensions/{}".format(api_version,
                                                                                site_id,
                                                                                extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_ipfixlocalprefixes(self, site_id, ipfixlocalprefix_id=None, api_version="v2.0"):
        """
        Get all IPFix site prefix association (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **ipfixlocalprefix_id**: (optional) IPFix Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfixlocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ipfixlocalprefixes".format(api_version,
                                                                                     site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                        site_id,
                                                                                        ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_natlocalprefixes(self, site_id, natlocalprefix_id=None, api_version="v2.0"):
        """
        Get site NAT prefixes (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **natlocalprefix_id**: (optional) NAT Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not natlocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/natlocalprefixes".format(api_version,
                                                                                   site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/natlocalprefixes/{}".format(api_version,
                                                                                      site_id,
                                                                                      natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id=None, api_version="v2.1"):
        """
        Get site Network policy prefix associations (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: (optional) Network Policy Local Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not networkpolicylocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/networkpolicylocalprefixes".format(api_version,
                                                                                             site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                                site_id,
                                                                                                networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_ngfwsecuritypolicylocalprefixes(self, site_id, ngfwsecuritypolicylocalprefix_id=None, api_version="v2.1"):
        """
        Get all security policy v2 local prefix site association for a site (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **ngfwsecuritypolicylocalprefix_id**: (optional) NGFW Security Policy Local Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ngfwsecuritypolicylocalprefixes".format(api_version,
                                                                                                  site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                                     site_id,
                                                                                                     ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id=None, api_version="v2.1"):
        """
        Get site Priority policy prefix associations (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: (optional) Priority Policy Local Prefix ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prioritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prioritypolicylocalprefixes".format(api_version,
                                                                                              site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                                 site_id,
                                                                                                 prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def siteciphers(self, site_id, api_version="v2.0"):
        """
        Get site ciphers (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/siteciphers".format(api_version,
                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sites(self, site_id=None, api_version="v4.13"):
        """
        Get all sites of a tenant (v4.13)

          **Parameters:**:

          - **site_id**: (optional) Site ID
          - **api_version**: API version to use (default v4.13)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not site_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}".format(api_version,
                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sitesecurityzones(self, site_id, sitesecurityzone_id=None, api_version="v2.0"):
        """
        Get site security zones (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **sitesecurityzone_id**: (optional) Site Security Zone ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not sitesecurityzone_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/sitesecurityzones".format(api_version,
                                                                                    site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/sitesecurityzones/{}".format(api_version,
                                                                                       site_id,
                                                                                       sitesecurityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sitesnapshots(self, sitesnapshot_id, api_version="v2.0"):
        """
        Retrieve deployment status by ID (v2.0)

          **Parameters:**:

          - **sitesnapshot_id**: Site Snapshot ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sitesnapshots/{}".format(api_version,
                                                                      sitesnapshot_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sitetemplates_bulkconfigurations_status(self, sitetemplate_id, api_version="v2.0"):
        """
        GET Sitetemplates_Bulkconfigurations_Status API Function

          **Parameters:**:

          - **sitetemplate_id**: Site Template ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/bulkconfigurations/sitetemplates/{}/status".format(api_version,
                                                                                                sitetemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def skus(self, sku_id=None, api_version="v2.0"):
        """
        Get all licenses skus for a tenant (v2.0)

          **Parameters:**:

          - **sku_id**: (optional) SKU ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not sku_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/skus".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/skus/{}".format(api_version,
                                                                 sku_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def snapshots(self, site_id, snapshot_id, api_version="v2.0"):
        """
        Retrieve yaml configuration by ID (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **snapshot_id**: Snapshot ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/snapshots/{}".format(api_version,
                                                                           site_id,
                                                                           snapshot_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def snapshots_status(self, site_id, snapshot_id, api_version="v2.0"):
        """
        Status of the job (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **snapshot_id**: Snapshot ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/snapshots/{}/status".format(api_version,
                                                                                  site_id,
                                                                                  snapshot_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def snmpagents(self, site_id, element_id, snmpagent_id=None, api_version="v2.1"):
        """
        Get SNMP Agent on an element (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: (optional) SNMP Agent ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not snmpagent_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmpagents".format(api_version,
                                                                                         site_id,
                                                                                         element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmpagents/{}".format(api_version,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            snmpagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def snmptraps(self, site_id, element_id, snmptrap_id=None, api_version="v2.0"):
        """
        Get All SNMP Trap on an element (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmptrap_id**: (optional) SNMP Trap ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not snmptrap_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmptraps".format(api_version,
                                                                                        site_id,
                                                                                        element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/snmptraps/{}".format(api_version,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           snmptrap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def software(self, machine_id, software_id=None, api_version="v2.0"):
        """
        Get all Machine Software (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **software_id**: (optional) Software ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not software_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/software".format(api_version,
                                                                              machine_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/software/{}".format(api_version,
                                                                                 machine_id,
                                                                                 software_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def software_state(self, element_id, api_version="v2.0"):
        """
        Get the software upgrade configuration of an element (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/software/state".format(api_version,
                                                                                element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def spnnpnsitemigration_remotenetworks(self, api_version="v2.0"):
        """
        Get all easy onboarding created remote networks for a tenant (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/spnnpnsitemigration/remotenetworks".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def spokeclusters(self, site_id, spokecluster_id=None, api_version="v2.0"):
        """
        Get all spokeclusters (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: (optional) Spoke Cluster ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not spokecluster_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters".format(api_version,
                                                                                site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/{}".format(api_version,
                                                                                   site_id,
                                                                                   spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def spywareprofiles(self, spywareprofile_id=None, api_version="v2.0"):
        """
        Get all Spyware Security Profiles by tenant ID (v2.0)

          **Parameters:**:

          - **spywareprofile_id**: (optional) Spyware Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not spywareprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/spywareprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/spywareprofiles/{}".format(api_version,
                                                                            spywareprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def state_waninterfaces_e(self, site_id, element_id, waninterface_id, api_version="v2.1"):
        """
        GET State_Waninterfaces_E API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **waninterface_id**: WAN Interface ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/waninterfaces/{}/state".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def staticroutes(self, site_id, element_id, staticroute_id=None, api_version="v2.3"):
        """
        Get static routes (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: (optional) Static Route ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not staticroute_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/staticroutes".format(api_version,
                                                                                           site_id,
                                                                                           element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/staticroutes/{}".format(api_version,
                                                                                              site_id,
                                                                                              element_id,
                                                                                              staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_bgppeers(self, site_id, element_id, api_version="v2.3"):
        """
        GET Status_Bgppeers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/status".format(api_version,
                                                                                          site_id,
                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_bgppeers_i(self, site_id, element_id, bgppeer_id, api_version="v2.3"):
        """
        GET Status_Bgppeers_I API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/bgppeers/{}/status".format(api_version,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_cellular_modules_e(self, element_id, cellular_module_id, api_version="v2.1"):
        """
        GET Status_Cellular_Modules_E API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}/status".format(api_version,
                                                                                            element_id,
                                                                                            cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_cellular_modules_m(self, machine_id, cellular_module_id, api_version="v2.0"):
        """
        GET Status_Cellular_Modules_M API Function

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: Cellular Module ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/cellular_modules/{}/status".format(api_version,
                                                                                            machine_id,
                                                                                            cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_directoryservices(self, api_version="v2.0"):
        """
        GET Status_Directoryservices API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/directoryservices/status".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_e(self, element_id, api_version="v2.6"):
        """
        GET Status_E API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.6)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/status".format(api_version,
                                                                        element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_firmware_cellular_modules_e(self, element_id, cellular_module_id, api_version="v2.0"):
        """
        GET Status_Firmware_Cellular_Modules_E API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/cellular_modules/{}/firmware/status".format(api_version,
                                                                                                     element_id,
                                                                                                     cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_firmware_cellular_modules_m(self, machine_id, cellular_module_id, api_version="v2.0"):
        """
        GET Status_Firmware_Cellular_Modules_M API Function

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: Cellular Module ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/cellular_modules/{}/firmware/status".format(api_version,
                                                                                                     machine_id,
                                                                                                     cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id, api_version="v3.0"):
        """
        GET Status_Hubclustermembers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: Hub Cluster Member ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/hubclustermembers/{}/status".format(api_version,
                                                                                                         site_id,
                                                                                                         hubcluster_id,
                                                                                                         hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_i(self, site_id, hubcluster_id, api_version="v4.0"):
        """
        GET Status_I API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **api_version**: API version to use (default v4.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/hubclusters/{}/status".format(api_version,
                                                                                    site_id,
                                                                                    hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_interface_authentication(self, element_id, api_version="v2.0"):
        """
        GET Status_Interface_Authentication API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/interface_authentication/status".format(api_version,
                                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_interfaces(self, site_id, element_id, interface_id, api_version="v3.9"):
        """
        GET Status_Interfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **api_version**: API version to use (default v3.9)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/interfaces/{}/status".format(api_version,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_lldp_neighbors(self, element_id, api_version="v2.0"):
        """
        GET Status_Lldp_Neighbors API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/lldp_neighbors/status".format(api_version,
                                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_mac_addresses(self, element_id, api_version="v2.0"):
        """
        GET Status_Mac_Addresses API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/mac_addresses/status".format(api_version,
                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_mstp_instances(self, site_id, element_id, mstp_instance_id, api_version="v2.0"):
        """
        GET Status_Mstp_Instances API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **mstp_instance_id**: MSTP Instance ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/mstp_instances/{}/status".format(api_version,
                                                                                                   site_id,
                                                                                                   element_id,
                                                                                                   mstp_instance_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_natpolicysets(self, natpolicyset_id, api_version="v2.0"):
        """
        GET Status_Natpolicysets API Function

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/natpolicysets/{}/status".format(api_version,
                                                                             natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_networkpolicysets(self, networkpolicyset_id, api_version="v2.0"):
        """
        GET Status_Networkpolicysets API Function

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicysets/{}/status".format(api_version,
                                                                                 networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_ntp(self, element_id, ntp_id, api_version="v2.0"):
        """
        GET Status_Ntp API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **ntp_id**: NTP Configuration ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/ntp/{}/status".format(api_version,
                                                                               element_id,
                                                                               ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_policysets(self, policyset_id, api_version="v3.0"):
        """
        GET Status_Policysets API Function

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/policysets/{}/status".format(api_version,
                                                                          policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_prioritypolicysets(self, prioritypolicyset_id, api_version="v2.0"):
        """
        GET Status_Prioritypolicysets API Function

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicysets/{}/status".format(api_version,
                                                                                  prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_prismasase_connections(self, site_id, prismasase_connection_id, api_version="v2.0"):
        """
        GET Status_Prismasase_Connections API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **prismasase_connection_id**: Prisma SASE Connection ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/prismasase_connections/{}/status".format(api_version,
                                                                                               site_id,
                                                                                               prismasase_connection_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_radii(self, element_id, radii_id, api_version="v2.0"):
        """
        GET Status_Radii API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **radii_id**: Radii ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/radii/{}/status".format(api_version,
                                                                                 element_id,
                                                                                 radii_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_s(self, site_id, api_version="v2.0"):
        """
        GET Status_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/status".format(api_version,
                                                                     site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_sdwanapps(self, sdwanapp_id, api_version="v2.0"):
        """
        GET Status_Sdwanapps API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sdwanapps/{}/status".format(api_version,
                                                                         sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_software_e(self, element_id, api_version="v2.1"):
        """
        GET Status_Software_E API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/elements/{}/software/status".format(api_version,
                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_software_m(self, machine_id, software_id, status_id=None, api_version="v2.0"):
        """
        GET Status_Software_M API Function

          **Parameters:**:

          - **machine_id**: Machine ID
          - **software_id**: Software ID
          - **status_id**: (optional) Software Status ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not status_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/software/{}/status".format(api_version,
                                                                                        machine_id,
                                                                                        software_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/machines/{}/software/{}/status/{}".format(api_version,
                                                                                           machine_id,
                                                                                           software_id,
                                                                                           status_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_spokeclusters(self, site_id, spokecluster_id, api_version="v2.0"):
        """
        GET Status_Spokeclusters API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/spokeclusters/{}/status".format(api_version,
                                                                                      site_id,
                                                                                      spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_staticroutes(self, site_id, element_id, staticroute_id, api_version="v2.2"):
        """
        GET Status_Staticroutes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/staticroutes/{}/status".format(api_version,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_vfflicenses(self, vfflicense_id, api_version="v2.1"):
        """
        GET Status_Vfflicenses API Function

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}/status".format(api_version,
                                                                           vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_vpnlinks(self, vpnlink_id, api_version="v2.2"):
        """
        GET Status_Vpnlinks API Function

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vpnlinks/{}/status".format(api_version,
                                                                        vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def status_waninterfaces(self, site_id, waninterface_id, api_version="v2.1"):
        """
        GET Status_Waninterfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces/{}/status".format(api_version,
                                                                                      site_id,
                                                                                      waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sys_metrics_monitor(self, api_version="v2.3"):
        """
        GET Sys_Metrics_Monitor API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/monitor/{}/api/monitor/sys_metrics".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def syslogserverprofiles(self, syslogserverprofile_id=None, api_version="v2.1"):
        """
        Get Syslog Server Profiles (v2.1)

          **Parameters:**:

          - **syslogserverprofile_id**: (optional) Sys Log Server Profile ID 
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not syslogserverprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/syslogserverprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/syslogserverprofiles/{}".format(api_version,
                                                                                 syslogserverprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def syslogservers(self, site_id, element_id, syslogserver_id=None, api_version="v2.3"):
        """
        Get Syslog Servers on an element (v2.3)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: (optional) SYSLOG server ID
          - **api_version**: API version to use (default v2.3)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not syslogserver_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/syslogservers".format(api_version,
                                                                                            site_id,
                                                                                            element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/syslogservers/{}".format(api_version,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               syslogserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tacacs_plus_profiles(self, tacacs_plus_profile_id=None, api_version="v2.0"):
        """
        Get TACACS+ Profiles (v2.0)

          **Parameters:**:

          - **tacacs_plus_profile_id**: (optional) Tacacs Plus Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not tacacs_plus_profile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/tacacs_plus_profiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/tacacs_plus_profiles/{}".format(api_version,
                                                                                 tacacs_plus_profile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tacacs_plus_servers(self, site_id, element_id, tacacs_plus_server_id=None, api_version="v2.0"):
        """
        Get TACACS+ Servers (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **tacacs_plus_server_id**: (optional) Tacacs Plus Server ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not tacacs_plus_server_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/tacacs_plus_servers".format(api_version,
                                                                                                  site_id,
                                                                                                  element_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/tacacs_plus_servers/{}".format(api_version,
                                                                                                     site_id,
                                                                                                     element_id,
                                                                                                     tacacs_plus_server_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def templates_ntp(self, ntp_id=None, api_version="v2.0"):
        """
        Get all existing NTP Template of tenant. (v2.0)

          **Parameters:**:

          - **ntp_id**: (optional) NTP Configuration ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ntp_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/templates/ntp".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/templates/ntp/{}".format(api_version,
                                                                          ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_anynetlinks(self, anynetlink_id, api_version="v4.0"):
        """
        GET Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **api_version**: API version to use (default v4.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/anynetlinks/{}".format(api_version,
                                                                    anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_api_versions(self, api_version="v2.0"):
        """
        Get API versions for given apiVersions (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/api_versions".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_ipfixlocalprefixes(self, ipfixlocalprefix_id=None, api_version="v2.0"):
        """
        Get all IPFix local prefix (v2.0)

          **Parameters:**:

          - **ipfixlocalprefix_id**: (optional) IPFix Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not ipfixlocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixlocalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ipfixlocalprefixes/{}".format(api_version,
                                                                               ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_networkpolicylocalprefixes(self, networkpolicylocalprefix_id=None, api_version="v2.0"):
        """
        Get Network Policy local prefixes. (v2.0)

          **Parameters:**:

          - **networkpolicylocalprefix_id**: (optional) Network Policy Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not networkpolicylocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicylocalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/networkpolicylocalprefixes/{}".format(api_version,
                                                                                       networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_operators(self, operator_id=None, api_version="v2.2"):
        """
        Get a list of tenant operators (v2.2)

          **Parameters:**:

          - **operator_id**: (optional) Operator ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not operator_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/operators".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/operators/{}".format(api_version,
                                                                      operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_permissions(self, permission_id=None, api_version="v2.0"):
        """
        Get a list of custom permissions (v2.0)

          **Parameters:**:

          - **permission_id**: (optional) Permission ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not permission_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/permissions".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/permissions/{}".format(api_version,
                                                                        permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_prioritypolicylocalprefixes(self, prioritypolicylocalprefix_id=None, api_version="v2.0"):
        """
        Get Priority Policy local prefixes. (v2.0)

          **Parameters:**:

          - **prioritypolicylocalprefix_id**: (optional) Priority Policy Local Prefix ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not prioritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicylocalprefixes".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                        prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenantpassageconfigs(self, api_version="v2.0"):
        """
        GET Tenantpassageconfigs API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/tenantpassageconfigs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenants(self, api_version="v2.12"):
        """
        Get tenant details for tenant id (v2.12)

          **Parameters:**:

          - **api_version**: API version to use (default v2.12)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def toolkitsessions_t(self, api_version="v2.0"):
        """
        GET Toolkitsessions_T API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/toolkitsessions".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def urlcustomcategories(self, urlcustomcategorie_id=None, api_version="v2.0"):
        """
        Get all custom URL categories for a tenant (v2.0)

          **Parameters:**:

          - **urlcustomcategorie_id**: (optional) URL Custom Categorie ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not urlcustomcategorie_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/urlcustomcategories".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/urlcustomcategories/{}".format(api_version,
                                                                                urlcustomcategorie_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def urlfilteringconfigs(self, api_version="v2.0"):
        """
        Get the URL filtering config for a tenant (v2.0)

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/urlfilteringconfigs".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def urlfilteringprofiles(self, urlfilteringprofile_id=None, api_version="v2.0"):
        """
        Get all URL Filtering Profiles by tenant ID (v2.0)

          **Parameters:**:

          - **urlfilteringprofile_id**: (optional) URL Filtering Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not urlfilteringprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/urlfilteringprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/urlfilteringprofiles/{}".format(api_version,
                                                                                 urlfilteringprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def useridagents(self, useridagent_id=None, api_version="v2.0"):
        """
        Get All User ID Agents (v2.0)

          **Parameters:**:

          - **useridagent_id**: (optional) User Id Agent ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not useridagent_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/useridagents".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/useridagents/{}".format(api_version,
                                                                         useridagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def users(self, user_id=None, api_version="v2.0"):
        """
        Get Users. (v2.0)

          **Parameters:**:

          - **user_id**: (optional) User ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not user_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/users".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/users/{}".format(api_version,
                                                                  user_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vfflicense_tokens(self, vfflicense_id, token_id=None, api_version="v2.0"):
        """
        Get all Tenant Vff License Tokens (v2.0)

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **token_id**: (optional) Token ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not token_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}/tokens".format(api_version,
                                                                               vfflicense_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}/tokens/{}".format(api_version,
                                                                                  vfflicense_id,
                                                                                  token_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vfflicenses(self, vfflicense_id=None, api_version="v2.1"):
        """
        Get all Vff Licenses for Tenant (v2.1)

          **Parameters:**:

          - **vfflicense_id**: (optional) Virtual Form Factor License ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not vfflicense_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/vfflicenses/{}".format(api_version,
                                                                        vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vlan_port_members(self, site_id, element_id, api_version="v2.0"):
        """
        Get VLAN to switch port mapping information for an element (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/elements/{}/vlan_port_members".format(api_version,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vpnlinks_state(self, vpnlink_id, api_version="v2.0"):
        """
        Get the VPNLink admin state (v2.0)

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/vpnlinks/{}/state".format(api_version,
                                                                       vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vrfcontextprofiles(self, vrfcontextprofile_id=None, api_version="v2.0"):
        """
        Get All VRF Context Profiles (v2.0)

          **Parameters:**:

          - **vrfcontextprofile_id**: (optional) VRF Context Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not vrfcontextprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontextprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontextprofiles/{}".format(api_version,
                                                                               vrfcontextprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vrfcontexts(self, vrfcontext_id=None, api_version="v2.0"):
        """
        Get VRF segments (v2.0)

          **Parameters:**:

          - **vrfcontext_id**: (optional) VRF Context ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not vrfcontext_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontexts".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/vrfcontexts/{}".format(api_version,
                                                                        vrfcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vulnerabilityprofiles(self, vulnerabilityprofile_id=None, api_version="v2.0"):
        """
        Get all Vulnerability Security Profiles by tenant ID (v2.0)

          **Parameters:**:

          - **vulnerabilityprofile_id**: (optional) Vulnerability Profile ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not vulnerabilityprofile_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/vulnerabilityprofiles".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/vulnerabilityprofiles/{}".format(api_version,
                                                                                  vulnerabilityprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfacelabels(self, waninterfacelabel_id=None, api_version="v2.6"):
        """
        Get WAN interface labels for a tenant (v2.6)

          **Parameters:**:

          - **waninterfacelabel_id**: (optional) WAN Interface Label ID
          - **api_version**: API version to use (default v2.6)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not waninterfacelabel_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/waninterfacelabels".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/waninterfacelabels/{}".format(api_version,
                                                                               waninterfacelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfaces(self, site_id, waninterface_id=None, api_version="v2.10"):
        """
        Get all Site WAN interfaces (v2.10)

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: (optional) WAN Interface ID
          - **api_version**: API version to use (default v2.10)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not waninterface_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces".format(api_version,
                                                                                site_id)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/waninterfaces/{}".format(api_version,
                                                                                   site_id,
                                                                                   waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wannetworks(self, wannetwork_id=None, api_version="v2.1"):
        """
        Get all tenant WAN networks (v2.1)

          **Parameters:**:

          - **wannetwork_id**: (optional) WAN Network ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not wannetwork_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/wannetworks".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/wannetworks/{}".format(api_version,
                                                                        wannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wanoverlaychannels(self, wanoverlaychannel_id=None, api_version="v2.0"):
        """
        GET Wanoverlaychannels API Function

          **Parameters:**:

          - **wanoverlaychannel_id**: (optional) WAN Overlay Channel ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not wanoverlaychannel_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/wanoverlaychannels".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/wanoverlaychannels/{}".format(api_version,
                                                                               wanoverlaychannel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wanoverlays(self, wanoverlay_id=None, api_version="v2.0"):
        """
        Get app/wan contexts (v2.0)

          **Parameters:**:

          - **wanoverlay_id**: (optional) WAN Overlay ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not wanoverlay_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/wanoverlays".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/wanoverlays/{}".format(api_version,
                                                                        wanoverlay_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wanpaths(self, site_id, api_version="v3.0"):
        """
        GET Wanpaths API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/sdwan/{}/api/sites/{}/wanpaths".format(api_version,
                                                                       site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ws_extensions(self, extension_id=None, api_version="v2.0"):
        """
        GET Ws_Extensions API Function

          **Parameters:**:

          - **extension_id**: (optional) Extension ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with sdk_status and sdk_content properties.
        """

        cur_ctlr = self._parent_class.controller

        if not extension_id:
            url = str(cur_ctlr) + "/sdwan/{}/api/ws/extensions".format(api_version)
        else:
            url = str(cur_ctlr) + "/sdwan/{}/api/ws/extensions/{}".format(api_version,
                                                                          extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    access_elementusers = elementusers_access
    """ Backwards-compatibility alias of `access_elementusers` to `elementusers_access`"""

    agg_bw_stats_monitor = monitor_agg_bw_stats
    """ Backwards-compatibility alias of `agg_bw_stats_monitor` to `monitor_agg_bw_stats`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    api_versions_t = tenant_api_versions
    """ Backwards-compatibility alias of `api_versions_t` to `tenant_api_versions`"""

    cellular_modules_e = element_cellular_modules
    """ Backwards-compatibility alias of `cellular_modules_e` to `element_cellular_modules`"""

    configs_prismasase_connections = prismasase_connections_configs
    """ Backwards-compatibility alias of `configs_prismasase_connections` to `prismasase_connections_configs`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    deployments_sitetemplates_bulkconfigurations = bulkconfigurations_deployments_sitetemplates
    """ Backwards-compatibility alias of `deployments_sitetemplates_bulkconfigurations` to `bulkconfigurations_deployments_sitetemplates`"""

    deviceidconfigs_i = deviceidconfigs
    """ Backwards-compatibility alias of `deviceidconfigs_i` to `deviceidconfigs`"""

    elementpassageconfigs_e = elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_e` to `elementpassageconfigs`"""

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

    ospfdiscoveredneighbors_ospfconfigs = ospfconfigs_ospfdiscoveredneighbors
    """ Backwards-compatibility alias of `ospfdiscoveredneighbors_ospfconfigs` to `ospfconfigs_ospfdiscoveredneighbors`"""

    ospfreachableprefixes_ospfconfigs = ospfconfigs_ospfreachableprefixes
    """ Backwards-compatibility alias of `ospfreachableprefixes_ospfconfigs` to `ospfconfigs_ospfreachableprefixes`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    passages_e = element_passages
    """ Backwards-compatibility alias of `passages_e` to `element_passages`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    probes_metrics_monitor = monitor_metrics_probes
    """ Backwards-compatibility alias of `probes_metrics_monitor` to `monitor_metrics_probes`"""

    remotenetworks_spnnpnsitemigration = spnnpnsitemigration_remotenetworks
    """ Backwards-compatibility alias of `remotenetworks_spnnpnsitemigration` to `spnnpnsitemigration_remotenetworks`"""

    sessions_t = operator_sessions
    """ Backwards-compatibility alias of `sessions_t` to `operator_sessions`"""

    sim_security_cellular_modules = cellular_modules_sim_security
    """ Backwards-compatibility alias of `sim_security_cellular_modules` to `cellular_modules_sim_security`"""

    sitetemplates_bulkconfigurations = bulkconfigurations_sitetemplates
    """ Backwards-compatibility alias of `sitetemplates_bulkconfigurations` to `bulkconfigurations_sitetemplates`"""

    snmpdiscoverystartnodes_deviceidconfigs = deviceidconfigs_snmpdiscoverystartnodes
    """ Backwards-compatibility alias of `snmpdiscoverystartnodes_deviceidconfigs` to `deviceidconfigs_snmpdiscoverystartnodes`"""

    state = element_state
    """ Backwards-compatibility alias of `state` to `element_state`"""

    state_m = machine_state
    """ Backwards-compatibility alias of `state_m` to `machine_state`"""

    state_software = software_state
    """ Backwards-compatibility alias of `state_software` to `software_state`"""

    state_vpnlinks = vpnlinks_state
    """ Backwards-compatibility alias of `state_vpnlinks` to `vpnlinks_state`"""

    status_copy_element_configurations_elementshells = copy_element_configurations_elementshells_status
    """ Backwards-compatibility alias of `status_copy_element_configurations_elementshells` to `copy_element_configurations_elementshells_status`"""

    status_cuid = cuid_status
    """ Backwards-compatibility alias of `status_cuid` to `cuid_status`"""

    status_deployments_sitetemplates_bulkconfigurations = deployments_sitetemplates_bulkconfigurations_status
    """ Backwards-compatibility alias of `status_deployments_sitetemplates_bulkconfigurations` to `deployments_sitetemplates_bulkconfigurations_status`"""

    status_perfmgmtpolicysets = perfmgmtpolicysets_status
    """ Backwards-compatibility alias of `status_perfmgmtpolicysets` to `perfmgmtpolicysets_status`"""

    status_sitetemplates_bulkconfigurations = sitetemplates_bulkconfigurations_status
    """ Backwards-compatibility alias of `status_sitetemplates_bulkconfigurations` to `sitetemplates_bulkconfigurations_status`"""

    status_snapshots = snapshots_status
    """ Backwards-compatibility alias of `status_snapshots` to `snapshots_status`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

